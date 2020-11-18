import pandas as pd

def checkDataset(dataset):
    check1 = False
    check2 = False
    
    df = pd.read_excel(dataset)
    if df != None:
        check1 = True
    if len(df.columns) > 5:
        check2 = True
    if check1 == True and check2 == True:
        return True

if __name__ == "__main__":
    check = checkDataset("./data/comm_public_2017.xlsx")
    return check
