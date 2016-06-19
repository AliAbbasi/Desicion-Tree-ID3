
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#			The ID3(Decision Tree) algorithm implemented in python 2.7.11
#			Ali Abbasi 
#			METU - Computer Engineering
#			ali.abbasi@metu.edu.tr
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

###################################################################################################################################################

from __future__ import division
import math
import sys

###################################################################################################################################################

trainingset      = [[]]						#define a 2D array for training set
testset          = [[]]				
attributeNumbers = 0						#the number of different attributes
trainingsetRows  = 1						#the index of rows at 2D trainingset array
testsetRows      = 1						#the index of rows at 2D testset array

###################################################################################################################################################

def ReadingData():									#define a function to reading data from txt and save it in array
	
	data = open(sys.argv[1],'r')					#reading file
		
	for line in data:								#read line by line
		line = line.replace(" ", "")				#remove empty spaces in data
		if line[:1] != "%" and line[:1] != "\n":	#check the first character of line
			if line[:1] == 'T':						#T: means the Header of columns
				line = line[2:-2]               	#cut the first(2) and end(-2) of string
				line = line.split(",")          	
				for word in line:
					global attributeNumbers
					attributeNumbers += 1			#the number of attributes
				
				global trainingset,testset
				trainingset = [[0 for x in range(10000)] for x in range(attributeNumbers)] 	#create a 2D array for training dataset
				testset     = [[0 for x in range(10000)] for x in range(attributeNumbers)] 
				j = 0	
				for word in line:								#fill the first row of training array with attribute names
					trainingset[j][0] = word.strip()			#trim in java
					testset[j][0] = word.strip()
					j += 1	
					
			elif line[:1] == 'A':        						#A: means training set
				line = line[2:-2]								#cut the first characters and last characters of line
				line = line.split(",")							#split data respect to comma
				j    = 0	
				for word in line:              					#fill trainingset array
					global trainingsetRows
					trainingset[j][trainingsetRows] = word.strip() 
					j += 1
				trainingsetRows += 1
				
			elif line[:1] == 'B':								#B: means test set
				line = line[2:-2]								#cut the first characters and last characters of line
				line = line.split(",")							#split data respect to comma
				j    = 0
				for word in line:              					#fill testset array
					global testsetRows
					testset[j][testsetRows] = word.strip() 
					j += 1	
				testsetRows += 1

###################################################################################################################################################

def Entropy(node):
	tempArr = []
	for x in range(1,trainingsetRows):
		if CheckPath(node,x) == PathDepth(node):			
			tempArr.append(trainingset[attributeNumbers - 1][x])
	return CalculateEntropy(tempArr)

###################################################################################################################################################

def IndexOfHeader(header):										#find the index of header in the array
	i = -1																			
	for num in range(0,attributeNumbers):
		if header == trainingset[num][0]:
			i = num
	return i
	
###################################################################################################################################################

def CalculateEntropy(arr):										#take an array of labels which related to the value and calculate entropy

	entropy = 0.0000
	tempStr = ""
	
	for item in arr:
		tempStr = tempStr + " " + item
	tempStr = tempStr.strip()
	tempStr = tempStr.split(" ")
	
	tempDic = {}
	for word in tempStr:										#find the number of different values in this attribute
		if word in tempDic:		
			tempDic[word]+= 1
		else:
			tempDic[word] = 1

	sum = 0.0000
	for word in tempDic:
		sum = sum + tempDic[word]
	
	for word in tempDic:										#calculate entropy
		entropy = entropy - (tempDic[word] / sum) * math.log(tempDic[word] / sum , 2) 
		
	return entropy

###################################################################################################################################################

class Node:					#each object of this class indicate each node of decision tree
	
	def __init__(self, isRoot   = 0,  isLeaf    = 0,  childNumber = 0,
                 value          = "", parent    = "", entropy     = 0, 
                 outputEdges    = [], inputEdge = "", children    = [],
                 instances      = {}, level	    = "", check	      = 0, 
                 numOfInstances = 0,  color     = "", depth       = 0):
				 
		self.isRoot         = isRoot	
		self.isLeaf         = isLeaf	
		self.childNumber    = childNumber
		self.value          = value	
		self.parent         = parent	
		self.entropy	    = entropy	
		self.outputEdges    = outputEdges
		self.inputEdge	    = inputEdge
		self.children       = children	
		self.instances 	    = instances
		self.level          = level		
		self.check          = check
		self.numOfInstances = numOfInstances
		self.color          = color
		self.depth          = depth

###################################################################################################################################################

