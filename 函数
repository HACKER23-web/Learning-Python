#调用函数

#abs函数
print(abs(-100))
print(abs(12.34))

#max函数
print(max(2,3,1,-5))

a=abs
a(-1)
print(a(-1))

#练习hex()函数把一个整数转换成16进制表示的字符串
n1=255
n2=1000
print(hex(n1))
print(hex(n2))

#######################################################
#定义函数
import math  #表示引入数学函数包
age=20
if age>=18:
    pass

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x>=0:
        return x
    else:
        return -x

print(my_abs(-99))

#返回多个值
def move(x,y,step,angle=0):
    nx= x + step * math.cos(angle)
    ny= y - step * math.sin(angle)
    return nx, ny

x, y=move(100,100,60,math.pi / 6)
print(x, y)

returns = move(100, 100, 60, math.pi / 6)
print(returns)  #返回的是一个tuple

#练习
def quadratic(a, b, c):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError('bad operand type')
    z1=(-b + math.sqrt(b * b -4 * a * c)) / (2 * a)
    z2=(-b - math.sqrt(b * b -4 * a * c)) / (2 * a)
    return z1, z2
print('quadratic(2, 3, 1)=',quadratic(2, 3, 1))
print('quadratic(1, 3, -4)=',quadratic(1, 3, -4))

if quadratic(2, 3, 1) != ( -0.5, -1.0):
    print('测试失败!')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败!')
else:
    print('测试成功!')

###########################################################
#函数的参数
  
#计算x的n次方
def power(x, n):  
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print(power(5, 3)) #125
print(power(5, 2)) #25

def power1(x, n=2):  #如果把n的默认值设置为2，那么当调用power1(5)时，n就会被赋值为2
    s=1
    while n>0:
        n=n-1
        s=s*x
    return s
print(power1(5)) #25
print(power1(5, 3)) #125

def add_end(L=[]):
    L.append('END')
    return L

print(add_end([1,2,3]))
add_end()
add_end()
add_end()
print(add_end())
#Python函数在定义的时候，
#默认参数L的值就被计算出来了，即[]，
#因为默认参数L也是一个变量，它指向对象[]，
#每次调用该函数，如果改变了L的内容，则下次调用时，
#默认参数的内容就变了，不再是函数定义时的[]了。

def add_end1(L=None):
    if L is None:
        L=[]
    L.append('END')
    return L
add_end1()
add_end1()
print(add_end1()) #['END']

#可变参数
def calc(*numbers):  #在函数内部，参数numbers接收到的是一个tuple
    sum=0
    for n in numbers:
        sum=sum+n*n
    return sum
print(calc(1,2)) #5
nums=[1,2,3]
print(calc(*nums)) #14

#关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

print(person('Michael', 30))
print(person('Bob', 35, city='Beijing'))
print(person('Adam', 45, gender='M', job='Engineer'))

extra={'city': 'Beijing', 'job': 'Engineer'}
print(person('Jack',24,city=extra['city'],job=extra['job']))
print(person('Jack', 24, **extra)) #**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

#命名关键字参数
def person1(name,age,**kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)

print(person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456))

def person2(name,age,*,city,job):
    print( name,age, city,job)

#city和job是关键字参数，如果缺少*则无法识别位置参数和关键字参数

print(person2('Jack', 24, city='Beijing', job='Engineer')) 

def person3(name, age, *args, city='Shanghai', job):
    print(name, age, args, city, job)

print(person3('Jack', 24,  job='Engineer')) #args接收的是一个tuple，city和job必须传入参数名

#参数组合

def f1(a, b, c=0, *args, **kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)
print(f1(1,2,0,'Hello',name='mike',age=18,gender='M'))

def f2(a,b,c=0,*,d,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'kw=',kw)
print(f2(1,2,d=99,city='shanghai',weather='hot',temperature='38'))

args=(1,2,3,4)
kw={'d':99,'x':'#'}
print(f1(*args,**kw))
args=(1,2,3)
kw={'d':88,'x':'#'}
print(f2(*args,**kw))

#练习
def mul(*num):
    if not num:
        raise TypeError('mul() 至少需要一个参数')
    sum=1
    for n in num:
        sum=sum*n
    return sum
print('mul(5) =', mul(5))
print('mul(5, 6) =', mul(5, 6))
print('mul(5, 6, 7) =', mul(5, 6, 7))
print('mul(5, 6, 7, 9) =', mul(5, 6, 7, 9))
if mul(5) != 5:
    print('mul(5)测试失败!')
elif mul(5, 6) != 30:
    print('mul(5, 6)测试失败!')
elif mul(5, 6, 7) != 210:
    print('mul(5, 6, 7)测试失败!')
elif mul(5, 6, 7, 9) != 1890:
    print('mul(5, 6, 7, 9)测试失败!')
else:
    try:
        mul()
        print('mul()测试失败!')
    except TypeError:
        print('测试成功!')
#########################################################################
#递归函数
def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

print(fact(5))
# =>fact(5)
# => 5 * fact(4)
# => 5 * (4 * fact(3))
# => 5 * (4 * (3 * fact(2)))
# => 5 * (4 * (3 * (2 * fact(1))))
# => 5 * (4 * (3 * (2 * 1)))
# => 5 * (4 * (3 * 2))
# => 5 * (4 * 6)
# => 5 * 24
# => 120

def fact1(n):
    return fact_iter(n,1)

def fact_iter(num,product):
    if num==1:
        return product
    return fact_iter(num-1,num* product)

print(fact1(5))

#练习
#汉诺塔
def move(n,a,b,c):
    if(n==1):
        print(a, '-->', c)
    else:
        move(n-1,a,c,b)
        print(a, '-->', c)
        move(n-1,b,a,c)

print(move(3,'A','B','C'))


