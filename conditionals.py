age=20
if age>=18:
  print('your age is',age)
  print('you are an adult')        
else:
  print('your age is %d' % age)      #这里用不同的表示方式用来复习前面的内容
  print('you are a teenager')

#注意不要少写了冒号:

age = 3
if age >= 18:
    print('adult')
elif age >= 6:             # elif等于else if
    print('teenager')
else:
    print('kid')

if x:                  #如果x为0或为空，则不会输出。否则输出True
    print('True')

s = input('birth: ')      #注意input返回的数据类型是str，不能和整数进行比较，所以要先转换成整形，否则就会报错
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')


