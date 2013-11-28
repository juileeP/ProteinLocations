import xml.etree.cElementTree as ET
import re
import MySQLdb

jepsld_id = 53791  #it will get a value after prot atlas insertion is completed
location_id = 53791 #it will get a value after prot atlas insertion is completed
publicationId = 21466

geneName = ""
proteinName = ""
proteinDesp = ""
pubmedIdS = ""
pubmedIdListS = []
swissProtId = ""
locGFP = ""
locGFPlist = []
locGFPset = []
pubmedIdG = ""
pubmedIdListG = []
locMS = ""
locMSlist = []
locMSset = []
pubmedIdM = ""
pubmedIdListM = []
GFPLocs = ""
MSLocs = ""
GFPPubmed = ""
MSPubmed = ""
Organism = "Arabidopsis thaliana"
ResourceDb = "Suba3"
TotalLocs = ""
TotalPubMeds = ""
count = 0
multiple = 0;
locationlength = 0;
MSLocsfinal = ""
#MSPubmedfinal = ""
#GFPPubmedfinal = ""
GFPLocsfinal = ""

mydb = MySQLdb.connect(host='db.eecis.udel.edu',port=3306,user='patankar',passwd='proteins',db='JEPSLD')
cursor = mydb.cursor()
locs1 = []
print "connected"

tree = ET.ElementTree(file='Suba3-04-06-2013.xml')
root = tree.getroot()
print("opened")


for i in root:
	#print child.tag
	for child in i:
		pubmedIdListM = []
		#pubmedIdM  = ""
		locMSlist = []
		pubmedIdListG = []
		#pubmedIdG = ""
		locGFPlist = []
		locMSset = []
		locGFPset = []
		TotalLocs = ""
		TotalPubMeds = ""
		GFPPubmed = ""
		MSPubmed = ""
	        if child.tag == "Gene":
			geneName = child.text
			#print "gene name : ", geneName
	        if child.tag == "Description":
			proteinDesp = child.text
			proteinName = proteinDesp.split(';')[0]
			#print "Protein Name : ", proteinName
		if child.tag == "Swiss-Prot_ID":
			swissProtId = child.text
			#print "Swiss Prot Id : ", swissProtId
		if child.tag  == "Location_GFP":
			#pubmedIdListG = []
	                pubmedIdG = ""
	                locGFPlist = []
	                
			#print "in GFP....."
			#print "tag is ", child.tag, "text is : ", child.text
			a = child.text
			if a:
				locGFP = re.sub("[^a-zA-Z;]", "", a)
				#print "before gfp is ", locGFP
				#locGFP.replace("'","")
				#print "after gfp is : ", locGFPlist
				pubmedIdG = re.sub("[^0-9;]", "", a)
				pubmedIdG.replace("'","")
		pubmedIdListG.append(pubmedIdG)
		locGFPlist.append(locGFP)

		if child.tag == "Location_Mass_Spec":
			#pubmedIdListM = []
			pubmedIdM  = ""
			locMSlist = []
			a = child.text
			if a:
				locMS = re.sub("[^a-zA-Z;]", "", a)
				#print "before MS is ", locMS
				#locMS.replace("'","")
				#print "after MS is : ", locMSlist
				pubmedIdM = re.sub("[^0-9;]", "", a)
				pubmedIdM.replace("'","")
		locMSlist.append(locMS)
		pubmedIdListM.append(pubmedIdM)
		
	if TotalLocs != locs1:
		locGFPset = set(locGFPlist)
		GFPLocs = ';'.join(locGFPset)
		GFPLocsfinal = ';'.join(map(str, list(set(GFPLocs.split(';')))))
		#print "GFP list : ", locGFPlist
		#print "GFP set : ", locGFPset
		
		GFPPubmed = ';'.join(pubmedIdListG)
		#print "GFP ids: ", GFPPubmed
		GFPPubmedfinal = ';'.join(map(str, list(set(GFPPubmed.split(';')))))
		#print "GFP ids final: ", GFPPubmedfinal
		locMSset = set(locMSlist)
		MSLocs = ';'.join(locMSset)
		MSLocsfinal = ';'.join(map(str, list(set(MSLocs.split(';')))))
		#print "MS list : ", locMSlist
		#print "MS set : ", locMSset
		#print "MS locs : ", MSLocsfinal
			#';'.join(map(str, list(set(MSlocs.split(';')))))
		MSPubmed = ';'.join(pubmedIdListM)
		MSPubmedfinal = ';'.join(map(str, list(set(MSPubmed.split(';')))))
		#print "MS pubmed ids: ", MSPubmed
		#print "GFP pubmed ids:", GFPPubmed
		#print "GFP locs : ", GFPLocsfinal
		#print "MS locs : ", MSLocsfinal
		TotalLocs = "GFP:"+GFPLocsfinal+";MS:"+MSLocsfinal
		#print "Total locs: ", TotalLocs
		TotalPubmeds = "GFP:"+GFPPubmed+";MS:"+MSPubmed
		
		#print "Total PubMed IDs: ", TotalPubmeds
		jepsld_id = jepsld_id+1
		location_id = location_id+1
		publicationId = publicationId+1
			
		print "JEPSLD ID : ", jepsld_id
	# 	print "Gene Name : ", geneName
	#        print "Swiss Prot Id : ", swissProtId
	#	print "Resource DB : ", ResourceDb
	#	print "Organism : ", Organism
	#	print "Protein Name : ", proteinName
		print "Location ID : ", location_id
		#print "Main Location : ", TotalLocs
		#locationlength = len(locGFPlist)+len(locMSlist)
		#if locationlength > 1:
			#multiple = multiple+1
		#print "Total no of protein with multiple locations: ", multiple
		#print " Location list length: ", locationlength
		print "Publication ID : ", publicationId
		#print "PubmedIDs : ", TotalPubmeds
		#print "*************************************"
			
		cursor.execute("""INSERT INTO protein_info(JEPSLD_ID, gene_name, swissprot_ID, ensemblgene_ID, ensemblprotein_ID, resource_database, organism, refseq_ID, protein_name, omim_ID, entrezgene_ID) \
		   VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (jepsld_id,geneName,swissProtId,"null","null",ResourceDb,Organism,"null",proteinName,"null","null"))
		cursor.execute("""INSERT INTO location(location_ID, gene_name,main_location,other_location,resource_database) VALUES (%s,%s,%s,%s,%s)""", (location_id,geneName,TotalLocs,"null",ResourceDb))
		cursor.execute("""INSERT INTO publication(publication_ID, gene_name, pubmed_ID, resource_database, ensemblprotein_ID) VALUES (%s,%s,%s,%s,%s)""", (publicationId,geneName,TotalPubmeds,ResourceDb,"null"))

