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
    labels = [0] * len(data)
    c_1 = data[int(len(data)/2)] 
    distances = []
    for i in range(0, len(data)):
        distances.append((i, LA.norm(c_1 - data[i])))
    distances.sort(reverse=True, key=lambda x:x[1])
    centers, center_lists = getCenters(data,distances, num)
    centers.insert(0, c_1)
    center_lists.insert(0, [])
    print(len(centers), len(center_lists))
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







