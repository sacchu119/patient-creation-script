import csv
import sys
import os
from dataFetcher import dataFetcher
#########################################################
# Reading the CSV data
#########################################################
class csvReader:
    def readCsvData(self,csvFile):
        try:
            with open(csvFile,'rb') as dataFile:
                print 'Reading data from CSV.....'
                csvDataDictionary = {}
                dataKeys = ['lastname','firstname','age','sex','encounter_type','building','pos','arrive_dt_tm','admit_EP_firstname','admit_EP_lastname','attend_EP_firstname','attend_EP_lastname','disch_dt_tm','disch_dis']
                csvDataList = []
                csvReader = csv.reader(dataFile, delimiter =',',quotechar='|')
                for row in csvReader:
                    csvDataList.append(row)
                finalList = []
                if not csvDataList:
                    print 'No data found in the CSV file'
                    sys.exit(1)
                for i in range(len(csvDataList)):
                    j=0
                    for col in csvDataList[i]:
                        csvDataDictionary[dataKeys[j]] = col
                        j = j+1
                    dataFetch = dataFetcher()
                    person_id = dataFetch.getNextPersonId()
                    csvDataDictionary['person_id'] = str(person_id)
                    finalList.append(csvDataDictionary)
                    csvDataDictionary = {}
                print 'Reading data from CSV completed'
                return finalList
        except IOError:
            print "The CSV data file not found!!"
