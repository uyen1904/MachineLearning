import pandas as pd
from pandas import NA #lấy hằng số NA (giá trị missing/thiếu trong pandas

data=pd.DataFrame([[1.,6.5,3.], #tạo một dataframe (bảng dữ liệu) từ list các list
                   [1.,NA,NA],
                   [NA,NA,NA],
                   [NA,6.5,3.]])
print(data)
print("-"*10) #in 10 dấu gạch ngang để phân cách dữ liệu ban đầu và kết quả sau khi chạy
cleaned=data.dropna() #dropna() mặc định xoá các dòng nào có ít nhất 1 giá trị NA
print(cleaned)
cleaned2=data.dropna(how='all') #xoá những dòng mà tất cả các cột đều NA => chỉ có hàng 2
print(cleaned2)