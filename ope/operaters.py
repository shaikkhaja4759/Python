data=[10,20,30,40,50]
print(data)
data.append(80)
print(data)


product =["laptop","iphone"]
print(product)
product.append("pc")
print(product)

data=[10,20,30,40,50]
data.extend([60,70,])
print(data)

data=[10,20,34,40,50]
data.pop(2)
print(data)

removed_element=data.pop
print(removed_element)
print(data)

data=[10,20,34,40,50,10,20,30]
while 10 in data:
    data.remove(10)
    print(data)


data=[10,20,34,40,50,10,20,30,50,60,70,80,90,20,20,20]
coun_20=data.count(20)
print(coun_20)


data=[10,20,34,40,50,10,20,30,50,60,70,80,90,20,20,20]
data.reverse()
print(data)


data=[10,20,34,40,50,10,20,30,50,60,70,80,90,20,20,20]
data.sort()
print(data)

data = ["H","E","L","L","O"]
data.sort()
print(data)




















             