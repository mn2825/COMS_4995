import random
import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA
import pandas as pd
from sklearn.metrics.pairwise import rbf_kernel
#from sklearn.metrics.pairwise import linear_kernel
#from sklearn.metrics.pairwise import polynomial_kernel
#import dash
#import dash_core_components as dcc
#import dash_html_components as html
#import plotly.express as px
#from mpl_toolkits import mplot3d
import matplotlib._color_data as mcd

def get_centers(data, distances, num):
    centers = []
    center_lists = [[] for center in range(0,4)]
    for center in range(1, 5):
        centers.append(data[distances[center][0]])
    return centers, center_lists

def plot(centers, center_lists):
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
            labels[point] = np.argmin(point_to_center_list)
        for label in range(0, len(labels)):
            center_lists[labels[label]].append(data[label])
        new_centers = [[] for center in range(len(centers))]
        print(len(new_centers))
        for cluster in range(0, len(new_centers)):
            for number in range(0, num):
                new_centers[cluster].append(np.mean([item[number] for item in center_lists[cluster]]))
        all_same = []
        for cluster in range(0, len(centers)):
            if(np.array_equal(new_centers[cluster], centers[cluster])):
                all_same.append("True")
            else:
                all_same.append("False")
        if all_same.count("True") == len(all_same):
            break
        for center in range(0, len(centers)):
            centers[center] = new_centers[center]
        center_lists = [[] for center in range(len(centers))]
    plot(centers, center_lists)

def compute_alpha(data, labels):
    z_0 = labels.count(0)
    z_1 = labels.count(1)
    z_2 = labels.count(2)
    z_3 = labels.count(3)
    z_4 = labels.count(4)
    alphas = [z_0, z_1, z_2, z_3, z_4]
    return alphas

def compute_distances(point, points,alpha): #alpha values for a particular cluster j (0 or 1)
    point = np.reshape(point,(1,-1))
    #first = polynomial_kernel(point, point, degree=2)
    #first = linear_kernel(point, point)
    first = rbf_kernel(point, point)
    second = 0
    third = 0
    #second =(alpha**2)*polynomial_kernel(points,points, degree=2)
    #second = (alpha**2)*linear_kernel(points,points)
    second = (alpha**2)*rbf_kernel(point, points)
    second_sum = np.sum(second)
    #third = polynomial_kernel(point, points, degree=2)
    #third= linear_kernel(point, points)
    third = rbf_kernel(point, points)
    third_sum = np.sum(third)
    distance = first + second_sum -(2*alpha*third_sum)
    return distance

def compute_initial(point1, point2):
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
    labels = [0] * len(data)
    c_1 = data[int(len(data)/2)]
    distances = []
    for i in range(0, len(data)):
        distances.append((i, LA.norm(c_1 - data[i])))
    distances.sort(reverse=True, key=lambda x:x[1])
    centers, center_lists = get_centers(data,distances, num)
    centers.insert(0, c_1)
    center_lists.insert(0, [])
    labels = [0] * len(data)
    for i in range(0, len(data)):
        d = [compute_initial(data[i], centers[0]), compute_initial(data[i], centers[1]), compute_initial(data[i], centers[2]), compute_initial(data[i], centers[3]), compute_initial(data[i], centers[4])]
        if (np.argmin(d) == 0):
            center_lists[0].append(data[i])
        elif(np.argmin(d) == 1):
            center_lists[1].append(data[i])
        elif(np.argmin(d) == 2):
            center_lists[2].append(data[i])
        elif(np.argmin(d) ==3):
            center_lists[3].append(data[i])
        else:
            center_lists[4].append(data[i])
    while(1):
        point_to_center_list = []
        alphas = compute_alpha(data, labels)
        for point in range(0, len(data)):
            point_to_center_list = []
            for cluster_num in range(0, len(centers)):
                alpha = alphas[cluster_num]
                point_to_center_list.append(compute_distances(data[point], center_lists[cluster_num], alpha))
            labels[point] = np.argmin(point_to_center_list)
        for point in range(0, len(labels)):
            center_lists[labels[point]].append(data[point])
        new_centers = [[] for point in range(len(centers))]
        print(len(new_centers))
        for cluster in range(0, len(new_centers)):
            for num in range(0, num):
                new_centers[cluster].append(np.mean([item[num] for item in center_lists[cluster]]))
        all_same = []
        for cluster in range(0, len(centers)):
            if(np.array_equal(new_centers[cluster], centers[cluster])):
                all_same.append("True")
            else:
                all_same.append("False")
        if all_same.count("True") == len(all_same):
            break
        else:
            for cluster_num in range(0, len(centers)):
                centers[cluster_num] = new_centers[cluster_num]
            center_lists = [[] for i in range(len(centers))]
    plot(centers, center_lists)

def process_and_run(features_list, num):
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
    
    #Add noise to each of parameters
    for point in range(len(data1)):
        for feat in range(len(features_list)):
            data1[point][feat] = data1[point][feat] + random.uniform(0,1)
    lloyds(data1, num)
    lloyds_kernel(data1, num)

if __name__ =='__main__':
    input_feat = []
    data_frame = pd.read_excel('./data/comm_public_2017.xlsx')
    print("Features to choose from: ")
    print("-------------------------------------------------------")
    print(list(enumerate(data_frame.columns)))
    n = int(input("How many features would you like to compare?"))
    for i in range(0, n):
        num = int(input())
        input_feat.append(num)
    print("Features you showed: ", input_feat)
    process_and_run(input_feat, len(input_feat))







