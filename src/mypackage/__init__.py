"""mypackage: Basic arithmetic operations on pandas DataFrames."""

from .math_ops import DataFrameMathOps

# Optional: function aliases for backward compatibility
add = DataFrameMathOps.add
subtract = DataFrameMathOps.subtract
multiply = DataFrameMathOps.multiply
divide = DataFrameMathOps.divide
