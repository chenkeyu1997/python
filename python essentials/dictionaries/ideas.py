person={}
person['first']="Jmes"
person['last']="Maxwell"
person['born']=1997
print(person)

person_modification={'first':'James','middle':'Clerk'}
person.update(person_modification)
print(person)


b='last'in person
print('James'in person)
print(b)

"""keys:所有键组成的列表
   values：所有值组成的列表
   items：所有键值对应元组组成的列表
"""
print(person.keys())
print(person.values())
print(person.items())