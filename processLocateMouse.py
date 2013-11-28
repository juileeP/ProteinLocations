import xml.etree.cElementTree as ET
import os
import MySQLdb

tree = ET.ElementTree(file='LOCATE_mouse.xml')
root = tree.getroot()
#_p = '{http://uniprot.org/uniprot}'

print "opened"

mydb = MySQLdb.connect(host='db.eecis.udel.edu',port=3306,user='patankar',passwd='proteins',db='JEPSLD')
cursor = mydb.cursor()
print "connected..."

# list of individual variables
jepsld_id = 21466  #it will get a value after prot atlas insertion is completed
locationId = 21466 #it will get a value after prot atlas insertion is completed
#publicationId = 21466
cellLineId = 0
taxonData = ""
taxonDataList = []
geneName = ""
geneNameList = []
proteinName = ""
organism = ""
uniprotID = ""
uniprotIdList = []
ensId = ""
mainLocation = ""
mainLocationList = []
otherLoc = ""
otherLocMin = []
otherLocStr = ""
ResourceDb = "LOCATE"
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
cellLineSet = []
cellLineLocation = ""
cellLineList = []
cellLineLocList = []
cellBool = False
taxon = 0
locs = []
locs1 = []
accn = ""
source_name = ""
pmid = []
pubmedIds = ""
entrezgeneID = ""
refseqID = ""
ensemblproteinID = ""
ensemblgeneID = ""
#f= open('workfilemouse','w')
uniprotcount = 0
ensemblproteincount = 0
ensemblgenecount = 0
entrezgenecount = 0
multiple = 0;
locationlength = 0;

