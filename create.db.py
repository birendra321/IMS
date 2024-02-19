import sqlite3
def Create_db():
    con=sqlite3.connect(database=r'ims.db')
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS employee(eid INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,contact  text,dob text,doj text,pass text,utype text,address text,salary text)")
    con.commit()
    

    cur.execute("CREATE TABLE IF NOT EXISTS supplier(invoice INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, contect TEXT, desc TEXT)")  # Corrected "contect" to "contact"
    con.commit()

    # try:
    #     # Rename the 'contect' column to 'contact' in the 'supplier' table
    #     cur.execute("PRAGMA foreign_keys=off")  # Disable foreign key constraints temporarily
    #     cur.execute("BEGIN TRANSACTION")
    #     cur.execute("ALTER TABLE supplier RENAME COLUMN contect TO contact")
    #     con.commit()
    #     cur.execute("PRAGMA foreign_keys=on")  # Re-enable foreign key constraints
    # except Exception as e:
    #     con.rollback()
    #     raise e
    

    cur.execute("CREATE TABLE IF NOT EXISTS category(cid INTEGER PRIMARY KEY AUTOINCREMENT, name text)")  # Corrected "contect" to "contact"
    con.commit()

                                                        # ("pid","Category","Supplier","name","price","qty","status")
    cur.execute("CREATE TABLE IF NOT EXISTS product(pid INTEGER PRIMARY KEY AUTOINCREMENT,Category text,Supplier text,name text,price  text,qty text,status text)")
    con.commit()


    


   
    
Create_db()
