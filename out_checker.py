# Function to check the out file. A 1 indicates that the senctence 
# reached required accuracy - stopping structural energy minimisation' is present in the out file.

import os
from conf_checker import conf_checker

def out_checker(model,li_concentration,structure,functional_list,U_value,conf,configuration):
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
        values = ([U_value])

    if (configuration == True):
        configurations=conf_checker(model,li_concentration,structure)
    else:
        configurations=[conf]



    if functional_list == 'pbeU':
        h=len(values)+1
        w=len(configurations)+1
        output = [[0 for x in range(w)] for y in range(h)] 
        q = 1
        p = 1
        for x in configurations:
            for i in values:
                directory=os.path.join(dir,"conf_"+str(x), 'pbeU',str(i))
                os.chdir(directory)
                with open('out', 'r') as searchfile:
                    for line in searchfile:
                        if 'reached required accuracy - stopping structural energy minimisation' in line:
                            output[p][q]=1
                            output[p][0]=values[p-1]
                p = p + 1
            p = 1
            output[0][q]=q-1
            q = q + 1

    elif functional_list == 'scan':
        try:
            h=2
            w=len(configurations)+1
            output = [[0 for x in range(w)] for y in range(h)] 
            q = 1
            for x in configurations:
                directory=os.path.join(dir,"conf_"+str(x), 'scan')
                os.chdir(directory)
                with open('out', 'r') as searchfile:
                    for line in searchfile:
                        if 'reached required accuracy - stopping structural energy minimisation' in line:
                            output[1][q]=1
                            output[0][q]=x
                q = q + 1
        except:
            output = 'No SCAN calculation.'

    elif functional_list == 'hse':
        try:
            h=2
            w=len(configurations)+1
            output = [[0 for x in range(w)] for y in range(h)] 
            q = 1
            for x in configurations:
                directory=os.path.join(dir,"conf_"+str(x), 'hse')
                os.chdir(directory)
                with open('out', 'r') as searchfile:
                    for line in searchfile:
                        if 'reached required accuracy - stopping structural energy minimisation' in line:
                            output[1][q]=1
                            output[0][q]=x
                q = q + 1
        except:
            output = 'No HSE calculation.'

    elif functional_list == ("pbeU", "scan" , "hse"):
        #pbeU
        h=len(values)+3
        w=len(configurations)+1
        output = [[0 for x in range(w)] for y in range(h)] 
        q = 1
        p = 1
        for x in configurations:
            for i in values:
                directory=os.path.join(dir,"conf_"+str(x), 'pbeU',str(i))
                os.chdir(directory)
                with open('out', 'r') as searchfile:
                    for line in searchfile:
                        if 'reached required accuracy - stopping structural energy minimisation' in line:
                            output[p][q]=1
                            output[p][0]=values[p-1]
                p = p + 1
            p = 1
            output[0][q]=q-1
            q = q + 1

        #scan
        try: 
            q = 1
            for x in configurations:
                directory=os.path.join(dir,"conf_"+str(x), 'scan')
                os.chdir(directory)
                with open('out', 'r') as searchfile:
                    for line in searchfile:
                        if 'reached required accuracy - stopping structural energy minimisation' in line:
                            output[len(values)+1][q]=1
                q = q + 1

        except:
            pass

        #hse
        try:
            q = 0
            for x in configurations:
                directory=os.path.join(dir,"conf_"+str(x), 'hse')
                os.chdir(directory)
                with open('out', 'r') as searchfile:
                    for line in searchfile:
                        if 'reached required accuracy - stopping structural energy minimisation' in line:
                            output[len(values)+2][q]=1
                q = q + 1
        except:
            pass
    
    
    elif functional_list == ("pbeU", "scan"):
        #pbeU
        h=len(values)+2
        w=len(configurations)+1
        output = [[0 for x in range(w)] for y in range(h)] 
        q = 1
        p = 1
        for x in configurations:
            for i in values:
                directory=os.path.join(dir,"conf_"+str(x), 'pbeU',str(i))
                os.chdir(directory)
                with open('out', 'r') as searchfile:
                    for line in searchfile:
                        if 'reached required accuracy - stopping structural energy minimisation' in line:
                            output[p][q]=1
                            output[p][0]=values[p-1]
                p = p + 1
            p = 1
            output[0][q]=q-1
            q = q + 1

        #scan
        try: 
            q = 1
            for x in configurations:
                directory=os.path.join(dir,"conf_"+str(x), 'scan')
                os.chdir(directory)
                with open('out', 'r') as searchfile:
                    for line in searchfile:
                        if 'reached required accuracy - stopping structural energy minimisation' in line:
                            output[len(values)+1][q]=1
                q = q + 1

        except:
            pass
        
        
    return output
