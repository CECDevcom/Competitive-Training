# 4000000
n = 100
a,b = 1,2
s=0
while b<4000000:
	if b%2==0:
		s += b
	a,b=b,a+b
print s