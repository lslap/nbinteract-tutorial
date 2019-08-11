
from voltage import voltage
from energy_check import energy_check
from conf_checker import conf_checker
import matplotlib.pyplot as plt


def voltage_visualization(model,structure,li_concentration,functional_list,U_value,conf,configuration):
    fig=plt.figure()
    ax = plt.subplot(111)

    if (configuration == True):
        configurations=conf_checker(model,li_concentration,structure)
    else:
        configurations=[conf]

    try:
        if (len(U_value)>1):
            values = U_value    
    except:
        values = [U_value]

    if (configuration == True):
        w=len(values)
        h=len(configurations)
        plot = [[0 for x in range(w)] for y in range(h)] 
        q = 0
        p = 0
        for j in configurations:
            for i in values:
                [header,result]=voltage(model,structure,li_concentration,functional_list,i,j,configuration)
                plot[p][q]=result[0][1]
                q = q + 1
            q = 0
            p = p + 1

        for j in configurations:
            i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
            plt.plot(i,plot[j],label='Conf_'+str(j),linestyle='--',marker='o')
    else:
        plot = [0] * len(values)
        q=0
        for i in values:
            [header,result]=voltage(model,structure,li_concentration,functional_list,i,conf,configuration)
            plot[q]=result[0][1]
            q = q + 1   

        i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        plt.plot(i,plot,label='Conf_'+str(conf),linestyle='--',marker='o')


    ax.legend()    
    my_xticks = (0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 3.9, 4, 4.5, 5, 5.5, 6)
    i = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    plt.xticks(i, my_xticks)
    plt.xlabel('U-value (eV)')
    plt.ylabel('Voltage (V)')
    plt.title('Voltage for different configurations and U-values')
    plt.show()