def TheGreaterOneIndex(arr):			#return the index of greater 'gain' in the array
	
	greater = arr[0]
	indexOfGreater = 0
	
	for x in range(1,len(arr)):
		if greater < arr[x]:
			greater = arr[x]
			indexOfGreater = x
	
	if greater > 0:
		return indexOfGreater
	else:
		return -1
		
###################################################################################################################################################

def TheChilds(indexOfHeader):				#return the Dic which include the number of childes, edges label,

	tempArr = []
	for x in range(1,trainingsetRows):
		tempArr.append(trainingset[indexOfHeader][x]) 

	tempStr = ""
	for item in tempArr:
		tempStr = tempStr + " " + item
	tempStr = tempStr.strip()
	tempStr = tempStr.split(" ")

	tempDic = {}
	for word in tempStr:					#find the number of different values in this attribute
		if word in tempDic:
			tempDic[word]+= 1
		else:
			tempDic[word] = 1
	return tempDic

###################################################################################################################################################

def CheckPath(node,x):			#return the length of relative attributes value
	
	if node.parent == "":
		return 0
	else:
		if trainingset[IndexOfHeader(node.parent.value)][x] == node.inputEdge:
			return 1 + CheckPath(node.parent,x)
	return 0

###################################################################################################################################################

def PathDepth(node):			#return the depth of node

	if node.parent == "":
		return 0
	else:
		return 1 + PathDepth(node.parent)

###################################################################################################################################################

def TheInstances(node):											#return the Dictionary value which include the number and the...

	tempArr = []												#...kind of instances(class labels) related to this node
	tempDic = {}
	if node.isRoot == 1:
		tempDic = TheChilds(attributeNumbers-1)
	
	else:		
		for x in range(1,trainingsetRows):
			if CheckPath(node,x) == PathDepth(node):					#if the length of path is equal to the same value as the edges, then 
				tempArr.append(trainingset[attributeNumbers-1][x])
		
		tempStr = ""
		for item in tempArr:
			tempStr = tempStr + " " + item
		tempStr = tempStr.strip()
		tempStr = tempStr.split(" ")

		tempDic = {}
		for word in tempStr:																	
			if word in tempDic:
				tempDic[word]+= 1
			else:
				tempDic[word] = 1
				
	return tempDic

###################################################################################################################################################

def IsLeafNode(node):
	
	tempDic = TheInstances(node)
	sum = 0
	for word in tempDic:
		sum = sum + tempDic[word]
		
	for word in tempDic:
		if sum == tempDic[word]:
			return 1
	
	return 0
	
###################################################################################################################################################

def EntropyOfArr(arr):			#return the entropy of instances inside 'arr'
	
	entropy = 0.000
	tempStr = ""
	for item in arr:
		tempStr = tempStr + " " + item
	tempStr = tempStr.strip()
	tempStr = tempStr.split(" ")

	tempDic = {}
	for word in tempStr:																	
		if word in tempDic:
			tempDic[word]+= 1
		else:
			tempDic[word] = 1
	
	sum = 0.0000
	for word in tempDic:
		sum = sum + tempDic[word]
	
	for word in tempDic:												#calculate entropy
		entropy = entropy - (tempDic[word] / sum) * math.log(tempDic[word] / sum , 2) 
		
	return entropy	

##################################################################################################################################################

def GainFunction(node,attribute):						#return the 'gain' of inputs

	s = 0.000
	s = sum(node.instances.values())					#indicate the sum of instances in the node
	
	i = IndexOfHeader(attribute)
	tempArr = []
	for x in range(1,trainingsetRows):
		tempArr.append(trainingset[i][x])
	
	tempStr = ""
	for item in tempArr:
		tempStr = tempStr + " " + item
	tempStr = tempStr.strip()
	tempStr = tempStr.split(" ")

	tempDic = {}
	for word in tempStr:																	
		if word in tempDic:
			tempDic[word]+= 1
		else:
			tempDic[word] = 1
			
	tempArr = []
	arr = []
	for word in tempDic:								#creat nodes from this node and put them inside the arr[]
		for x in range(1,trainingsetRows):
			if CheckPath(node,x) == PathDepth(node):			
				if trainingset[i][x] == word:
					tempArr.append(trainingset[attributeNumbers-1][x])
		arr.append(tempArr)
		tempArr = []
		
	gain = 0.000
	for item in arr:
		gain = gain + (len(item) / s) * EntropyOfArr(item)	#calculate gain
		
	gain = Entropy(node) - gain
	
	return gain

###################################################################################################################################################

