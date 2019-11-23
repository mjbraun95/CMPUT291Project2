from bsddb3 import db
import re
import os
database = db.DB() #handle for Berkeley DB database
DB_File = "miniproject2.db"
database.open(DB_File, None, db.DB_BTREE, db.DB_CREATE)
curs = database.cursor()

def b_terms():
    os.chdir("C:\\Users\\Ishara\\OneDrive\\University of Alberta\\2019\\YEAR 2\\CMPUT 291\\mini project 2")
    os.system('sort -u terms.txt > output.txt')
    with open('output.txt', 'r') as termfile:
        for line in termfile:
            line = line.strip()
            print(line)
            line = re.split("[-:]+", line)
            #print(line)
            key = line[1]
            #print(key)
            data = line[2]
            #print(data)
            #database.put(b'%s' % (key), data)
            file = open("tempterms.txt", "a")
            file.write('%s\n%s\n' % (key, data))
            file.close()

    os.chdir("C:\\Users\\Ishara\\OneDrive\\University of Alberta\\2019\\YEAR 2\\CMPUT 291\\mini project 2")
    os.system('db_load -f tempterms.txt -T -t btree miniproject2.db')
    #os.remove("tempterms.txt")
    #os.remove("output.txt")
    os.system('db_dump -p -f te.idx miniproject2.db')

    for key in database.keys():
        print('{}: {}'.format(key, database[key]))

    result = database.get(b'category')
    print(result)

    curs.close()
    database.close()

b_terms()