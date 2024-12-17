

tuple1 = ('zayan', 7, 'Shafaet', 8, 'Fardin', 17, 'Lamim', 6)
print(tuple1[1])
print(type(tuple1))

#a set is not subsciptable
set1 = {'midfielder', 'striker', 'defender'}
# print(set1[1]) 
dict1 = {'zayan':'midfielder'}
dict1['shafaet'] = 'midfielder'
print(dict1)
del dict1['shafaet']
print(dict1)

dict2 = dict1
print(dict2)
dict2.clear()
print(dict2)