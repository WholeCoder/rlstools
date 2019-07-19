
outputString = ""

def saveCharacter(l):
    global outputString
    print("saveCharacter called = saving " + l)
    outputString += l

def saveCharacterAToStartState(l):
    global outputString
    outputString += "<" + l

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
      '<':('Error',
      error),
      '%':('B',
      nothing),
      '=':('Error',
      error),
      '>':('Error',
      error),
      'Space':('StartState',
      error),
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
      saveCharacter),
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
      saveCharacter),
      '<':('Error',
      error),
      '%':('F',
      nothing),
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
      nothing),
      '=':('Error',
      error),
      '>':('Error',
      error),
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
      saveCharacter)
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
      nothing),
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
      saveCharacter),
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
      saveCharacter),
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
        print("ch == "+convert(c))
        print("State == " + state)
        stateTuple = stateDict[state][convert(c)]
        print("stateTuple == " + str(stateTuple))
        stateTuple[1](c)
        state = stateTuple[0]
        if not c:
            print ("End of file")
            break
        print ("Read a character:", c)

print("outputString == "+outputString)