def PrintTree(tree):
	file = open("Output.dot", "w")
	
	line = "digraph G\n"
	file.write(line)
	line = "{\n"
	file.write(line)
	
	numOfNodes   = 0
	numOfSplits  = 0
	maximumDepth = 0
	for node in tree:
		numOfNodes   += 1
		if node.depth > maximumDepth:
			maximumDepth = node.depth
		if node.isLeaf == 0:
			numOfSplits  += 1
	line = "    graph [label=" + '"' + "Decision Tree\\n\\nNumber of Nodes = " + str(numOfNodes) + "\\nNumber of Splits = " + str(numOfSplits) + "\\nMaximum Depth = " + str(maximumDepth) + "\\n\\n" + '"' + ", labelloc=t] ;\n"
	file.write(line)
	
	for node in tree:
	
		numOfDiffInstances = ""
		for i, j in node.instances.items():
			numOfDiffInstances = numOfDiffInstances + str(i) + ": " + str(j) + "\\n"
		
		if node.isLeaf == 0:
			line = "    " + node.level + " " + "[shape=box, " + "color=" + node.color + ", label=" + '"' + "Split: " + str(node.value) + '\\n' + "Entropy = " + str(float("{0:.4f}".format(node.entropy))) + "\\nInstances = " + str(node.numOfInstances) + "\\nDecision = " + str(max(node.instances, key=node.instances.get)) + "\\n" + numOfDiffInstances + '"' + "] ;\n" 
			file.write(line)
			for x in range(0,node.childNumber):
				line = "    " + node.level + " -> " + node.children[x].level + " [label=" + '"' + node.children[x].inputEdge + '"] ;\n' 
				file.write(line)
		else:
			line = "    " + node.level + " " + "[shape=box, " + "color=" + node.color + ", label=" + '"' + "Leaf" + '\\n' + "Entropy = " + str(float("{0:.4f}".format(node.entropy))) + "\\nInstances = " + str(node.numOfInstances) + "\\nDecision = " + str(max(node.instances, key=node.instances.get)) + "\\n" + numOfDiffInstances + '"' + "] ;\n" 
			file.write(line)
	
	line = "}\n"
	file.write(line)
	
	file.close()
	
#################### Main Process of Program ###################################################################################################################################

ReadingData()

dtree = []																							#save decision tree inside 'dtree' array
tempDic = {}
tempDic = TheChilds(attributeNumbers - 1)															#insert the classification instances as root instances
dtree.append(Node(1,0,0,"","",0,"","",[],tempDic,"1",1))											#create the root node with the classification label instances
tempArr = []

for x in range(0,attributeNumbers - 1):																#choose the attribute with the greater 'gain' value for root node of tree
	tempArr.append(GainFunction(dtree[0],trainingset[x][0]))
index = TheGreaterOneIndex(tempArr)										
tempDic = TheChilds(index)
childNumber = 0
outputEdges = []
for word in tempDic:
	childNumber += 1
	outputEdges.append(word)
	
tempDic = TheInstances(dtree[0])

dtree[0].childNumber = childNumber																	#add extra information to root node 
dtree[0].outputEdges = outputEdges
dtree[0].value = trainingset[index][0]
dtree[0].entropy = Entropy(dtree[0])
dtree[0].numOfInstances = sum(dtree[0].instances.values())
dtree[0].color = "red"
dtree[0].depth = 0


for x in range(0,dtree[0].childNumber):																#create the second level empty nodes
	dtree.append(Node(0,0,0,"",dtree[0],0,"",dtree[0].outputEdges[x],[],"",dtree[0].level + str(x+1),0))
	tempDic = TheInstances(dtree[x+1])
	dtree[x+1].instances = tempDic
	dtree[x+1].isLeaf = IsLeafNode(dtree[x+1])
	dtree[x+1].numOfInstances = sum(dtree[x+1].instances.values())
	dtree[x+1].depth = 1
	dtree[0].children.append(dtree[x+1])
	

arr   = []																							#temp array in order to save new nodes
level = 2																							#the level of nodes ( 1 for root node )
flag  = 0																							#check flag for break the while loop

