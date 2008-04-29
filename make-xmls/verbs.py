#!-- encoding:utf-8 --#
soreg=u'    <e lm="presROOTیدن"><par n="P__prefixes"/><i>presROOT</i><par n="چش/یدن__vblex"/></e>\r\n'
boreg=u'    <e lm="pastROOTن"><par n="P__prefixes"/><i></i> <par n="/pastROOTن__vblex"/></e>\r\n'
byoreg=u'    <e lm="pastROOTن"><par n="P__prefixes"/><i></i> <par n="/pastROOTن__vblex"/></e>\r\n'
spara =u''
bpara =u''''
    <pardef n="/pastROOTن__vblex">
      <e>
        <p>
          <l>pastROOT</l>
          <r>pastROOTن<s n="vblex"/><s n="past"/></r>
        </p>
        <par n="V__چشید/ن__vblex"/>
      </e>
      <e>
        <p>
          <l>presROOT</l>
          <r>pastROOTن<s n="vblex"/><s n="pres"/></r>
        </p>
        <par n="V__چش/[چشیدن]__vblex"/>
      </e>
    </pardef>'''

bypara =u'''
    <pardef n="/pastROOTن__vblex">
      <e>
        <p>
          <l>pastROOT</l>
          <r>pastROOTن<s n="vblex"/><s n="past"/></r>
        </p>
        <par n="V__چشید/ن__vblex"/>
      </e>
      <e>
        <p>
          <l>presROOT</l>
          <r>pastROOTن<s n="vblex"/><s n="pres"/></r>
        </p>
        <par n="V__آزما/[آزمودن]__vblex"/>
      </e>
    </pardef>'''

def makeVerbDefs(verbRoot , verbRoot0 , mode=0):
	if(mode==0):
		result = soreg.replace('presROOT',verbRoot)
	elif(mode==1):
		result =boreg.replace('presROOT',verbRoot0)
	return result

def makeVerbParas(pastRoot, presentRoot,mode=0)
	if (mode==0):
		result =''
	elif (mode==1):
		result = bpara.replace('presROOT', presRoot)
		result = result.replace('pastROOT', pastRoot)
	elif (mode==2):
		result = bypara.replace('presROOT',presRoot)
		result = result.replace('pastROOT',pastRoot)
	elif 

def getVerbsFile(fileName):
	import codecs
	f = codecs.open(fileName, 'r', 'utf-8')
	allLines = f.readlines()
	f.close()
	return allLines

#This is used for csv files have been created by ooo. so all the lines have 3 ,
#if n's column is empty all N>n will be empty
mlist =getVerbsFile('verbs.csv');
simpleDefs = u""
twoRootDefs =u""
ycontainedDefs =u""
for pairs in mlist:
	vroot = pairs.split(',');
	if (len(vroot[1].strip())==0):
		#using the format of cheshidan
		if(vroot[0].strip()!=''):
			simpleDefs = simpleDefs + makeVerbDefs(vroot[0].strip()[1:-1])
	elif (len(vroot[2].strip())==0):
		#using the format of regular 2 rooted
			brootDefs = brootDefs + makeVerbDefs(vroot[0],vroot[0],mode =2)
		print vroot[1]
	elif (len(vroot[3].strip())==0):
		#using the format of azmaayidan
		print 'hi'
	elif ((len(vroot[4])>1)):
		#Do nothing in this case because they should be thought later
	elif (len(vroot[0])>0):
		#using to prevent processing if it is empty
print simpleDefs
		



