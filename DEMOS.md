# 1. Retrieve list of features in dataset
```python
inputFeatures = []
df = pd.read_excel('./data/comm_public_2017.xlsx')
print("Features to choose from: ")
print("-------------------------------------------------------")
print(list(enumerate(df.columns)))
```
![Image](/images/list_of_features.png?raw=true)
The image above shows the list of features available to you from the 2017 CHS dataset. The user can select any number of features (at least 2) to perform K-means clustering on. 






# 2, Choose features to perform clustering
![Image](/images/add_features.png?raw=true)

In this example, the user choose four features (14, 39, 66, and 36) which address questions regarding race, experience with medical care, smoking, and insurance. K-Means will now compute the centers of the five clusters/regions we are aiming to identify within the data based on the chosen features. 




# 3. Clustering results
```python
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
```
![Image](/images/result2.png?raw=true)
The code and plot above show the result of the K-means algorithm after convergence with respect to the first two features that were chosen. As we can see, there are five clearly segmented regions, each with an X at the region's mean.
