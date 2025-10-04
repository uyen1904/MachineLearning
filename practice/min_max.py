import pandas as pd


class MyStatistic:
    def find_orders_within_range(self, df, minValue, maxValue, sortType=True):
        """
        Tìm các đơn hàng có tổng giá trị trong khoảng [minValue, maxValue]

        Parameters:
        - df: DataFrame chứa dữ liệu đơn hàng
        - minValue: Giá trị tối thiểu
        - maxValue: Giá trị tối đa
        - sortType: True (sắp xếp tăng dần), False (sắp xếp giảm dần)

        Returns:
        - List of tuples: [(OrderID, Sum), ...]
        """
        # Tính tổng giá trị từng đơn hàng
        # Giả sử df có cột 'OrderID' và 'Sum' hoặc tương tự
        if 'Sum' in df.columns:
            order_totals = df.groupby('OrderID')['Sum'].sum()
        elif 'UnitPrice' in df.columns and 'Discount' in df.columns:
            order_totals = df.groupby('OrderID').apply(
                lambda x: (x['UnitPrice'] * (1 - x['Discount'])).sum()
            )
        else:
            # Trường hợp đơn giản: chỉ có OrderID và Sum
            order_totals = df.set_index('OrderID')['Sum']

        # Lọc đơn hàng trong khoảng [minValue, maxValue]
        orders_within_range = order_totals[
            (order_totals >= minValue) & (order_totals <= maxValue)
            ]

        # Sắp xếp theo sortType
        if sortType:
            # True: sắp xếp tăng dần
            orders_within_range = orders_within_range.sort_values(ascending=True)
        else:
            # False: sắp xếp giảm dần
            orders_within_range = orders_within_range.sort_values(ascending=False)

        # Trả về list of tuples (OrderID, Sum)
        result = [(order_id, total) for order_id, total in orders_within_range.items()]

        return result
