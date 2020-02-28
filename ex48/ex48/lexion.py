

def scan(a):
    b=a.split()
    secetence=[]

    for c in b:
        i=0
        if c in ['north','south','east']:
            first_word=['direction',str(c)]
            secetence.append(first_word)
            
        elif c in ['go','kill','eat']:
            second_word=['verb',str(c)]
            secetence.append(second_word)

        elif c in ['the','in','of']:
            third_word=['stop',str(c)]
            secetence.append(third_word)

        elif c in ['bear','princess']:
            forth_word=['noun',str(c)]
            secetence.append(forth_word)

        elif c in ['3','1234','91234']:
            fifth_word=['number',str(c)]
            secetence.append(fifth_word)
    
        else:
            sixth_word=['error',str(c)]
            secetence.append(sixth_word)
        
        i=i+1       
        if i==int(len(b)):
                break

    return secetence





    
