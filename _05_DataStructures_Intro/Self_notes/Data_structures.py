list1 = [110, 23.5, True, 'Mohan', [1,2,3], (1,2), {1:10,2:20}, {1,2,3}]
print("List1 : ", id(list1))
print("Index 3rd  : ", id(list1[3]))
print("Index : ", id(list1[3][1]))
print("Slice : ", list1[3][1:3])

# Tuple
print("------------TUPLE------------")

tup1 = (110, 23.5, True, 'Mohan', [1,2,3], (1,2), {1:10,2:20}, {1,2,3})
print("Tuple : ", tup1)
print("Index : ", tup1[3])
print("Index : ", id(tup1[3][1]) , id(tup1[3][-1]))


print("------------DICTIONARY------------")

e_data = {'eid': 100,
          'name': 'Mohan Narayana',
          'sal': 15000,
          'loc': 'Bangalore',
          'gender': 'Male'
          }

print("Dict data : ", e_data)
print("Dict data : ", e_data['name'])
print("Dict data : ", e_data['sal'])


print("------------SET------------")

set1 = {1, 2, 3, 4, 5, 6}
print("Set1 : ", set1)
