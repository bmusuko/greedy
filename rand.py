from random import choice

rand =[]
for i in range (52):
	rand.append(i)

n1 = choice(rand)
rand.remove(n1)
n2 = choice(rand)
rand.remove(n2)
n3 = choice(rand)
rand.remove(n3)
n4 = choice(rand)
print(n1," ",n2," ",n3," ",n4)

