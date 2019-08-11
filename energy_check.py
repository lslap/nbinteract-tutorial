
import os
from conf_checker import conf_checker

def energy_check(model,structure,li_concentration,functional_list,U_value,conf,configuration):
    if (model == 'Li2MnO3'):
        dir = os.path.join('/scratch/antwerpen/204/vsc20412',model,model[0:2]+li_concentration+model[3:],structure)
    elif (model == 'Li2IrO3'):
        dir = os.path.join('/scratch/antwerpen/204/vsc20412',model,model[0:2]+li_concentration+model[3:])
    elif (model == 'Li2MnSnO3'):
        dir = os.path.join('/scratch/antwerpen/204/vsc20412',model,'Li'+li_concentration)
    else:
        print("This file doesn't exists")

    if (configuration == True):
        configurations=conf_checker(model,li_concentration,structure)
    else:
        configurations=[conf]

    try:
        h=len(U_value)
        w=len(configurations)+1
        b = [[0 for x in range(w)] for y in range(h)]   
    except:
        h=1
        w=len(configurations)+1
        b = [[0 for x in range(w)] for y in range(h)] 

    try:
        if (len(U_value)>1):
            values = U_value    
    except:
        values = [U_value]

    #pbeU 
    if functional_list == 'pbeU':
        j = 1
        q = 0
        for x in configurations:
            for i in values:
                directory=os.path.join(dir,"conf_"+str(x), 'pbeU',str(i))
                os.chdir(directory)
                with open('OUTCAR', 'r') as searchfile:
                    for line in searchfile:
                        if 'free  en' in line:
                            try:
                                b[q][j]=line[-len(U_value)-3:-10]
                            except:
                                b[q][j]=line[-17:-10]
                b[q][0] = i
                q = q + 1
            q = 0
            j = j + 1
    
    #scan
    try:
        if functional_list == 'scan':
            h=1
            w=len(configurations)+1
            b = [[0 for x in range(w)] for y in range(h)]
            j = 1
            for x in configurations:
                directory=os.path.join(dir,"conf_"+str(x), 'scan')
                os.chdir(directory)
                with open('OUTCAR', 'r') as searchfile:
                    for line in searchfile:
                        if 'free  en' in line:
                            try:
                                b[0][j]=line[-len(U_value)-3:-10]
                            except:
                                b[0][j]=line[-17:-10]
                j = j + 1
    except:
        pass
    
    #hse
    try:
        if functional_list == 'hse':
            h=1
            w=len(configurations)+1
            b = [[0 for x in range(w)] for y in range(h)]
            j = 1
            for x in configurations:
                directory=os.path.join(dir,"conf_"+str(x), 'hse')
                os.chdir(directory)
                with open('OUTCAR', 'r') as searchfile:
                    for line in searchfile:
                        if 'free  en' in line:
                            try:
                                b[0][j]=line[-len(U_value)-3:-10]
                            except:
                                b[0][j]=line[-17:-10]
                j = j + 1
    except:
        pass
    
    #pbeU,scan and hse
    if functional_list == ("pbeU", "scan" , "hse"):
        try:
            h=len(values)+2
            w=len(configurations)+1
            b = [[0 for x in range(w)] for y in range(h)]   
        except:
            h=3
            w=len(configurations)+1
            b = [[0 for x in range(w)] for y in range(h)] 
        
        j = 1
        q = 0
        for x in configurations:
            for i in values:
                directory=os.path.join(dir,"conf_"+str(x), 'pbeU',str(i))
                os.chdir(directory)
                with open('OUTCAR', 'r') as searchfile:
                    for line in searchfile:
                        if 'free  en' in line:
                            try:
                                b[q][j]=line[-len(U_value)-3:-10]
                            except:
                                b[q][j]=line[-17:-10]
                b[q][0] = i
                q = q + 1
            q = 0
            j = j + 1
            
        #scan    
        try:  
            j=1
            for x in configurations:
                directory=os.path.join(dir,"conf_"+str(x), 'scan')
                os.chdir(directory)
                with open('OUTCAR', 'r') as searchfile:
                    for line in searchfile:
                        if 'free  en' in line:
                            try:
                                b[len(values)][j]=line[-len(U_value)-3:-10]
                            except:
                                b[len(values)][j]=line[-17:-10]
                j = j + 1
        except:
            pass
        
        #hse
        try:
            j=1
            for x in configurations:
                directory=os.path.join(dir,"conf_"+str(x), 'hse')
                os.chdir(directory)
                with open('OUTCAR', 'r') as searchfile:
                    for line in searchfile:
                        if 'free  en' in line:
                            try:
                                b[len(values)+1][j]=line[-len(U_value)-3:-10]
                            except:
                                b[len(values)+1][j]=line[-17:-10]
                j = j + 1
        except:
            pass
        
    #pbeU,scan
    if functional_list == ("pbeU", "scan"):
        try:
            h=len(values)+1
            w=len(configurations)+1
            b = [[0 for x in range(w)] for y in range(h)]   
        except:
            h=3
            w=len(configurations)+1
            b = [[0 for x in range(w)] for y in range(h)] 
        
        j = 1
        q = 0
        for x in configurations:
            for i in values:
                directory=os.path.join(dir,"conf_"+str(x), 'pbeU',str(i))
                os.chdir(directory)
                with open('OUTCAR', 'r') as searchfile:
                    for line in searchfile:
                        if 'free  en' in line:
                            try:
                                b[q][j]=line[-len(U_value)-3:-10]
                            except:
                                b[q][j]=line[-17:-10]
                b[q][0] = i
                q = q + 1
            q = 0
            j = j + 1
            
        #scan    
        try:  
            j=1
            for x in configurations:
                directory=os.path.join(dir,"conf_"+str(x), 'scan')
                os.chdir(directory)
                with open('OUTCAR', 'r') as searchfile:
                    for line in searchfile:
                        if 'free  en' in line:
                            try:
                                b[len(values)][j]=line[-len(U_value)-3:-10]
                            except:
                                b[len(values)][j]=line[-17:-10]
                j = j + 1
        except:
            pass



    tuple_join = ()
    for i in range(0,len(configurations)):
        lst_mixed = ['E. conf',i, '(eV)']
        str_join = " ".join(str(x) for x in lst_mixed)
        tuple_join = tuple_join + tuple([str_join])   

    header = ("U-value (eV)",) + tuple_join

    #test = tabulate(b,headers=header, tablefmt="latex", floatfmt=(".1f",".2f"))
   
    return (header,b)
