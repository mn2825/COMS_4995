**Retrieve list of features in dataset**
```python
inputFeatures = []
df = pd.read_excel('./data/comm_public_2017.xlsx')
print("Features to choose from: ")
print("-------------------------------------------------------")
print(list(enumerate(df.columns)))
```
![Image](/images/list_of_features.png?raw=true)

