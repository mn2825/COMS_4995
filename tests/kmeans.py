import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import random
from mpl_toolkits import mplot3d
import matplotlib._color_data as mcd

def getCenters(data, distances, num):
    centers = []
    center_lists = [[] for i in range(0,4)]
    for i in range(1, 5):
        centers.append(data[distances[i][0]])
    return centers, center_lists

def plot(centers, center_lists):
    for l in center_lists:
        if len(l) == 0:
            return None
    labels = ["Cluster 1", "Cluster 2", "Cluster 3", "Cluster 4", "Cluster 5"]
    for i in range(0, len(centers)):
        a = np.random.randint(0, len(list(mcd.CSS4_COLORS.values())))
        plt.scatter([item[0] for item in center_lists[i]], [item[1] for item in center_lists[i]], color = list(mcd.CSS4_COLORS.values())[a])
    for i in range(0, len(centers)):    
        plt.scatter(centers[i][0], centers[i][1], color = 'black',  marker = 'x', s=50, label=labels[i])
    plt.xlabel("")
    plt.ylabel("")
    plt.title("K-Means prediction for five borough clusters")
    plt.show()

def lloyds(data, num):
    if len(data)==0:
        return None
    labels = [0] * len(data)
    c_1 = data[int(len(data)/2)] 
    distances = []
    for i in range(0, len(data)):
        distances.append((i, LA.norm(c_1 - data[i])))
    distances.sort(reverse=True, key=lambda x:x[1])
    centers, center_lists = getCenters(data,distances, num)
    centers.insert(0, c_1)
    center_lists.insert(0, [])
    labels = [0] * len(data)
    while(1):
        point_to_center_list = []
        for i in range(0, len(data)):
            point_to_center_list = []
            for j in range(0, len(centers)):
                point_to_center_list.append(LA.norm(data[i]- centers[j]))
            labels[i] = np.argmin(point_to_center_list)
        for i in range(0, len(labels)):
            center_lists[labels[i]].append(data[i])
        new_centers = [[] for i in range(len(centers))]
        print(len(new_centers))
        for i in range(0, len(new_centers)):
            for j in range(0, num):
                new_centers[i].append(np.mean([item[j] for item in center_lists[i]]))
        allSame = []
        for i in range(0, len(centers)):
            if(np.array_equal(new_centers[i], centers[i])):
                allSame.append("True")
            else:
                allSame.append("False")
        if allSame.count("True") == len(allSame):
            break
        else:
            for a in range(0, len(centers)):
                centers[a] = new_centers[a]
            center_lists = [[] for i in range(len(centers))]
    plot(centers, center_lists)
def computeAlpha(data, labels):
    z_0 = labels.count(0)
    z_1 = labels.count(1)
    z_2 = labels.count(2)
    z_3 = labels.count(3)
    z_4 = labels.count(4)
    alphas = [z_0, z_1, z_2, z_3, z_4]
    return alphas

def computeDistances(point, points,alpha): #alpha values for a particular cluster j (0 or 1)
    point = np.reshape(point,(1,-1))
    #first = polynomial_kernel(point, point, degree=2)
    #first = linear_kernel(point, point)
    first = rbf_kernel(point, point)
    second = 0
    third = 0
    #second =(alpha**2)*polynomial_kernel(points,points, degree=2)
    #second = (alpha**2)*linear_kernel(points,points)
    second = (alpha**2)*rbf_kernel(point, points)
    s = np.sum(second)
    #third = polynomial_kernel(point, points, degree=2)
    #third= linear_kernel(point, points)
    third = rbf_kernel(point, points)
    t = np.sum(third)
    distance = first + s -(2*alpha*t)
    return distance

def computeInitial(point1, point2):
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
    centers, center_lists = getCenters(data,distances, num)
    centers.insert(0, c_1)
    center_lists.insert(0, [])
    labels = [0] * len(data)
    for i in range(0, len(data)):
        d = [computeInitial(data[i], centers[0]), computeInitial(data[i], centers[1]), computeInitial(data[i], centers[2]), computeInitial(data[i], centers[3]), computeInitial(data[i], centers[4])]
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
        alphas = computeAlpha(data, labels)
        for i in range(0, len(data)):
            point_to_center_list = []
            for j in range(0, len(centers)):
                alpha = alphas[j]
                point_to_center_list.append(computeDistances(data[i], center_lists[j], alpha))
            labels[i] = np.argmin(point_to_center_list)
        for i in range(0, len(labels)):
            center_lists[labels[i]].append(data[i])
        new_centers = [[] for i in range(len(centers))]
        print(len(new_centers))
        for i in range(0, len(new_centers)):
            for j in range(0, num):
                new_centers[i].append(np.mean([item[j] for item in center_lists[i]]))
        allSame = []
        for i in range(0, len(centers)):
            if(np.array_equal(new_centers[i], centers[i])):
                allSame.append("True")
            else:
                allSame.append("False")
        if allSame.count("True") == len(allSame):
            break
        else:
            for a in range(0, len(centers)):
                centers[a] = new_centers[a]
            center_lists = [[] for i in range(len(centers))]
    plot(centers, center_lists)
def processAndRun(featuresList, num):
    df = pd.read_excel('./data/comm_public_2017.xlsx')
    data = [np.array([row[num] for num in featuresList]) for row in df.values]
    data1 = []
    isNan = []
    for person in data:
        for i in range(0, len(featuresList)):
            if np.isnan(person[i]):
                isNan.append(False)
            else:
                isNan.append(True)
        if isNan.count(True) == len(isNan):     
            data1.append(person)
        isNan = []
    
    #Add noise to each of parameters
    for i in range(len(data1)):
        for j in range(len(featuresList)):
            data1[i][j] = data1[i][j] + random.uniform(0,1)
    lloyds(data1, num)

if __name__ =='__main__':
    inputFeatures = []
    df = pd.read_excel('./data/comm_public_2017.xlsx')
    print("Features to choose from: ")
    print("-------------------------------------------------------")
    print(list(enumerate(df.columns)))
    n = int(input("How many features would you like to compare?"))
    for i in range(0, n):
        num = int(input())
        inputFeatures.append(num)
    print("Features you showed: ", inputFeatures)
    processAndRun(inputFeatures,len(inputFeatures))







