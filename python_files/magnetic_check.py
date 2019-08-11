
import os
import pymatgen as pmg

# Gives the magnetization for a specific configuration
def magnetic_check(model,structure,li_concentration,functional_list,U_value,conf):

    if (model == 'Li2MnO3'):
        dir = os.path.join('/scratch/antwerpen/204/vsc20412',model,model[0:2]+li_concentration+model[3:],structure)
    elif (model == 'Li2IrO3'):
        dir = os.path.join('/scratch/antwerpen/204/vsc20412',model,model[0:2]+li_concentration+model[3:])
    elif (model == 'Li2MnSnO3'):
        dir = os.path.join('/scratch/antwerpen/204/vsc20412',model,'Li'+li_concentration)

    try:
        if (len(U_value)>1):
            values = U_value
            h=len(values)
            if (model == 'Li2MnSnO3'):
                w=4
            else:
                w=3
            results = [[0 for x in range(w)] for y in range(h)] 
            results_test = [[0 for x in range(w)] for y in range(h)] 

    except:
        values = [U_value]
        h=1
        if (model == 'Li2MnSnO3'):
            w=4
        else:
            w=3
        results = [[0 for x in range(w)] for y in range(h)] 
        results_test = [[0 for x in range(w)] for y in range(h)]
    
    
    #pbeU
    if functional_list == 'pbeU':    
        q = 0
        p = 0
        for i in values:
            results[p][0] = i
            results_test[p][0] = i
            p = p + 1


        for u in values:
            directory=os.path.join(dir,"conf_"+str(conf), 'pbeU',str(u)) # <--- Specify U-vaule (last number) or dir for SCAN and HSE06
            os.chdir(directory)

            i = 0
            free_energy_form_different_U_values={}
            with open('OUTCAR','r') as searchfile:
                content = searchfile.readlines()
            with open('OUTCAR','r') as searchfile:
                for line in searchfile:
                        i = i + 1
                        if '# of ion       s       p       d       tot' in line:
                            free_energy_form_different_U_values[i]=line
            free_energy_form_different_U_values


            key = sorted(free_energy_form_different_U_values.keys())[-1]

            s = pmg.Structure.from_file('POSCAR')
            if (model == 'Li2MnSnO3'):
                a=s.formula
                x = int(a[2])
                y = int(a[6:8])
                z = int(a[-2:])
            else:
                a=s.formula
                x = int(a[2])
                y = int(a[6])
                z = int(a[-1:])

        # Calculates the avarage magnetic moment on the second element
            j = 0
            a = 0
            magnetic={}
            for i in range(x,y+x):
                j = j + 1
                mag = content[key+i+1]
                magnetic[j] = mag[-6:-1]

            count = 0
            _sum = 0
            for i in range(1,len(magnetic)):
                count += 1
                _sum += float(magnetic[i])
                magnetic_Mn = _sum/count
            results[q][1]= magnetic_Mn

        # Calculates the avarage magnetic moment on the third element
            j = 0
            a = 0
            magnetic={}
            for i in range(y+x,y+x+z+1):
                j = j + 1
                mag = content[key+i+1]
                magnetic[j] = mag[-7:-1]

            count = 0
            _sum = 0
            for i in range(1,len(magnetic)):
                count += 1
                _sum += float(magnetic[i])
            magnetic_O = _sum/count
            if (model == 'Li2MnSnO3'):
                mag = content[key+x+y+1]
                magnetic_Sn = mag[-6:-1]
                results[q][2]=magnetic_Sn
                results[q][3]= magnetic_O
            else:
                results[q][2]= magnetic_O
            q = q + 1


    ## SCAN
    elif functional_list == 'scan':
        h=1
        if (model == 'Li2MnSnO3'):
            w=4
        else:
            w=3
        results = [[0 for x in range(w)] for y in range(h)] 
        results_test = [[0 for x in range(w)] for y in range(h)] 


        #try:
        directory=os.path.join(dir,"conf_"+str(conf), 'scan') # <--- Specify U-vaule (last number) or dir for SCAN and HSE06
        os.chdir(directory)

        i = 0
        free_energy_form_different_U_values={}
        with open('OUTCAR','r') as searchfile:
            content = searchfile.readlines()

        with open('OUTCAR','r') as searchfile:
            for line in searchfile:
                    i = i + 1
                    if '# of ion       s       p       d       tot' in line:
                        free_energy_form_different_U_values[i]=line
        free_energy_form_different_U_values

        key = sorted(free_energy_form_different_U_values.keys())[-1]

        s = pmg.Structure.from_file('POSCAR')
        if (model == 'Li2MnSnO3'):
            a=s.formula
            x = int(a[2])
            y = int(a[6:8])
            z = int(a[-2:])
        else:
            a=s.formula
            x = int(a[2])
            y = int(a[6])
            z = int(a[-1:])

        # Calculates the avarage magnetic moment on the second element
        j = 0
        a = 0
        magnetic={}
        for i in range(x,y+x):
            j = j + 1
            mag = content[key+i+1]
            magnetic[j] = mag[-6:-1]

        count = 0
        _sum = 0
        for i in range(1,len(magnetic)):
            count += 1
            _sum += float(magnetic[i])
        magnetic_Mn = _sum/count
        results[0][1]= magnetic_Mn

        # Calculates the avarage magnetic moment on the third element
        j = 0
        a = 0
        magnetic={}
        for i in range(y+x,y+x+z+1):
            j = j + 1
            mag = content[key+i+1]
            magnetic[j] = mag[-7:-1]

        count = 0
        _sum = 0
        for i in range(1,len(magnetic)):
            count += 1
            _sum += float(magnetic[i])
        magnetic_O = _sum/count
        if (model == 'Li2MnSnO3'):
            mag = content[key+x+y+1]
            magnetic_Sn = mag[-6:-1]
            results[0][2]=magnetic_Sn
            results[0][3]= magnetic_O
        else:
            results[0][2]= magnetic_O  

        #except:
            #pass


    ## HSE06
    elif functional_list == 'hse':
        h=1
        if (model == 'Li2MnSnO3'):
            w=4
        else:
            w=3
        results = [[0 for x in range(w)] for y in range(h)] 
        results_test = [[0 for x in range(w)] for y in range(h)] 


        try:
            directory=os.path.join(dir,"conf_"+str(conf), 'hse') # <--- Specify U-vaule (last number) or dir for SCAN and HSE06
            os.chdir(directory)

            i = 0
            free_energy_form_different_U_values={}
            with open('OUTCAR','r') as searchfile:
                content = searchfile.readlines()

            with open('OUTCAR','r') as searchfile:
                for line in searchfile:
                        i = i + 1
                        if '# of ion       s       p       d       tot' in line:
                            free_energy_form_different_U_values[i]=line
            free_energy_form_different_U_values

            key = sorted(free_energy_form_different_U_values.keys())[-1]

            s = pmg.Structure.from_file('POSCAR')
            if (model == 'Li2MnSnO3'):
                a=s.formula
                x = int(a[2])
                y = int(a[6:8])
                z = int(a[-2:])
            else:
                a=s.formula
                x = int(a[2])
                y = int(a[6])
                z = int(a[-1:])
            # Calculates the avarage magnetic moment on the second element
            j = 0
            a = 0
            magnetic={}
            for i in range(x,y+x):
                j = j + 1
                mag = content[key+i+1]
                magnetic[j] = mag[-6:-1]

            count = 0
            _sum = 0
            for i in range(1,len(magnetic)):
                count += 1
                _sum += float(magnetic[i])
            magnetic_Mn = _sum/count
            results[0][1]= magnetic_Mn

            # Calculates the avarage magnetic moment on the third element
            j = 0
            a = 0
            magnetic={}
            for i in range(y+x,y+x+z+1):
                j = j + 1
                mag = content[key+i+1]
                magnetic[j] = mag[-7:-1]

            count = 0
            _sum = 0
            for i in range(1,len(magnetic)):
                count += 1
                _sum += float(magnetic[i])
            magnetic_O = _sum/count
            if (model == 'Li2MnSnO3'):
                mag = content[key+x+y+1]
                magnetic_Sn = mag[-6:-1]
                results[0][2]=magnetic_Sn
                results[0][3]= magnetic_O
            else:
                results[0][2]= magnetic_O
        except:
            pass
    
    
    elif functional_list == ("pbeU", "scan" , "hse"):
        try:
            if (len(U_value)>1):
                values = U_value
                h=len(values)+2
                if (model == 'Li2MnSnO3'):
                    w=4
                else:
                    w=3
                results = [[0 for x in range(w)] for y in range(h)] 
                results_test = [[0 for x in range(w)] for y in range(h)] 

        except:
            values = [U_value]
            h=1+2
            if (model == 'Li2MnSnO3'):
                w=4
            else:
                w=3
            results = [[0 for x in range(w)] for y in range(h)] 
            results_test = [[0 for x in range(w)] for y in range(h)]
            
        #pbeU   
        q = 0
        p = 0
        for i in values:
            results[p][0] = i
            results_test[p][0] = i
            p = p + 1


        for u in values:
            directory=os.path.join(dir,"conf_"+str(conf), 'pbeU',str(u)) # <--- Specify U-vaule (last number) or dir for SCAN and HSE06
            os.chdir(directory)

            i = 0
            free_energy_form_different_U_values={}
            with open('OUTCAR','r') as searchfile:
                content = searchfile.readlines()
            with open('OUTCAR','r') as searchfile:
                for line in searchfile:
                        i = i + 1
                        if '# of ion       s       p       d       tot' in line:
                            free_energy_form_different_U_values[i]=line
            free_energy_form_different_U_values


            key = sorted(free_energy_form_different_U_values.keys())[-1]

            s = pmg.Structure.from_file('POSCAR')
            if (model == 'Li2MnSnO3'):
                a=s.formula
                x = int(a[2])
                y = int(a[6:8])
                z = int(a[-2:])
            else:
                a=s.formula
                x = int(a[2])
                y = int(a[6])
                z = int(a[-1:])

        # Calculates the avarage magnetic moment on the second element
            j = 0
            a = 0
            magnetic={}
            for i in range(x,y+x):
                j = j + 1
                mag = content[key+i+1]
                magnetic[j] = mag[-6:-1]

            count = 0
            _sum = 0
            for i in range(1,len(magnetic)):
                count += 1
                _sum += float(magnetic[i])
                magnetic_Mn = _sum/count
            results[q][1]= magnetic_Mn

        # Calculates the avarage magnetic moment on the third element
            j = 0
            a = 0
            magnetic={}
            for i in range(y+x,y+x+z+1):
                j = j + 1
                mag = content[key+i+1]
                magnetic[j] = mag[-7:-1]

            count = 0
            _sum = 0
            for i in range(1,len(magnetic)):
                count += 1
                _sum += float(magnetic[i])
            magnetic_O = _sum/count
            if (model == 'Li2MnSnO3'):
                mag = content[key+x+y+1]
                magnetic_Sn = mag[-6:-1]
                results[q][2]=magnetic_Sn
                results[q][3]= magnetic_O
            else:
                results[q][2]= magnetic_O
            q = q + 1


    ## SCAN
        try:
            directory=os.path.join(dir,"conf_"+str(conf), 'scan') # <--- Specify U-vaule (last number) or dir for SCAN and HSE06
            os.chdir(directory)

            i = 0
            free_energy_form_different_U_values={}
            with open('OUTCAR','r') as searchfile:
                content = searchfile.readlines()

            with open('OUTCAR','r') as searchfile:
                for line in searchfile:
                        i = i + 1
                        if '# of ion       s       p       d       tot' in line:
                            free_energy_form_different_U_values[i]=line
            free_energy_form_different_U_values

            key = sorted(free_energy_form_different_U_values.keys())[-1]

            s = pmg.Structure.from_file('POSCAR')
            if (model == 'Li2MnSnO3'):
                a=s.formula
                x = int(a[2])
                y = int(a[6:8])
                z = int(a[-2:])
            else:
                a=s.formula
                x = int(a[2])
                y = int(a[6])
                z = int(a[-1:])

            # Calculates the avarage magnetic moment on the second element
            j = 0
            a = 0
            magnetic={}
            for i in range(x,y+x):
                j = j + 1
                mag = content[key+i+1]
                magnetic[j] = mag[-6:-1]

            count = 0
            _sum = 0
            for i in range(1,len(magnetic)):
                count += 1
                _sum += float(magnetic[i])
            magnetic_Mn = _sum/count
            results[q][1]= magnetic_Mn

            # Calculates the avarage magnetic moment on the third element
            j = 0
            a = 0
            magnetic={}
            for i in range(y+x,y+x+z+1):
                j = j + 1
                mag = content[key+i+1]
                magnetic[j] = mag[-7:-1]

            count = 0
            _sum = 0
            for i in range(1,len(magnetic)):
                count += 1
                _sum += float(magnetic[i])
            magnetic_O = _sum/count
            if (model == 'Li2MnSnO3'):
                mag = content[key+x+y+1]
                magnetic_Sn = mag[-6:-1]
                results[q][2]=magnetic_Sn
                results[q][3]= magnetic_O
            else:
                results[q][2]= magnetic_O  

        except:
            pass


    ## HSE06
        try:
            directory=os.path.join(dir,"conf_"+str(conf), 'hse') # <--- Specify U-vaule (last number) or dir for SCAN and HSE06
            os.chdir(directory)

            i = 0
            free_energy_form_different_U_values={}
            with open('OUTCAR','r') as searchfile:
                content = searchfile.readlines()

            with open('OUTCAR','r') as searchfile:
                for line in searchfile:
                        i = i + 1
                        if '# of ion       s       p       d       tot' in line:
                            free_energy_form_different_U_values[i]=line
            free_energy_form_different_U_values

            key = sorted(free_energy_form_different_U_values.keys())[-1]

            s = pmg.Structure.from_file('POSCAR')
            if (model == 'Li2MnSnO3'):
                a=s.formula
                x = int(a[2])
                y = int(a[6:8])
                z = int(a[-2:])
            else:
                a=s.formula
                x = int(a[2])
                y = int(a[6])
                z = int(a[-1:])
            # Calculates the avarage magnetic moment on the second element
            j = 0
            a = 0
            magnetic={}
            for i in range(x,y+x):
                j = j + 1
                mag = content[key+i+1]
                magnetic[j] = mag[-6:-1]

            count = 0
            _sum = 0
            for i in range(1,len(magnetic)):
                count += 1
                _sum += float(magnetic[i])
            magnetic_Mn = _sum/count
            results[q+1][1]= magnetic_Mn

            # Calculates the avarage magnetic moment on the third element
            j = 0
            a = 0
            magnetic={}
            for i in range(y+x,y+x+z+1):
                j = j + 1
                mag = content[key+i+1]
                magnetic[j] = mag[-7:-1]

            count = 0
            _sum = 0
            for i in range(1,len(magnetic)):
                count += 1
                _sum += float(magnetic[i])
            magnetic_O = _sum/count
            results[q+1][2]= magnetic_O
            if (model == 'Li2MnSnO3'):
                mag = content[key+x+y+1]
                magnetic_Sn = mag[-6:-1]
                results[q+1][2]=magnetic_Sn
                results[q+1][3]= magnetic_O
            else:
                results[q+1][3]= magnetic_O
        except:
            pass
        
        
    elif functional_list == ("pbeU", "scan"):
        try:
            if (len(U_value)>1):
                values = U_value
                h=len(values)+1
                if (model == 'Li2MnSnO3'):
                    w=4
                else:
                    w=3
                results = [[0 for x in range(w)] for y in range(h)] 
                results_test = [[0 for x in range(w)] for y in range(h)] 

        except:
            values = [U_value]
            h=1+1
            if (model == 'Li2MnSnO3'):
                w=4
            else:
                w=3
            results = [[0 for x in range(w)] for y in range(h)] 
            results_test = [[0 for x in range(w)] for y in range(h)]
            
        #pbeU   
        q = 0
        p = 0
        for i in values:
            results[p][0] = i
            results_test[p][0] = i
            p = p + 1


        for u in values:
            directory=os.path.join(dir,"conf_"+str(conf), 'pbeU',str(u)) # <--- Specify U-vaule (last number) or dir for SCAN and HSE06
            os.chdir(directory)

            i = 0
            free_energy_form_different_U_values={}
            with open('OUTCAR','r') as searchfile:
                content = searchfile.readlines()
            with open('OUTCAR','r') as searchfile:
                for line in searchfile:
                        i = i + 1
                        if '# of ion       s       p       d       tot' in line:
                            free_energy_form_different_U_values[i]=line
            free_energy_form_different_U_values


            key = sorted(free_energy_form_different_U_values.keys())[-1]

            s = pmg.Structure.from_file('POSCAR')
            if (model == 'Li2MnSnO3'):
                a=s.formula
                x = int(a[2])
                y = int(a[6:8])
                z = int(a[-2:])
            else:
                a=s.formula
                x = int(a[2])
                y = int(a[6])
                z = int(a[-1:])

        # Calculates the avarage magnetic moment on the second element
            j = 0
            a = 0
            magnetic={}
            for i in range(x,y+x):
                j = j + 1
                mag = content[key+i+1]
                magnetic[j] = mag[-6:-1]

            count = 0
            _sum = 0
            for i in range(1,len(magnetic)):
                count += 1
                _sum += float(magnetic[i])
                magnetic_Mn = _sum/count
            results[q][1]= magnetic_Mn

        # Calculates the avarage magnetic moment on the third element
            j = 0
            a = 0
            magnetic={}
            for i in range(y+x,y+x+z+1):
                j = j + 1
                mag = content[key+i+1]
                magnetic[j] = mag[-7:-1]

            count = 0
            _sum = 0
            for i in range(1,len(magnetic)):
                count += 1
                _sum += float(magnetic[i])
            magnetic_O = _sum/count
            if (model == 'Li2MnSnO3'):
                mag = content[key+x+y+1]
                magnetic_Sn = mag[-6:-1]
                results[q][2]= magnetic_Sn
                results[q][3]= magnetic_O
            else:
                results[q][2]= magnetic_O
            q = q + 1


    ## SCAN
        try:
            directory=os.path.join(dir,"conf_"+str(conf), 'scan') # <--- Specify U-vaule (last number) or dir for SCAN and HSE06
            os.chdir(directory)

            i = 0
            free_energy_form_different_U_values={}
            with open('OUTCAR','r') as searchfile:
                content = searchfile.readlines()

            with open('OUTCAR','r') as searchfile:
                for line in searchfile:
                        i = i + 1
                        if '# of ion       s       p       d       tot' in line:
                            free_energy_form_different_U_values[i]=line
            free_energy_form_different_U_values

            key = sorted(free_energy_form_different_U_values.keys())[-1]

            s = pmg.Structure.from_file('POSCAR')
            if (model == 'Li2MnSnO3'):
                a=s.formula
                x = int(a[2])
                y = int(a[6:8])
                z = int(a[-2:])
            else:
                a=s.formula
                x = int(a[2])
                y = int(a[6])
                z = int(a[-1:])

            # Calculates the avarage magnetic moment on the second element
            j = 0
            a = 0
            magnetic={}
            for i in range(x,y+x):
                j = j + 1
                mag = content[key+i+1]
                magnetic[j] = mag[-6:-1]

            count = 0
            _sum = 0
            for i in range(1,len(magnetic)):
                count += 1
                _sum += float(magnetic[i])
            magnetic_Mn = _sum/count
            results[q][1]= magnetic_Mn

            # Calculates the avarage magnetic moment on the third element
            j = 0
            a = 0
            magnetic={}
            for i in range(y+x,y+x+z+1):
                j = j + 1
                mag = content[key+i+1]
                magnetic[j] = mag[-7:-1]

            count = 0
            _sum = 0
            for i in range(1,len(magnetic)):
                count += 1
                _sum += float(magnetic[i])
            magnetic_O = _sum/count
            if (model == 'Li2MnSnO3'):
                mag = content[key+x+y+1]
                magnetic_Sn = mag[-6:-1]
                results[q][2]= magnetic_Sn
                results[q][3]= magnetic_O
            else:
                results[q][2]= magnetic_O 

        except:
            pass
        
    if model == 'Li2MnO3':
        header = ("U-value (eV)", 'Mn (\mu_B)', 'O (\mu_B)')
    elif model == 'Li2IrO3':
        header = ("U-value (eV)", 'Ir (\mu_B)', 'O (\mu_B)')
    elif model == 'Li2MnSnO3':
        header = ("U-value (eV)", 'Mn (\mu_B)', 'Sn (\mu_B)', 'O (\mu_B)')
        
    #return (tabulate(results, headers=header, tablefmt="latex", floatfmt=".2f"),results)
    return (header,results)
