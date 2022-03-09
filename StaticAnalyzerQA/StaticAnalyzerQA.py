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
         for operator in operators:
                  if operator in line and str(x) in line:
                                print("Line : ",line , "Contains equal")

