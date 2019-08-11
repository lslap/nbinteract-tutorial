
from energy_check import energy_check

def voltage(model,structure,li_concentration,functional_list,U_value,conf,configuration):
    
    try:
        if (len(U_value)>1):
            values = U_value    
    except:
        values = [U_value]
        
    if structure == 'conv':
        if (len(values)>1):
            h=len(values)
            w=2
            result = [[0 for x in range(w)] for y in range(h)] 
            q=0
            for i in values:
                [header,energy]=energy_check(model,structure,'0.5',functional_list,i,conf,False)
                b = float(energy[0][1])

                [header,energy]=energy_check(model,structure,'2',functional_list,i,'0',False)
                a = float(energy[0][1])

                result[q][1] = (a/4-b/4+1.9*1.5)/1.5
                result[q][0] = i
                q = q + 1
        else:
            result = [0]*2
            
            [header,energy]=energy_check(model,structure,'0.5',functional_list,U_value,conf,False)
            b = float(energy[0][1])

            [header,energy]=energy_check(model,structure,'2',functional_list,U_value,'0',False)
            a = float(energy[0][1])

            result[1] = (a/4-b/4+1.9*1.5)/1.5
            result[0] = float(U_value)
            result = [result]
    else:
        if (len(values)>1):
            h=len(values)
            w=2
            result = [[0 for x in range(w)] for y in range(h)] 
            q=0
            for i in values:
                [header,energy]=energy_check(model,structure,'0.5',functional_list,i,conf,False)
                b = float(energy[0][1])

                [header,energy]=energy_check(model,structure,'2',functional_list,i,'0',False)
                a = float(energy[0][1])

                result[q][1] = (a/2-b/2+1.9*1.5)/1.5
                result[q][0] = i
                q = q + 1
        else:
            result = [0]*2
            [header,energy]=energy_check(model,structure,'0.5',functional_list,U_value,conf,False)
            b = float(energy[0][1])

            [header,energy]=energy_check(model,structure,'2',functional_list,U_value,'0',False)
            a = float(energy[0][1])

            result[1] = (a/2-b/2+1.9*1.5)/1.5
            result[0] = float(U_value)
            result = [result]
            
    header = ("U-value (eV)", 'Voltage (V)')
    return (header,result)