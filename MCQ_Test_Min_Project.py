import mysql.connector
import time
import sys

count = 0
myDB = mysql.connector.connect(host="localhost", user="root", passwd="", database="online_exam")
myCursor = myDB.cursor()

user = input("Enter uname: ")
password = input("Enter password:")





try:
    myCursor.execute("select * from login where user_id={} and password='{}' ".format(user, password))
except Exception as a:
    print(a)
result = myCursor.fetchone()
print(type(result))

if result == None:
    print ("Wrong Credentials....Kindly login again\n")
    sys.exit()
else:
    print ("===================================")
    print ("Welcome", result[0])

def testPython(tName):
    myCursor.execute("select * from questions where technology = '"+tName+"'")
    result = myCursor.fetchall()
    print("=========="+tName+"'s Test===========")
    qno = 1
    for i in result:
        
        print ("===================================")
        print ("Question ",qno,": ",i[1],"\n")
        print (i[2],"\t",i[3],"\t",i[4],"\t",i[5],"\n")
        print ("===================================")
        ans = input("Enter your ans: ")
        if ans==i[6]:
            #print "Correct Answer"
            global count
            count = count + 1
        qno += 1
    print ("===================================")
    myCursor.execute("select count(*) from questions where technology = '"+tName+"'")
    result = myCursor.fetchone()
    print ("You scored: (",count,"/",result[0],")")
    percentage = (float(count)/float(result[0]))*100
    print ("Your Percentile Score is: ", percentage, "%")
    

choice = int(input("Choose technology to start test: \n 1. Python\n 2. C\n"))

if choice == 1:
    print ("Python test starting in 5 seconds...")
    time.sleep(5)
    testPython('Python')
if choice == 2:
    print ("C test starting in 5 seconds...")
    time.sleep(5)
    testPython('C')






