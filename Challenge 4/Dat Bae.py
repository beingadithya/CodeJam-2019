import sys 
TC=int(sys.stdin.readline())
workersBitList=[]
while(TC>0):
	parameters=sys.stdin.readline()
	N,B,F=parameters.split()
	N=int(N)
	B=int(B)
	F=int(F)
	#print(N)
	numberOfSentZeros=0
	NumberOfSentOnes=0
	workersBitList=[]
	for p in range(0,N):
		workersBitList.append(str(p%2)); # initialise with Odd and Even Bit patterns 
		if(p%2==0):
			numberOfSentZeros=numberOfZeros+1
		else:
			NumberOfSentOnes=NumberOfOnes+1;
			
	numberOfRecievedZeros=0
	NumberOfRecievedOnes=0
	bitlistOutput=""
	bitlistOutput=bitlistOutput.join(workersBitList)
	sys.stdout.write(bitlistOutput+'\n') #send the bitlist
	sys.stdout.flush() # flush the buffer
	F=F-1
	judgeResponse=sys.stdin.readline() #wait for judge

	for p in range(0,N-B): # we expect only N-B slaves to respond
		if(judgeResponse[p]=="0"):
			numberOfRecievedZeros=numberOfRecievedZeros+1
		if (judgeResponse[p]=="1"):
			NumberOfRecievedOnes=NumberOfRecievedOnes+1
				
	ZeroDifference=numberOfSentZeros-numberOfRecievedZeros; # Even numbered slaves
	OneDifference=NumberOfSentOnes-NumberOfRecievedOnes; #Odd numbered Slaves

	if(OneDifference==0): #Number of Ones Sent have all come back, so Odd number slaves are responding

	if(ZeroDifference==0): #Number of Zeros Sent have all come back, so Even number slaves are responding



	
	# faultyWorkers=[]
	# for p in range(0,N):		
	# 	workersBitList=[] #Reinitialise the array
	# 	workersBitList=["0"]*N #update array with all Zeros
	# 	workersBitList[p]="1" #turn on one of the Bits
	# 	bitlistOutput=""
	# 	bitlistOutput=bitlistOutput.join(workersBitList)
	# 	sys.stdout.write(bitlistOutput+'\n')#send the bitlist
	# 	sys.stdout.flush() # flush the buffer

	# 	judgeResponse=sys.stdin.readline() #wait for judge

	# 	#print(verdict)
	# 	if(int(judgeResponse) ==-1):
	# 		#print("Have to exit")
	# 		exit()
	# 	inJudge=judgeResponse.find("1") #find if the 1 we sent has it come back. 

	# 	if(inJudge==-1):# The 1 we sent was Lost, means that worker is not responding
	# 		faultyWorkers.append(str(p)) #record who is the faulty worker
	# 	if(len(faultyWorkers)==B): # Yay, we found enough faulty workers
	# 		#faultyWorkers.reverse()
	# 		faultyWorkersResponse=" "
	# 		faultyWorkersResponse=faultyWorkersResponse.join(faultyWorkers)
	# 		#faultyWorkersList=faultyWorkers.join(" ")
	# 		sys.stdout.write(faultyWorkersResponse+'\n')#send the bitlist
	# 		sys.stdout.flush()
	# 		#print("Waiting for Verdict")
	# 		verdict=int(sys.stdin.readline()) # just read it so the sequence is not broken
	# 		#print(verdict)
	# 		if(verdict ==-1):
	# 			#print("Have to exit")
	# 			exit()
	# 		faultyWorkersResponse=""
	# 		faultyWorkers=[]
	# 		break


	TC=TC-1