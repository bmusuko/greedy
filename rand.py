from random import choice

rand =[]
for i in range (52):
	rand.append(i)

for i in range(13):	
	n1 = choice(rand)
	rand.remove(n1)
	n2 = choice(rand)
	rand.remove(n2)
	n3 = choice(rand)
	rand.remove(n3)
	n4 = choice(rand)
	rand.remove(n4)
	print(n1," ",n2," ",n3," ",n4)

