import MySQLdb

###database connection####
mydb = MySQLdb.connect(host='db.eecis.udel.edu',port=3306,user='patankar',passwd='proteins',db='JEPSLD')
cursor = mydb.cursor()
print "connected"

#cursor.execute("""SELECT * from protein_info WHERE jepsld_id < 100""")
#data = cursor.fetchall()
#for row in data:
#    print row[0]
#    print row[1]
#    print row[2]

######variables#####

role = ""
bool = True

#####Subroutines######


def userFunction():
    geneName = ""
    proteinName = ""
    swissProtId = ""
    global bool
    option = "100"
    print "Enter the on which basis you would like to query the database : \n"
    print "0. Gene Name"
    print "1. Protein Name"
    print "2. Accession No :"
    print "2a. Swiss Prot ID"
    print "2b. Ref Sequence ID"
    print "2c. Entrez Gene"
    print "2d. Ensemble Protein ID"
    print "2e. OMIM"
    print "2f. Ensemble Gene ID"
    print "3. JEPSLD ID"
    print "4. Location"
    print "5. Organism"
    print "6. Tissue Name"
    print "7. Cell Line"

    option = raw_input()


    if option == "0":
        print "Enter Gene Name \n"
        geneName = raw_input()
        cursor.execute("""SELECT gene_name from protein_info WHERE gene_name =%s""",(geneName))
        dataSet = cursor.fetchall()
        #print "Type is : ", type(data_from_Main)
        #for row in data_from_Main:
        #    print row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10]
        print "data set is ",dataSet
        getUserData(dataSet)

    elif option == "1":
        print "Enter Protein Name \n"
        proteinName = raw_input()
        cursor.execute("""SELECT gene_name from protein_info WHERE protein_name=%s""",(proteinName))
        data = cursor.fetchall()
        if data == ():
           bool = False
           cursor.execute("""SELECT ensemblprotein_ID from protein_info WHERE protein_name=%s""",(proteinName))
           data = cursor.fetchall()
        dataSet = set(data)
        getUserData(dataSet)

    elif option == "2a":
        print "Enter Swiss Prot ID \n"
        swissProtId = raw_input()
        cursor.execute("""SELECT gene_name from protein_info WHERE swissprot_ID=%s""",(swissProtId))
        data = cursor.fetchall()
        if data == ():
           bool = False
           cursor.execute("""SELECT ensemblprotein_ID from protein_info WHERE swissprot_ID=%s""",(proteinName))
           data = cursor.fetchall()
        dataSet = set(data)
        getUserData(dataSet)

    elif option == "2b":
        print "Enter Ref Sequence ID \n"
        refseqId = raw_input()
        cursor.execute("""SELECT gene_name from protein_info WHERE refseq_ID=%s""",(refseqId))
        data = cursor.fetchall()
        if data == ():
           bool = False
           cursor.execute("""SELECT ensemblprotein_ID from protein_info WHERE refseq_ID=%s""",(refseqId))
           data = cursor.fetchall()
        dataSet = set(data)
        getUserData(dataSet)

    elif option == "2c":
        print "Enter Entrez Gene \n "
        entrezgeneId = raw_input()
        cursor.execute("""SELECT gene_name from protein_info WHERE entrezgene_ID=%s""",(entrezgeneId))
        data = cursor.fetchall()
        if data == ():
           bool = False
           cursor.execute("""SELECT ensemblprotein_ID from protein_info WHERE entrezgene_ID=%s""",(entrezgeneId))
           data = cursor.fetchall()
        dataSet = set(data)
        getUserData(dataSet)

    elif option == "2d":
        print "Enter Ensemble Protein ID \n "
        ensemblProt = raw_input()
        cursor.execute("""SELECT gene_name from protein_info WHERE ensemblprotein_ID=%s""",(ensemblProt))
        data = cursor.fetchall()
        if data == ():
           bool = False
           cursor.execute("""SELECT ensemblprotein_ID from protein_info WHERE ensemblprotein_ID=%s""",(ensemblProt))
           data = cursor.fetchall()
        dataSet = set(data)
        getUserData(dataSet)

    elif option == "2e":
        print "Enter OMIM \n "
        omim = raw_input()
        cursor.execute("""SELECT gene_name from protein_info WHERE omim_ID=%s""",(omim))
        data = cursor.fetchall()
        if data == ():
           bool = False
           cursor.execute("""SELECT ensemblprotein_ID from protein_info WHERE omim_ID=%s""",(omim))
           data = cursor.fetchall()
        dataSet = set(data)
        getUserData(dataSet)

    elif option == "2f":
        print "Enter Ensemble Gene ID\n "
        ensemblGene = raw_input()
        cursor.execute("""SELECT gene_name from protein_info WHERE ensemblgene_ID=%s""",(ensemblGene))
        data = cursor.fetchall()
        if data == ():
           bool = False
           cursor.execute("""SELECT ensemblprotein_ID from protein_info WHERE ensemblgene_ID=%s""",(ensemblGene))
           data = cursor.fetchall()
        dataSet = set(data)
        getUserData(dataSet)

    elif option == "3":
        print "Enter JEPSLD ID \n "
        jepsld = raw_input()
        jepsld_id = int(jepsld)
        cursor.execute("""SELECT gene_name from protein_info WHERE jepsld_id=%s""",(jepsld_id))
        data = cursor.fetchall()
        if data == ():
           bool = False
           cursor.execute("""SELECT ensemblprotein_ID from protein_info WHERE jepsld_id=%s""",(jepsld_id))
           data = cursor.fetchall()
        dataSet = set(data)
        getUserData(dataSet)

    elif option == "4":
        print "Enter Location \n "
        location = raw_input()
        cursor.execute("""SELECT gene_name from protein_info WHERE main_location=%s""",(location))
        data = cursor.fetchall()
        print "gene name :", data
        if data == ():
           bool = False
           cursor.execute("""SELECT ensemblprotein_ID from protein_info WHERE main_location=%s""",(location))
           data = cursor.fetchall()
           print "ensembl : ", data
        dataSet = set(data)
        getUserData(dataSet)

    elif option == "5":
        print "Enter Organism \n "
        organism = raw_input()
        cursor.execute("""SELECT gene_name from protein_info WHERE organism=%s""",(organism))
        data = cursor.fetchall()
        #print "gene name : ", data
        if data == ():
           bool = False
           cursor.execute("""SELECT ensemblprotein_ID from protein_info WHERE organism=%s""",(organism))
           data = cursor.fetchall()
           print "Ensembl : ", data
        dataSet = set(data)
        getUserData(dataSet)

    elif option == "6":
        print "Enter Tissue Name \n "
        tissue = raw_input()
        cursor.execute("""SELECT gene_name from tissue_name WHERE tissue=%s""",(tissue))
        data = cursor.fetchall()
        if data == ():
            bool = False
            cursor.execute("""SELECT ensemblprotein_id from tissue_name WHERE tissue=%s""",(tissue))
            data = cursor.fetchall()
        dataSet = set(data)
        getUserData(dataSet)

    elif option == "7":
        print "Enter Cell Line \n "
        cellLine = raw_input()
        cursor.execute("""SELECT gene_name from cell_line WHERE cell_line=%s""",(cellLine))
        data = cursor.fetchall()
        if data == ():
            bool = False
            cursor.execute("""SELECT ensemblprotein_id from cell_line WHERE cell_line=%s""",(cellLine))
            data = cursor.fetchall()
        dataSet = set(data)
        getUserData(dataSet)
    else:
        print "Invalid option \n"

  


