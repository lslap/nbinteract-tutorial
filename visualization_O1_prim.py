# This function will determine which direcotry('s) will be looked at.
import os

def visualization_O1_prim(model,li_concentration,structure,conf,functional_list,U_value):

    
    if (model == 'Li2MnO3'):
        dir = os.path.join('/scratch/antwerpen/204/vsc20412',model,model[0:2]+li_concentration+model[3:],structure)
    elif (model == 'Li2IrO3'):
        dir = os.path.join('/scratch/antwerpen/204/vsc20412',model,model[0:2]+li_concentration+model[3:])
    elif (model == 'Li2MnSnO3'):
        dir = os.path.join('/scratch/antwerpen/204/vsc20412',model,'Li'+li_concentration)

    directory=os.path.join(dir,"conf_"+str(conf), 'pbeU',str(U_value)) # <--- Specify U-vaule (last number) or dir for SCAN and HSE06   
    fig=plt.figure()
    ax = plt.subplot(111)
    if functional_list == 'pbeU':
        try:
            if (len(U_value)>1):
                values = U_value    
        except:
            values = [U_value]

        #fig=plt.figure()
        #ax = plt.subplot(111)

        if (configuration == True):
            configurations=conf_checker(model,li_concentration,structure)
            if len(configurations) > 10:
                configurations = configurations[0:-1]

            w=14
            h=len(configurations)
            energy = [[0 for x in range(w)] for y in range(h)] 

            try:
                for j in range(0,len(configurations)):
                    q=0
                    for a in values:
                        directory=os.path.join(dir,"conf_"+str(j), 'pbeU',str(a))
                        os.chdir(directory)
                        with open('OUTCAR', 'r') as searchfile:
                            for line in searchfile:
                                if 'free  en' in line:
                                    try:
                                        if float(line[-len(values)-3:-10]) > -100:
                                            energy[j][q]=float(line[-len(values)-3:-9])
                                        else:
                                            energy[j][q]=float(line[-len(values)-3:-10])
                                    except:
                                        if float(line[-len(values)-3:-10]) > -100:
                                            energy[j][q]=float(line[-16:-10])
                                        else:
                                            energy[j][q]=float(line[-17:-10])
                        q = q + 1
            except:
                pass
    
            if (energy_baseline == 'Absolute'):
                energy_new = energy
            elif (energy_baseline == 'Minimum'):
                w=14
                h=len(configurations)
                energy_new = [[0 for x in range(w)] for y in range(h)] 
                energy_min=[0] * h
                energy_min_label = [0] * len(values)

                for j in range(0,len(values)):
                    energy_min=[0] * h
                    for i in range (0,len(configurations)):
                        energy_min[i]=energy[i][j]
                    energy_min_label[j] = min(energy_min)

                for j in range(0,h):
                    for i in range (0,len(values)):
                        energy_new[j][i] = float(energy[j][i]) - float(energy_min_label[i])
                
            elif (energy_baseline == 'Discharged'):
                w=14
                h=len(configurations)
                energy_new = [[0 for x in range(w)] for y in range(h)] 
                energy_min=[0] * h
                energy_min_label = [0] * len(values)
                
                baseline = baseline_energy(model,li_concentration,structure,functional_list,U_value,conf)
                for j in range(0,len(values)):
                    for i in range (0,len(configurations)):
                        energy_new[i][j] = energy[i][j]-baseline[j]
                        #energy_new[i][j] = energy[i][j]-baseline_energy(model,li_concentration,structure,U_value,conf)[j]

            for x in range(0,len(configurations)):
                i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
                ax.plot(i, energy_new[x], label='Conf_'+str(x),linestyle='--',marker='o')

            ax.legend()
            my_xticks = (0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 3.9, 4, 4.5, 5, 5.5, 6)
            plt.xticks(i, my_xticks)
            test = ax.legend(loc='upper center', bbox_to_anchor=(1.2, 1), shadow=True, ncol=1)
            plt.xlabel('U-value (eV)')
            plt.ylabel('Energy difference (eV)')
            plt.title('Energy difference for different configurations and U-values')
            plt.show()

        else:
            configurations=conf
            w=14
            energy = [0]*w
            energy_new = [0]*w

            try:
                q=0
                for a in values:
                    directory=os.path.join(dir,"conf_"+str(configurations), 'pbeU',str(a))
                    os.chdir(directory)
                    with open('OUTCAR', 'r') as searchfile:
                        for line in searchfile:
                            if 'free  en' in line:
                                try:
                                    if float(line[-len(values)-3:-10]) > -100:
                                        energy[q]=float(line[-len(values)-3:-9])
                                    else:
                                        energy[q]=float(line[-len(values)-3:-10])
                                except:
                                    if float(line[-len(values)-3:-10]) > -100:
                                        energy[q]=float(line[-16:-10])
                                    else:
                                        energy[q]=float(line[-17:-10])
                    q = q + 1  
                q=0
                energy_max=max(energy)
                for i in values:
                    energy_new[q]=float(energy_max)-float(energy[q])
                    q=q+1
                    
                if (energy_baseline == 'Absolute'):
                    energy_new = energy
                elif (energy_baseline == 'Minimum'):
                    q=0
                    energy_max=max(energy)
                    for i in values:
                        energy_new[q]=float(energy_max)-float(energy[q])
                        q=q+1

                elif (energy_baseline == 'Discharged'):
                    baseline = baseline_energy(model,li_concentration,structure,functional_list,U_value,conf)
                    q=0
                    for i in values:
                        energy_new[q]=float(energy[q])-float(baseline[q])
                        q=q+1 
            except:
                pass

            i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
            ax.plot(i, energy_new, label='Conf_'+str(configurations),linestyle='--',marker='o')

            ax.legend()
            my_xticks = (0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 3.9, 4, 4.5, 5, 5.5, 6)
            plt.xticks(i, my_xticks)
            test = ax.legend(loc='upper center', bbox_to_anchor=(1.2, 1), shadow=True, ncol=1)
            plt.xlabel('U-value (eV)')
            plt.ylabel('Energy difference (eV)')
            plt.title('Energy difference for configuration '+str(configurations)+' with different U-values')
            plt.show()

        os.chdir('/scratch/antwerpen/204/vsc20412/temp_files')
        fig.savefig("Test.pdf",bbox_inches='tight',pad_inches=1)
        
    elif functional_list == 'scan':
        if (configuration == True):
            configurations=conf_checker(model,li_concentration,structure)
            if len(configurations) > 10:
                configurations = configurations[0:-1]
        else:
            configurations=conf
                
        plotting = [0] * (len(configurations))
        plotting_new = [0] * (len(configurations))
        [header,energy] = energy_check(model,structure,li_concentration,functional_list,U_value,conf,configuration)
        q=1
        for i in configurations:
            plotting[i]=float(energy[0][i+1])
            q = q + 1
        
        if (energy_baseline == 'Absolute'):
            plotting_new = plotting
        elif (energy_baseline == 'Minimum'):
            plotting_max=max(plotting)
            for i in configurations:
                plotting_new[i]=plotting_max-plotting[i]

        elif (energy_baseline == 'Discharged'):
            baseline = baseline_energy(model,li_concentration,structure,functional_list,U_value,conf)
            for i in range (0,len(configurations)):
                plotting_new[i] = plotting[i]-baseline
                #energy_new[i][j] = energy[i][j]-baseline_energy(model,li_concentration,structure,U_value,conf)[j]

        plt.plot(configurations,plotting_new,linestyle='--',marker='o')
        my_xticks=()
        for i in configurations:
            a = tuple(['c_'+str(i)])
            my_xticks = my_xticks + a
        plt.xticks(configurations, my_xticks)
        plt.xlabel('Configurations')
        plt.ylabel('Energy difference (eV)')
        plt.title('Energy difference for configurations calculated with SCAN')
        plt.show()
    

    elif functional_list == 'hse':
        if (configuration == True):
            configurations=conf_checker(model,li_concentration,structure)
            if len(configurations) > 10:
                configurations = configurations[0:-1]
        else:
            configurations=conf
                
        plotting = [0] * (len(configurations))
        plotting_new = [0] * (len(configurations))
        [header,energy] = energy_check(model,structure,li_concentration,functional_list,U_value,conf,configuration)
        q=1
        for i in configurations:
            plotting[i]=float(energy[0][i+1])
            q = q + 1
        
        if (energy_baseline == 'Absolute'):
            plotting_new = plotting
        elif (energy_baseline == 'Minimum'):
            plotting_max=max(plotting)
            for i in configurations:
                plotting_new[i]=plotting_max-plotting[i]

        elif (energy_baseline == 'Discharged'):
            baseline = baseline_energy(model,li_concentration,structure,functional_list,U_value,conf)
            for i in range (0,len(configurations)):
                plotting_new[i] = plotting[i]-baseline
                #energy_new[i][j] = energy[i][j]-baseline_energy(model,li_conc
    
    
        plt.plot(configurations,plotting_new,linestyle='--',marker='o')
        my_xticks=()
        for i in configurations:
            a = tuple(['c_'+str(i)])
            my_xticks = my_xticks + a
        plt.xticks(configurations, my_xticks)
        plt.xlabel('Configurations')
        plt.ylabel('Energy difference (eV)')
        plt.title('Energy difference for configurations calculated with HSE06')
        plt.show()
        
    elif functional_list == ("pbeU", "scan" , "hse"):
        try:
            if (len(U_value)>1):
                values = U_value    
        except:
            values = [U_value]

        #fig=plt.figure()
        #ax = plt.subplot(111)

        if (configuration == True):
            configurations=conf_checker(model,li_concentration,structure)
            if len(configurations) > 10:
                configurations = configurations[0:-1]

            w=14
            h=len(configurations)
            energy = [[0 for x in range(w)] for y in range(h)] 

            try:
                for j in range(0,len(configurations)):
                    q=0
                    for a in values:
                        directory=os.path.join(dir,"conf_"+str(j), 'pbeU',str(a))
                        os.chdir(directory)
                        with open('OUTCAR', 'r') as searchfile:
                            for line in searchfile:
                                if 'free  en' in line:
                                    try:
                                        if float(line[-len(values)-3:-10]) > -100:
                                            energy[j][q]=float(line[-len(values)-3:-9])
                                        else:
                                            energy[j][q]=float(line[-len(values)-3:-10])
                                    except:
                                        if float(line[-len(values)-3:-10]) > -100:
                                            energy[j][q]=float(line[-16:-10])
                                        else:
                                            energy[j][q]=float(line[-17:-10])
                        q = q + 1
            except:
                pass
            #pbeu
            w=16
            h=len(configurations)
            energy_new = [[0 for x in range(w)] for y in range(h)] 
            energy_min=[0] * h
            energy_min_label = [0] * len(values)

            for j in range(0,len(values)):
                energy_min=[0] * h
                for i in range (0,len(configurations)):
                    energy_min[i]=energy[i][j]
                energy_min_label[j] = max(energy_min)

            for j in range(0,h):
                for i in range (0,len(values)):
                    energy_new[j][i] = float(energy[j][i]) - float(energy_min_label[i])
            
            #scan
            plotting = [0] * (len(configurations))
            plotting_new = [0] * (len(configurations))
            [header,energy] = energy_check(model,structure,li_concentration,functional_list,U_value,conf,configuration)
            q=1
            for i in configurations:
                plotting[i]=float(energy[-2][i+1])
                q = q + 1
            plotting_max=max(plotting)    
            for j in configurations:
                energy_new[j][-2]=plotting_max-plotting[j]
            
            #hse
            for i in configurations:
                plotting[i]=float(energy[-1][i+1])
                q = q + 1
            plotting_max=max(plotting)    
            for j in configurations:
                energy_new[j][-1]=plotting_max-plotting[j]
            
            
            
            for x in range(0,len(configurations)):
                i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14,15]
                ax.plot(i, energy_new[x], label='Conf_'+str(x),linestyle='--',marker='o')

            ax.legend()
            my_xticks = (0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 3.9, 4, 4.5, 5, 5.5, 6,'scan','hse')
            plt.xticks(i, my_xticks)
            test = ax.legend(loc='upper center', bbox_to_anchor=(1.2, 1), shadow=True, ncol=1)
            plt.xlabel('U-value (eV)')
            plt.ylabel('Energy difference (eV)')
            plt.title('Energy difference for different configurations and U-values')
            plt.show()
        
    elif functional_list == ("pbeU", "scan"):
        try:
            if (len(U_value)>1):
                values = U_value    
        except:
            values = [U_value]

        #fig=plt.figure()
        #ax = plt.subplot(111)

        if (configuration == True):
            configurations=conf_checker(model,li_concentration,structure)
            if len(configurations) > 10:
                configurations = configurations[0:-1]

            w=14
            h=len(configurations)
            energy = [[0 for x in range(w)] for y in range(h)] 

            try:
                for j in range(0,len(configurations)):
                    q=0
                    for a in values:
                        directory=os.path.join(dir,"conf_"+str(j), 'pbeU',str(a))
                        os.chdir(directory)
                        with open('OUTCAR', 'r') as searchfile:
                            for line in searchfile:
                                if 'free  en' in line:
                                    try:
                                        if float(line[-len(values)-3:-10]) > -100:
                                            energy[j][q]=float(line[-len(values)-3:-9])
                                        else:
                                            energy[j][q]=float(line[-len(values)-3:-10])
                                    except:
                                        if float(line[-len(values)-3:-10]) > -100:
                                            energy[j][q]=float(line[-16:-10])
                                        else:
                                            energy[j][q]=float(line[-17:-10])
                        q = q + 1
            except:
                pass
            
            #pbeu
            w=15
            h=len(configurations)
            energy_new = [[0 for x in range(w)] for y in range(h)] 
            energy_min=[0] * h
            energy_min_label = [0] * len(values)

            for j in range(0,len(values)):
                energy_min=[0] * h
                for i in range (0,len(configurations)):
                    energy_min[i]=energy[i][j]
                energy_min_label[j] = min(energy_min)

            for j in range(0,h):
                for i in range (0,len(values)):
                    energy_new[j][i] = float(energy[j][i]) - float(energy_min_label[i])
            
            #scan
            plotting = [0] * (len(configurations))
            plotting_new = [0] * (len(configurations))
            [header,energy] = energy_check(model,structure,li_concentration,functional_list,U_value,conf,configuration)
            q=1
            for i in configurations:
                plotting[i]=float(energy[-2][i+1])
                q = q + 1
            plotting_max=max(plotting)    
            for j in configurations:
                energy_new[j][-1]=plotting_max-plotting[j]
            
            for x in range(0,len(configurations)):
                i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,14]
                ax.plot(i, energy_new[x], label='Conf_'+str(x),linestyle='--',marker='o')

            ax.legend()
            my_xticks = (0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 3.9, 4, 4.5, 5, 5.5, 6,'scan')
            plt.xticks(i, my_xticks)
            test = ax.legend(loc='upper center', bbox_to_anchor=(1.2, 1), shadow=True, ncol=1)
            plt.xlabel('U-value (eV)')
            plt.ylabel('Energy difference (eV)')
            plt.title('Energy difference for different configurations and U-values')
            plt.show()

        else:
            print('This figure is only interesting for multiple configurations')
    
    os.chdir('/scratch/antwerpen/204/vsc20412/temp_files')
    fig.savefig("Test.pdf",bbox_inches='tight',pad_inches=1)
