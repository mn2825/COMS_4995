import pandas as pd
import pytest

#trying to trigger workflow w this comment
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
