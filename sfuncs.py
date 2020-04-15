#This is just a module to whisk away function declarations.

def parse(ptext):
    slicestart = 0
    slicestop = 0
    output = []
    i = 0
    j = 0
    depth = 0
    if len(ptext) == 1:
        output.append(ptext)
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
                output.append(ptext[slicestart:slicestop])
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
                output.append(ptext[slicestart:slicestop])
            i += 1



        
    return output
