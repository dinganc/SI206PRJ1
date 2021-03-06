import os
import filecmp

def getData(file):

#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.

	#Your code here:
	import csv
	header=[]
	state=0
	returnlist=[]
	for line in csv.reader(open(file,'r')):
		emptydic={}
		if state==0:
			header=line
			state=1
			continue
		for col in range(len(line)):
			emptydic[header[col]]=line[col]
		returnlist.append(emptydic)
	return returnlist

#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName
	#Your code here:
	return sorted(data,key=lambda x:x[col])[0]['First']+" "+sorted(data,key=lambda x:x[col])[0]['Last']


#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]

	#Your code here:
	d={}
	for stu in data:
		if stu['Class'] not in d.keys():d[stu['Class']]=1
		else:d[stu['Class']]+=1
	return [(i,d[i]) for i in sorted(d,key=lambda x:d[x],reverse=True)]



# Find the most common day of the year to be born
def findDay(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	d={}
	for day in a:
		if day['DOB'].split("/")[1] not in d.keys():d[day['DOB'].split("/")[1]]=1
		else:d[day['DOB'].split("/")[1]]+=1
	return int(sorted(d,key=lambda x:d[x],reverse=True)[0])


# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	d={}
	for mo in a:
		if mo['DOB'].split("/")[2] not in d.keys():d[mo['DOB'].split("/")[2]]=1
		else:d[mo['DOB'].split("/")[2]]+=1
	sumage=0
	for year in d.keys():
		sumage+=(2017-int(year))*d[year]
	return int(sumage/len(a),)

#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here:
	import csv
	for row in sorted(a, key=lambda x: x[col]):
		open(fileName,'a').write(row['First']+","+row['Last']+","+row['Email']+'\n')


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

