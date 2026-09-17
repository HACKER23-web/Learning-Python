classmates=['Michael','Bob','Tracy']
print(classmates)
print(len(classmates))

#列表的下标从0开始
print(classmates[0],classmates[1], classmates[2])

#-1表示倒数第一个元素，-2表示倒数第二个元素，以此类推但是不能超过列表的大小
print(classmates[-1], classmates[-2], classmates[-3])

#在尾部进行插入
classmates.append('Adam')
print(classmates)

#对指定位置进行插入
classmates.insert(1,'Jack')
print(classmates)

#删除表尾的元素
classmates.pop()
print(classmates)

#删除指定下标的元素
classmates.pop(1)
print(classmates)

#直接对指定下标的元素进行修改
classmates[1]='Sarah'
print(classmates)

#list的元素不一定要是同类型的
L=['Apple',123,True]
print(L)

#list里面还可以存list
s=['python','java',['asp','php'],'scheme']
print(len(s))
print(s[0],s[1],s[2][0],s[2][1])

#tuple,tuple里的元素一旦初始化就不能修改，获取元素的方式和list一样
t=('Michael','Bob','Tracy')
print(t)

#只有1个元素的tuple定义时必须加一个逗号,否则括号()既可以表示tuple，又可以表示数学公式中的小括号
t1=(1,)
print(t1)


output:
['Michael', 'Bob', 'Tracy']
3
Michael Bob Tracy
Tracy Bob Michael
['Michael', 'Bob', 'Tracy', 'Adam']
['Michael', 'Jack', 'Bob', 'Tracy', 'Adam']
['Michael', 'Jack', 'Bob', 'Tracy']
['Michael', 'Bob', 'Tracy']
['Michael', 'Sarah', 'Tracy']
['Apple', 123, True]
4
python java asp php
('Michael', 'Bob', 'Tracy')
(1,)
