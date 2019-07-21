global accString
global outputString

outputString = ""
accString = ""


def saveCharacter(l):
    global outputString
    global accString
    print("saveCharacter called = saving " + l)
    if l == "\n":
        accString = "print('"+accString+"')\n"
        outputString += accString
        accString = ""
    else:
        accString += l

def saveCharacterAToStartState(l):
    global outputString
    global accString
    accString += "<" + l
    print("saving to acc string----------------------- inf function accString == "+accString)

def saveCharacterIndented(l):
    global outputString
    global accString
    #accString += l
    outputString += "   print(\""+accString+"\")\n"
    accString = ""

def saveAccWithIndent(l):
    global outputString
    global accString
    outputString += "   print("+accString+")\n"
    accString = ""

def sendToGAndAddGreaterThanSign(l):
    global outputString
    global accString
    accString += l+">"

def saveCharacterAToEnd(l):
    accString += l + ">"

def saveAccString(l):
    global outputString
    global accString

    outputString += "print('"+accString+"')\n"
    accString = ""

def saveCharacterForloopheader(l):
    global accString
    global outputString
    if l == 'f':
        accString = l
    elif l == '%':
        accString += '\n'
        outputString += accString
        accString = ""
    else:
        accString += l
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
      'f':('Error',
      error),
      'e':('Error',
      error)
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
      'e':('Error',
      error)
   },
   'C':{
      '':('C',
      nothing),
      '*':('C',
      saveCharacter),
      '<':('C',
      saveCharacter),
      '%':('D',
      nothing),
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
      'e':('F',
      saveCharacter)
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
      'f':('Error',
      error),
      'e':('L',
      nothing)
   },
   'J':{
      '':('J',
      nothing),
      '*':('J',
      saveCharacter),
      '<':('Error',
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
    if letter == 'e' or letter == 'f' or letter == '<' or letter == '=' or letter == '%' or letter == '>' or letter == '':
        return letter
    return '*'

testString = ""

print(convert(" "))
state = 'StartState'
with open('Office.pyht') as f:
    while True:
        c = f.read(1)
        testString += c
        print("testString == "+testString)
        print("ch == "+convert(c) + "   ("+c+")")
        print("State == " + state)
        stateTuple = stateDict[state][convert(c)]

        print("stateTuple == " + str(stateTuple))
        stateTuple[1](c)
        print("accString in main while== "+accString)

        state = stateTuple[0]
        if not c:
            print ("End of file")
            break
        print ("Read a character:", c)

print("outputString == "+outputString)

