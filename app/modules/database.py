import psycopg2
import psycopg2.extras

DB_HOST="localhost"
DB_USER="postgres"
DB_PASS="admin"
DB1_NAME="node1"
DB2_NAME="node2"
DB3_NAME="node3"
DB4_NAME="node4"
DB5_NAME="node5"


class db():

    def __init__(self):

        self.status=[1,1,1,1,1]

        print("DB initiated")
        self.conn1=psycopg2.connect(dbname=DB1_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        self.conn2=psycopg2.connect(dbname=DB2_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        self.conn3=psycopg2.connect(dbname=DB3_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        self.conn4=psycopg2.connect(dbname=DB4_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)
        self.conn5=psycopg2.connect(dbname=DB5_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST)

        print("db conncted")

        self.cur1=self.conn1.cursor(cursor_factory=psycopg2.extras.DictCursor)
        self.cur2=self.conn2.cursor(cursor_factory=psycopg2.extras.DictCursor)
        self.cur3=self.conn3.cursor(cursor_factory=psycopg2.extras.DictCursor)
        self.cur4=self.conn4.cursor(cursor_factory=psycopg2.extras.DictCursor)
        self.cur5=self.conn5.cursor(cursor_factory=psycopg2.extras.DictCursor)

    def closeTheDB(self):
        self.cur1.close()
        self.cur2.close()
        self.cur3.close()
        self.cur4.close()
        self.cur5.close()

        self.conn1.close()
        self.conn2.close()
        self.conn3.close()
        self.conn4.close()
        self.conn5.close()

    def retrieveKeyById(self,id):
        counter=0
        ss=[]
        try:
            self.cur1.execute("select * from keyfragment where id=%s",(id,))
            ss.append(self.cur1.fetchone()['fragment'])
            counter=counter+1
        except:
            print("node 1 offline")

        try:
            self.cur2.execute("select * from keyfragment where id=%s",(id,))
            ss.append(self.cur2.fetchone()['fragment'])
            counter=counter+1
        except:
            print("node 2 offline")

        try:
            self.cur3.execute("select * from keyfragment where id=%s",(id,))
            ss.append(self.cur3.fetchone()['fragment'])
            counter=counter+1
        except:
            print("node 3 offline")

        try:
            self.cur4.execute("select * from keyfragment where id=%s",(id,))
            ss.append(self.cur4.fetchone()['fragment'])
            counter=counter+1
        except:
            print("node 4 offline")

        try:
            self.cur5.execute("select * from keyfragment where id=%s",(id,))
            ss.append(self.cur5.fetchone()['fragment'])
            counter=counter+1
        except:
            print("node 5 offline")
        if counter < 3:
            return 0
        return ss

    def purgeDB(self):
        self.cur1.execute("delete from keyfragment")
        self.cur2.execute("delete from keyfragment")
        self.cur3.execute("delete from keyfragment")
        self.cur4.execute("delete from keyfragment")
        self.cur5.execute("delete from keyfragment")

        self.conn1.commit()
        self.conn2.commit()
        self.conn3.commit()
        self.conn4.commit()
        self.conn5.commit()

    def checkNodesStatus(self):
        counter=0
        try:
            self.cur1.execute("select * from keyfragment")
            print("node 1 online")
            counter=counter+1
        except:
            print("node 1 offline")

        try:
            self.cur2.execute("select * from keyfragment")
            print("node 2 online")
            counter=counter+1
        except:
            print("node 2 offline")

        try:
            self.cur3.execute("select * from keyfragment")
            print("node 3 online")
            counter=counter+1
        except:
            print("node 3 offline")

        try:
            self.cur4.execute("select * from keyfragment")
            print("node 4 online")
            counter=counter+1
        except:
            print("node 4 offline")

        try:
            self.cur5.execute("select * from keyfragment")
            print("node 5 online")
            counter=counter+1
        except:
            print("node 5 offline")
        return counter

    def saveFragments(self,fragmentId,fragments):
        if self.checkNodesStatus()!=5:
            print("not all nodes are active, can't save shares")
            return 0
        #print(fragmentId)
        #print(fragments)
        self.cur1.execute("insert into keyfragment (id, fragment) values (%s,%s)",(fragmentId,fragments[0]))
        self.cur2.execute("insert into keyfragment (id, fragment) values (%s,%s)",(fragmentId,fragments[1]))
        self.cur3.execute("insert into keyfragment (id, fragment) values (%s,%s)",(fragmentId,fragments[2]))
        self.cur4.execute("insert into keyfragment (id, fragment) values (%s,%s)",(fragmentId,fragments[3]))
        self.cur5.execute("insert into keyfragment (id, fragment) values (%s,%s)",(fragmentId,fragments[4]))

        self.conn1.commit()
        self.conn2.commit()
        self.conn3.commit()
        self.conn4.commit()
        self.conn5.commit()
        return 1
    

