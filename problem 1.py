a=3
b=5
l=1000
s=0
for i in range(1,1000):
    if (i % a)==0 or ( i % b)==0:
        s=s+i
        print i
print s
     