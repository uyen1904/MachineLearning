import pandas as pd


class MyStatistic:
    def find_orders_within_range(self, df, minValue, maxValue, orders_within_range=None):
        #tổng giá trị từng đơn hàng
        order_totals=df.groupby('OrderID').apply(lambda x:(x['UnitPrice']*(1-x['Discount'])).sum())
        #lọc đơn hàng trong range
        order_within_range=order_totals[(order_totals >=minValue) & (order_totals <=maxValue)]
        #danh sách các mã đơn hàng không trùng nhau
        unique_orders=df[df['OrderID'].isin(orders_within_range.index)]['OrderID'].drop_duplicates().tolist()
        
        return unique_orders
    df=pd.read_csv('../dataset/SalesTransactions/SalesTransactions.csv')
    
    minValue=float(input("Nhập giá trị min:"))
    maxValue=float(input("Nhập giá trị max:"))
    result=find_orders_within_range(df,minValue, maxValue)
    print('Danh sách các hoá đơn trong phạm vi giá trị từ',minValue,'đến',maxValue,'là:',result)
