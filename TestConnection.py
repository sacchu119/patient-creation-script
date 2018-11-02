import cx_Oracle
try:
    con = cx_Oracle.connect('') '''username/password@domain_name:port_number/instance_name'''
    print "There Connection Success!"
except Exception as e:
    print(e)
    print "There was an error while connecting to domain!"
