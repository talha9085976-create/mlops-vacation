stu = {
"name" : "Talha",
"age" : 23,
"city" : "Karachi",
"marks" : [23 , 45 , 67 , 89 , 90],
"SUBJECTS" : {"Physics": 10 , 
"Maths": 20 , "Chemistry": 30}
}
print(stu["SUBJECTS"]["Maths"])



set={3 , 3 , 4 ,5 ,3 , 7 }
print(type(set))


set1 = {1 , 2 , 3 , 4 , 5}
set2 = {4 , 5 , 6 , 7 , 8}
print(set1.union(set2))
print(set1.intersection(set2))