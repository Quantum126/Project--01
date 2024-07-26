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
