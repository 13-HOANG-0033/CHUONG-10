#bài 10.1
a=int(input('a= '))
b=int(input('b= '))
c=int(input("c= "))
d=int(input('d= '))
S=[a,b,c,d]
print("Giá trị lớn nhất : ",max(S))
print("Giá trị nhỏ nhất: ",min(S))

#bài 10.2
# Tìm |x| bằng cách sử dụng hàm thư viện
x=int(input('Nhập số nguyên x : '))
print("Giá trị tuyệt đối của",x,"là:",abs(x))

#bài 10.3
import math
#Nhập vào số nguyên n
print("Nhập n :")
n=int(input())
#Nhập vào số thực x
print("Nhập x :")
x=float(input())
S=math.pow((math.pow(x,2)+1),n)
print("S=(x*x + 1)^n =",S)

#bài 10.4
import math
#Nhập vào số nguyên n
print("Nhập n:")
n=int(input())
#Nhập vào số thực x3
print("Nhập x:")
x=float(input())
A=math.pow(math.pow(x,2)+x+1,n)+math.pow(math.pow(x,2)-x+1,n)
print("A=(x*x +x+1)^n + (x*x -x + 1)^n =",A)

#bài 10.5
def kiem_tra_ma_zip(z):
    if len(z)==6 and z.isdigit()==True:
        return True
    else:
        return False
z=input("Nhập mã zip :")
print(kiem_tra_ma_zip(z))

#bài 10.6
#Hàm giải phương trình bậc 2
import math
def giaiptb2(a,b,c):
    if(a==0):
        if b==0:
            print("Phương trình vô nghiệm!")
        else:
            print("Phương trình có một nghiệm: x = ",(-c/b))
        return
    delta = b*b-4*a*c
    if delta > 0:
        x1= float((-b+math.sqrt(delta))/(2*a))
        x2=float((-b-math.sqrt(delta))/(2*a))
        print("Phương trình có 2 nghiệm là: x1 = ",x1,"và x2 = ",x2)
    elif delta==0:
        x=-b/(2*a)
        print("Phương trình có nghiệm là : x1 = x2 = ",x)
    else:
        print("Phương trình vô nghiệm!")        
a=float(input("a = "))
b=float(input("b = "))               
c=float(input("c = "))
giaiptb2(a,b,c)

#bài 10.7
s=input("Nhập chuỗi s: ")
s_sub=input("Nhập chuỗi con s_sub: ")
s_find=input("Nhập chuỗi s_find: ")
s_replace=input("Nhập chuỗi thay thế s_replace: ")
print("Chuỗi s :",s)
print("Loại bỏ khoảng trắng ở đầu và cuối: ",s.strip())
print("Chuỗi s_find với kí tự đầu viết hoa: ",s_find.capitalize())
print("Số lần s_sub xuất hiện trong s :",s.count(s_sub,0,16))
print("Thay thế s_find bằng s_replace : ",s.replace(s_find,s_replace))

#bài 10.8
ng=int(input('Nhập ngày: '))
t=int(input('Nhập tháng: '))
n=int(input('Nhập năm: '))
from datetime import datetime
a=datetime(n,t,ng)
print("Ngày tháng năm vừa nhập: ",a.strftime("%d-%m-%Y"))
import calendar
if calendar.isleap(n)==True:
    print("Năm",n,"là năm nhuận")
else:
    print("Năm",n,"không phải là năm nhuận")    
if calendar.weekday(n,t,ng)==0:
    print(a.strftime("%d-%m-%Y"),"là thứ 2")
elif calendar.weekday(n,t,ng)==1:
    print(a.strftime("%d-%m-%Y"),"là thứ 3") 
elif calendar.weekday(n,t,ng)==2:
    print(a.strftime("%d-%m-%Y"),"là thứ 4")
elif calendar.weekday(n,t,ng)==3:
    print(a.strftime("%d-%m-%Y"),"là thứ 5")
elif calendar.weekday(n,t,ng)==4:
    print(a.strftime("%d-%m-%Y"),"là thứ 6")
elif calendar.weekday(n,t,ng)==5:
    print(a.strftime("%d-%m-%Y"),"là thứ 7")
else:
    print(a.strftime("%d-%m-%Y"),"là chủ nhật")
print("Số ngày trong tháng",t,"là:",calendar.monthrange(n,t))