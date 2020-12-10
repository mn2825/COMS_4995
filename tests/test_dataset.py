import pandas as pd
import pytest
from kmeans import get_centers
from kmeans import compute_alpha
from kmeans import lloyds
from kmeans import plot

def test_dataset(cmdopt):
    check1 = False
    check2 = False

    df = pd.read_excel(cmdopt)
    if df is not None: 
        check1 = True
    if len(df.columns) > 5:
        check2 = True
    if check1 != True or check2 != True:
       pytest.fail("{}".format("Not a valid dataset"))

def test_center_inits():
	data = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
	distances = [(0,0.1),(1,0.2), (2, 0.3), (3,0.4), (4, 0.5), (5, 0.6)]
	centers, center_lists = getCenters(data, distances, 5)
	if len(centers) != len(center_lists) or len(centers) != 4:
		pytest.fail("{}".format("Centers and center lists are not initialized correctly."))

def test_alpha_int():
	data = None
	labels = [0,1,2,3,1,2,4]
	alphas = computeAlpha(data, labels)
	if len(alphas) !=5:
		pytest.fail("{}".format("Alphas list not initialized correctly."))
	if alphas[0] != 1 or alphas[1] != 2 or alphas[2] != 2 or alphas[3] != 1 or alphas[4] != 1:
		pytest.fail("{}".format("Incorrect alpha count."))

def test_data_after_processing():
	data = []
	num = 5
	res = lloyds(data, 5)
	if res != None:
		pytest.fail("{}".format("Empty data after preprocessing not detected."))

def test_before_plot():
	centers = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
	center_lists = [[],[(3, 4)], [(1, 2)], [(7, 8)], [(9, 10)]]
	res = plot(centers, center_lists)
	if res != None:
		pytest.fail("{}".format("Error in cluster assignment not detected."))
	
