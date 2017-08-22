'''Bag of Words'''
import os
import sys
import math
e = os.getcwd()
alltext = [f for f in os.listdir(e) if f.endswith('.txt')]
print(alltext)
def list1(z, n):
    print(str(z) +" and "+ str(n))
    def list2():
        cha = ['_']
        for i in range(97, 123):
            cha.append(chr(i))
        for j in range(48, 58):
            cha.append(chr(j))
        h = ''.join(cha)
        return h
    def check(inp):
        y = list2()
        g = []
        for c in inp:
            a = []
            i = 0
            for char in c:
                if char in y:
                    a.append(char)
            d = ''.join(a)
            g.append(d)
        return g
    def file(y):
        data = []
        try:
            fh = open(y, 'r')
        except IOError:
            print('There is no file with that name to open')
            return 0
        else:
            for new1 in fh:
                if new1!='\n':
                    new = new1.lower()
                    ad = new[:-1].split(' ')
                    le = len(ad)
                    for i in range(le):
                        x = ad[i]
                        data.append(x)
            da = check(data)
            return da
            fh.close()
    path1 = z
    x = file(path1) #print(x)
    path2 = n
    y = file(path2) #print(y)
    a = set(x)
    b = set(y)
    c = a | b #print(c)
    d = list(c)
    def di(x):
        ly = x[:]
        lh = len(ly)
        e = []
        d = {}
        for i in range(0,lh):
            c = 0
            for k in range(0,lh):
                if ly[i] == ly[k]:
                    c = c+1
            e.append(c)
        d = dict(zip(x,e))
        e1 = list(d.keys())
        f1 = list(d.values())
        s = 0
        for i in f1:
            s = s + (i**2)
        r = math.sqrt(s)
        return d, e1, f1, r
    w, s, t, r1 = di(x)
    z, u, v, r2 = di(y) #print(r2) #print(r1)
    q = []
    for k in d:
        if k in w.keys():
            q.append(w[k])
        else:
            q.append(0)     #print(l)
    l = []
    for k in d:
        if k in z.keys():
            l.append(z[k])
        else:
            l.append(0)     #print(l)
    m = 0
    for i in range(len(d)):
        m = m + (q[i]*l[i])     #print(m)
    cos = (m)/(r1*r2)
    print(str(cos*100) + " % matching")
la = len(alltext)
for i in range(la):
	j = 0
	while j<la:
		if j!=i:
			list1(alltext[i], alltext[j])
			j = j+1
		else:
			j = j+1
		print("\n")