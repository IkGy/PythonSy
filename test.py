import keyword
print(keyword.kwlist)
# thisClass 클래스는 이런식으로 작성
print(type("ddd"))

print(type(10000))
print(type(False))

print('test')
print('''
t
e
s
t''')
print('================')
print('t\ne\ns\nt')
print('================')
print("test'test'test")
print('test\'test\'test')
print('================')
print('test \
  test\
    test\
      test')
print(3*'text3')
item = '안녕하세요'

print(item[0])
print(item[1])
print(item[2])
print(item[3])
print(item[4])
print('================')
print(item[-1])
print(item[-2])
print(item[-3])
print(item[-4])
print(item[-5])
print('================')
#[시작(포함):끝(미포함 앞에까지)]
print(item[0:2])#안녕
print(item[-5:-1])#안녕하세
print(item[-5:])#안녕하세요
print(item[-4:4])#녕하세
print(item[-4:])#녕하세요
print(item[:4])#안녕하세
print(item[:])#안녕하세요
print('================')
# print(item.len)#error
print(len(item))#5
print('=======================')
list = [0,1,2,3,4]
for i in list: print(item[i])

pi = 3.14159265
r = 10

print(pi-2)#1.1415926500000002
print(pi%2)#1.1415926500000002

print('둘레',pi*2*r)
print('넓이',pi*(r**2))

r *= 3
print(r)

s = input('팔')
print(s,type(s))

s = int(s)
print(s,type(s))


item
