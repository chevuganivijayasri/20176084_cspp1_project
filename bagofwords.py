import math
File1,File2 = open("file1.txt","r"), open("file2.txt","r")
Read1,Read2 = File1.read().lower(),File2.read().lower()
def sets(p):
	dictionary = {}
	for i in p:
		if i not in dictionary:
			dictionary[i] = 1
		else:
			dictionary[i] += 1
	return dictionary
def squareroot(x,y):
	s1 = 0
	s2 = 0
	for j in x:
		s1 += (x[j]**2)
	for k in y:
		s2 += (y[k]**2)
	sq1 = math.sqrt(s1)
	sq2 = math.sqrt(s2)
	return sq1*sq2
def dot(x,y):
	sum=0
	for i in x:
		for j in y:
			if i == j:
				multiplication = x.get(i)*y.get(j)
				sum = sum + multiplication
	return sum
l = (Read1.split(" "))
m = (Read2.split(" "))
x,y = sets(l),sets(m)
f = squareroot(x,y)
g = dot(x,y)
h = (g/f)*100
print(h ,"% matched")