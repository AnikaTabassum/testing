import pandas as pd
import sys
def takeInput():
	global numberOfVariables, inx
	numberOfVariables= input("How many variables ")
	numberOfVariables=int(numberOfVariables)
	j=1

	for i in range (numberOfVariables):
		val= "var "+str(j)
		j+=1
		#print(val)
		ranging= input("Enter value for variable "+str(i+1)+": ")
		rangeArray=ranging.split(",")
		upper=int(rangeArray[0])
		lower= int(rangeArray[1])

		makeValues(upper,lower,val)
		keys.append(val)

	while inx !=0:
		inx= input("\n\n\nChoose testing method\n 1. Boundary Value Checking\n 2. Robustness testing method\n 3. Worst-case testing method \n 4. press 0 to exit\n")
		inx=int(inx)
		if inx==3:
			printWorstCase()
		if inx==1:
			printBVC()
		if inx==2:
			printRobust()
		if inx==0:
			printint("exiting")
			sys.exit()

def makeValues(lower,upper,val):
	global worst_array, bvc_array,nominal, robust_array
	arr_worst=list()
	arr_bvc=list()
	arr_robust=list()

	mx=upper
	arr_worst.append(mx)
	arr_bvc.append(mx)
	arr_robust.append(mx)

	mx1=upper-1
	arr_worst.append(mx1)
	arr_bvc.append(mx1)
	arr_robust.append(mx1)

	mn=lower
	arr_worst.append(mn)
	arr_bvc.append(mn)
	arr_robust.append(mn)

	mn1=lower+1
	arr_worst.append(mn1)
	arr_bvc.append(mn1)
	arr_robust.append(mn1)

	nomi=int((upper+lower)/2)
	arr_worst.append(nomi)
	nominal.append(nomi)

	mx2=upper+1
	arr_robust.append(mx2)

	mn2=lower-1
	arr_robust.append(mn2)

	worst_array[val]=arr_worst

	bvc_array[val]=arr_bvc

	robust_array[val]=arr_robust


def printRobust():
	global nominal, keys, robust_array
	finalList=list()

	for i in range(robust_array.__len__()):	
		temp=robust_array.get(keys[i])
		for val in temp:
			amarList=list()
			amarList.append(val)
			for noms in range(nominal.__len__()):
				if noms!=i:	
					amarList.append(nominal[noms])			
			finalList.append(amarList)
	finalList.append(nominal)
	
	amarLoop=int(0)
	for j in (range(0,finalList.__len__()-1)):
		amarLoop=int(j/6)
		for i in range(0, amarLoop):
			finalList[j][i], finalList[j][i+1]= finalList[j][i+1], finalList[j][i]
	for t in range(numberOfVariables):
		arr=list()
		caseId=1
		cases=list()
		for val in finalList:
			arr.append(val[t])
			cases.append("case "+str(caseId))
			caseId+=1
	
		robustDict[keys[t]]=arr
	myDF=pd.DataFrame(robustDict, index=cases)
	print("Robustness testing method")
	print(myDF)


def printBVC():
	global nominal, keys, BVCdict
	finalList=list()

	for i in range(bvc_array.__len__()):
		
		temp=bvc_array.get(keys[i])
		for val in temp:
			amarList=list()
			amarList.append(val)
			for noms in range(nominal.__len__()):
				if noms!=i:	
					amarList.append(nominal[noms])
			finalList.append(amarList)
	finalList.append(nominal)
	amarLoop=int(0)
	for j in (range(0,finalList.__len__()-1)):
		amarLoop=int(j/4)
		for i in range(0, amarLoop):
			finalList[j][i], finalList[j][i+1]= finalList[j][i+1], finalList[j][i]
	for t in range(numberOfVariables):
		arr=list()
		caseId=1
		cases=list()
		for val in finalList:
			arr.append(val[t])
			cases.append("case "+str(caseId))
			caseId+=1
		BVCdict[keys[t]]=arr
	myDF=pd.DataFrame(BVCdict, index=cases)
	print("Boundary Value Checking testing method")
	print(myDF)

def printWorstCase():
	i= int(0)
	allCombination=worst_array.get(keys[0])
	listOfString=list()
	printingVal=list()

	for keyVal in range(1,keys.__len__()):
		strTemp=worst_array.get(keys[keyVal])
		for t in allCombination:
			for l in strTemp:
				iki= str(t)+","+ str(l)
				listOfString.append(iki)
			stringToList=listOfString
		allCombination.clear()
		for val in stringToList:
			allCombination.append(val)

	rangers=5**numberOfVariables

	for t in range(numberOfVariables):
		#print(t)
		tempArr=list()
		end=allCombination.__len__()-1
		itr=0
		cases=list()
		caseId=int(1)
		while itr <= rangers-1:
			myString= str(allCombination[end])
			end-=1
			temp=myString.split(",")
			tempArr.append(temp[t])

			cases.append("case "+str(caseId))
			itr+=1
			caseId+=1

		worst_dict[keys[t]]=tempArr

	myDF=pd.DataFrame(worst_dict, index=cases)
	print("Worst-case testing method")
	print(myDF)

keys=list()
worst_array={}
numberOfVariables=int()
worst_dict={}
bvc_array={}
nominal=list()
BVCdict={}

robust_array={}
robustDict={}
inx=int(925)
takeInput()

