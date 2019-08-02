import sys
import webbrowser
from math import ceil
from ind_inveted import Index_inverted

args = sys.argv[1:]

index = Index_inverted()

index.read_index(args[0])
index.read_file1()
a = ' '
op = '1'
page = 0
while(not a == ''):
    a = input("insira a consulta: ")
    if (a == ''): break
    r = index.busca(a)
    d = 0
    n = 5
    op = '1'
    page = 0
    flag = 0
    if(len(r)<5): n = len(r)
    while(not op == ''):
        if (op == '1' and flag == 0):
            if((len(r) - d) < 5): 
            	n = len(r)
            	flag = 1

            for i in range(d,n):
                print('\n{} - {}'.format(i+1,r[i]))
            d = d + 5
            n = n + 5
            page = page + 1

        if (op == '2'):
            i = int(input('\nposicao ---->>>>> '))
            webbrowser.open(r[i-1].get_path())

        print('\nPAGINA {} de {}\n'.format(page,ceil(len(r)/5)))
        print('\n{} Arquivos de resultado da consulta\n'.format(len(r)))

        if(flag == 0):
        	op = input("\n\t1 - Mostrar as proximas 5 recuperações. \n\t2 - Mostrar o Mth documento recuperado.\n\n")
        else:
        	op = input("\n\t2 - Mostrar o Mth documento recuperado.\n\t3 - voltar ao topo\n\n")
        	if (op == '3'):
        		op = 1
        		n = 5
        		d = 0
        		flag = 0
        		page = 0

print('\n\n\t>>>>>>>>>>>>>>>>>>>> COMPLETE <<<<<<<<<<<<<<<<<<<<\n\n')        
