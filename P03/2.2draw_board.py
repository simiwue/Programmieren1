
#r: row
#c: column

for r in range(0,15):
    #create a new empty line
    line = ""

    # fill line with . or x
    for c in range(0,15):

        if c <= (r+1) and c >= (r-1):
            line += ".  "
        else:
            line += "X  "

    print(line)