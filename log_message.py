class log_message_file():
    
    def __init__(self,filename):
        self.__filename = filename
        
    def read(self):
        file_in = open(self.__filename, 'r')
        for line in file_in:
            print(line, end='')
        file_in.close()
            
    def write(self, message):
        file_out = open(self.__filename, 'a')
        for line in message:
            file_out.write(line)
        file_out.close()

# file = log_message_file('new.txt')
# file.write('Testing..' + '\n')
# file.write('test..1..2..3' + '\n')
# file.read()  

import sqlite3

class log_message_db:
    def __init__(self,dbname):
        self.dbname = dbname
        db = sqlite3.connect(self.dbname)
        db.execute('create table if not exists log_message_db (message)')
        db.commit()
        db.close()
    def read(self):
        db = sqlite3.connect(self.dbname)
        data = db.execute('select * from log_message_db')
        for each in data:
            print(each)
        db.close()
    def write(self,message):
        db = sqlite3.connect(self.dbname)
        db.execute('insert into log_message_db (message) values (?)', (message,))
        db.commit()
        db.close()
    
# log = log_message_db('test.db')
# log.write('Testing')
# log.write('Test')
# log.read()

