import xml.etree.cElementTree as ET
import MySQLdb

tree = ET.ElementTree(file='uniprot_sprot.xml')
root = tree.getroot()
_p = '{http://uniprot.org/uniprot}'

print "opened"

mydb = MySQLdb.connect(host='db.eecis.udel.edu',port=3306,user='patankar',passwd='proteins',db='JEPSLD')
cursor = mydb.cursor()
locs1 = []
print "connected"

# list of individual variables
jepsld_id = 66178  #it will get a value after prot atlas insertion is completed
locationId = 66178 #it will get a value after prot atlas insertion is completed
publicationId = 23943
taxonData = ""
taxonDataList = []
geneName = ""
geneNameList = []
proteinName = ""
organism = ""
uniprotId = ""
uniprotIdList = []
ensId = ""
mainLocation = ""
mainLocationList = []
otherLoc = ""
otherLocMin = []
otherLocStr = ""
ResourceDb = "UniProtKB/SwissProt"
bool = False
list = []
listO = []
listL = []
tissueId = 0
tissueName = ""
cellId = 0
cellType = ""
cellLineId = 0
cellLine = ""
cellLineLocList = []
cellLineLoc = ""
cellBool = False
refseqId = ""
ensemblId = ""
taxon = 0
locs = []
locs1 = []
multiple = 0;
locationlength = 0;
pubmedId = ""
pubmedIdlist = []
ensemblgeneID = ""
ensemblproteinID= ""

genenameStr = ""
locationStr = ""
pubmedidsStr = ""
uniprotidStr = ""

for child in root:
	uniprotIdList = []
	geneNameList = []
	taxonDataList = []
	mainLocationList = []
	listO = []
	listL = []
	count = 0
	taxon = 0
	locs = []
	pubmedIdlist = []
	ensemblgeneID = ""
	ensemblproteinID= ""
	if child.tag == _p+'entry':
		#print "in entry"
		for i in child:
			#print "in i", i.tag
			if i.tag == _p+'accession':   #swiss prot id
				uniprotId = i.text
				uniprotId.replace("'","")
				uniprotIdList.append(uniprotId)
				#print "Uniprot ID : ", uniprotIdList
			if i.tag == _p+"protein":
				for j in i:
					#print "in j", j.tag
					if j.tag == _p+"recommendedName":
						for k in j:
							#print "in k", k.tag
							if k.tag == _p+"fullName":
								proteinName = k.text
								#print "Protein name : ", proteinName
		#for i in child:
			if i.tag == _p+'gene':   #genename	
				for j in i:
					if j.tag == _p+"name":            
						geneName = j.text 
						geneName.replace("'","")
						geneNameList.append(geneName)
						#print "gene name : ", geneNameList 
		#for i in child:
			if i.tag == _p+'organism':   #organism	
				for j in i:
					if j.tag == _p+"name":   
						listO = j.attrib
                                    		if listO['type'] == "scientific":
                                        		organism = j.text  
							#print "organism : ", organism
					
					if j.tag == _p+"lineage":
						#print "in lineage: ", j.tag
						for k in j:
							#print "in taxon tage is: ", k.tag
							if k.tag == _p+"taxon":
								taxonData = k.text
								if taxonData == "Eukaryota":
									taxon=1
								taxonData.replace("'","")
								taxonDataList.append(taxonData)
								#print "taxon : ", taxon

		#for i in child:
			if i.tag == _p+'comment':   #location	
				#print "in comment: ", i.tag
				listL = i.attrib
				if listL['type'] == "subcellular location":
					
					for j in i:
						if j.tag == _p+"subcellularLocation":
							#print "in subcellular location: ", j.tag
							for k in j:
								#print "k.attrib ", k.attrib
								if k.tag == _p+'location' and \
									len(k.attrib) == 0:
									locs.append(k.text)
									#print "Locations: ", locs
									#mainLocation = k.text  
									#mainLocation.replace("'","")
									#mainLocationList.append(mainLocation)

			if i.tag == _p+"reference":
				for j in i:
					if j.tag == _p+"citation":
						for k in j:
							if k.tag == _p+"dbReference":
                						list = k.attrib
                						if list['type'] == "PubMed":               #ensemble id
                   							#print " Ensemble Id : ", list['id']
                							pubmedId = list['id']
									pubmedIdlist.append(pubmedId)


			if i.tag == _p+"dbReference" :
                		list = i.attrib
                		if list['type'] == "RefSeq":               #ensemble id
                   			#print " Ensemble Id : ", list['id']
                  			refseqId = list['id']
				if list['type'] == "Ensembl":   
				           
					#ensemblId = list['id']
					for j in i:
						if j.tag == _p+"property":
							list = j.attrib
							if list['type'] == "protein sequence ID":
								ensemblproteinID = list['value']
							if list['type'] == "gene ID":
								ensemblgeneID = list['value']

                		#if list['type'] == "Pubmed":               #ensemble id
                   			#print " Ensemble Id : ", list['id']
                    			#pubmedId = list['id']
	if taxon == 1:
		if locs != locs1:
			jepsld_id = jepsld_id+1
			publicationId = publicationId+1
			locationId = locationId+1
			genenameStr = ';'.join(geneNameList)
			locationStr = ';'.join(locs)
			pubmedidsStr = ';'.join(pubmedIdlist)
			uniprotidStr = ';'.join(uniprotIdList)
			print "JEPSLD ID : ", jepsld_id
			#print "Uniprot ID : ", uniprotidStr
			#print "Protein name : ", proteinName
			#print "gene name : ", genenameStr
			#print "organism : ", organism
			#print "taxon : ", taxonDataList
			#print "taxon : ", taxon
			print "Location ID : ", locationId
			#print "location: ", locationStr
			#locationlength = len(locs)
			#if locationlength > 1:
			#	multiple = multiple+1
			#print "Total no of protein with multiple locations: ", multiple
			#print " Location list length: ", locationlength
			print "Publication ID : ", publicationId
			#print "RefSeqID : ", refseqId
			#print "EnsemblproteinID: ", ensemblproteinID
			#print "EnsemblgeneID:  ", ensemblgeneID
			#print "pubmed ID: ", pubmedidsStr
			print" *************************************************** /"
			cursor.execute("""INSERT INTO location(location_ID, gene_name,main_location,other_location,resource_database,ensemblprotein_ID) VALUES (%s,%s,%s,%s,%s,%s)""", (locationId,genenameStr,locationStr,"null",ResourceDb,ensemblproteinID))
			cursor.execute("""INSERT INTO protein_info(jepsld_id, gene_name, swissprot_ID, ensemblgene_ID, ensemblprotein_ID, resource_database, organism, refseq_ID, protein_name, omim_ID, entrezgene_ID) \
        		 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (jepsld_id,genenameStr,uniprotidStr,ensemblgeneID,ensemblproteinID,ResourceDb,organism,refseqId,proteinName,"null","null"))
        		cursor.execute("""INSERT INTO publication(publication_ID, gene_name, pubmed_ID, resource_database, ensemblprotein_ID) VALUES (%s,%s,%s,%s,%s)""", (publicationId,genenameStr,pubmedidsStr,ResourceDb,"null"))


     
                
