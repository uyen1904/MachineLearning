class ListProduct:
    def __init__(self):
        self.products=[] #có cấp phát ô nhớ cho products quản lý nhưng chưa có data
                         #nếu là self.product=None thì không cấp ô nhớ cho products quản lý
    def add_product(self,p):
        self.products.append(p)
    def print_products(self):
        for p in self.products:
            print(p)

#CÁCH 1
    """def sort_by_price_desc(self):
        self.products.sort(key=lambda p: p.price,reverse=True)
    def sort_by_price_asc_then_quantity_desc(self):
        self.products.sort(key=lambda  p:(p.price, -p.quantity))""" #cách này hoặc dùng cách khác, tuwc là chỉ thêm code trong test_products

#CÁCH 3
    def sort_desc_price(self):
        for i in range(0,len(self.products)):
            for j in range(i+1, len(self.products)):
                pi=self.products[i]
                pj=self.products[j]
                if pi.price < pj.price:
                    self.products[i]=pj
                    self.products[j]=pi