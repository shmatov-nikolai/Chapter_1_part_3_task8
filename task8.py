'''
8. Напишите программу (функцию), которая принимает список и возвращает тот же список
без, но уже с уникальными значениями.
'''

listok = [1, 2, 3, 4, 5, 6, 7, 1, 2, 4, 2, 3, 7, 6, 1, 2]
print(listok)

def list_to_uniqueList(some_list):
    uniqueList = list(set(some_list))
    return uniqueList

listok = list_to_uniqueList(listok)
print (listok)