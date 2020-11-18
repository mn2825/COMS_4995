import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

if __name__ == '__main__':
    df = pd.read_excel('chp-pud-2018.xlsx')
    data = [list(row) for row in df.values]
    all_attributes = []
    for vals in list(df.columns):
        if "lower_95CL" in str(vals) or "upper_95CL" in str(vals) or "Uninsured_reliability_note" in str(vals):
            continue
        else:
            all_attributes.append(vals)
    #print(all_attributes)

    key_attributes = {}
    keyNum = 0
    for i in range(17, len(all_attributes)):
        if "Comparison" in all_attributes[i]: 
            continue
        else:
            keyNum +=1
            key_attributes[keyNum] = all_attributes[i]
    #print(key_attributes)
    
    positive_att = ["On_Time_HS_Grad", "Edu_HSGrad_Some_College", "Edu_College_Degree_And_Higher", "Helpful_Neighbor", "Homes_No_Defects", "Homes_AC", "Bike_Coverage", "Fruit_Veg", "HPV_Vaccination_All",
                    "HPV_Vaccination_Female", "HPV_Vaccination_Male", "Flu_Vaccination", "Life_Expectancy"]
    negative_att = []
    for att in key_attributes.values():
        if att not in positive_att:
            negative_att.append(att)
    print(positive_att)
    print(negative_att)
    
    print("ON TIME: ", df["On_Time_HS_Grad"].values)
    
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

    fig = px.scatter(df, x="On_Time_HS_Grad", y="Edu_College_Degree_And_Higher",
                 size="Overall_Pop", color="Borough", hover_name="Name",
                 log_x=True, size_max=60)

    app.layout = html.Div([
    dcc.Graph(id='life-exp-vs-gdp',figure=fig)
    ])

    app.run_server(debug=True)
