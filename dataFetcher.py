import re
from connect import connect

###############################################################
# Fetching the required values from the database
###############################################################
class dataFetcher:
    def getNextPersonId(self):
        connectionObj = connect()
        connection = connectionObj.getConnection()
        cursor = connection.cursor()
        cursor.execute('select person_only_seq.NEXTVAL from dual')
        row = cursor.fetchone()
        connectionObj.disconnect(connection,cursor)
        for col in row:
            person_id = col
        return str(person_id)
    
    def getNextId(self,tableName,primaryKey):
        connectionObj = connect()
        connection = connectionObj.getConnection()
        cursor = connection.cursor()
        queryString = 'select max(' + primaryKey + ') + 1 from ' + tableName
        cursor.execute(queryString)
        row = cursor.fetchone()
        for col in row:
            nextKey = col
        connectionObj.disconnect(connection,cursor)
        return str(nextKey)
       
    def getCodeValue(self,column,codeSet,value):
        connectionObj = connect()
        connection = connectionObj.getConnection()
        cursor = connection.cursor()
        if(column == 'DISPLAY_KEY'):
            value = re.sub('[^a-zA-Z0-9 \n\.]', '', value)
        queryString = 'select code_value from code_value where ' +column + '= \'' + value + '\' and code_set = '+ (codeSet) +'order by ACTIVE_DT_TM DESC'
        cursor.execute(queryString)
        row = cursor.fetchone()
        if(cursor.rowcount > 0):
            for col in row:
                codeValue = col
            connectionObj.disconnect(connection,cursor)
            return str(codeValue)
        else:
            connectionObj.disconnect(connection,cursor)
            return str(0)
    def checkIfPersonExist(self,firstName,lastName):
        nameLastKey = re.sub('[^a-zA-Z0-9 \n\.]', '', lastName)
        nameFirstKey = re.sub('[^a-zA-Z0-9 \n\.]', '', firstName)
        connectionObj = connect()
        connection = connectionObj.getConnection()
        cursor = connection.cursor()
        queryString = 'select * from person p where p.name_first_key = upper(\'' + nameFirstKey + '\') and name_last_key = upper(\'' +nameLastKey + '\')'
        cursor.execute(queryString)
        row = cursor.fetchone()
        if(cursor.rowcount > 0):
            connectionObj.disconnect(connection,cursor)
            return 1
        else:
            connectionObj.disconnect(connection,cursor)
            return 0
