# Function 3 -> this will separte all the equations
def seprator3(list_eq):
    string=' '.join(map(str,list_eq))
    #print(type(string))
    string2=string.replace('[','')
    #print(string2)
    
    string3=string2.replace(']','')
    
    string4=string3.replace(' ',',')
    #print(string4)
    
    list4=string4.split(',')
    #print(list4)
    li2=[]
    for i in list4:
        
        #print(i)
        if i!='':
            li2.append(i)
    return li2
