
def createQueries(in_name, out_name, table):
  with open(out_name, 'a') as file_out:
    file_out.write(f"print('Start inserting data into {table} table<br />')\n")

    with open(f'Raw Data/{in_name}.csv') as file_in:
      header = file_in.readline()
      field_names = header.strip().split(',')
      records = []
      for line in file_in.readlines():
        record = line.strip().split(',')
        records.append(record)
      for record in records:
        if record[0] != "":
          line = f"cursor.execute('''INSERT INTO {table} ("
          for name in field_names:
            line += f'{name}, '
          line = f"{line[:-2]}) VALUES ("
          for field in record:
            if field.isdigit():
              line += f"{field.strip()}, "
            else:
              line += f'"{field.strip()}", '
            out_line = f"{line[:-2]})''')\n" 
          file_out.write(out_line)
    file_out.write(f"print('Finish inserting data into {table} table<br />')\n")

def setupCGI(dbName, out_file):
  with open(out_file, 'w') as f_out:
    script = '''#!/usr/bin/python
print('Content-type: text/html\\n\\n')

import cgi
import cgitb; cgitb.enable()
import sqlite3\n\n'''
    script += f"database_name = '{dbName}'\n"
    script += '''conn = sqlite3.connect(database_name)
cursor = conn.cursor()\n\n'''
    f_out.write(script)
  

def closeCGI(out_file):
    with open(out_file, "a") as f_out:
        script = 'conn.commit()\ncursor.close()'
        f_out.write(script)


in_files = ["CurrentDoc", "Employee", "Job", "MainOffice", "PastDoc", "Team"]
tables = ["CurrentDoc", "Employee", "Job", "MainOffice", "PastDoc", "Team"]

database = "Leader_Cabling_DB.db"

out_file = "insert_data.py"

setupCGI(database, out_file)
for i in range(len(in_files)):
    createQueries(in_files[i], out_file, tables[i])
    closeCGI(out_file)
