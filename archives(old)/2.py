while len(inputList) != val_calc:
    for x in inputList[0 + val_calc]:
        preLet.append(ord(x) - 96)
    
    while len(preLet) != c1:
        
        if preLet[c1] == 1:
            preVal.insert(c1, "2")
        elif preLet[c1] == 5:
            preVal.insert(c1, "2")
        elif preLet[c1] == 9:
            preVal.insert(c1, "2")
        elif preLet[c1] == 15:
            preVal.insert(c1, "2")
        elif preLet[c1] == 21:
            preVal.insert(c1, "2")
        elif preLet[c1] == -52:
            preVal.insert(c1, "0") #for commas
        elif preLet[c1] == -64:
            preVal.insert(c1, "0") #for spaces
        elif preLet[c1] == 137:
            preVal.insert(c1, "2") # é
        elif preLet[c1] == 129:
            preVal.insert(c1, "2") # á
        elif preLet[c1] == 141:
            preVal.insert(c1, "2") # í
        elif preLet[c1] == 147:
            preVal.insert(c1, "2") # ó
        elif preLet[c1] == 154:
            preVal.insert(c1, "2") # ú
        else:
            preVal.insert(c1, "1")
        c1 = c1 + 1
        