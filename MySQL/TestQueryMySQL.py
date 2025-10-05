import mysql.connector

server="localhost"
port=3306
database="studentmanagement"
username="root"
password="yune1904@"

conn=mysql.connector.connect( #lệnh connect() sẽ trr về một MySQLConnection
                host=server,
                port=port,
                database=database,
                user=username,
                password=password)

#1.Truy vấn toàn bộ Sinh viên
cursor=conn.cursor()
sql="select * from student"
cursor.execute(sql)
dataset=cursor.fetchall()
align='{0:<3} {1:<6} {2:<15} {3:<10}'
print(align.format('ID','Code','Name','Age'))
for item in dataset:
    id=item[0]
    code=item[1]
    name=item[2]
    age=item[3]
    avatar=item[4]
    intro=item[5]
    print(align.format(id,code,name,age))
cursor.close()

#2.Truy vấn các Sinh viên có độ tuổi từ 15 đến 20
cursor=conn.cursor()
sql="select * from student where Age>=15 and Age<=20"
cursor.execute(sql)
dataset=cursor.fetchall()
align='{0:<3} {1:<6} {2:<15} {3:<10}'
print(align.format('ID','Code','Name','Age'))
for item in dataset:
    id=item[0]
    code=item[1]
    name=item[2]
    age=item[3]
    avatar=item[4]
    intro=item[5]
    print(align.format(id,code,name,age))
cursor.close()

#3.Truy vấn toàn bộ sinh viên và sắp xếp theo tuổi tăng dần
cursor=conn.cursor()
sql="select * from student "\
    "order by Age asc"
cursor.execute(sql)
dataset=cursor.fetchall()
align='{0:<3} {1:<6} {2:<15} {3:<10}'
print(align.format('ID','Code','Name','Age'))
for item in dataset:
    id=item[0]
    code=item[1]
    name=item[2]
    age=item[3]
    avatar=item[4]
    intro=item[5]
    print(align.format(id,code,name,age))
cursor.close()

#4.Truy vấn các Sinh viên có độ tuổi từ 15 tới 20 và sắp xếp theo tuổi giảm dần
cursor=conn.cursor()
sql="select * from student "\
    "where Age>=15 and Age<=20 "\
    "order by Age desc"
cursor.execute(sql)
dataset=cursor.fetchall()
align='{0:<3} {1:<6} {2:<15} {3:<10}'
print(align.format('ID','Code','Name','Age'))
for item in dataset:
    id=item[0]
    code=item[1]
    name=item[2]
    age=item[3]
    avatar=item[4]
    intro=item[5]
    print(align.format(id,code,name,age))
cursor.close()

#5.Truy vấn chi tiết thông tin Sinh viên khi biết Id
cursor=conn.cursor()
sql="select * from student "\
    "where ID=1"
cursor.execute(sql)
dataset=cursor.fetchone()
if dataset!=None:
    Id,Name,Code,Age,Avatar,Intro=dataset
    print("ID=",Id)
    print("Code=",Code)
    print("Name=",Name)
    print("Age=",Age)
cursor.close()

#6.Truy vấn dạng phân trang Student (truy vấn 3 dòng dữ liệu đầu tiên)
cursor=conn.cursor()
sql="select * from student LIMIT 3 OFFSET 0" #LIMIT: số phần tử mà ta muốn truy vấn, OFFSET: vị trí mà ta bắt đầu truy vấn
cursor.execute(sql)
dataset=cursor.fetchall()
align='{0:<3} {1:<6} {2:<15} {3:<10}'
print(align.format('ID','Code','Name','Age'))
for item in dataset:
    id=item[0]
    code=item[1]
    name=item[2]
    age=item[3]
    avatar=item[4]
    intro=item[5]
    print(align.format(id,code,name,age))
cursor.close()

