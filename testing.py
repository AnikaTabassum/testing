import pandas as pd
from itertools import product
def takeInput():
	
	numberOfVariables= input("How many variables ")
	numberOfVariables=int(numberOfVariables)
	j=0

	for i in range (numberOfVariables):
		val= "var "+str(j)
		j+=1
		print(val)
		ranging= input("Enter value for variable ")
		anika=ranging.split(",")
		upper=int(anika[0])
		lower= int(anika[1])

		print("upper ", upper)
		print("lower ", lower)
		makeValues(upper,lower,val)
		keys.append(val)

def makeValues(lower,upper,val):
	global final
	arr=list()
	mx=upper
	arr.append(mx)
	mx1=upper-1
	arr.append(mx1)
	mn=lower
	arr.append(mn)
	mn1=lower+1
	arr.append(mn1)
	nomi=int((upper+lower)/2)
	arr.append(nomi)
	mx2=upper+1
	arr.append(mx2)
	mn2=lower-1
	arr.append(mn2)

	print(arr)
	final[val]=arr
	#final.append(arr)

keys=list()
final={}
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])

data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print (df)
takeInput()
pap=pd.DataFrame(final)
print(pap)
print(pap["var 1"][0])
print(pap.__len__())
while (True):
	for key in keys:
		for i in range (7):
			print(pap[key][i])

'''prod = product(df['var 0'].unique(), df['var 1'].unique())
student_cols = [x for x in df.columns if x not in ('var 0', 'var 1')]
students = df[student_cols].drop_duplicates().values.tolist()

res = pd.DataFrame([s + list(p) for p in prod for s in students],
                   columns=list(student_cols+['var 0', 'var 1']))\
        .sort_values(list(student_cols+['var 0', 'var 1']))'''

