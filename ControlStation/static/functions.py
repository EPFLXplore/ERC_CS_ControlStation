import sys

def add(n):
	return n+2

def determinant(sa:str,sb:str,sc:str,sd:str):
	a=int(sa)
	b=int(sb)
	c=int(sc)
	d=int(sd)
	return (a * d) - (c * b)

if __name__ == '__main__' and len(sys.argv)>1:
	arg = sys.argv
	l = len(arg)
	name = arg[1]
	
	if   l==3 and name=="add":
		print(globals()[name](float(arg[2])))
	elif l==6 and name=="determinant":
		print(globals()[name](arg[2], arg[3], arg[4], arg[5]))
