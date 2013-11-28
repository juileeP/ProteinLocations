import xml.etree.cElementTree as ET

tree = ET.ElementTree(file='proteinatlas.xml')
root = tree.getroot()

geneNameList = []
geneName = ""
ensembleIdList = []
uniprotIdList = []

f = open("output.txt", "w")
#for child in root:
#    if child.tag == 'entry':
#       for i in child:
#            if i.tag == 'name':
#                geneName = i.text
#               # f.write(geneName+"\n")
#            geneNameList.append(i.text)
            

#print "gene list : ", geneNameList
#stro = ''.join(geneNameList)
#f.write(stro)
intList = []
strList = ""
ensId = ""
#for child in root:
#    if child.tag == "entry":
#       for i in child:
#            if i.tag == "identifier":
#                list = i.attrib
#                if list['db'] == "Ensembl":
#                    print " Ensemble Id : ", list['id']
#                    ensId = list['id']
#            #intList.append(ensId)
#            #strList = ''.join(intList)
#            #print "string is : ", strList  
#            ensembleIdList.append(ensId)
#            
#            for j in i:
#                    if j.tag == "xref":
#                       list = j.attrib
#                       if list['db'] == "Uniprot/SWISSPROT":
#                          print "Uniprot ID : ", list['id']
#                          uniprotIdList.append(list['id'])
#                          
#print " Ensemble Ids List is : ", ensembleIdList
#print "Uniprot Id list : ", uniprotIdList

tissueDict = {}
tissueName = ""
cellType = ""
tissueList = []
string = ""
str2 = ""
str3 = ""

string = " Dictionary value : \n"
f.write(string)
for child in root:
    if child.tag == "entry":
       for i in child:
           if i.tag == "tissueExpression":
               for j in i:
                   if j.tag == "data":
                       for k in j:
                           if k.tag == "tissue":
                               listT = k.attrib
                               if listT['status'] == "normal":
                                  tissueName = "Normal; "+k.text
                           if k.tag == "cellType":
                              cellType = k.text
                   tissueDict[tissueName]=cellType
                   str2 = ''.join(tissueDict)
                   f.write(str2)
    tissueList.append(tissueDict)
str3 = ''.join(tissueList)
f.write(str3)
                         

listL = []
mainLocation = ""
#mainLocationList = []
#otherLoc = ""
#otherLocMin = []
#otherLocList = []
#otherLocStr = ""
#mainStr = ""
#otherStr = ""
#for child in root:
#    if child.tag == "entry":
#       for i in child:
#           if i.tag == "subcellularLocation":
#               for j in i:
#                   if j.tag == "data":
#                       for k in j:
#                           if k.tag == "location":
#                              listL = k.attrib
#                              if listL['status'] == "main":
#                                  mainLocation = k.text
#                                  #print "Main Location : ", mainLocation, "\n"
#                              if listL['status'] == "additional":
#                                  otherLoc = k.text
#                                  #print "Other Location : ", otherLoc, "\n"
#                                  otherLocMin.append(otherLoc)
#                              otherLocStr = ';'.join(otherLocMin)
#    otherLocList.append(otherLocStr)
#    mainLocationList.append(mainLocation)
#
#mainStr = ';'.join(mainLocationList)
#otherStr = ''.join(otherLocStr)

#f.write("Main Location : \n")
#f.write(mainStr+"\n")
#f.write("Other Location : \n")
#f.write(otherStr+"\n")
