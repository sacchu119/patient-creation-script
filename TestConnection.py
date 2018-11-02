import cx_Oracle
try:
    con = cx_Oracle.connect('v500/v500@ipaca1.ip.devcerner.net:1521/cmtcrt.world')
    print "There Connection Success!"
except:
    print "There was an error while connecting to domain!"
