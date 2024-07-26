# -> Function one 
# input : Should be list e.g ->'mass*acc*cos(x)-force,1/2*mass*velocity**2-KE,mass*height*gravity-PE,displacement*time-velocity'  => basically force = mass * acc * cos(x) -> 'mass*acc*cos(x)-force
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
