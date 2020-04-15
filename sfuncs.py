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
                
                output.append([generictype, ptext[slicestart:slicestop]])
            i += 1
            
    return output


#atomeval() evaluates atoms
#integers will be cast to int, Floats to float, and anything else will be checked to see if it is defined. If it is, it will be evaluated

def atomeval(atoms):
    for index in range(len(atoms)):
        if atoms[index][0] == inttype or atoms[index][0] == stringtype:
            metastack[stackname].append(atoms[index])
        else:
            try:
                int(atoms[index][1])
                atoms[index][0] = inttype
                atoms[index][1] = int(atoms[index][1])
                metastack[stackname].append(atoms[index])
            except:
                try:
                    float(atoms[index][1])
                    atoms[index][0] = floattype
                    atoms[index][1] = float(atoms[index][1])
                    metastack[stackname].append(atoms[index])
                except:
                    metastack[stackname].append(atoms[index])
