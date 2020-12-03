# Retrieve list of features in dataset
```python
inputFeatures = []
df = pd.read_excel('./data/comm_public_2017.xlsx')
print("Features to choose from: ")
print("-------------------------------------------------------")
print(list(enumerate(df.columns)))
```
![Image](/images/list_of_features.png?raw=true)
The image above shows the list of features available to you from the 2017 CHS dataset. The user can select any number of features (at least 2) to perform K-means clustering on. 


# Choose features to perform clustering
![Image](/images/add_features.png?raw=true)

# Clustering results
![Image](/images/result.png?raw=true)
