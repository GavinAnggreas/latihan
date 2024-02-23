print("-"*30, "LATIHAN PERTAMA")
data1 = [ i for i in range (10, 20, 2)]
data2 = [z for z in range (91, 100,2)]
print(data1 + data2)


print()


print("-"*30, "LATIHAN KEDUA")
data1 = [];
data1.insert(1, "Mi")
data1.insert(2, "Do")
data1.insert(3, "Fa")
data1.insert(4, "So")
data1.insert(5, "La")
data1.insert(6, "Ti")
data1.insert(7, "Re")
print(data1)

#cara kedua:
# data1 = ["Do", "Re", "Mi", "Fa", "So", "La", "Ti"];
# data2= [data1[2], data1[0],data1[3], data1[4], data1[5], data1[6], data1[1]]
# print(data2)


print()

print("-"*30, "LATIHAN KETIGA")
data1 = "IgNatIus"

#cara kedua:
# x = [i for i in data1 if i.isupper()]
# print(x)

datalist=[]
for n in data1:
    if (n.isupper() == True):
        datalist.append(n)
print(datalist)