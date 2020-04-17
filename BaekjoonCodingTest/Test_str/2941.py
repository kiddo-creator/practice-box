string = input()
# croa=[c=,c-,dz=,d-,lj,nj,s=,z=]
croa_three = 0
croa_dub = 0
count=0

for i in range(len(string)):
    if string[i]=="c":
        if string[i+1] == "-" or string[i+1] == "=":
            croa_dub= croa_dub+1
        else:
            pass
    elif string[i]=="d":
        if string[i+1] == "z":
            if string[i+2] == "=":
                croa_three = croa_three + 1
                croa_dub=croa_dub-1
            else:
                pass
        elif string[i+1] == "-":
            croa_dub= croa_dub+1
        else:
            pass
    elif string[i]=="l":
        if string[i+1] == "j":
            croa_dub=croa_dub+1
        else:
            pass
    elif string[i]=="n":
        if string[i+1]=="j":
            croa_dub=croa_dub+1
        else:
            pass
    elif string[i] =="s" or string[i]=="z":
        if string[i+1] == "=":
            croa_dub=croa_dub+1
        else:
            pass
    else:
        pass

print(len(string)-(1*croa_dub)-(2*croa_three))
