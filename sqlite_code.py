import sqlite3

class Masterdb:
    def __init__(self,db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()
    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS master(id INTEGER PRIMARY KEY,name VARCHAR(500),num_master VARCHAR(50));")
        self.connection.commit()
    def insert_db(self,name,num_master):
        try:
            self.cursor.execute("INSERT INTO master VALUES(NULL,?,?)",(name,num_master))
            self.connection.commit()
            return True
        except:
            return False
    def select_db(self,num_master):
        self.cursor.execute("SELECT name , num_master FROM master WHERE num_master=?",(num_master,))
        result = self.cursor.fetchone() 
        self.connection.commit()
        return result
    def close(self):
        self.connection.close()
class Teacherdb:
    def __init__(self,db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()
    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS teach(id INTEGER PRIMARY KEY,name_teach VARCHAR(500),num_teach VARCHAR(50));")
        self.connection.commit()
    def insert_dbt(self,name_teach,num_teach):
        try:
            self.cursor.execute("INSERT INTO teach VALUES(NULL,?,?)",(name_teach,num_teach))
            self.connection.commit()
            return True
        except:
            return None
    def select_dbt(self,num_teach):
        self.cursor.execute("SELECT name_teach,num_teach FROM teach WHERE num_teach=?",(num_teach,))
        result = self.cursor.fetchone()
        self.connection.commit()
        return result
    def close(self):
        self.connection.close()
class Studentdb:
    def __init__(self,db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()
    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY,name_stu VARCHAR(500),num_stu INTEGER(50));")
        self.connection.commit()
    def insert_dbs(self,name_stu,num_stu):
        try:
            self.cursor.execute("INSERT INTO student VALUES(NULL,?,?)",(name_stu,num_stu))
            self.connection.commit()
            return True
        except:
            return None
    def select_dbs(self,num_stu):
        self.cursor.execute("SELECT name_stu,num_stu FROM student WHERE num_stu=?",(num_stu,))
        result = self.cursor.fetchone()
        self.connection.commit()
        return result
    def close(self):
        self.connection.close()
class reportdb:
    def __init__(self,db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_table()
    def create_table(self):
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS report(
        id INTEGER PRIMARY KEY,
        name VARCHAR(500),
        nation_code INTEGER(50),
        math INTEGER(5),
        persian INTEGER(5),
        science INTEGER(5),
        quran INTEGER(5)
        );
        """)
    def insert_dbr(self,name,nation_code,math,persian,science,quran):
        try:
            self.cursor.execute("INSERT INTO report VALUES(NULL,?,?,?,?,?,?)",(name,nation_code,math,persian,science,quran))
            self.connection.commit()
            return True
        except:
            return None
    def select_dbr(self,nation_code):
        self.cursor.execute("SELECT name,nation_code FROM report WHERE nation_code=?",(nation_code,))
        result = self.cursor.fetchone()
        self.connection.commit()
        return result
    def select_for_report(self,nation_code):
        self.cursor.execute("SELECT * FROM report WHERE nation_code=?", (nation_code,))
        result = self.cursor.fetchall()
        self.connection.commit()
        return result
    def close(self):
        self.connection.close()
