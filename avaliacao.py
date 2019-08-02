import matplotlib.pyplot as plt
from indexer import read_docs,tratar_consulta,isEmpty
from ind_inveted import Index_inverted

def cobertura_precisao():

    ind = Index_inverted()
    ind.sref('/home/marcus/Dropbox/Semestre 2018.1/Recuperação da informação/Indice_invertido/avaliacao/arquivos/')
    xs = list()
    ys = list()
    hs = list()
    gs = list()
    ts = list()
    qs = list()
    m_precision = 0
    qtd = 0

    for query in read_docs('/home/marcus/Dropbox/Semestre 2018.1/Recuperação da informação/Indice_invertido/avaliacao/consultas_cfc/'):
        actualQuery, realAmount, realResult = tratar_consulta(query)
        resultado = ind.busca(actualQuery)
        precision, lastIndex, xs, ys, fMeasure = tratar_documentos(resultado, set(realResult))
        m_precision += precision
        #plotar_grafico(xs, ys)
        resultado = resultado[:lastIndex]

        print('\nBusca: '+actualQuery)
        print('qtd_origin: '+str(realAmount))
        print('qtd_return: '+str(len(resultado)))
        print('F-Measure: '+str(fMeasure))
        print('Precisao Media: '+str(precision))
        hs.append(qtd)
        gs.append(fMeasure)
        ts.append(qtd)
        qs.append(precision)
        qtd += 1
    print('media_precisao_media = ',m_precision/qtd)
    plotar_f(hs,gs)
    plotar_p(ts,qs)


def stemming_test():
    source_folder = '/home/marcus/Dropbox/Semestre 2018.1/Recuperação da informação/Indice_invertido/avaliacao/nosafe/'
    ind = Index_inverted()
    ind.sref('/home/marcus/Dropbox/Semestre 2018.1/Recuperação da informação/Indice_invertido/avaliacao/arquivos/')
    ind1 = Index_inverted()
    ind1.sref1('/home/marcus/Dropbox/Semestre 2018.1/Recuperação da informação/Indice_invertido/avaliacao/arquivos/')
    xs = list()
    ys = list()
    ts = list()
    qs = list()
    qtd = 0
    
    for query in read_docs(source_folder):
        nekis = None
        actualQuery, nekis, realResult = tratar_consulta(query)

        resultado = ind.busca(actualQuery)
        prec1, nekis, xs, ys, nekis = tratar_documentos(resultado, realResult[:])

        resultado1 = ind1.busca1(actualQuery)
        prec2, nekis, zs, ps, nekis = tratar_documentos(resultado1, realResult[:])
        qtd+=1

        plotar_grafico_stem(xs,ys,zs,ps)

        nekis = 'perdeu perdeu passa o lapis mlk !!!'


def interpola(x):
    result = x
    for i in range(0,len(x)):
        for j in range(i,len(x)):
            if x[i] < x[j]:
                result[i] = x[j]
    return result

def tratar_documentos(resultado, pos_rec):
    precision = 0
    pos_size = len(pos_rec)
    r_precisao = 0
    r_cob = 0
    xs = list()
    ys = list()
    for index, result in enumerate(resultado):
        if result in pos_rec:
            pos_rec.remove(result)
            index += 1
            precision += 1

            xs.append(precision/pos_size)
            ys.append(precision/index)

        if isEmpty(pos_rec): break
     
    for x in xs:
        r_precisao += x
    for y in ys:
        r_cob += y

    r_precisao = r_precisao/len(xs)
    r_cob = r_cob/len(ys)

    if r_precisao != 0 and r_cob != 0:
        f_measure = 2/((1/r_precisao) + (1/r_cob))

    return r_precisao, index, xs, ys, f_measure 

def plotar_grafico(x, y):
    plt.plot(x, y, linestyle='-', marker='o', color='green')
    plt.title('Cobertura/Precisao') 
    plt.xlabel('cobertura')
    plt.ylabel('precisão')
    plt.show()
def plotar_grafico_stem_p(x, y,z,k):
    plt.plot(x, y, linestyle='-', marker='', color='green',label='Stem')
    plt.plot(z, k, linestyle='-', marker='', color='red',label='noStem')
    plt.title('Stem/notStem')    
    plt.xlabel('Consultas')
    plt.ylabel('Precisão')
    plt.legend(loc='right')
    plt.show()
def plotar_grafico_stem(x, y,z,k):
    plt.plot(x, y, linestyle='-', marker='', color='green',label='Stem')
    plt.plot(z, k, linestyle='-', marker='', color='red',label='noStem')
    plt.title('Stem/notStem')    
    plt.xlabel('cobertura')
    plt.ylabel('precisão')
    plt.legend(loc='right')
    plt.show()
def plotar_f(x,y):
    plt.plot(x, y, linestyle='-', marker='o', color='green')
    plt.title('Medida F') 
    plt.xlabel('Consultas')
    plt.ylabel('F-measure')
    plt.show()
def plotar_p(x,y):
    plt.plot(x, y, linestyle='-', marker='o', color='green')
    plt.title('Media Precisao') 
    plt.xlabel('Consultas')
    plt.ylabel('Precisao')
    plt.show()

if __name__== '__main__':
    cobertura_precisao()
    #stemming_test()