#7.Truy vấn dạng phân trang Student (truy vấn 3 dòng dữ liệu cuối cùng)
cursor = conn.cursor()
sql="SELECT * FROM student LIMIT 3 OFFSET 3"
cursor.execute(sql)
dataset=cursor.fetchall()
align='{0:<3} {1:<6} {2:<15} {3:<10}'
print(align.format('ID', 'Code','Name',"Age"))
for item in dataset:
    id=item[0]
    code=item[1]
    name=item[2]
    age=item[3]
    avatar=item[4]
    intro=item[5]
    print(align.format(id,code,name,age))
cursor.close()

#8.Giả sử ta có N dòng Sinh viên, mỗi lần truy vấn là 3 sinh viên,
#hãy viết lệnh SQL để chương trình Paging toàn bộ dữ liệu N dòng này
print("PAGING ĐI!!!")
cursor=conn.cursor()
sql="Select count(*) from student"
cursor.execute(sql)
dataset=cursor.fetchone()
rowcount=dataset[0]

limit=3
step=3
for offset in range(0,rowcount,step):
    sql=f"Select * from student LIMIT {limit} OFFSET {offset}"
    cursor.execute(sql)

    dataset=cursor.fetchall()
    align='{0:<3} {1:<6} {2:<15} {3:<10}'
    print(align.format('ID', 'Code','Name',"Age"))
    for item in dataset:
        id=item[0]
        code=item[1]
        name=item[2]
        age=item[3]
        avatar=item[4]
        intro=item[5]
        print(align.format(id,code,name,age))

cursor.close()

#Mã lệnh ở trên hay ở chỗ nào?
#Hay ở chỗ nếu như ta muốn phân trang bao nhiêu phần tử thì chỉ cần đổi limit và offset là được.
#Ví dụ như muốn phân trang mỗi lần chạy truy vấn 50 Sinh viên thì đổi limit=50 và step=50
#(Bạn thấy Gmail không? email rất nhiều,
#nhưng mỗi lần họ cho truy vấn xem 50 email, muốn xem trước sau thì bấm nút. Đó là minh họa PAGING)

#9.Thêm mới 1 Student
cursor=conn.cursor()
sql="insert into student (code,name,age) values (%s,%s,%s)"
val=("sv05","yune nae",20)
cursor.execute(sql,val)
conn.commit()
print(cursor.rowcount,"recode inserted")
cursor.close()

#10.Thêm mới nhiều Student
cursor=conn.cursor()
sql="insert into student (code,name,age) values (%s,%s,%s)"
val=[
    ("sv06","hihi",21),
    ("sv07","kk",18),
    ("sv08","hẹ hẹ",21),
    ]
cursor.executemany(sql,val)
conn.commit()
print(cursor.rowcount,"record inserted")
cursor.close()

#11.Cập nhật tên Sinh viên có Code=’sv07′ thành tên mới "nina"
cursor = conn.cursor()
sql="update student set name='nina' where Code='sv07'"
cursor.execute(sql)
conn.commit()
print(cursor.rowcount," record(s) affected")

#12.Cập nhật tên Sinh viên có Code=’sv05′ thành tên mới “nae nae"
cursor = conn.cursor()
sql="update student set name=%s where Code=%s"
val=('nae nae','sv05')

cursor.execute(sql,val)

conn.commit()

print(cursor.rowcount," record(s) affected")

#13.Xóa Student có ID=14
conn = mysql.connector.connect(
                host=server,
                port=port,
                database=database,
                user=username,
                password=password)
cursor = conn.cursor()
sql="DELETE from student where ID=14"
cursor.execute(sql)
conn.commit()
print(cursor.rowcount," record(s) affected")

#14.Xóa Student có ID=13 với SQL Injection
conn = mysql.connector.connect(
                host=server,
                port=port,
                database=database,
                user=username,
                password=password)
cursor = conn.cursor()
sql = "DELETE from student where ID=%s"
val = (13,)
cursor.execute(sql, val)
conn.commit()
print(cursor.rowcount," record(s) affected")