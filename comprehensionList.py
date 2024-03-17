usuarios = [["Chanchito"],["Mr Bean"], ['Dollars']]

#nombres = [ expression for item in items ]

nombres = [usuario[0] for usuario in usuarios ]
#this is the same of this expression
names=[]
for usuario in usuarios:
    names.append(usuario[0])



#filtrar
users = [["Chanchito", 1],["Mr Bean", 2], ['Dollars', 3]]
usersFilters = [user[0] for user in users if user[1] > 1 ]

#maps
map_name  = list(map(lambda usuario: usuario[0], usuarios )) # map( expresion arrow function , iterable o array)
#filter
filter_name = list(filter(lambda usuario: usuario[1] > 1), usuarios)