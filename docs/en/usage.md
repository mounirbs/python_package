# Usage

```python
import pandas as pd
from mypackage import add, subtract, multiply, divide

df1 = pd.DataFrame([[1, 2], [3, 4]])
df2 = pd.DataFrame([[5, 6], [7, 8]])

print(add(df1, df2))
print(subtract(df1, df2))
print(multiply(df1, df2))
print(divide(df1, df2))
```

## Example

You can run the example script without installing the package:

```sh
python -m examples/example_usage.py
```
