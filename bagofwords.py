import math
file,file1=open("f1.txt","r"),open("f1.txt","r")
f1,f2=file.read().lower(),file1.read().lower()
def list1(z, n):
    print(str(z) +" and "+ str(n))
    def list2():
        cha = ['_']
        for l in range(97, 123):
            cha.append(chr(l))
        for m in range(48, 58):
            cha.append(chr(m))
        p = ''.join(cha)
        return p
    def check(inp):
        v = list2()
        o = []
        for c in inp:
            a = []
            i = 0
            for char in c:
                if char in v:
                    a.append(char)
            d = ''.join(a)
            o.append(d)
        return o
    def file(v):
        data = []
        try:
            fo = open(v, 'r')
        except IOError:
            print("No text file found")
            return 0
        else:
            for newlist in fo:
                if newlist!='\n':
                    newlist1 = newlist.lower()
                    nl = newlist1[:-1].split(' ')
                    le = len(nl)
                    for i in range(le):
                        ke = nl[i]
                        data.append(ke)
            nl = check(data)
            return nl
            fh.close()
    patha = z
    x = file(patha)
    pathb = n
    y = file(pathb)
    ao = set(x)
    bo = set(y)
    co = ao | bo 
    do = list(co)
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
        li = dict(zip(x,e))
        e1 = list(li.keys())
        f1 = list(li.values())
        wq = 0
        for jh in f1:
            wq = wq + (jh**2)
        sq = math.sqrt(wq)
        return li, e1, f1, sq
    w, s, t, sq1 = di(x)
    z, u, v, sq2 = di(y)
    q = []
    for k in do:
        if k in w.keys():
            q.append(w[k])
        else:
            q.append(0)   
    l = []
    for k in do:
        if k in z.keys():
            l.append(z[k])
        else:
            l.append(0)
    x = 0
    for j in range(len(do)):
        x = x + (q[j]*l[j])
    cos = (x)/(sq1*sq2)
    print(str(cos*100) + " % matching")
la = len(alltext)
for g in range(la):
	h = 0
	while h<la:
		if h!=g:
			list1(alltext[g], alltext[h])
			h = h+1
		else:
			h = h+1
		print("\n")