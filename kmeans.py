import random
import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA
import pandas as pd
from sklearn.metrics.pairwise import rbf_kernel
from sklearn.metrics.pairwise import linear_kernel
from sklearn.metrics.pairwise import polynomial_kernel
import matplotlib._color_data as mcd

def get_centers(data, distances, num):
    """ Returns list of initialized cluster centers and cluster lists

    Parameters
    ----------
    data
        List of vectorized data points.
    distances
        List of norms between first cluster and all data points.
     
    """
    centers = []
    center_lists = [[] for center in range(0,4)]
    for center in range(1, 5):
        centers.append(data[distances[center][0]])
    return centers, center_lists

def plot(centers, center_lists):
    """ Plots cluster centers and data points based on assigned cluster
    
    Parameters
    ----------
    centers
        List of vectorized center points
    center_lists
        List of all the points in each cluster as determined by K-Means

    """
    labels = ["Cluster 1", "Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5"]
    for l in center_lists:
        if len(l) == 0:
            return None
    for center in range(0, len(centers)):
        random_col = np.random.randint(0, len(list(mcd.CSS4_COLORS.values())))
        plt.scatter([item[0] for item in center_lists[center]], [item[1] for item in center_lists[center]], color = list(mcd.CSS4_COLORS.values())[random_col])
    for center in range(0, len(centers)):    
        plt.scatter(centers[center][0], centers[center][1], color = 'black',  marker = 'x', s=50, label=labels[center])
    plt.xlabel("")
    plt.ylabel("")
    plt.title("K-Means prediction for five borough clusters")
    plt.show()

def lloyds(data, num):
    """Performs the Lloyd algorithm for k-Means Clustering. Once data points no longer switch from a previously assigned cluster to a new one, data points are plotted.
    
    Parameters
    ----------
    data
        List of vectorized data points.
    num
        Number of features chosen.

    """
    if len(data) == 0:
        return None
    labels = [0] * len(data)
    c_1 = data[int(len(data)/2)] 
    distances = []
    for point in range(0, len(data)):
        distances.append((point, LA.norm(c_1 - data[point])))
    distances.sort(reverse=True, key=lambda x:x[1])
    centers, center_lists = get_centers(data,distances, num)
    centers.insert(0, c_1)
    center_lists.insert(0, [])
    labels = [0] * len(data)
    while(1):
        point_to_center_list = []
        for point in range(0, len(data)):
            point_to_center_list = []
            for center in range(0, len(centers)):
                point_to_center_list.append(LA.norm(data[point]- centers[center]))
            print(point_to_center_list)
            labels[point] = np.argmin(point_to_center_list)
            print("------------", labels[point])
        for label in range(0, len(labels)): #determine label of data point, and add to corresponding center list
            center_lists[labels[label]].append(data[label])
        new_centers = [[] for center in range(len(centers))]
        for cluster in range(0, len(new_centers)):
            for number in range(0, num): #calc mean of everything to determine new cluster centers
                new_centers[cluster].append(np.mean([item[number] for item in center_lists[cluster]]))
        all_same = []
        for cluster in range(0, len(centers)):
            if(np.array_equal(new_centers[cluster], centers[cluster])):
                all_same.append("True")
            else:
                all_same.append("False")
        if all_same.count("True") == len(all_same):
            break
        for center in range(0, len(centers)):#update centers
            centers[center] = new_centers[center]
        center_lists = [[] for point in range(0, len(centers))]
    plot(centers, center_lists)

def compute_alpha(data, labels):
    """Computes number of data points in each cluster for each round of the kernelized Lloyd's algorithm
    
    Parameters
    ----------
    data
        List of vectorized data points.
    labels
        Assigned labels for each data point.

    """
    z_0 = labels.count(0)
    z_1 = labels.count(1)
    z_2 = labels.count(2)
    z_3 = labels.count(3)
    z_4 = labels.count(4)
    alphas = [1/z_0, 1/z_1, 1/z_2, 1/z_3, 1/z_4]
    return alphas

def compute_distances(point, points,alpha): #alpha values for a particular cluster j (0 or 1)
    """Computes kernel function on a data point.
    
    Parameters
    ----------
    point
        Point to be kernelized.
    points
        Other data points necessary to compute kernel function.
    alpha
        Alpha values for clusters 1-5.

    """
    point = np.reshape(point,(1,-1))
    #first = polynomial_kernel(point, point, degree=2)
    first = linear_kernel(point, point)
    #first = rbf_kernel(point, point)
    #second = 0
    #third = 0
    #second =(alpha**2)*polynomial_kernel(points,points, degree=2)
    second = (alpha**2)*linear_kernel(points,points)
    #second = (alpha**2)*rbf_kernel(point, points)
    second_sum = np.sum(second)
    #third = polynomial_kernel(point, points, degree=2)
    third= linear_kernel(point, points)
    #third = rbf_kernel(point, points)
    third_sum = np.sum(third)
    distance = first + second_sum -(2*alpha*third_sum)
    return distance

