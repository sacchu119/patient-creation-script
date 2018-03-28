import sys
import os
from csvReader import csvReader
from dataFetcher import dataFetcher
from dataInserter import dataInserter

###########################################################
#main function/ starting point
###########################################################
def main(argv):
    while True:
        csvFile = raw_input('Please enter the CSV filename with .csv extension\n')
        if(not os.path.exists(csvFile)):
            print 'File not found, Please Enter a valid file name again'
            continue
        else:
            if (csvFile.split(".")[1] != "csv"):
                print 'Not a valid file, Please enter a valid CSV file'
                continue
            else:
                break
    csvReaderObject = csvReader() 
    csvData = csvReaderObject.readCsvData(csvFile)
    dataInsert = dataInserter()
    dataFetch = dataFetcher()  
    for i in range(len(csvData)):
        print '###########################################################################################################'
        print 'Inserting data for patient ' + csvData[i]['lastname'] + ', ' + csvData[i]['firstname']
        print '###########################################################################################################'
        if(dataFetch.checkIfPersonExist(csvData[i]['firstname'],csvData[i]['lastname']) == 0):
            dataInsert.insertPerson(csvData[i])
            dataInsert.insertEncounter(csvData[i])
        else:
            print('Patient already exists, Inserting only encounters')
            dataInsert.insertEncounter(csvData[i])
        print '###########################################################################################################'
#calling main function
if __name__ == '__main__':
    main(sys.argv)


        
