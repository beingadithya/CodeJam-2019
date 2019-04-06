import sys
import math 
import numbers
def getPrimeList(maxPrime):


	primeList=[]	
	n=int(maxPrime) #Change the number to an integer 
	#for index in range (0, n+1):
	#    primeList.append(index) # populate a list with all numbers starting from 0 to n+1
	primeList.extend(range(0, n+1))
	squareRoot=math.sqrt(n) #Find the square root of n

	# since the square root can be decimal,
	#lets convert it to the next highest integer using the ceil function
	divisorRange=math.ceil(squareRoot) 
	for index in range ( 2, divisorRange): #Start with 2, till the divisorRange, increment by 1.
	    # there could be numbers which are factors already, and may have been set to 0, lets ignore them.
	    if primeList[index]==0:
	        continue # use continue to proceed to the next loop item, without executing anything below 
	    for factors in range( index*2, n, index): #Start with twice the index, increment by index
	        primeList[factors]=0 # find all factors of the chosen number, set all factors to 0
	    #print(primeList)

	while 0 in primeList:
	    primeList.remove(0) # remove all 0's

	return primeList

## Program starts here
###########################################################################################





T=int(sys.stdin.readline())
NLInput=[]
cipherInput=[]
primeArray=[]
primeFactorList=[]
for i in range(0,T):
	NLInput.append(sys.stdin.readline())
	cipherInput.append(sys.stdin.readline())
largestPrime=1
for i in range(0,T):
	primeMax,cipherLength=NLInput[i].split()	
	primeMaxRange=int(primeMax)
	if(primeMaxRange>largestPrime):
		largestPrime=primeMaxRange
	cipherLength=int(cipherLength)
#print(largestPrime)
primeArray=getPrimeList(largestPrime)
#print(primeArray)
totalPrimes=len(primeArray)
# once you have the prime list
for i in range(0,T):
	cipherentries=cipherInput[i].split()
	primeMax,cipherLength=NLInput[i].split()
	primeMax=int(primeMax)

	cipherLength=int(cipherLength)
	primeFactorList=[]
	lettersFactorList=[]


	for i in range(0,cipherLength):
		currentPrimeProduct=int(cipherentries[i]) #this is a product of two primes
		primeProductRoot=int(math.sqrt(currentPrimeProduct)) #go backwards from this sqrt and find primes 
		#print(totalPrimes)

		for prime in range(0,totalPrimes):
			if(primeArray[prime]>primeProductRoot):
				closestIndex=prime-1
				#print('Closests Index for %s is %s' %(primeProductRoot,closestIndex))
				break

		for reverseSearchIndex in range(closestIndex,0,-1):
			#print(primeArray[reverseSearchIndex])
			quotient=currentPrimeProduct/primeArray[reverseSearchIndex]
			#print(quotient)
			
			if (quotient.is_integer()): # basically the division happened
				sys.stdout.write("Factors for %d: %d %d\n" % (currentPrimeProduct, primeArray[reverseSearchIndex],quotient))
				currentLengthOfPrimeList=len(primeFactorList)
				quotient=int(quotient)
				if(currentLengthOfPrimeList==0):
					primeFactorList.append(quotient)
					primeFactorList.append(primeArray[reverseSearchIndex])					
				else:
					if(primeFactorList[-1]==quotient):					
						primeFactorList.append(primeArray[reverseSearchIndex])
					else:
						primeFactorList.append(quotient)
		#lettersFactorList=primeFactorList
		#lettersFactorList.sort()			
				

	print(primeFactorList)


					






