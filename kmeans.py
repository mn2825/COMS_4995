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

def lloyds(data):#implementation for 4 features
    labels = [0] * len(data)
    clusterNum = 5
    c_1 = data[int(len(data)/2)] #random assignment for cluster 1
    distances = []
    for i in range(0, len(data)):
        distances.append(LA.norm(c_1 - data[i])) 
    distances = distances.sort(reverse=True)
    c_2 = data[0] #cluster 2 is the farthest data point from cluster 1
    c_3 = data[1] 
    c_4 = data[2]
    c_5 = data[3]

    c1_list = []
    c2_list = []
    c3_list = []
    c4_list = []
    c5_list = []
    j = 0
    while(1):
        j+=1
        print(j)
        for i in range(0, len(data)):
            point_to_center_list= [LA.norm(data[i]- c_1), LA.norm(data[i]- c_2), LA.norm(data[i]- c_3), LA.norm(data[i]- c_4), LA.norm(data[i]- c_5)]
            if(np.argmin(point_to_center_list)==0):
                labels[i] = 1
            elif(np.argmin(point_to_center_list) == 1):
                labels[i]= 2
            elif(np.argmin(point_to_center_list) == 2):
                labels[i]= 3
            elif(np.argmin(point_to_center_list) == 3):
                labels[i] = 4
            else:
                labels[i] = 5
        for i in range(0, len(labels)):
            if(labels[i]==1):
                c1_list.append(data[i])
            elif(labels[i]==2):
                c2_list.append(data[i])
            elif(labels[i]==3):
                c3_list.append(data[i])
            elif(labels[i]==4):
                c4_list.append(data[i])
            else:
                c5_list.append(data[i])
        new_c_1 = [np.mean([item[0] for item in c1_list]), np.mean([item[1] for item in c1_list]), np.mean([item[2] for item in c1_list]), np.mean([item[3] for item in c1_list])]
        new_c_2 = [np.mean([item[0] for item in c2_list]), np.mean([item[1] for item in c2_list]), np.mean([item[2] for item in c2_list]), np.mean([item[3] for item in c2_list])]
        new_c_3 = [np.mean([item[0] for item in c3_list]), np.mean([item[1] for item in c3_list]), np.mean([item[2] for item in c3_list]), np.mean([item[3] for item in c3_list])]
        new_c_4 = [np.mean([item[0] for item in c4_list]), np.mean([item[1] for item in c4_list]), np.mean([item[2] for item in c4_list]), np.mean([item[3] for item in c4_list])]
        new_c_5 = [np.mean([item[0] for item in c5_list]), np.mean([item[1] for item in c5_list]), np.mean([item[2] for item in c5_list]), np.mean([item[3] for item in c5_list])]
        if(np.array_equal(new_c_1, c_1) and np.array_equal(new_c_2, c_2) and np.array_equal(new_c_3,c_3) and np.array_equal(new_c_4,c_4) and np.array_equal(new_c_5,c_5)):
            break
        else:
            c_1 = new_c_1
            c_2 = new_c_2
            c_3 = new_c_3
            c_4 = new_c_4
            c_5 = new_c_5
            c1_list = []
            c2_list = []
            c3_list = []
            c4_list = []
            c5_list = []
    print(len(c1_list), len(c2_list), len(c3_list), len(c4_list), len(c5_list))

    plt.scatter([item[0] for item in c1_list], [item[1] for item in c1_list], color = 'red')
    plt.scatter([item[0] for item in c2_list],[item[1] for item in c2_list],  color = 'green')
    plt.scatter([item[0] for item in c3_list],[item[1] for item in c3_list],  color = 'blue')
    plt.scatter([item[0] for item in c4_list],[item[1] for item in c4_list],  color = 'orange')
    plt.scatter([item[0] for item in c5_list],[item[1] for item in c5_list],  color = 'purple')

    plt.scatter(c_1[0], c_1[1], color = 'black', marker = 'x', s=50, label="Cluster 1")
    plt.scatter(c_2[0], c_2[1], color = 'black', marker = 'x', s=50, label="Cluster 2")
    plt.scatter(c_3[0], c_3[1], color = 'black', marker = 'x', s=50, label="Cluster 3")
    plt.scatter(c_4[0], c_4[1], color = 'black', marker = 'x', s=50, label="Cluster 4")
    plt.scatter(c_5[0], c_5[1], color = 'black', marker = 'x', s=50, label="Cluster 5")

    plt.title("K-Means prediction for five borough clusters") 
    plt.show()

def processAndRun(featuresList):
    df = pd.read_excel('./data/comm_public_2017.xlsx')
    data = [np.array([row[num] for num in featuresList]) for row in df.values]
    data1 = []
    for person in data:
        if np.isnan(person[0]) or np.isnan(person[1]) or np.isnan(person[2]) or np.isnan(person[3]):
            continue
        else:
            data1.append(person)
    
    #Add noise to each of the four parameters
    for i in range(len(data1)):
        data1[i][0] = data1[i][0] + random.uniform(0,1)
    for i in range(len(data1)):
        data1[i][1] = data1[i][1] + random.uniform(0,1)
    for i in range(len(data1)):
        data1[i][2] = data1[i][2] + random.uniform(0,1)
    for i in range(len(data1)):
        data1[i][3] = data1[i][3] + random.uniform(0,1)

    lloyds(data1)

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

    processAndRun(inputFeatures)











