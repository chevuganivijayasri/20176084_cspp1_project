import os
import sys
class StringMatching:
	def __init__(self,msg):
		self.msg=msg
		pass
	def Input(File1,File2):
		content = open(File1,"r")
		s1 = content.read()
		content = open(File2,"r")
		s2 = content.read()
		str1 = s1.replace(" ","")
		str2 = s2.replace(" ","")
		str1 = str1.lower()
		str2 = str2.lower()
		p = len(str1)
		q = len(str2)	
		return str1, str2, p, q
	def ConvertToList(str1,str2):
		list1=[]
		list2=[]
		for i in str1:
			list1.append(i)
		for j in str2:
			list2.append(j)
		y = len(list1)
		a = len(list2)
		return y, a, list1, list2
	def AddingWords(y, a, list1, list2):
		list3 = []
		list4 = []
		s=""
		for i in range(y):
			for j in range(i,y):
				s = s + list1[j]
				list3.append(s)
			s = ""
		s1 = ""
		for i in range(a):
			for j in range(i,a):
				s1=s1+list2[j]
				list4.append(s1)
			s1 = ""
		return list3,list4
	def ListComparision(list3,list4):
		list5 = []
		for i in list3:
			if i in list4:
				x = i
				list5.append(x)
		return list5
	def HighestValue(list5):
		list6 = []
		for i in list5:
			z = i
			list6.append(len(z))
		c = max(list6)
		return c
	def Calculation(c,x,y):
		w = x + y
		copy = ((c*2)/w)*100
		return copy
cwd = os.getcwd()
files = os.listdir(cwd)
text = [z for z in files if z.endswith('.txt')]
for File1 in text:
	for File2 in text:
		if (text.index(File1) <= text.index(File2)):
			pass
		else:		
			str1,str2,p,q = StringMatching.Input(File1,File2)
			y, a, list1, list2 = StringMatching.ConvertToList(str1, str2)
			list3,list4 = StringMatching.AddingWords(y, a, list1, list2)
			list5 = StringMatching.ListComparision(list3, list4)
			c = StringMatching.HighestValue(list5)
			copy = StringMatching.C(c,p,q)
			print(File1,"and",File2,"is",copy,"% matched")
