import pandas as pd

from practice.min_max import MyStatistic

# Tạo DataFrame mẫu
data = {
    'OrderID': ['OrderID1', 'OrderID2', 'OrderID3'],
    'Sum': [500, 800, 900]
}
df = pd.DataFrame(data)

# Hoặc đọc từ file CSV thật
# df = pd.read_csv('../dataset/SalesTransactions/SalesTransactions.csv')

# Khởi tạo class
stats = MyStatistic()

# Nhập giá trị min và max
minValue = float(input("Nhập giá trị min: "))
maxValue = float(input("Nhập giá trị max: "))
sortType = input("Sắp xếp tăng dần? (True/False): ").strip().lower() == 'true'

# Gọi hàm và hiển thị kết quả
result = stats.find_orders_within_range(df, minValue, maxValue, sortType)

print(f"\nSortType={sortType}")
print(f"Các đơn hàng trong khoảng [{minValue}, {maxValue}]:")
print("-" * 40)
for order_id, total in result:
    print(f"{order_id}: {total}")