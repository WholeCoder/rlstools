# flake8: noqa
import os
import sys
sys.path.append('.')
from router import router


class TemplateParser:
    def __init__(self, table, action):

        self.outputString = ""
        self.forLoopIndent = 0
        with open(os.getcwd()+"/controllers/"+table+".py", "r") as controller_file_handle:
            file_contents = controller_file_handle.readlines()

        for line in file_contents:
            self.outputString += line

        self.outputString += table+"Controller."+action+"()\n"

        self.outputString += "currString = ''\n\n"
        self.accString = ""
        
        def decrementForLoopIndent(l):
            self.forLoopIndent -= 1

        def saveCharacter(l):
            print("saveCharacter called = saving " + l)
            if l == "\n": # noqa
                self.accString = replaceWithQuotesIfNotForLoopHeader(self.accString)
                self.accString = (self.forLoopIndent*"    ")+"currString += '"+self.accString+"'\n"
                self.outputString += self.accString
                self.accString = ""
            else:
                self.accString += l

        def saveAccAndAppendController(l):
            self.accString = replaceWithQuotesIfNotForLoopHeader(self.accString)
            self.accString = (self.forLoopIndent*"    ")+"currString += "+self.accString+"\n"
            self.outputString += self.accString
            self.accString = ''

        def saveCharacterAToStartState(l):
            self.accString += "<" + l

        def saveCharacterIndented(l):
            self.outputString += (self.forLoopIndent*"    ")+"currString += '"+self.accString+"'\n"
            self.accString = ""

        def saveAccWithIndent(l):
            self.accString = replaceWithQuotesIfNotForLoopHeader(self.accString)
            self.outputString += (self.forLoopIndent*"    ")+"currString += "+self.accString+"\n"
            self.accString = ""

        def sendToGAndAddGreaterThanSign(l):
            self.accString += l+">"

        def saveCharacterAToEnd(l):
            self.accString += l + ">"

        def replaceWithQuotesIfNotForLoopHeader(accString):
            if not "for" in accString:
                return accString.replace("'","&apos;")
            return accString

        def saveAccString(l):
            self.accString = replaceWithQuotesIfNotForLoopHeader(self.accString)
 
            self.outputString +=(self.forLoopIndent*"    ")+ "currString += '"+self.accString+"'\n"
            self.accString = ""

        def saveCharacterForloopheader(l):
            if l == 'f': # noqa
                self.accString = l
            elif l == '%': # noqai
                self.forLoopIndent += 1
                self.accString = (self.forLoopIndent-1)*"    " + self.accString
                self.accString += '\n'
                
                self.accString = self.accString.replace("rows", table+"Controller.rows")# noqa

                self.accString = replaceWithQuotesIfNotForLoopHeader(self.accString)
                self.outputString += self.accString
                self.accString = ""
            else:
                self.accString += l
            print("saveCharacterForloopheader called")

        def nothing(l):
            print("nothing(l) called ----------------->")
            pass

        def error(l):
            raise Exception

        stateDict = {
           'StartState':{
              '':('StartState',
              saveCharacter),
              '*':('StartState',
              saveCharacter),
              '<':('A',
              nothing),
              '%':('StartState',
              saveCharacter),
              '=':('StartState',
              saveCharacter),
              '>':('StartState',
              saveCharacter),
              'Space':('StartState',
              saveCharacter),
              'f':('StartState',
              saveCharacter),
              'e':('StartState',
              saveCharacter)
           },
           'A':{
              '':('A',
              nothing),
              '*':('StartState',
              saveCharacterAToStartState),
              '<':('StartState',
              saveCharacterAToStartState),
              '%':('B',
              saveAccString),
              '=':('Error',
              error),
              '>':('StartState',
              saveCharacterAToEnd),
              'Space':('StartState',
              saveCharacterAToStartState),
              'f':('StartState',
              saveCharacterAToStartState),
              'e':('StartState',
              saveCharacterAToStartState)
           },
           'B':{
              '':('B',
              nothing),
              '*':('Error',
              error),
              '<':('Error',
              error),
              '%':('Error',
              error),
              '=':('C',
              nothing),
              '>':('Error',
              error),
              'Space':('B',
              nothing),
              'f':('E',
              saveCharacterForloopheader),
              'e':('L',
              decrementForLoopIndent)
           },
           'C':{
              '':('C',
              nothing),
              '*':('C',
              saveCharacter),
              '<':('C',
              saveCharacter),
              '%':('D',
              saveAccAndAppendController),
              '=':('C',
              nothing),
              '>':('C',
              nothing),
              'Space':('C',
              saveCharacter),
              'f':('C',
              saveCharacter),
              'e':('C',
              saveCharacter)
           },
           'D':{
              '':('D',
              error),
              '*':('Error',
              error),
              '<':('Error',
              error),
              '%':('Error',
              error),
              '=':('Error',
              error),
              '>':('StartState',
              nothing),
              'Space':('Error',
              error),
              'f':('Error',
              error),
              'e':('Error',
              error)
           },
           'E':{
              '':('E',
              nothing),
              '*':('E',
              saveCharacterForloopheader),
              '<':('Error',
              error),
              '%':('F',
              saveCharacterForloopheader),
              '=':('F',
              saveCharacter),
              '>':('E',
              saveCharacter),
              'Space':('E',
              saveCharacter),
              'f':('E',
              saveCharacter),
              'e':('E',
              saveCharacterForloopheader)
           },
           'F':{
              '':('F',
              nothing),
              '*':('Error',
              error),
              '<':('Error',
              error),
              '%':('Error',
              error),
              '=':('Error',
              error),
              '>':('G',
              nothing),
              'Space':('Error',
              error),
              'f':('Error',
              error),
              'e':('Error',
              error)
           },
           'G':{
              '':('G',
              nothing),
              '*':('G',
              saveCharacter),
              '<':('H',
              nothing),
              '%':('G',
              saveCharacter),
              '=':('G',
              saveCharacter),
              '>':('G',
              saveCharacter),
              'Space':('G',
              saveCharacter),
              'f':('G',
              saveCharacter),
              'e':('G',
              saveCharacter)
           },
           'H':{
              '':('H',
              nothing),
              '*':('G',
              saveCharacterAToStartState),
              '<':('Error',
              error),
              '%':('I',
              saveCharacterIndented),
              '=':('Error',
              error),
              '>':('G',
              sendToGAndAddGreaterThanSign),
              'Space':('Error',
              error),
              'f':('Error',
              error),
              'e':('Error',
              error)
           },
           'I':{
              '':('I',
              nothing),
              '*':('Error',
              error),
              '<':('Error',
              error),
              '%':('Error', #mistake in CSV
              error),
              '=':('J',
              nothing),
              '>':('Error',
              error),
              'Space':('I',
              saveCharacter),
              'f':('E',
              saveCharacterForloopheader),
              'e':('L',
              decrementForLoopIndent)
           },
           'J':{
              '':('J',
              nothing),
              '*':('J',
              saveCharacter),
              '<':('J',
              saveCharacter),
              '%':('K',
              nothing),
              '=':('Error',
              error),
              '>':('J',
              saveCharacter),
              'Space':('J',
              saveCharacter),
              'f':('J',
              saveCharacter),
              'e':('J',
              saveCharacter)
           },
           'K':{
              '':('K',
              nothing),
              '*':('Error',
              error),
              '<':('Error',
              error),
              '%':('Error',
              error),
              '=':('Error',
              error),
              '>':('G',
              saveAccWithIndent),
              'Space':('Error',
              error),
              'f':('Error',
              error),
              'e':('Error',
              error)
           },
           'L':{
              '':('L',
              nothing),
              '*':('L',
              nothing),
              '<':('L',
              saveCharacter),
              '%':('M',
              nothing),
              '=':('L',
              saveCharacter),
              '>':('L',
              saveCharacter),
              'Space':('L',
              saveCharacter),
              'f':('L',
              nothing),
              'e':('L',
              saveCharacter)
           },
           'M':{
              '':('M',
              nothing),
              '*':('Error',
              error),
              '<':('Error',
              error),
              '%':('Error',
              error),
              '=':('Error',
              error),
              '>':('StartState',
              nothing),
              'Space':('Error',
              error),
              'f':('Error',
              error),
              'e':('Error',
              error)
           }
        }

        def convert(letter):
            if letter == " ":
                return 'Space'
            if letter == 'e' or letter == 'f' or letter == '<' or letter == '=' or letter == '%' or letter == '>' or letter == '': # noqa
                return letter
            return '*'

        #testString = ""

        print(convert(" "))
        state = 'StartState'
        with open(os.getcwd()+"/views/"+router[table][action]) as f:
            while True:
                c = f.read(1)
                #testString += c
                #print("testString == "+testString)
                print("ch == "+convert(c) + "   ("+c+")")
                print("State == " + state)
                stateTuple = stateDict[state][convert(c)]

                print("stateTuple == " + str(stateTuple))
                stateTuple[1](c)
                print("self.accString in main while== "+self.accString)

                state = stateTuple[0]
                if not c:
                    print("End of file")
                    break
                print("Read a character:", c)

        saveAccString("doesn't matter")

        with open("template_output.py", "w") as file_handle:
            file_handle.write(self.outputString)


