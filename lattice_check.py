# Getting lattice parameters
import os
import pymatgen as pmg

def lattice_check(model,structure,li_concentration,functional_list,U_value,conf):
    if (model == 'Li2MnO3'):
        dir = os.path.join('/scratch/antwerpen/204/vsc20412',model,model[0:2]+li_concentration+model[3:],structure)
    elif (model == 'Li2IrO3'):
        dir = os.path.join('/scratch/antwerpen/204/vsc20412',model,model[0:2]+li_concentration+model[3:])
    elif (model == 'Li2MnSnO3'):
        dir = os.path.join('/scratch/antwerpen/204/vsc20412',model,'Li'+li_concentration)
    
    try:
        if (len(U_value)>1):
            values = U_value    
    except:
        values = [U_value]
    
    if functional_list == 'pbeU':
            
        h=len(values)
        w=4
        lattice_parameters_length = [[0 for x in range(w)] for y in range(h)]

        for i in range(0,3):
            q=0
            for u in values:
                directory=os.path.join(dir,"conf_"+str(conf), 'pbeU',str(u)) # <--- Specify U-vaule (last number) or dir for SCAN and HSE06
                os.chdir(directory)
                s = pmg.Structure.from_file('CONTCAR')
                lattice_parameters_length[q][i+1]=s.lattice.abc[i]
                lattice_parameters_length[q][0]=u
                q = q + 1
        
    elif functional_list == 'scan':
        h=1
        w=4
        lattice_parameters_length = [[0 for x in range(w)] for y in range(h)]
        try:
            directory=os.path.join(dir,"conf_"+str(conf), 'scan') # <--- Specify U-vaule (last number) or dir for SCAN and HSE06
            os.chdir(directory)
            s = pmg.Structure.from_file('CONTCAR')
            for i in range(0,3):
                lattice_parameters_length[0][i+1]=s.lattice.abc[i]
        except:
            pass
            
    elif functional_list == 'hse':
        h=1
        w=4
        lattice_parameters_length = [[0 for x in range(w)] for y in range(h)]
        try:
            directory=os.path.join(dir,"conf_"+str(conf), 'hse') # <--- Specify U-vaule (last number) or dir for SCAN and HSE06
            os.chdir(directory) 
            s = pmg.Structure.from_file('CONTCAR')
            for i in range(0,3):
                lattice_parameters_length[0][i+1]=s.lattice.abc[i]
        except:
            pass
        
    elif functional_list == ("pbeU", "scan" , "hse"):
        h=len(values)+2
        w=4
        lattice_parameters_length = [[0 for x in range(w)] for y in range(h)]
    #pbeu part
        try:
            if (len(U_value)>1):
                values = U_value    
        except:
            values = [U_value]

        for i in range(0,3):
            q=0
            for u in values:
                directory=os.path.join(dir,"conf_"+str(conf), 'pbeU',str(u)) # <--- Specify U-vaule (last number) or dir for SCAN and HSE06
                os.chdir(directory)
                s = pmg.Structure.from_file('CONTCAR')
                lattice_parameters_length[q][i+1]=s.lattice.abc[i]
                lattice_parameters_length[q][0]=u
                q = q + 1
        try:     
        #scan part
            directory=os.path.join(dir,"conf_"+str(conf), 'scan') # <--- Specify U-vaule (last number) or dir for SCAN and HSE06
            os.chdir(directory)
            s = pmg.Structure.from_file('CONTCAR')
            for i in range(0,3):
                lattice_parameters_length[q][i+1]=s.lattice.abc[i]
        except:
            pass

        #hse part  
        try:
            directory=os.path.join(dir,"conf_"+str(conf), 'hse') # <--- Specify U-vaule (last number) or dir for SCAN and HSE06
            os.chdir(directory)
            s = pmg.Structure.from_file('CONTCAR')
            for i in range(0,3):
                lattice_parameters_length[q+1][i+1]=s.lattice.abc[i]       
        except:
            pass
    
    elif functional_list == ("pbeU", "scan"):
        h=len(values)+1
        w=4
        lattice_parameters_length = [[0 for x in range(w)] for y in range(h)]
    #pbeu part
        try:
            if (len(U_value)>1):
                values = U_value    
        except:
            values = [U_value]

        for i in range(0,3):
            q=0
            for u in values:
                directory=os.path.join(dir,"conf_"+str(conf), 'pbeU',str(u)) # <--- Specify U-vaule (last number) or dir for SCAN and HSE06
                os.chdir(directory)
                s = pmg.Structure.from_file('CONTCAR')
                lattice_parameters_length[q][i+1]=s.lattice.abc[i]
                lattice_parameters_length[q][0]=u
                q = q + 1
        try:     
        #scan part
            directory=os.path.join(dir,"conf_"+str(conf), 'scan') # <--- Specify U-vaule (last number) or dir for SCAN and HSE06
            os.chdir(directory)
            s = pmg.Structure.from_file('CONTCAR')
            for i in range(0,3):
                lattice_parameters_length[q][i+1]=s.lattice.abc[i]
        except:
            pass
    
    else:
        pass
    
    header = ("U-value (eV)", 'a-lattice (A)', 'b-lattice (A)','c-lattice (A)')
    
    return (header,lattice_parameters_length)
    #return tabulate(lattice_parameters_length, headers=header, tablefmt="latex", floatfmt=(".1f",".5f"))
