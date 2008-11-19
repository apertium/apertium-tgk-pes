#!-- encoding:utf-8 --#

casualVerbLemma = u'    <e lm="pastROOTن"><i></i><par n="/VERBS" prm="pastROOT" prm2="presROOT" prm3="hasTHEY" /></e>'

def makeVerbDefs(verbRoot , verbRoot0 , theY):
	result = casualVerbLemma.replace('pastROOT',verbRoot)
	result = result.replace('presROOT',verbRoot0)
	result = result.replace('hasTHEY', theY)
	return result

def getVerbsFile(fileName):
	import codecs
	f = codecs.open(fileName, 'r', 'utf-8')
	allLines = f.readlines()
	f.close()
	return allLines

def writeVerbsFile(fileName, theStr):
	import codecs
	f = codecs.open(fileName, 'w', 'utf-8')
	f.write(theStr)
	f.close()

#This is used for csv files have been created by ooo. so all the lines have 3 ,
#if n's column is empty all N>n will be empty
mlist =getVerbsFile('verbs.csv');
simpleDefs = u""
twoRootDefs =u""
ycontainedDefs =u""
for pairs in mlist:
	vroot = pairs.split(',');
	#using to prevent processing if it is empty
	if (len(vroot[0])<2 or len(vroot[1])<2):
		pass
	#using the format of cheshidan
	if(vroot[0].strip()!=''):
		if (len(vroot[2].strip())>1): 
			endY = vroot[2].strip()[1:-1]
		else:
			endY = u""
		simpleDefs = simpleDefs + makeVerbDefs(vroot[0].strip()[1:-1],vroot[1].strip()[1:-1],endY)+'\n'
print simpleDefs
writeVerbsFile('myverbparadigms.txt', simpleDefs)
		



