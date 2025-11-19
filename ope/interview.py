#list methods/Operations

data=[10,20,30,40]
data.append(50)
print(data)

#list inside the list
data=[10,20,30,40,50]
data.append([60,70,80])
print(data)

#inside the list string can be added
data1=["Nihal","iphone","laptop"]
data1.append("khaja")
print(data1)

#multipule data to be add in the list([])
data2=[10,20,30,40,50]
data2.extend([60,70,80,90])
print(data2)

#insert()befor the index
data=[10,30,40,50]
data.insert(1,20)
print(data)

#
data=[10,20,30,40,50,60]
data.insert(10,100)
print(data)

#modifty the data
data=[10,20,30,40,50,60]
data[2]=35
print(data)

#pop to remove # based on index also we can delete
data=[1,2,3,4,5]
data.pop(3)
print(data)

#remove the value without index number
data=[1,2,3,4,5,6]
data.remove(3)
print(data)

#removed only first occurances
data=[10,20,30,40,40,40,60,70,80]
data.remove(40)
print(data)

#removed all  occurances
data=[10,2,30,40,40,40,40,50,60,70,70]
#logic to remove all occurance of duplicate number 
while 40 and 70 in data:
    data.remove(40)
    data.remove(70)
    print(data)
#clear()remove all elements
data=[10,2,30,40,40,40,40,50,60,70,70]
data.clear()
print(data)

#index() how to get index position 
data=[10,2,30,40,40,40,40,50,60,70,70]
print(data.index(40))

#i want to remove 3(40) from the list
data=[10,2,30,40,40,40,40,50,60,70,70]
count=0
for x in data[:]:
    if x==40:
        count+=1
        data.remove(x)
        if count==3:
            break
print(data)


#remove 2(40) in list 
data=[10,2,30,40,40,40,40,50,60,70,70]
count=0
for x in data[:]:
    if x==40:
        count+=1
        data.remove(x)
        if count==2:
            break
print(data)

    

















