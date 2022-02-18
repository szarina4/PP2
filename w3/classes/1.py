from pdb import line_prefix


class Upper():
    def get_string(self):
        self.line=input()
    def printString(self):
        print(self.line.upper())


a=Upper()
a.get_string()
a.printString()