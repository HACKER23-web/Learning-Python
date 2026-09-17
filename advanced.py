#切片
L=['Michael','Sarah','Tracy','Bob','Jack']
print(L[0:3])  #L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
#0可以省略
print(L[:3])

print(L[-2:])     #从倒数第2个开始，一直到末尾（冒号后没写=取到底）
print(L[-2:-1])   # 从倒数第2个开始，到倒数第1个为止（但不包含它）

L=list(range(100))

print(L[:10])

print(L[10:20])#前11-20个数
print(L[:10:2])#前10个数，每两个取一个
print(L[::5])#所有数，没5个取一个

print(L[:])#复制一个list

L1=(0,1,2,3,4,5)#tuple
print(L1[:3])

L2='ABCDEFG' #字符串
print(L2[:3])
print(L2[::2])

#练习
def trim(s):
    while s[:1]==' ':
        s=s[1:]
    while s[-1:]==' ':
        s=s[:-1]
    return s

# 测试:
if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
#################################################################
#迭代
d={'a':1,'b':2,'c':3}
for key in d:
    print(key)


#练习
def findMinAndMax(L):
    if not L:
        return (None,None)
    max=L[0]
    min=L[0]
    for res in L:
        if res>max:
            max=res
        if res<min:
            min=res
    return (min,max)

# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
###################################################
#列表生成式
# x*x是要生成的东西写在最前面
print([ x*x for x in range(1,11)])

#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方
print([x*x for x in range(1,11) if x%2==0])

#还可以使用两层循环，可以生成全排列
print([m+n for m in 'ABC' for n in 'XYZ'])

#for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value
d={'x': 'A','y':'B','z': 'C'}
for k,v in d.items():
    print(k, '=' ,v)

#列表生成式也可以使用两个变量来生成list
print([k + '=' + v for k,v in d.items()])

#把一个list中所有的字符串变成小写
L=['Hello','World','IBM','Apple']
print([s.lower() for s in L])

#如果想用if...else语句就要放在前面并且缺一不可
print([x if x%2==0 else -1 for x in range(1,11)])

#练习
L1 = ['Hello', 'World', 18, 'Apple', None]
L2=[x.lower() for x in L1 if isinstance(x,str)]

# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')
