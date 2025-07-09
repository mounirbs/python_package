"""Provides DataFrameMathOps class for arithmetic operations on pandas DataFrames."""

import pandas as pd

class DataFrameMathOps:
    """
    Provides static methods for element-wise arithmetic operations on pandas DataFrames.
    """

    @staticmethod
    def add(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        """
        Element-wise addition of two pandas DataFrames.

        Args:
            df1 (pd.DataFrame): The first DataFrame.
            df2 (pd.DataFrame): The second DataFrame.

        Returns:
            pd.DataFrame: The result of adding df1 and df2 element-wise.
        """
        return df1.add(df2)

    @staticmethod
    def subtract(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        """
        Element-wise subtraction of two pandas DataFrames.

        Args:
            df1 (pd.DataFrame): The first DataFrame.
            df2 (pd.DataFrame): The second DataFrame.

        Returns:
            pd.DataFrame: The result of subtracting df2 from df1 element-wise.
        """
        return df1.sub(df2)

    @staticmethod
    def multiply(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        """
        Element-wise multiplication of two pandas DataFrames.

        Args:
            df1 (pd.DataFrame): The first DataFrame.
            df2 (pd.DataFrame): The second DataFrame.

        Returns:
            pd.DataFrame: The result of multiplying df1 and df2 element-wise.
        """
        return df1.mul(df2)

    @staticmethod
    def divide(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
        """
        Element-wise division of two pandas DataFrames.

        Args:
            df1 (pd.DataFrame): The first DataFrame.
            df2 (pd.DataFrame): The second DataFrame.

        Returns:
            pd.DataFrame: The result of dividing df1 by df2 element-wise.
        """
        return df1.div(df2)