def getUserData(dataSet):
    for row in dataSet:
        print "row : ", row
        if bool:
            cursor.execute("""SELECT * from protein_info WHERE gene_name=%s""",(row))
            data_from_Main = cursor.fetchall()
            cursor.execute("""SELECT * from location WHERE gene_name=%s""",(row))
            data_from_Location = cursor.fetchall()
            cursor.execute("""SELECT * from cell_line WHERE gene_name=%s""",(row))
            data_from_CellLine = cursor.fetchall()
            cursor.execute("""SELECT * from tissue WHERE gene_name=%s""",(row))
            data_from_Tissue = cursor.fetchall()
            cursor.execute("""SELECT * from cell_type WHERE gene_name=%s""",(row))
            data_from_CellType = cursor.fetchall()
            cursor.execute("""SELECT * from publication WHERE gene_name=%s""",(row))
            data_from_Publication = cursor.fetchall()
        else:
            cursor.execute("""SELECT * from protein_info WHERE ensemblprotein_ID=%s""",(row))
            data_from_Main = cursor.fetchall()
            cursor.execute("""SELECT * from location WHERE ensemblprotein_ID=%s""",(row))
            data_from_Location = cursor.fetchall()
            print "Location data...."
            for row in data_from_Location:
                print row[0], row[1], row[2], row[3], row[4]
            cursor.execute("""SELECT * from cell_line WHERE ensemblprotein_ID=%s""",(row))
            data_from_CellLine = cursor.fetchall()
            cursor.execute("""SELECT * from tissue WHERE ensemblprotein_ID=%s""",(row))
            data_from_Tissue = cursor.fetchall()
            cursor.execute("""SELECT * from cell_type WHERE ensemblprotein_ID=%s""",(row))
            data_from_CellType = cursor.fetchall()
            cursor.execute("""SELECT * from publication WHERE ensemblprotein_ID=%s""",(row))
            data_from_Publication = cursor.fetchall()
    printUserData(data_from_Main,data_from_Location,data_from_CellLine,data_from_Tissue,data_from_CellType,data_from_Publication)


