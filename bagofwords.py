import os
import sys
class BagOfWords():
        def __init__(self):
                self
        def Input(self,lista):                      #### Creating Dictionary for given file
                a = {}
                list1 = open(lista,'r')
                list1 = list1.read().split(' ')
                s = "\n@!#$%^&*()_+=|?+-`~';?.,:<>;"
                for j in s:
                        for i in range(0, len(list1)):
                                if j in list1[i]:
                                        list1[i] = list1[i].lower().replace(j," ")
                for i in range(len(list1)):
                    if list1[i] in a:
                        continue
                    else:
                        a[list1[i]] = list1.count(list1[i])
                return a

        def dotproduct(self,s1,s2):              #Dot product of count of strings that are repeated
            sum = 0
            for i in s1:
                if i in s2:
                    sum = sum + (s1[i]*s2[i])
            return sum
        def Eucledian(self,s):            ####   ----> caluculating eucledian of given set of strings
            e = 0
            for i in s:
                e = e + (s[i]**2)
            norm = (e)**(1/2)
            return norm
        def Percentage(self,a,b):            ####  ---> Plagarism percentage calculation   
                result=(a/b)*100
                return result
        def ReadingFile(self):                     ## ---->Input of directory
                n=input("Enter the directory name: ")
                file = []
                for i in os.listdir(n):
                    if i.endswith(".txt"):
                        file.append(i)
                os.chdir(n)
                list3=[]
                list4=[]
                for i in range(0, len(file)):
                    list3.append(p.Input(file[i]))
                print(" ",file)
                for i in range(len(file)):
                        for j in range(len(file)):
                                if(i==j):
                                    list4.append(0)
                                else:
                                    file1 = p.dotproduct(list3[i],list3[j])
                                    file2 = p.Eucledian(list3[i])
                                    file3 = p.Eucledian(list3[j])
                                    file4 = file2*file3
                                    list4.append(p.Percentage(file1,file4))
                        print(file[i],list4)
                        list4=[]

p = BagOfWords()
p.ReadingFile()
