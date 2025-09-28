import pandas as pd
from pandas import NA

from data_processing.filtering import cleaned

data=pd.DataFrame([[1.,6.5,3.],
                   [1.,NA,NA],
                   [NA,NA,NA],
                   [NA,6.5,3.]])
print(data)
print("-"*10)
cleaned=data.fillna(data.mean()) #tính giá trị trung bình theo cột (bỏ qua NA)
                                 #tính từ cột có chứa NA: cột 0: (1.0 + 1.0)/2=1.0
                                                         #cột 1: (6.5 + 6.5) / 2 = 6.5
                                                         #cột 2: (3.0 + 3.0) / 2 = 3.0
print(cleaned)