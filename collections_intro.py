shopping_list = ['eggs','bread','milk']
print(shopping_list)
shopping_list.append('chocolate')
print(shopping_list)
print(shopping_list[0])

#Tuple
essentials_tuple = ('bread','eggs')
print(essentials_tuple)
print(essentials_tuple)


#Sets arent ordered
car_parts = {'wheels','doors','windows'}
print(car_parts)

#Frozen sets are immutable
x = frozenset([1,2,3,4])
print(x)

#Embedded lists
emb_list = [[1,2,3],[4,5,6]]
for item in emb_list:
    print(item)
    for number in item:
        print(number)