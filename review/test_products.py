from review.products import ListProduct
from review.review_list import Product

lp=ListProduct()
lp.add_product(Product("p1","Juice",19,20.000))
lp.add_product(Product("p2","Water",4,10.000))
lp.add_product(Product("p3","Detox",20,12.000))
lp.add_product(Product("p4","Coca",9,12.000))
lp.print_products()

#CÁCH 3
lp.sort_desc_price()
print("---List Products - Sort Desc Price:-----")
lp.print_products()

#CÁCH 1
#sắp xếp products theo giá giảm dần
"""print("\n Sắp xếp theo giá giảm dần:")
lp.sort_by_price_desc()
lp.print_products()"""
#sắp xếp list products theo giá tăng dần, nếu giá bằng nhau thì sắp xếp theo thứ tự giảm dần
"""print("\n Sắp xếp theo giá tăng dần, nếu giá bằng nhau thì sắp xếp theo số lượng giảm dần:")
lp.sort_by_price_asc_then_quantity_desc()
lp.print_products()"""

#CÁCH 2
"""print("\n Sắp xếp theo giá giảm dần:")
for p in sorted(lp.products, key=lambda x:x.price, reverse=True):
    print(p)

print("\n Sắp xếp theoo giá tăng dần, nếu giá bằng nhau thì sắp xếp theo số lượng giảm dần:")
for p in sorted(lp.products, key=lambda  x:(x.price, -x.quantity)):
    print(p)"""