def printUserData(data_from_protein_info, data_from_location, data_from_cellLine, data_from_tissue, data_from_cellType, data_from_publication):
    #print "Im inside print function : "
    print "Protein Info data ******************************************** \n"
    print "JESPLD_ID    |   Protein Name    |   Gene Name   | Resource Database   |   SwissProt ID    |   RefSeq ID   | EntrezGene ID   |   Ensemblgene ID  |   Ensemblprotein ID   | Organism    |   OMIM ID |\n"

    for row in data_from_protein_info:
        print row[0], "|",row[1],"|", row[2],"|", row[3], "|",row[4],"|", row[5],"|", row[6],"|", row[7],"|", row[8],"|", row[9],"|", row[10]

    if data_from_location != ():
        print "Location data ************************************************* \n"
        print "Location ID  |   Main Location   |   Other Location |   Gene Name   |   Resource Database   |   Ensemblprotein ID   |\n"

        for row in data_from_location:
            print row[0], "|",row[1],"|", row[2],"|", row[3],"|", row[4], "|",row[5]

    if data_from_cellLine != ():
        print "Cell Line data ***************************************************** \n"
        print "Cell Line ID |   Cell Line   |   Cell Line Location |   Gene Name   |   Resource Database   |   Ensemblprotein ID   |\n"

        for row in data_from_cellLine:
            print row[0],"|", row[1],"|", row[2],"|", row[3],"|", row[4],"|", row[5]

    if data_from_tissue != ():
        print "Tissue data ************************************************************* \n"
        print "Tissue ID    |   Tissue Name |   Gene Name   | Resource Database   |   Ensemblprotein ID   |\n"

        for row in data_from_tissue:
            print row[0], "|",row[1],"|", row[2],"|", row[3], "|",row[4]

    if data_from_cellType != ():
        print "Cell Type data *************************************************************** \n"
        print "Cell Type ID |   Cell Type   |   Gene Name   | Resource Database   |   Ensemblprotein ID   |\n"

        for row in data_from_cellType:
            print row[0], "|",row[1],"|", row[2],"|", row[3],"|", row[4]

    if data_from_publication != ():
        print "Publication data ****************************************************************** \n"
        print "Publication ID   |   Pubmed IDs  |   Gene Name   | Resource Database   |   Ensemblprotein ID   |\n"

        for row in data_from_publication:
            print row[0],"|", row[1],"|", row[2],"|", row[3],"|", row[4]

def adminFunction():
    print "inside admin function..."
    print "Please select an option: "
    print "1. Insert new data"
    print "2. Delete data"
    print "3. Update data"
    option = raw_input()
    if option == "1":
        adminInsertFunction()
    elif option == "2":
        adminDeleteFunction()
    elif option == "3":
        adminUpdateFunction()
    else:
        print "You entered an invalid input \n"

