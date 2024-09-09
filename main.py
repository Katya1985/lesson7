grades = [[5, 3, 3, 5, 4],[2, 2, 2 ,3],[4, 5, 5, 2],[4, 4, 3],[5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
list (students)
res = sorted (students)
print (res)
averge = [sum (i) / len (i) for i in grades]
print (averge)
dict_1 = dict (zip(res, averge))
print (dict_1)