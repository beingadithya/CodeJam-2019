import sys 
T=int(sys.stdin.readline())
inputNumbers=[]
for i in range(0,T):
	N=int(sys.stdin.readline())
	inputNumbers.append(N)
#print(inputNumbers)
for i in range(0,T):
	solutionfound=False
	solutionsTested=0;
	totalSolutions=int(inputNumbers[i]/2)
	iterations=0;
	while solutionsTested < totalSolutions:
		iterations=iterations+1;
		A=totalSolutions+solutionsTested
		B=inputNumbers[i]-A;
		Astr=str(A)
		Bstr=str(B)
		inA=Astr.find("4")
		inB=Bstr.find("4")
		# inA=re.search("4",str(A))
		# inB=re.search("4",str(B))
		#print("Case #%d: %d %d\n" % (i+1, A,B))
		if(inA==-1 and inB==-1):
			sys.stdout.write("Case #%d: %d %d\n" % (i+1, A,B))
			sys.stdout.flush()
			#print(A)
			#print(B)
			break
		solutionsTested=solutionsTested+(3*iterations)
