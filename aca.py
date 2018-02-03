def Filenaming(names):
	for i in range(1,len(names)):
		flag=0
		for j in range(0,i):
			if(names[i]==names[j]):
				flag=1
				break
		x=1
		while 1:
			y=0
			for k in range(0,i):
				if(names[k]==names[i]+'('+str(x)+')'):
					y=1
			if(y==0):
				break
			x+=1
		if flag==1:
			names[i]=names[i]+'('+str(x)+')'
	print names

name=raw_input()
names=name.split()
Filenaming(names)
