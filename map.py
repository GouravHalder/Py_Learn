for i in range(4):
    print (i)

a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])

a1 = ['Mary', 'had', 'a', 'little', 'lamb']
for i in a1:
    print(i)
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}
print (users.keys())
print (users.values())
print (users.items())

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

print (users.items())

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status

print ("active Users are :",active_users)
print ("active Users are :",users)