def compute_initial(point1, point2):
    """Compute distance between two data points in kernelized space
    
    Parameters
    ----------
    point1
        First point
    point2
        Second point, often the cluster center.

    """
    point1 = np.reshape(point1, (1,-1))
    point2 = np.reshape(point2, (1,-1))
    #first = polynomial_kernel(point1, point1, degree=2)
    #first = linear_kernel(point1, point1)
    first = rbf_kernel(point1, point1)
    #second = polynomial_kernel(point2, point2, degree=2)
    #second = linear_kernel(point2, point2)
    second = rbf_kernel(point2, point2)
    #third = polynomial_kernel(point1, point2, degree=2)
    #third = linear_kernel(point1, point2)
    third = rbf_kernel(point1, point2)
    distance = first + second -(2*third)
    return distance

def lloyds_kernel(data, num):
    """Performs the kernelized version of Lloyd algorithm for k-Means Clustering. Once data points no longer switch from a previously assigned cluster to a new one, data points are plott
    
    Parameters
    ----------
    data
        List of vectorized data points.
    num
        Number of chosen features.
    """
    np.random.shuffle(data)
    np.random.seed(40)
    centers = [data[0]]
    for c in range(1, 5):
        mins = [min([np.inner(c-d,c-d) for c in centers]) for d in data]
        squared = np.array(mins)
        probs = squared/squared.sum()
        all_probs = probs.cumsum()
        generated = np.random.rand()
        for ind, val in enumerate(all_probs):
            if generated < val:
                centers.append(data[ind])
                break
    center_lists = [[] for center in range(0,5)]
    labels = [0] * len(data)
    for i in range(0, len(data)):
        d = [compute_initial(data[i], centers[0]), compute_initial(data[i], centers[1]), compute_initial(data[i], centers[2]), compute_initial(data[i], centers[3]), compute_initial(data[i], centers[4])]
        if (np.argmin(d) == 0):
            center_lists[0].append(data[i])
            labels[i] = 0
        elif(np.argmin(d) == 1):
            center_lists[1].append(data[i])
            labels[i] = 1
        elif(np.argmin(d) == 2):
            center_lists[2].append(data[i])
            labels[i] = 2
        elif(np.argmin(d) ==3):
            center_lists[3].append(data[i])
            labels[i] = 3
        else:
            center_lists[4].append(data[i])
            labels[i] = 4
    new_center_lists = [[] for point in range(0,5)]
    while(1):
        point_to_center_list = []
        alphas = compute_alpha(data, labels)
        for point in range(0, len(data)):
            point_to_center_list = []
            for cluster_num in range(0, len(centers)):
                alpha = alphas[cluster_num]
                point_to_center_list.append(compute_distances(data[point], center_lists[cluster_num], alpha))
            labels[point] = np.argmin([point_to_center_list[0][0][0], point_to_center_list[1][0][0], point_to_center_list[2][0][0], point_to_center_list[3][0][0], point_to_center_list[4][0][0]])
        for point in range(0, len(labels)):
            new_center_lists[labels[point]].append(data[point])
        all_same = []
        for cluster in range(0, len(centers)):
            if(np.array_equal(new_center_lists[cluster], center_lists[cluster])):
                all_same.append("True")
            else:
                all_same.append("False")
        if all_same.count("True") == len(all_same):
            break
        else:
            for cluster_num in range(0, len(centers)):
                center_lists[cluster_num] = new_center_lists[cluster_num]
    plot(centers, center_lists)

def process_and_run(features_list, num):
    """Preprocesses data based on the features chosen by the user
    
    Parameters
    ----------
    featuresList
        Column numbers corresponding to chosen features.
    num
        Number of features chosen.
    """
    data_frame = pd.read_excel('./data/comm_public_2017.xlsx')
    data = [np.array([row[num] for num in features_list]) for row in data_frame.values]
    data1 = []
    is_nan = []
    for person in data:
        for i in range(0, len(features_list)):
            if np.isnan(person[i]):
                is_nan.append(False)
            else:
                is_nan.append(True)
        if is_nan.count(True) == len(is_nan):     
            data1.append(person)
        is_nan = []
    
    #Add noise to each data point for each feature
    for point in range(len(data1)):
        for feat in range(len(features_list)):
            data1[point][feat] = data1[point][feat] + random.uniform(0,1)
    
    #lloyds(data1, num)
    lloyds_kernel(data1, num) 
        
if __name__ =='__main__':
    input_feat = []
    data_frame = pd.read_excel('./data/comm_public_2017.xlsx')
    print("Features to choose from: ")
    print("-------------------------------------------------------")
    for elem in list(enumerate(data_frame.columns)):
        print(elem)
    n = int(input("How many features would you like to compare?"))
    for i in range(0, n):
        num = int(input())
        input_feat.append(num)
    print("Features you entered: ", input_feat)
    process_and_run(input_feat, len(input_feat))
