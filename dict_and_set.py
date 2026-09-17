#dict
d={'Michael':95,'Bob':75,'Tracy':85}
for name,score in d.items():
    print(name,score)

#判断key是否存在的两种方法：
#1
if 'Thomas' in d:
    print(d['Thomas'])
else:
    print('Not found')
#2
print(d.get('Thomas')) #如果key不存在，返回None
print(d.get('Thomas',-1)) #如果key不存在，返回-1

###################################

print(d)
a=d.pop('Bob')     #弹出key为'Bob'的键值对，并返回其值
print(a)
print(d)

#set
s={1,2,3,3,3,2} #集合中的元素是唯一的
print(s)

s=set([1,2,3]) #通过set()函数创建集合
print(s)

s.add(4)#添加元素
print(s)

s.remove(2)#删除元素
print(s)

s1={1,2,3}
s2={2,3,4}
print(s1&s2)##交集
print(s1|s2)##并集

a='abc'
a.replace('a','A') #字符串是不可变对象，所有操作会创建新的字符串
print(a) #原字符串没有改变

b=a.replace('a','A') #返回新的字符串
print(b) #原字符串没有改变
print(a) #原字符串没有改变

以上代码的全部输出内容：
Michael 95
Bob 75
Tracy 85
Not found
None
-1
{'Michael': 95, 'Bob': 75, 'Tracy': 85}
75
{'Michael': 95, 'Tracy': 85}
{1, 2, 3}
{1, 2, 3}
{1, 2, 3, 4}
{1, 3, 4}
{2, 3}
{1, 2, 3, 4}
abc
Abc
abc
