# Cannot mask with non-boolean array containing NA / NaN values

import pandas as pd

df = pd.DataFrame({
    'first_name': ['Alice', 'Bobby', 'Carl', None],
    'salary': [175.1, 180.2, 190.3, 205.3],
    'experience': [10, 15, 20, 25]
})


result = df[df['first_name'].str.contains('Bob', na=False)]

#   first_name  salary  experience
# 1      Bobby   180.2          15
print(result)