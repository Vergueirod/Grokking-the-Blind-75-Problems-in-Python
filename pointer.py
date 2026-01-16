#a = 10
#b = a
#print(id(a))
#print(id(b))
'''
lst1 = [10,20,30]

for x in lst1:
    print(x, id(x))

print(f"#####################")    


lst2 = [10,20,30]

for x in lst2:
    x = x + 1

print(lst2)
'''

print(f"#####################")    


lst3 = [30,20,10]
validation = 0
new_lst = []

'''
for x in lst3:
    print(f"{x}")
print(lst3)
'''

for idx, value in enumerate(lst3):
    print(idx, value, id(value))