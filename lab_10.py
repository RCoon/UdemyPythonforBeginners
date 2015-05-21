class LogMessage():
    
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

file = LogMessage('new.txt')

file.write('Testing..' + '\n')
file.write('test..1..2..3' + '\n')
file.read()  