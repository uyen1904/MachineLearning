#khi viết mô hình lớp là để sử dụng cho mọi nơi nên test product trong file py khác
from review.review_list import Product

p1=Product("p1","Juice",19,20.000)
print(p1) #->auto invoke __str__

p2=Product() #lúc này các thuộc tính không được gán giá trị nên bị None --> không sài được => bắt buộc ta phải làm thủ công
p2.id="p2"
p2.name="water"
p2.quantity="4"
p2.price="10.000" #nếu không gán giá trị price thì khi chạy ra price sẽ hiện None
print(p2)