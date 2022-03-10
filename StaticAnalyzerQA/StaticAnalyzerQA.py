text = open('text.txt', 'r')
Lines = text.readlines()
count = 0
for line in Lines:
    count += 1

substrings = ["int","long", "char","float","string","double"]
operators = ["+","-","*","/"]
equal = "="
for line in Lines:
    for x in range(10):
        if str(x) in line:
            for substring in substrings:
                if substring in line:
                    for operator in operators:
                        if operator in line:
                            print("Line : ",line , "Contains Magic Number")

for line in Lines:
    if equal in line:
        for x in range (10):
            if str(x) in line:
                print("Line : ",line , "Contains Magic Number")
 
for word in line.split():
        for substring in substrings:
            if word == substring :
                i=i+1
    if i > 3:
        print(line ,"has more than 3 parametars")

for line in Lines:
    for word in line.split():
        if word == "return" or word == "break" or word =="continue":
            print(line, "unreachable code")               
               
#####################
## attributes test
def GetTypeFromFunction(line, variable):
    line = line.replace("(","")
    line = line.replace(")","")
    line = line.replace(","," ")
    line = line.split()
    return line[(line.index(variable))-1]
    

def GetTypeFromDefenion(lines, variable):
    DefLine = ""
    for line in lines:
        if line.__contains__(variable+"=") or line.__contains__(variable+" ="):
            DefLine = line
            break
    # print(variable+"=")        
    DefLine = DefLine.replace(","," ")
    DefLine = DefLine.split()
    # print (DefLine)
    return DefLine[DefLine.index(variable)-1]

def GetVarAndTypes (FunLine):
    variables = []
    types = []
    FunLine = FunLine[FunLine.find("("):FunLine.find(")")]
    FunLine = FunLine.replace("( ","")
    FunLine = FunLine.replace(" )","")
    FunLine = FunLine.replace("(","")
    FunLine = FunLine.replace(")","")
    FunLine = FunLine.replace(", ",",")
    FunLine = FunLine.replace(" ,",",")
    FunLine = FunLine.split(",")
    # print(FunLine)
    switch = 0
    for section in FunLine:
        section = section.split(" ")
        for word in section:
            if switch == 0:
                variables.append(word)
                switch = 1
            else:
                types.append(word)
                switch = 0
    return variables , types


def Attributes (lines):
    defType=[]
    dataTypes = ['int', 'void', 'bool', 'double', 'float', 'long']
    variables = []
    funTypes = []
    for line in lines:
        for type in dataTypes:
            if type in line and '{' in line and '(' in line and ';' not in line:
                funTypes, variables = GetVarAndTypes(line)
    
    
    for variable in variables:
        defType.append(GetTypeFromDefenion(lines, variable))
    # print(variables) 
    # print (funTypes)
    # print (defType)
    for i in range(len(funTypes)):
        if defType[i] != funTypes[i]:
            print('{',variables[i],'} data type of ', defType[i], ' has called by wrong datatype ', funTypes[i])
            

Attributes(readFile())
                
