from sympy import *
# function 1
def wd(equation):
    b = []
    for i in equation:
        if ord(i) in range(97, 122):
            b.append(i)
        else:
            i = '1'
            b.append(i)
  
    bb = (''.join(b))
  
    cc = bb.replace('1', ' ')

    dd = cc.split(' ')
 
    li = []
    for i in dd:
        if i != '':
            li.append(i)
   
    return li

# function 2
def generator(equation,respect):
    
    s_q = equation.split(',')
      
    
    def symb(respect):
        globals_dict = {}
        for i in respect:
            globals_dict[i] = i
        #print(globals_dict)
        for var_name, var_value in globals_dict.items():
            globals()[var_name] = symbols(var_value)
        
    list_eq = []
    for i in s_q:
        list_eq.append(solve(i, respect)) 
    return list_eq

# function 3
def seprator3(list_eq):
    string=' '.join(map(str,list_eq))

    string2=string.replace('[','')

    
    string3=string2.replace(']','')
    
    string4=string3.replace(' ',',')
  
    
    list4=string4.split(',')

    li2=[]
    for i in list4:
        
    
        if i!='':
            li2.append(i)
    return li2

#function
def symb(respect):
        globals_dict = {}
        for i in respect:
            globals_dict[i] = i
        #print(globals_dict)
        for var_name, var_value in globals_dict.items():
            globals()[var_name] = symbols(var_value)

#fucntion 4
def generator2(equation,respect):
    li=generator(equation,respect)
 
    return seprator3(li)

equation = 'mass*acc*cos(x)-force,1/2*mass*velocity**2-KE,mass*height*gravity-PE,displacement*time-velocity'
respect = ['velocity']
k=generator2(equation,respect)
print(k)
   
