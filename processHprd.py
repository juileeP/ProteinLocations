
__author__ = 'Juilee'
#import re
import xml.etree.cElementTree as ET
import os
import MySQLdb


###############VARIABLES FOR EACH FILE######################

jepsld_id = 0  # will get value after Suba file
locationId = 0  #same
publicationId = 0 #same
geneName = ""
proteinName = ""
omimId = ""
refSeqId = ""
mainLocation = ""
mainLocList = []
mainLocStr = ""
otherLocation = ""
otherLocs = []
otherLocationSet = []
pubmedIds = ""
pubmed = []
pubmedO = []
pubmedIdsO = ""
pubmedIdList = ""
resourceDb = "Human Protein Reference Database"
uniProtId = ""
entrezGeneId = ""
organism = "Homo Sapiens"
countTotal = 0
countMultiple = 0
bool = False

#################SUBROUTINES#######################


def openFolder():
    global countTotal
    global jepsld_id
    global locationId
    global publicationId
    path = '/eecis/shatkay/homes/patankar/HPRDXML/'
    listing = os.listdir(path)
    for infile in listing:
        countTotal = countTotal+1
        print "current file is: ", infile 
        #print "calliing the root function..."
        root = makeRoot(path+infile) 
        bool = checkCellularComp(root)
        if bool:
           jepsld_id = jepsld_id+1
           locationId = locationId+1
           publicationId = publicationId+1
           getData(root)
           #printData()
           print "inserting..."
           dbInsertion()
        else:
            continue

def makeRoot(infile):
    tree = ET.parse(infile)
    root = tree.getroot()
    return root



def checkCellularComp(root):
    for child in root:
        for i in child:
            if i.tag == "{org:hprd:dtd:hprd3r}cellular_component":
               #print " IM in the right file..........."
               bool = True
               return bool

def dbInsertion():
    global cursor
    cursor.execute("""INSERT INTO protein_info(JEPSLD_ID, gene_name, swissprot_ID, ensemblgene_ID, ensemblprotein_ID, resource_database, organism, refseq_ID, protein_name, omim_ID, entrezgene_ID) \
                   VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (jepsld_id,geneName,uniProtId,"null","null",resourceDb,organism,refSeqId,proteinName,omimId,entrezGeneId))
    cursor.execute("""INSERT INTO location(location_ID, gene_name,main_location,other_location,resource_database) VALUES (%s,%s,%s,%s,%s)""", (locationId,geneName,mainLocation,otherLocation,resourceDb))
    cursor.execute("""INSERT INTO publication(publication_ID, gene_name, pubmed_ID, resource_database, ensemblprotein_ID) VALUES (%s,%s,%s,%s,%s)""", (publicationId,geneName,pubmedIds,resourceDb,"null"))
 

def printData():
    print "JESPLD ID: ", jepsld_id
    print "Location ID : ", locationId
    print "Publication ID : ", publicationId
    print "Gene Name : ", geneName
    print "protein name : ", proteinName
    print "pubmedIds is ", pubmedIdList
    print "OMIM ID ", omimId
    print "Ref seq ID : ", refSeqId
    print "organism is : ", organism
    print "Main Location is : ", mainLocation
    print "Other Location is : ", otherLocation
    print "Resource database is :  ", resourceDb
    print "Swiss Prot : ", uniProtId
    print "EntrezGene Id : ", entrezGeneId
    print "\n"
    print "****************"

def getData(root):
    global uniProtId
    global entrezGeneId
    global pubmed
    global pubmedO
    global pubmedIdsO
    global pubmedIdList
    global otherLocs
    global mainLocStr
    global countMultiple
    mainLocMin = []
    otherLocs = []
    pubmedO = []
    pubmed = []
    
    print " im inside get data ....."
    for child in root:
        for i in child:
            if i.tag == "{org:hprd:dtd:hprd3r}external_links":
               for j in i:
                   if j.tag == "{org:hprd:dtd:hprd3r}SwissProt":
                      uniProtId = j.text
                   if j.tag == "{org:hprd:dtd:hprd3r}EntrezGene":
                      entrezGeneId = j.text
    for child in root:
        for i in child:
            if i.tag == "{org:hprd:dtd:hprd3r}cellular_component":
               for j in i:
                   if j.tag == "{org:hprd:dtd:hprd3r}primary":
                      for k in j:
                          if k.tag == "{org:hprd:dtd:hprd3r}title":
                             global mainLocation
                             mainLocation = k.text
                             mainLocMin.append(mainLocation)
                          if k.tag == "{org:hprd:dtd:hprd3r}pubmed":     
                             global pubmedIds
                             pubmed.append(k.text)
                   if j.tag == "{org:hprd:dtd:hprd3r}alternate":
                      for k in j:
                          if k.tag == "{org:hprd:dtd:hprd3r}title":
                             global otherLocation
                             otherLocs.append(k.text)
                          if k.tag == "{org:hprd:dtd:hprd3r}pubmed":
                             pubmedO.append(k.text)
    otherLocationSet = set(otherLocs)
    mainLocStr = ';'.join(mainLocMin)
    listLen = len(mainLocMin);
    if listLen > 1:
        countMultiple = countMultiple+1
    otherLocation = ';'.join(otherLocationSet)           #OTHER LOCATION
    pubmedIds = ';'.join(pubmed)                         #PUBMED IDS
    pubmedIdsO = ';'.join(pubmedO)
    pubmedIdList = "Main:"+pubmedIds+";Other:"+pubmedIdsO
    for child in root:
        for i in child:
            if i.tag == "{org:hprd:dtd:hprd3r}titles":
               for j in i:
                   if j.tag == "{org:hprd:dtd:hprd3r}title":
                      global geneName
                      geneName = j.text                               #GENE NAME
                      bool = True
                   if j.tag == "{org:hprd:dtd:hprd3r}alt_title":
                      global proteinName
                      proteinName = j.text                            #PROTEIN NAME
                      bool = False
                   if bool == False:
                      break
    for child in root:
        for i in child:
            if i.tag == "{org:hprd:dtd:hprd3r}omim":
               global omimId
               omimId = i.text                             #OMIM
    for child in root:
        for i in child:
            #print i.tag
            if i.tag == "{org:hprd:dtd:hprd3r}isoform":
               for j in i:
                   if j.tag == "{org:hprd:dtd:hprd3r}seq_entry":
                      for k in j:
                          if k.tag == "{org:hprd:dtd:hprd3r}entry_protein":
                             global refSeqId
                             refSeqId = k.text                          #REFSEQ_ID                                                          
                            
##############MAIN PROCESS STARTS HERE##############

mydb = MySQLdb.connect(host='db.eecis.udel.edu',port=3306,user='patankar',passwd='proteins',db='JEPSLD')
cursor = mydb.cursor()
print "connected..."
openFolder()

print "final JEPSLD_ID is : ", jepsld_id
print "final total count is : ", countTotal
print "final multiple loc count is : ", countMultiple
