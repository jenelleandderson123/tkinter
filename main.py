import pandas as pd
import numpy as np

exam_data = {
    'name': ['Anastasia', 'Dima','Mathew', 'Sam', 'Kayla', 'Joseph','Michael', 'Jordyn', 'Hope','Faith'],
    'Score' : [12.5, 16, 18, 5, np.nan, 15, 7, 19, 20,3, np.nan],
    'attempt' : [1, 3 , 2, 1 , 3, 3, 1, 2, 1, 3, 2, 2],
    'qualify': ['yes', 'yes', 'yes','no', 'no','yes','no','yes', 'yes','yes', 'no' ,'yes']

}
labels = ['a', 'b','c','d','e', 'f', 'g','h','i', 'j','k','l']
df = pd.DataFrame(exam_data, index = labels)

print
print("Data Frame")
print(df.sort_values(by = 'Score', ascending = False))
print(df)
print("\nSummary of basic info")
df.info()