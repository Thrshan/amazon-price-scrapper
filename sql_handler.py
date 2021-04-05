import sqlite3

def insert_data_db(db_file, table_name, data):    
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    # # Create table
    cur.execute('''CREATE TABLE IF NOT EXISTS {}
                (date text, timestamp real, price real)'''.format(table_name))

    # Insert a row of data
    cur.execute("INSERT INTO {} VALUES (?,?,?)".format(table_name), (data['date'], data['ts'],data['price']))

    # # Save (commit) the changes
    con.commit()

    # # We can also close the connection if we are done with it.
    # # Just be sure any changes have been committed or they will be lost.
    con.close()