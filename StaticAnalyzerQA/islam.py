for line in Lines:
    i=0
    for word in line.split():
        for substring in substrings:
            if word == substring :
                i=i+1
    if i > 3:
        print(line ,"has more than 3 parametars")