def adminInsertFunction():
    print "Inside insert function for Admin \n"

    print "Select the table to insert data"
    print "1. protein_info"
    print "2. location"
    print "3. cell_line"
    print "4. tissue"
    print "5. cell_type"
    print "6. publication"
    
    table = raw_input()

    try:
        if table == "1":
            print "Inserting protein_info table \n"
            print "Enter the following values seperated by a comma : (if there is no data for a field, enter a null) "
            print "Protein name, Gene name, Resource database, Swissprot ID, Refseq ID, entrezgene ID, ensemblgene ID, ensemblprotein ID, organism, OMIM ID"
            protein = raw_input()
            proteinArr = protein.split(",")
            prot_name = proteinArr[0]
            gene_name = proteinArr[1]
            resource_db = proteinArr[2]
            swissprot_id = proteinArr[3]
            refseq_id = proteinArr[4]
            entrez = proteinArr[5]
            ensemblgene = proteinArr[6]
            ensemblprot = proteinArr[7]
            organism = proteinArr[8]
            omim = proteinArr[9]
            cursor.execute("""INSERT INTO protein_info(jepsld_id, gene_name, swissprot_ID, ensemblgene_ID, ensemblprotein_ID, resource_database, organism, refseq_ID, protein_name, omim_ID, entrezgene_ID) \
                         VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", ('',gene_name,swissprot_id,ensmblgene,ensemblprot,resource_db,organism,refseq_id,prot_name,omim,entrez))
    
    
        if table == "2":
            print "Inserting location table data \n"
            print "Enter the following values seperated by a comma : (if there is no data for a field, enter a null) "
            print "Main Location (if more than 1, seperated by a ;), Other location, Gene name, Ensemble Protein ID, Resource Database"
            location = raw_input()
            locationArr = location.split(",")
            main_location = locationArr[0]
            other_location = locationArr[1]
            gene_name = locationArr[2]
            ensemblprotein_ID = locationArr[3]
            resource_database = locationArr[4]
            cursor.execute("""INSERT into location(location_ID,main_location,other_location,gene_name,resource_database,ensemblprotein_ID) VALUES(%s,%s,%s,%s,%s) \
              """,('',main_location,other_location,gene_name,resource_database,ensemblprotein_ID))
    
    
        if table == "3":
            print "Inserting in the cell_line table \n"
            print "Enter the following values seperated by a comma : (if there is no data for a field, enter a null) "
            print "Cell Line, Cell Line location, Gene name, Ensemble Protein ID, Resource Database"
            cellLine = raw_input()
            cellLineArr = cellLine.split(",")
            cell_line = cellLineArr[0]
            cell_line_loc = cellLineArr[1]
            gene_name = cellLineArr[2]
            ensemblprotein_id = cellLineArr[3]
            resource_db = cellLineArr[4]
            cursor.execute("""INSERT INTO cell_line(cell_line_ID, cell_line, cell_line_location, gene_name, resource_database, ensemblprotein_ID) VALUES (%s,%s,%s,%s,%s,%s)""", ('',cell_line,cell_line_loc,gene_name,resource_db,ensemblprotein_id))
    
    
        if table == "4":
            print "Inserting in tissue table \n"
            print "Enter the following values seperated by a comma : (if there is no data for a field, enter a null) "
            print "Tissue Name, Gene name, Ensemble Protein ID, Resource Database"
            tissue = raw_input()
            tissueArr = tissue.split(",")
            tissue_name = tissueArr[0]
            gene_name = tissueArr[1]
            ensemblprotein_id = tissueArr[2]
            resource_db = tissueArr[3]
            cursor.execute("""INSERT INTO tissue(tissue_ID, tissue_name, gene_name, resource_database, ensemblprotein_ID) VALUES (%s,%s,%s,%s,%s)""", ('',tissue_name,gene_name,resource_db,ensemblprotein_id))
    
    
        if table == "5":
            print "Inserting in cell_type table \n"
            print "Enter the following values seperated by a comma : (if there is no data for a field, enter a null) "
            print "Cell type, Cell type Location, Gene name, Ensemble Protein ID, Resource Database"
            celltype = raw_input()
            celltypeArr = celltype.split(",")
            cell_type = celltypeArr[0]
            cell_type_loc = celltypeArr[1]
            gene_name = celltypeArr[2]
            ensemblprotein_id = celltypeArr[3]
            resource_db = celltypeArr[4]
            cursor.execute("""INSERT INTO cell_type(cell_type_ID, cell_type, gene_name, resource_database, ensemblprotein_ID) VALUES (%s,%s,%s,%s,%s)""", ('',cell_type,cell_type_loc,resource_db,ensemblprotein_id))
    
    
        if table == "6":
            print "Inserting in publication table \n"
            print "Enter the following values seperated by a comma : (if there is no data for a field, enter a null) "
            print "PubMed Ids (seperated by ;), Gene name, Ensemble Protein ID, Resource Database"
            pubmed = raw_input()
            pubmedArr = pubmed.split(",")
            pubmedid = pubmedArr[0]
            gene_name = pubmedArr[1]
            ensemblprotein_id = pubmedArr[2]
            resource_db = pubmedArr[3]
            cursor.execute("""INSERT INTO publication(publication_ID, gene_name, pubmed_ID, resource_database, ensemblprotein_ID) VALUES (%s,%s,%s,%s,%s)""", ('',gene_name,pubmedid,resource_db,ensemblprotein_id))
        mydb.commit()
    except:
        print "Some error in inserting data \n"
        mydb.rollback()

def adminDeleteFunction():
    print "Inside delete function of Admin \n"
    print "Enter the fild you wish to delete : "
    print "1. Gene Name"
    print "2. Protein Name"
    print "3. Swiss Prot ID"
    print "4. Ref Sequence ID"
    print "5. Entrez Gene ID"
    print "6. Ensemble Protein ID"
    print "7. Ensemble Gene ID"
    print "8. OMIM ID"
    print "9. Location"
    print "10. Organism"
    print "11. Tissue Name"
    print "12. Cell Line"
    print "13. Cell Line Location"
    print "14. Resource Database"
    print "15. Cell type"
    
    option = raw_input()
    try:
        if option == "1":
            print "Enter the gene name"
            name = raw_input()
        elif option == "2":
            print "Deleting Protein name"
            print "Enter the protein name"
            name = raw_input()
            cursor.execute("""DELETE FROM protein_info WHERE protein_name=%s""",(name))
        elif option == "3":
            print "Enter the uniprot / swissprot ID "
            uniprot = raw_input()
            cursor.execute("""DELETE FROM protein_info WHERE swissprot_ID=%s""",(uniprot))
        elif option == "4":
            print "Enter the Ref Seq ID"
            refseq = raw_input()
            cursor.execute("""DELETE FROM protein_info WHERE refseq_ID=%s""",(refseq))
        elif option == "5":
            print "Enter the entrez gene ID"
            entrez = raw_input()
            cursor.execute("""DELETE FROM protein_info WHERE entrezgene_ID=%s""",(entrez))
        elif option == "6":
            print "Enter the Ensembl Protein ID"
            ensprot = raw_input()
            #cursor.execute("""DELETE FROM protein_info WHERE ensemblprotein_ID=%s""",(ensprot))
        elif option == "7":
            print "Enter the Ensembl Gene ID"
            ensgene = raw_input()
            cursor.execute("""DELETE FROM protein_info WHERE ensemblgene_ID=%s""",(ensgene))
        elif option == "8":
            print "Enter the OMIM ID"
            omim = raw_input()
            cursor.execute("""DELETE FROM protein_info WHERE omim_ID=%s""",(omim))
        elif option == "9":
            print "Enter the Location"
            location = raw_input()
            #cursor.execute("""DELETE FROM protein_info WHERE omim_ID=%s""",(omim))
        elif option == "10":
            print "Enter the Organism name"
            organism = raw_input()
            cursor.execute("""DELETE FROM protein_info WHERE organism=%s""",(organism))
        elif option == "11":
            print "Enter the Tissue name"
            tissue = raw_input()
            cursor.execute("""DELETE FROM tissue WHERE tissue_name=%s""",(tissue))
        elif option == "12":
            print "Enter the Cell Line"
            cellLine = raw_input()
            cursor.execute("""DELETE FROM cell_line WHERE cell_line=%s""",(cellLine))
        elif option == "13":
            print "Enter the Cell Line Location"
            cellLineLoc = raw_input()
            cursor.execute("""DELETE FROM cell_line WHERE cell_line_location=%s""",(cellLineLoc))
        elif option == "14":
            print "Enter the Resource Database"
            resourcedb = raw_input()
        elif option == "15":
            print "Enter the Cell Type"
            celltype = raw_input()
            cursor.execute("""DELETE FROM cell_type WHERE cell_type=%s""",(celltype))
        else:
            print "Invalid input"
        mydb.commit()
            
    except:
        print "Error in deleting data \n"
        mydb.rollback()

def adminUpdateFunction():
    print "Inside update function of Admin \n"
    

#####main functions######

print "Enter U for user and A for admin \n"
role = raw_input()
if role == "U":
    print "Welcome user \n"
    userFunction()
elif role == "A":
    print "Welcome Admin \n"
    adminFunction()
else:
    print "Invalid input \n"
