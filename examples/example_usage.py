import sys
import os
import pandas as pd

# Add src to sys.path for local testing without package installation
#sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from mypackage import DataFrameMathOps, add, subtract, multiply, divide

df1 = pd.DataFrame([[1, 2], [3, 4]])
df2 = pd.DataFrame([[5, 6], [7, 8]])

print("Addition (class):\n", DataFrameMathOps.add(df1, df2))
print("Subtraction (class):\n", DataFrameMathOps.subtract(df1, df2))
print("Multiplication (class):\n", DataFrameMathOps.multiply(df1, df2))
print("Division (class):\n", DataFrameMathOps.divide(df1, df2))

print("Addition (alias):\n", add(df1, df2))
print("Subtraction (alias):\n", subtract(df1, df2))
print("Multiplication (alias):\n", multiply(df1, df2))
print("Division (alias):\n", divide(df1, df2))