while True:																							#find 'gain's and build the dtree
	for node in dtree:
		if node.isLeaf == 0 and node.check == 0:													#check the middle nodes and create new nodes from them if they're not leaf node		
			tempArr = []
			for x in range(0,attributeNumbers - 1):
				if dtree[0].value != trainingset[x][0]:												#check which attribute has more 'gain' value except the parent node attribute
					tempArr.append(GainFunction(node,trainingset[x][0]))
				else:
					tempArr.append(0)
			
			index = TheGreaterOneIndex(tempArr)
			
			if index >= 0:
				node.value = trainingset[index][0]													#the node spilt value	
				tempDic = TheChilds(index)
				childNumber = 0
				outputEdges = []
				for word in tempDic:
					childNumber += 1
					outputEdges.append(word)
				
				node.childNumber = childNumber
				node.outputEdges = outputEdges
				node.check = 1
				node.entropy = Entropy(node)
				node.color = "red"
					
				for x in range(0,node.childNumber):													#creating new nodes and save them into temp array arr[]
					arr.append(Node(0,0,0,"",node,0,"",node.outputEdges[x],[],"",node.level + str(x+1),0))		
					tempDic = TheInstances(arr[len(arr) - 1])
					arr[len(arr) - 1].instances = tempDic
					arr[len(arr) - 1].isLeaf = IsLeafNode(arr[len(arr) - 1])
					arr[len(arr) - 1].numOfInstances = sum(arr[len(arr) - 1].instances.values())
					arr[len(arr) - 1].depth = node.depth + 1
					node.children.append(arr[len(arr) - 1])
				
			else:
				node.value  = node.instances
				node.isLeaf = 1
				node.check  = 1
				node.entropy = Entropy(node)
				node.numOfInstances = sum(node.instances.values())
				node.depth = node.parent.depth + 1
				if node.entropy == 0:
					node.color = "green"
				else:
					node.color = "blue"
				
		elif node.isLeaf == 1:																		#if node is leaf then assing the value attribute
			node.value = node.instances
			node.check = 1
			node.entropy = Entropy(node)
			node.numOfInstances = sum(node.instances.values())
			if node.entropy == 0:
				node.color = "green"
			else:
				node.color = "blue"
	
	for node in arr:																				#insert new nodes into main arr
		dtree.append(node)
	arr = []
	
	for node in dtree:																				#check the condition of breaking while loop
		if node.check == 1:
			flag = 1
		else:
			flag = 0
			break
	
	if flag == 1:
		break
	
	level += 1
#END OF while(True)

PrintTree(dtree)

#start to trace the tree and check the test set values according to tree edges value,
	# 'currentNode' stand for the which node we are now in the tree

currentNode = dtree[0]
tempHeaderIndex = 0
exitFlag = 0
defaultIndex = 0
	
for j in range(0,attributeNumbers-1):
	if currentNode.value == testset[j][0]:
		tempHeaderIndex = j
		defaultIndex = j
		break
	
tempArr = []
for i in range(1,testsetRows):								#for each row of testset
	tempHeaderIndex = defaultIndex							#reset the current node index in each iteration						
	n = currentNode.childNumber
	x = 0													#x refers to the number of children
	while True:												#while loop for each row of testset
		#trace the children of current node and check the label of edges
		if currentNode.children[x].inputEdge.strip() == testset[tempHeaderIndex][i].strip():
			currentNode = currentNode.children[x]
			if currentNode.isLeaf == 1:						#if the current node is leaf node so it is going to end, else, go deeper and find next node
				if str(max(currentNode.instances, key=currentNode.instances.get)) == testset[attributeNumbers-1][i]:
					# print "ok"							#the answer of my tree equal to the real answer, print ok
					tempArr.append("Pass!")
					currentNode = dtree[0]					#reset the current node, break while loop and go to next row of testset
					break
				else:			
					# print "fail"							#the answer of my tree in not equal to the real answer, print fail
					tempArr.append("Fail!")
					currentNode = dtree[0]					#reset the current node, break while loop and go to next row of testset
					break
			else:
				for j in range(0,attributeNumbers-1):
					if currentNode.value == testset[j][0]:
						tempHeaderIndex = j
						x = 0
						break
				
		else:
			x += 1
			if x > n:
				currentNode = dtree[0]
				#print "noisy data"									#noisy data case, happen when the test set attributes are different than tree edge labels
				tempArr.append("NoisyData!")
				break
				
	

file = open("Testset Report.txt", "w")								#write the testset result to textfile						
file.write("The testset output by my own decision tree and test error for each line of testset is:\n\n")		
for item in tempArr:
	file.write(item)
	file.write("\n")
file.write("\n'Fail!' means the output of tree is not the same as real classification label\n")
file.write("'Pass!' means the output of tree is same as real classification label\n")
file.write("'NoisyData!' means the values of testset at that row has noisy data\n\n")
file.write("The test error is as below:\n")
	
numOfFails = 0
all = 0
for item in tempArr:
	all += 1
	if item == "Fail!":
		numOfFails += 1

file.write("The number of failed test cases: " + str(numOfFails) + "\n") 
file.write("The number of all test cases: " + str(all) + "\n") 
answer = 0.0000
answer = numOfFails / all
file.write("The test error: " + str(numOfFails) + "/" + str(all) + " = " + str(answer)) 	#write the testset error to textfile	
file.close()
