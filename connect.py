import cx_Oracle
class connect:
    def getConnection(self):
        try:
            connection = cx_Oracle.connect('')
            #print "Connected to domain successfully"
            return connection
        except:
            print "There was an error while connecting to domain!"
        #cur.execute('select * from prsnl p  where p.name_full_formatted = \'Boregowda , Sachin\'')
    def disconnect(self,connection,cursor):
        cursor.close()
        connection.close()
            #print "Connection to database was successfully closed!"
        
        
