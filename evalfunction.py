#eval()
'''a=int(input("a value"))
b=int(input("b value"))
print(a+b)'''

'''a=float(input("a value"))
b=float(input("b value"))
print(a+b)'''

'''a=input("data1")
b=input("data2")
print(a+b)'''

'''while True:
    a=eval(input("a value"))
    b=eval(input("b value"))
    print(a+b)'''

#[],(),{}
'''a=[]
print(type(a))

b=()
print(type(b))

c={}
print(type(c))

d=set()
print(type(d))'''

#zip()->we can combine multiple collections
#into one collection
'''a=[10,20,30,40,50]
names=["joy","rajesh","sruthi","manju","rajendra"]
values=(4,3,2,1,7)
print(a+names)

b=zip(a,names)
print(b)

b=list(zip(a,names))
print(b)

b=tuple(zip(a,names))
print(b)

b=set(zip(a,names))
print(b)

b=dict(zip(a,names))
print(b)'''

'''a=[1,2,3,4,5]
b=["apple","banana","grapes","mango","kiwi"]
c=["1kg","2kg","3kg","4kg","5kg"]
d=["vja","hyd","bng","vzg","chennai"]
print(a+b+c)

d=list(zip(a,b,c))
print(d)

d=tuple(zip(a,b,c))
print(d)

d=set(zip(a,b,c))
print(d)

d=dict(zip(a,b,c,d))
print(d)'''

#enumerate->we can give counter to the collection
'''names=["deepika","tejasri","sruthi","swarna","kerthana"]
for i in range(len(names)):
    print(i)
for i in range(len(names)):
    print(i,names[i])
a=dict(enumerate(names,10))
b=list(enumerate(names,1))
c=set(enumerate(names,100))
d=tuple(enumerate(names,20))
print(a)
print(b)
print(c)
print(d)'''



'''a=[1,2,3,4,5,6]
for i in a:
    print(i+1,end=" ")

b=[i+1 for i in a]
print(b)

for i in a:
    i+=1
    print(i,end=" ")'''


a=[2,3,4,5,6,7]
sum=0
for i in a:
    sum+=i   
print(sum)






