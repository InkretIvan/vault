import psycopg2

DB_HOST="localhost"
DB_USER="postgres"
DB_PASS="admin"
DB1_NAME="node1"
DB2_NAME="node2"
DB3_NAME="node3"
DB4_NAME="node4"
DB5_NAME="node5"

conn1=psycopg2.connect(dbname=DB1_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
conn2=psycopg2.connect(dbname=DB2_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
conn3=psycopg2.connect(dbname=DB3_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
conn4=psycopg2.connect(dbname=DB4_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
conn5=psycopg2.connect(dbname=DB5_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

cur1=conn1.cursor()
cur2=conn2.cursor()
cur3=conn3.cursor()
cur4=conn4.cursor()
cur5=conn5.cursor()



conn1.commit()
conn2.commit()
conn3.commit()
conn4.commit()
conn5.commit()

def initTheDB():
    print("bok")

def closeTheDB():
    cur1.close()
    cur2.close()
    cur3.close()
    cur4.close()
    cur5.close()

    conn1.close()
    conn2.close()
    conn3.close()
    conn4.close()
    conn5.close()

def checkNodesStatus():
    try:
        cur1.execute("select * from keyfragment")
        print("1 ok")
    except:
        print("1 dcd")

    try:
        cur2.execute("select * from keyfragment")
        print("2 ok")
    except:
        print("2 dcd")

    try:
        cur3.execute("select * from keyfragment")
        print("3 ok")
    except:
        print("3 dcd")

    try:
        cur4.execute("select * from keyfragment")
        print("4 ok")
    except:
        print("4 dcd")

    try:
        cur5.execute("select * from keyfragment")
        print("5 ok")
    except:
        print("5 dcd")

closeTheDB()