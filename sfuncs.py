#This is just a module to whisk away function declarations. I'm weird like that
typedline = []
metastack = {"main":[]}
macrotable = {}
stackname = "main"
inttype = 0
floattype = 1
stringtype = 2
generictype = 3


#parse() divides the input up into its various atoms
#Square brackets, "[" and "]", are used for quotes. anything between them will
#be placed on the stack as a single atom without being evaluated. They can be nested.
#Parentheses, "(" and ")", are used for comments. Anything between them will be ignored. They can be nested.
#Anything else delimited by spaces will be single atoms. They will be evaluated.
#Numbers will be automatically typed to float or int as appropriate. Unquoted
#strings will be looked up to see if they are defined. If they are undefined,
#they will be placed onto the stack as strings

def parse(ptext):
    slicestart = 0
    slicestop = 0
    output = []
    i = 0
    j = 0
    depth = 0

    #step zero is to check if the input is a single charcter
    if len(ptext) == 1:
        if ptext.isdigit():
            output.append([inttype, ptext])
        else:
            output.append([generictype, ptext])
    else:
        while i < len(ptext):
            #first we check for strings
            if ptext[i] == "[":
                depth += 1
                i += 1
                slicestart = i
                while depth != 0 and i < len(ptext):
                    if ptext[i] == "[":
                        depth += 1
                    if ptext[i] == "]":
                        depth -= 1

                    i += 1
                i -= 1
                slicestop = i
                output.append([stringtype, ptext[slicestart:slicestop]])
            #next we check for comments
            if ptext[i] == "(":
                depth += 1
                i += 1
                while depth != 0 and i < len(ptext):
                    if ptext[i] == "(":
                        depth += 1
                    if ptext[i] == ")":
                        depth -= 1

                    i += 1
                i -= 1

            #then we check for anything else
            if ptext[i] != " " and i < len(ptext) - 1:
                slicestart = i
                flag = 0
                i += 1
                while flag == 0 and i < len(ptext):
                    if ptext[i] == " ":
                        flag = 1
                    else:
                        i += 1

                slicestop = i

                try:
                    int(ptext[slicestart:slicestop])
                    inty = int(ptext[slicestart:slicestop])
                    output.append([inttype, inty])
                except:
                    try:
                        float(ptext[slicestart:slicestop])
                        floaty = float(ptext[slicestart:slicestop])
                        output.append([floattype, floaty])
                    except:
                        texty =  ptext[slicestart:slicestop]
                        output.append([generictype, texty])
            i += 1
            
    return output


#atomeval() evaluates atoms
#Integers, floats, and strings will be placed on the stack, and anything else will be checked to see if it is defined. If it is, it will be evaluated

def atomeval(atoms):
    for index in range(len(atoms)):
        if atoms[index][0] != generictype:
            metastack[stackname].append(atoms[index])
        else:
           try:
               macrotable[atoms[index][1]]
               atomeval(macrostack[atoms[index]])
           except:
               if atoms[index][1] == "+":
                   result = addbuiltin()
                   if result != 0:
                       return "Atom #" + str(index) + ": " + str(result)
               elif atoms[index][1] == "-":
                    subtractbuiltin()
               elif atoms[index][1] == "*":
                    multiplybuiltin()
               elif atoms[index][1] == "/":
                    dividebuiltin()
               elif atoms[index][1] == ">":
                   greaterthanbuiltin()
               elif atoms[index][1] == "<":
                   lessthanbuilin()
               elif atoms[index][1] == "top":
                   topbuiltin()
               elif atoms[index][1] == "if":
                   ifbuiltin()
               elif atoms[index][1] == "pop":
                   popbuiltin()
               elif atoms[index][1] == "dup":
                   dupbuiltin()
               else:
                   metastack[stackname].append(atoms[index])
                   



def addbuiltin():
    if len(metastack[stackname]) < 2:
        return "Stack must be at least two atoms for \"+\""
    elif metastack[stackname][-1][0] == stringtype or \
       metastack[stackname][-2][0] == stringtype:
        return "Top two atoms must be of type int or float for addition"
    else:
        if metastack[stackname][-1][0] == floattype or \
           metastack[stackname][-2][0] == floattype:
            addend1 = metastack[stackname].pop()
            addend2 = metastack[stackname].pop()
            thesum = float(addend1[1]) + float(addend2[1])
            metastack[stackname].append([floattype, str(thesum)])
        else:
            addend1 = metastack[stackname].pop()
            addend2 = metastack[stackname].pop()
            thesum = int(addend1[1]) + int(addend2[1])
            metastack[stackname].append([inttype, str(thesum)])
            
        return 0
        
        

def subtractbuiltin():
    GNDN = 0

def multiplybuiltin():
    GNDN = 0

def dividebuiltin():
    GNDN = 0
                    
def greaterthanbuiltin():
    GNDN = 0

def lessthanbuiltin():
    GNDN = 0

def topbuiltin():
    GNDN = 0

def ifbuiltin():
    GNDN = 0

def popbuiltin():
    GNDN = 0

def dupbuiltin():
    GNDN = 0
