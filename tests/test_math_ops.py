import sys
import os
import pandas as pd
import pytest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from mypackage import DataFrameMathOps

@pytest.fixture
def dfs():
    df1 = pd.DataFrame([[1, 2], [3, 4]])
    df2 = pd.DataFrame([[5, 6], [7, 8]])
    return df1, df2

def test_add(dfs):
    df1, df2 = dfs
    result = DataFrameMathOps.add(df1, df2)
    expected = pd.DataFrame([[6, 8], [10, 12]])
    pd.testing.assert_frame_equal(result, expected)

def test_subtract(dfs):
    df1, df2 = dfs
    result = DataFrameMathOps.subtract(df1, df2)
    expected = pd.DataFrame([[-4, -4], [-4, -4]])
    pd.testing.assert_frame_equal(result, expected)

def test_multiply(dfs):
    df1, df2 = dfs
    result = DataFrameMathOps.multiply(df1, df2)
    expected = pd.DataFrame([[5, 12], [21, 32]])
    pd.testing.assert_frame_equal(result, expected)

def test_divide(dfs):
    df1, df2 = dfs
    result = DataFrameMathOps.divide(df1, df2)
    expected = pd.DataFrame([[0.2, 0.333333], [0.428571, 0.5]])
    pd.testing.assert_frame_equal(result, expected, rtol=1e-4)
