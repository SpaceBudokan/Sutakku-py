#This is just a module to whisk away function declarations.

def parse(ptext):
    slicestart = 0
    slicestop = 0
    output = []
    i = 0
    j = 0
    depth = 0
    while i < len(ptext):
        if ptext[i] == "<":
            depth += 1
            i += 1
            slicestart = i
            while depth != 0 and i < len(ptext):
                if ptext[i] == "<":
                    depth += 1
                if ptext[i] == ">":
                    depth -= 1
                
                i += 1
            i -= 1
            slicestop = i
            output.append(ptext[slicestart:slicestop])

        if ptext[i] == "(":
            depth += 1
            i += 1
            while depth != 0 and i < len(ptext):
                if ptext[i] == "(":
                    depth += 1
                if ptext[i] == ")":
                    depth -= 1
                
                i += 1
            i += 1
        print(i)

         
    return output
