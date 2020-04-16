#! /usr/bin/python3
"""
   Sutakku
   A simple stack based interpreted language

   Copyright 2020 SpaceBudokan

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <https://www.gnu.org/licenses/>. 
"""


import readline

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
                slicestop = i - 1
                output.append([stringtype, ptext[slicestart:slicestop]])
            #next we check for comments
            if i != len(ptext):
                if ptext[i] == "(":
                    depth += 1
                    i += 1
                    while depth != 0 and i < len(ptext):
                        if ptext[i] == "(":
                            depth += 1
                        if ptext[i] == ")":
                            depth -= 1

                        i += 1

            #then we check for anything else
            if i !=len(ptext):
                if ptext[i] != " " and i < len(ptext):
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
#Integers, floats, and strings will be placed on the stack, and anything else will be checked to see if it is defined. If it is, it will be evaluated

def atomeval(atoms):
    for index in range(len(atoms)):
        if atoms[index][1] in macrotable:
            result = atomeval([macrotable[atoms[index][1]]])
        else:
            try:
                int(atoms[index][1])
                metastack[stackname].append([inttype, atoms[index][1]])
            except:
                try:
                    float(atoms[index][1])
                    metastack[stackname].append([floattype, atoms[index][1]])
                except:
                    result = 0
                    if atoms[index][1] == "define":
                        result = definebuiltin()
                    elif atoms[index][1] == "stack":
                        result = stackbuiltin()
                    elif atoms[index][1] == "+":
                        result = addbuiltin()
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
                        metastack[stackname].append([stringtype, atoms[index][1]])
                    if result != 0:
                        return "Atom #" + str(index) + ": " + str(result)   
  
    return 0

def definebuiltin():
    if len(metastack[stackname]) < 2:
        return "Stack requires at least two atoms for definition"
    key = metastack[stackname].pop()
    key = key[1]
    definition = metastack[stackname].pop()
    macrotable[key] = definition  
    return 0

def stackbuiltin():
    global stackname
    global metastack
    if metastack[stackname] == []:
        return "Stack must contain at least one atom to make/change current stack"
    if metastack[stackname][-1][1] in metastack:
        stackname = metastack[stackname].pop()
        stackname = stackname[1]
        return 0
    else:
        stackname = metastack[stackname].pop()
        stackname = stackname[1]
        metastack[stackname] = []
        return 0

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











print("Welcome to Sutakku")
print("Copyright 2020 SpaceBudokan")
print("This program comes with ABSOLUTELY NO WARRANTY; This is free software, and you are welcome to redistribute it under certain conditions.")
print("")
print("I'm so glad you're here!")
print("Type \"bye\" to Exit")

print(generictype)
while typedline != "bye":
    typedline = input(stackname + ">")
    atoms = parse(typedline)
    result = atomeval(atoms)
    if result != 0:
        print(result)
    print(metastack)


print("Goodbye! I'll miss you...")