for child in root:
	mainLocationList = []
	pmid = []
	imagefilename = []
	cellLine = []
	uniprotID = ""
	entrezgeneID = ""
	refseqID = ""
	ensemblproteinID = ""
	ensemblgeneID = ""
	#print child.tag
	if child.tag == 'LOCATE_protein':
		for i in child:
			#print i.tag
			if i.tag == "protein":
				for j in i:
					#print j.tag
					if j.tag == "organism":
						organism = j.text
						#print "Organism: ", organism
					if j.tag == "source":
						for k in j:
							#print k.tag
							if k.tag == "source_name":
								source_name = k.text
							if k.tag == "accn":
								#accn = k.text
								if source_name == "Entrez Gene":
									entrezgeneID = k.text
								if source_name == "RefSeq Protein":
									refseqID = k.text
								if source_name == "Ensembl-Peptide Mouse":
									ensemblproteinID = k.text


			if i.tag == "experimental_data":
				for j in i:
					#print j.tag
					if j.tag == "images":
						for k in j:
							#print k.tag
							if k.tag == "rep_image":
								for l in k:
									#print k.tag
									if l.tag == "filename":
										imagefilename.append(l.text)

									if l.tag == "celltype":
										cellLineList.append(l.text)
							if k.tag == "image":
								for l in k:
									#print k.tag
									if l.tag == "filename":
										imagefilename.append(l.text)

									if l.tag == "celltype":
										cellLineList.append(l.text)
							if k.tag == "locations":
								
								for l in k:
									#print k.tag
									if l.tag == "location":
										for m in l:
											#print k.tag
											if m.tag == "tier1":
												mainLocationList.append(m.text)
											if m.tag == "tier2":
												mainLocationList.append(m.text)
											if m.tag == "tier3":
												mainLocationList.append(m.text)


										
			if i.tag == "externalannot":
				for j in i:
					#print j.tag
					if j.tag == "reference":
						for k in j:
							#print k.tag
							if k.tag == "pmid":
								pmid.append(k.text)
							if k.tag == "locations":
								for l in k:
									#print k.tag
									if l.tag == "location":
										for m in l:
											#print k.tag
											if m.tag == "tier1":
												mainLocationList.append(m.text)
											if m.tag == "tier2":
												mainLocationList.append(m.text)
											if m.tag == "tier3":
												mainLocationList.append(m.text)






			if i.tag == "xrefs":
				for j in i:
					#print j.tag
					if j.tag == "xref":
						for k in j:
							#print k.tag
							if k.tag == "source":
								for l in k:
									#print k.tag
									if l.tag == "source_name":
										xref_source = l.text				
									if l.tag == "accn":
										if xref_source == "Entrez Gene":
											entrezgeneID = l.text
										if xref_source == "RefSeq Protein":
											refseqID = l.text
										if xref_source == "UniProtKB-SwissProt":
											uniprotID = l.text
										if xref_source == "Ensembl-Peptide Mouse":
											ensemblproteinID = l.text
										if xref_source == "Ensembl-Gene Mouse":
											ensemblgeneID = l.text

								


	if mainLocationList != locs1:   # main location list is the list containing location....locs 1 is an empty list (checking if a protein has a location here)
		jepsld_id = jepsld_id+1
		#publicationId = publicationId+1
		locationId = locationId+1
		cellLineId = cellLineId+1
		mainLocation = ";".join(mainLocationList)
		#pubmedIds = ";".join(pmid)
		cellLineSet = set(cellLineList)
		cellLine = ";".join(cellLineSet)
		print "JEPSLD ID : ", jepsld_id                             # JEPSLD ID
		#print "Uniprot ID : ", uniprotIdList
		#print "Protein name : ", proteinName
		#print "gene name : ", geneNameList
		#print "organism : ", organism                            # organism name 
		#print "Source name: ", source_name                       # resource database
		#print "taxon : ", taxon
		#print "Location ID : ", locationId                       # location id
		#print "location: ", mainLocation                  # main location as list
		#locationlength = len(mainLocationList)
		#if locationlength > 1:
			#multiple = multiple+1
		#print "Total no of protein with multiple locations: ", multiple
		#print " Location list length: ", locationlength
		#print "Publication ID : ", publicationId                 # publication id
		#print "PubMed ID: ", pubmedIds				 # pubmed id as list								
		#print "RefSeqID : ", refseqID                            # refseq id
		#print "Ensembl protein ID:  ", ensemblproteinID          # refseq protein id
		#print "Ensembl gene ID: ", ensemblgeneID                 # ensembl gene id
		#print "Entrez gene ID: ", entrezgeneID                   # entrez gene id
		#print "UniProt/SwissProt ID: ", uniprotID                # swissprot id
		#print "Image filename: ", imagefilename   #variable contains file name of images....we are not storing this information currently
		#print "Cell line: ", cellLine                            # cell line name
		#if uniprotID != "":
			#uniprotcount = uniprotcount+1
		#if ensemblgeneID != "":
			#ensemblgenecount = ensemblgenecount+1
		#if ensemblproteinID != "":
			#ensemblproteincount = ensemblproteincount+1
		#if entrezgeneID != "":
			#entrezgenecount = entrezgenecount+1
		#print "uniprot count: ", uniprotcount
		#print "ensemblgene count: ", ensemblgenecount
		#print "ensemblprotein count: ", ensemblproteincount
		#print "entrezgene count: ", entrezgenecount
		#print "Accn: ", accn
		#print" *************************************************** 
		print "inserting ..."
		cursor.execute("""INSERT INTO protein_info(JEPSLD_ID, gene_name, swissprot_ID, ensemblgene_ID, ensemblprotein_ID, resource_database, organism, refseq_ID, protein_name, omim_ID, entrezgene_ID) \
                 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (jepsld_id,"null",uniprotID,ensemblproteinID,ensemblgeneID,ResourceDb,organism,refseqID,"null","null",entrezgeneID))                 
                cursor.execute("""INSERT INTO location(location_ID, gene_name,main_location,other_location,resource_database,ensemblprotein_ID) VALUES (%s,%s,%s,%s,%s,%s)""", (locationId,"null",mainLocation,"null",ResourceDb,ensemblproteinID))
                cursor.execute("""INSERT INTO cell_line(cell_line_ID, cell_line, cell_line_location, gene_name, resource_database, ensemblprotein_ID) VALUES (%s,%s,%s,%s,%s,%s)""", (cellLineId,cellLine,"null","null",ResourceDb,ensemblproteinID))
                    
		#f.write(uniprotID)
		#f.write('\n')

