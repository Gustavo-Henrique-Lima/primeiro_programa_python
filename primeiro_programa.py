from tkinter.constants import E
from PySimpleGUI import PySimpleGUI as sg 
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import BUTTON_TYPE_REALTIME, Button, WINDOW_CLOSED, Window, popup
##Variáveis
pontos=0
acerto=0
erro=0
##Definindo Janelas
def janela_apresentacao0():
    sg.theme('Reddit')
    layout =[
        [sg.Text('Olá e bem-vindo, temos algumas instruções para você, portanto leia com atenção:')],
        [sg.Text('1-O simulado é composto por 10 questões;')],
        [sg.Text('2-Você só pode escolher uma matéria por vez;')],
        [sg.Text('3-Não há tempo para responder as perguntas, mas uma vez respondida não é possivel voltar atrás;')],
        [sg.Text('4-Todas as questões foram retiradas de concursos anteriores organizados pela banca CESPE/CEBRASPE.')],
        [sg.Button('Avançar')]
    ]
    return sg.Window('Bem-Vindo', layout=layout,finalize=True)
def janela_apresentacao():
    sg.theme('Reddit')
    layout =[
        [sg.Text('5-O aplicativo segue todos os critérios da banca para avaliar o resultado final ou seja;')],
        [sg.Text('6-Cada questão errada anula uma certo;')],
        [sg.Text('7-Por fim, a cada questão respondida você terá o retorno de acerto ou erro! E no final das 10 questões será mostrando sua pontuação final.')],
        [sg.Text('Pronto? Vamos lá, escolha a matéria.')],
        [sg.Button('Direito Penal') ,sg.Button('Direito Constitucional')]
    ]
    return sg.Window('Entrada', layout=layout,finalize=True)
##Questões somente de PENAL
def janela_questaoP():
    sg.theme('Reddit')
    layout = [
        [sg.Text('2021 - TCE/RJ - Analista de Controle Externo\nCom relação ao direito penal, julgue o item a seguir.\nO crime de concussão se consuma com a obtenção da vantagem indevida pelo servidor público.')],
        [sg.Button('Certo'), sg.Button('Errado')]
    ]
    return sg.Window('Direito penal 1 de 10', layout=layout,finalize=True)
def janela_questao1P():
    sg.theme('Reddit')
    layout = [
        [sg.Text('2021 - TCE/RJ - Analista de Controle Externo\nCom relação ao direito penal, julgue o item a seguir.\nA oposição manifestada pelo indivíduo, mediante resistência passiva, sem o uso da violência\ncontra ordem emanada por autoridades policiais que pretendessem levá-lo à delegacia, sem que houvesse flagrante, é suficiente para caracterizar o delito de resistência.')],
        [sg.Button('Errado'),sg.Button('Certo')]
    ]
    return sg.Window('Direito penal 2 de 10', layout=layout,finalize=True)
def janela_questao2P():
    sg.theme('Reddit')
    layout = [
        [sg.Text('2021 - CODEVASF - Assessor Jurídico\nCom relação ao direito penal, julgue o item a seguir.\nFuncionário público que exija para si vantagem indevida para realizar ato de ofício pratica o crime de corrupção passiva.')],
        [sg.Button('Errado'),sg.Button('Certo')]
        ]
    return sg.Window('Direito penal 3 de 10', layout=layout,finalize=True)
def janela_questao3P():
    sg.theme('Reddit')
    layout = [
        [sg.Text('2021 - PF- Escrivão de Polícia Federal\nCom relação ao direito penal e ao direito processual penal, julgue o item que se segue.\nA consumação do delito de descaminho independe do esgotamento da via administrativa.')],
        [sg.Button('Certo'),sg.Button('Errado')]
        ]
    return sg.Window('Direito penal 4 de 10', layout=layout,finalize=True)
def janela_questao4P():
    sg.theme('Reddit')
    layout = [
        [sg.Text('2021 - Polícia Federal - Delegado de Polícia Federal\nCom base na Lei n.º 7.492/1986, que diz respeito aos crimes contra o Sistema Financeiro Nacional, e na Lei n.º 8.137/1990, que se refere aos crimes contra a ordem econômica, tributária e as relações de consumo,\njulgue o item que se segue\nA Súmula Vinculante n.º 24 do STF — que dispõe que não se tipifica crime material contra a ordem tributária, conforme previsto no art. 1.º, incisos I a IV, da Lei n.º 8.137/1990,\nantes do lançamento definitivo do tributo — não pode ser aplicada a fatos anteriores a sua edição.')],
        [sg.Button('Certo'),sg.Button('Errado')]
        ]
    return sg.Window('Direito penal 5 de 10', layout=layout,finalize=True)
def janela_questao5P():
    sg.theme('Reddit')
    layout = [
        [sg.Text('2021 - Polícia Federal - Delegado de Polícia Federal\nCom base na Lei n.º 7.492/1986, que diz respeito aos crimes contra o Sistema Financeiro Nacional, e na Lei n.º 8.137/1990, que se refere aos crimes contra a ordem econômica, tributária e as relações de consumo,\njulgue o item que se segue\nOs crimes contra a ordem tributária, a ordem econômica e as relações de consumo previstos na Lei n.º 8.137/1990 submetem-se à ação penal pública incondicionada.')],
        [sg.Button('Errado'),sg.Button('Certo')]
        ]
    return sg.Window('Direito penal 6 de 10', layout=layout,finalize=True)
def janela_questao6P():
    sg.theme('Reddit')
    layout = [
        [sg.Text('2011 -AL-CE- Analista Legislativo\nA respeito de crimes, penas, prazos e aplicação da lei penal, julgue o item a seguir.\nCaso um indivíduo pratique furto sem violência à pessoa e restitua, voluntariamente, o objeto furtado antes do recebimento da denúncia, sua pena, em caso de condenação, será reduzida de um a dois terços.')],
        [sg.Button('Certo'),sg.Button('Errado')]
        ]
    return sg.Window('Direito penal 7 de 10', layout=layout,finalize=True)
def janela_questao7P():
    sg.theme('Reddit')
    layout = [
        [sg.Text('2021 -TCE-RJ-Analista de Controle Externo\nConsiderando aspectos gerais do direito penal brasileiro, julgue o item subsecutivo.\nNos crimes de falsidade documental, a prescrição só começa a correr na data em que o fato tenha-se tornado conhecido.')],
        [sg.Button('Errado'),sg.Button('Certo')]
        ]
    return sg.Window('Direito penal 8 de 10', layout=layout,finalize=True)
def janela_questao8P():
    sg.theme('Reddit')
    layout = [
        [sg.Text('2015-DEPEN-Agente e Técnico\nJulgue o item subsequente, com relação às disposições da Lei de Execução Penal (LEP).\nPreso que praticar fato definido como crime, doloso ou culposo, ou falta grave deverá ser transferido para regime mais rigoroso.')],
        [sg.Button('Errado'),sg.Button('Certo')]
        ]
    return sg.Window('Direito penal 9 de 10', layout=layout,finalize=True)
def janela_questao9P():
    sg.theme('Reddit')
    layout = [
        [sg.Text('2014 -PC-DF-Escrivão de Polícia\nAcerca das características dos direitos humanos, julgue o próximo item.\nO crime de abuso de autoridade, por caracterizar uma violação aos direitos humanos, é imprescritível.')],
        [sg.Button('Certo'),sg.Button('Errado')]
        ]
    return sg.Window('Direito penal 10 de 10', layout=layout,finalize=True)
##Questões de CONSTITUCIONAL
def janela_questaoC():
    sg.theme('Reddit')
    layout = [
        [sg.Text(' 2021 -PF-Escrivão de Polícia Federal\nA polícia foi acionada para atender a um chamado de suspeita de ocorrência de tráfico ilícito de entorpecentes no interior de determinada sociedade de economia mista federal.\nAo chegar ao local, os policiais verificaram que um dos traficantes era um brasileiro naturalizado.\nConsiderando essa situação hipotética, julgue o item subsecutivo.\nO tráfico ilícito de entorpecentes é crime inafiançável.')],
        [sg.Button('Errado'), sg.Button('Certo')]
    ]
    return sg.Window('Direito Constitucional 1 de 10', layout=layout,finalize=True)
def janela_questao1C():
    sg.theme('Reddit')
    layout = [
        [sg.Text('2021 -PF-Delegado de Polícia Federal\nCom base no texto da CF e nos princípios e nas normas do direito financeiro, julgue o item a seguir\nA possibilidade de a emenda parlamentar impositiva alocar recursos a estados e municípios, por meio da transferência especial constitucional, a qual permite o repasse direto sem convênio,\nsó é cabível no caso de emenda individual, e não de emenda de bancada.')],
        [sg.Button('Certo'), sg.Button('Errado')]
    ]
    return sg.Window('Direito Constitucional 2 de 10', layout=layout,finalize=True)
def janela_questao2C():
    sg.theme('Reddit')
    layout = [
        [sg.Text('2021 - ANM - Técnico em Segurança de Barragens\nNo que diz respeito aos direitos e às garantias fundamentais, bem como aos direitos do servidor público, assegurados na Constituição Federal de 1988, julgue o item a seguir.\nAs práticas de tortura e de racismo são consideradas crimes inafiançáveis, porém, entre esses dois, apenas o crime de tortura deve ser considerado, pela lei, insuscetível de graça ou de anistia.')],
        [sg.Button('Certo'), sg.Button('Errado')]
    ]
    return sg.Window('Direito Constitucional 3 de 10', layout=layout,finalize=True)
def janela_questao3C():
    sg.theme('Reddit')
    layout = [
        [sg.Text('2021 - Polícia Federal - Delegado de Polícia Federal\nCom base no disposto na Constituição Federal de 1988 (CF), julgue o item subsequente\nCabe originariamente ao STF processar e julgar habeas data contra ato de ministro de estado.')],
        [sg.Button('Errado'), sg.Button('Certo')]
    ]
    return sg.Window('Direito Constitucional 4 de 10', layout=layout,finalize=True)
def janela_questao4C():
    sg.theme('Reddit')
    layout = [
        [sg.Text('2021 - TC-DF - Procurador\nCom relação às modalidades de intervenção do Estado na ordem econômica, julgue o item subsequente.\nAs alíquotas das contribuições de intervenção no domínio econômico relativas às atividades de comercialização do petróleo e seus derivados não poderão ser diferenciadas por produto ou uso.')],
        [sg.Button('Certo'), sg.Button('Errado')]
    ]
    return sg.Window('Direito Constitucional 5 de 10', layout=layout,finalize=True)
def janela_questao5C():
    sg.theme('Reddit')
    layout = [
        [sg.Text('2011 -AL-CE-Analista Legislativo\nA respeito dos direitos e garantias fundamentais, julgue o item subsequente.\nO brasileiro naturalizado pode ser eleito senador,\nmas não poderá ocupar o cargo de presidente do Senado, privativo de brasileiro nato.')],
        [sg.Button('Errado'), sg.Button('Certo')]
    ]
    return sg.Window('Direito Constitucional 6 de 10', layout=layout,finalize=True)
def janela_questao6C():
    sg.theme('Reddit')
    layout = [
        [sg.Text('2021 -PRF-Policial Rodoviário Federal\nÀ luz da Constituição Federal de 1988 (CF), do Pacto de São José da Costa Rica e do entendimento do Supremo Tribunal Federal,\njulgue o item que se segue, relativo aos direitos humanos.\nO aviso prévio é uma condicionante ao exercício do direito de reunião previsto na CF:\na inexistência de notificação às autoridades competentes torna ilegal a manifestação coletiva.')],
        [sg.Button('Certo'), sg.Button('Errado')]
    ]
    return sg.Window('Direito Constitucional 7 de 10', layout=layout,finalize=True)
def janela_questao7C():
    sg.theme('Reddit')
    layout = [
        [sg.Text('2021 -TCE-RJ-Analista de Controle Externo\nAcerca do Sistema Tributário Nacional, julgue o item que se segue.\nÉ compatível com a Constituição Federal de 1988 a cobrança de taxa municipal em virtude do serviço\nde combate a incêndios prestado pelo Corpo de Bombeiros Militar.')],
        [sg.Button('Errado'), sg.Button('Certo')]
    ]
    return sg.Window('Direito Constitucional 8 de 10', layout=layout,finalize=True)
def janela_questao8C():
    sg.theme('Reddit')
    layout = [
        [sg.Text('2021 -PRF-Policial Rodoviário Federal\nAcerca de direitos fundamentais, garantias e remédios constitucionais, julgue o item a seguir.\nA Constituição Federal de 1988 não garante o direito à escusa de consciência sobre o dever de votar para os maiores de 18 anos de idade\ne para os menores de 70 anos de idade.')],
        [sg.Button('Errado'), sg.Button('Certo')]
    ]
    return sg.Window('Direito Constitucional 9 de 10', layout=layout,finalize=True)
def janela_questao9C():
    sg.theme('Reddit')
    layout = [
        [sg.Text('2018 -PF-Agente de Polícia Federal\nCom relação à segurança pública e à atuação da Polícia Federal, julgue o item seguinte.\nCompete à Polícia Federal exercer, com exclusividade, as funções de polícia judiciária da União.')],
        [sg.Button('Certo'), sg.Button('Errado')]
    ]
    return sg.Window('Direito Constitucional 10 de 10', layout=layout,finalize=True)
#Criando Janelas
janela100,janela1,janela2,janela13,janela14,janela15,janela16,janela17,janela18,janela19,janela20,janela21= janela_apresentacao0(),None,None,None,None,None,None,None,None,None,None,None
janela3,janela4,janela5,janela6,janela7,janela8,janela9,janela10,janela11,janela12= None,None,None,None,None,None,None,None,None,None
#Loop
while True:
    window,event,values = sg.read_all_windows()
    if window==janela100 and event==sg.WINDOW_CLOSED:
        break
    if window==janela100 and event=='Avançar':
        janela1=janela_apresentacao()
        janela100.hide()
    if window==janela1 and event==sg.WINDOW_CLOSED:
        break
    if window== janela1 and event == 'Direito Constitucional':
        janela2=janela_questaoC()
        janela1.hide()
    if window == janela2 and event == sg.WINDOW_CLOSED:
        break
    if window == janela2 and event=='Certo':
        acerto+=1
        sg.popup('Você acertou!\nComentário:\nConstitui crimes inafiançáveis\nTráfico de drogas, tortura, terrorismo, crimes hediondos, racismo, ação de grupos armados.')
        janela13=janela_questao1C()
        janela2.hide()
    elif window==janela2 and event=='Errado':
        erro+=1
        sg.popup('Você errou!\nComentário:\nConstitui crimes inafiançáveis\nTráfico de drogas, tortura, terrorismo, crimes hediondos, racismo, ação de grupos armados.')
        janela13=janela_questao1C()
        janela2.hide()
    if window==janela13 and event==sg.WINDOW_CLOSED:
        break
    if window==janela13 and event=='Certo':
        acerto+=1
        sg.popup('Você acertou!\nComentário:\nArt. 166-A. As emendas individuais impositivas apresentadas ao projeto de lei orçamentária anual poderão alocar recursos a Estados, ao Distrito Federal e a Municípios por meio de:\nI - transferência especial; ou\nII - transferência com finalidade definida.')
        janela14=janela_questao2C()
        janela13.hide()
    elif window==janela13 and event=='Errado':
        erro+=1
        sg.popup('Você errou!\nComentário:\nArt. 166-A. As emendas individuais impositivas apresentadas ao projeto de lei orçamentária anual poderão alocar recursos a Estados, ao Distrito Federal e a Municípios por meio de:\nI - transferência especial; ou\nII - transferência com finalidade definida.')
        janela14=janela_questao2C()
        janela13.hide()
    if window==janela14 and event==sg.WINDOW_CLOSED:
        break
    if window==janela14 and event=='Certo':
         acerto+=1
         sg.popup('Você acertou!\nComentário:\nSão crimes inafiançáveis- Racismo, Ação de grupos armados, Tráfico, Tortura, Terrorismo e hediondos.')
         janela15=janela_questao3C()
         janela14.hide()
    elif window==janela14 and event=='Errado':
        erro+=1
        sg.popup('Você errou!\nComentário:\nSão crimes inafiançáveis- Racismo, Ação de grupos armados, Tráfico, Tortura, Terrorismo e hediondos.')
        janela15=janela_questao3C()
        janela14.hide()
    if window==janela15 and event==sg.WINDOW_CLOSED:
        break
    if window==janela15 and event=='Certo':
        erro+=1
        sg.popup('Você errou!\nComentário:\nSTJ - Julga originalmente - os mandados de segurança e os  habeas data  contra ato de Ministro de\nEstado, dos Comandantes da Marinha, do Exército e da Aeronáutica ou do próprio Tribunal;')
        janela16=janela_questao4C()
        janela15.hide()
    elif window==janela15 and event=='Errado':
        acerto+=1
        sg.popup('Você acertou!\nComentário:\nSTJ - Julga originalmente - os mandados de segurança e os  habeas data  contra ato de Ministro de\nEstado, dos Comandantes da Marinha, do Exército e da Aeronáutica ou do próprio Tribunal;')
        janela16=janela_questao4C()
        janela15.hide()
    if window==janela16 and event==sg.WINDOW_CLOSED:
        break
    if window==janela16 and event=='Certo':
        erro+=1
        sg.popup('Você errou!\nComentário:\nArt. 177, §4°, I - a alíquota da contribuição poderá ser:\na) diferenciada por produto ou uso;')
        janela17=janela_questao5C()
        janela16.hide()
    elif window==janela16 and event=='Errado':
        acerto+=1
        sg.popup('Você acertou!\nComentário:\nArt. 177, §4°, I - a alíquota da contribuição poderá ser:\na) diferenciada por produto ou uso;')
        janela17=janela_questao5C()
        janela16.hide()
    if window==janela17 and event==sg.WINDOW_CLOSED:
        break
    if window==janela17 and event=='Certo':
        acerto+=1
        sg.popup('Você acertou!\nComentário:\nCargos privativos de brasileiros natos: Ministro do Supremo Tribunal Federal;\nPresidente e Vice-Presidente da República;\nPresidente da Câmara dos Deputados;\nPresidente do Senado Federal;')
        janela18=janela_questao6C()
        janela17.hide()
    elif window==janela17 and event=='Errado':
        erro+=1
        sg.popup('Você errou!\nComentário:\nCargos privativos de brasileiros natos:\nMinistro do Supremo Tribunal Federal;\nPresidente e Vice-Presidente da República;\nPresidente da Câmara dos Deputados;\nPresidente do Senado Federal;')
        janela18=janela_questao6C()
        janela17.hide()
    if window==janela18 and event==sg.WINDOW_CLOSED:
        break
    if window==janela18 and event=='Errado':
        acerto+=1
        sg.popup('Você acertou!\nComentário:\nSTF = Não é necessário aviso prévio (dispensável)\nCF/88 = é necessário aviso prévio (indispensável)')
        janela19=janela_questao7C()
        janela18.hide()
    elif window==janela18 and event=='Certo':
        erro+=1
        sg.popup('Você errou!\nComentário:\nSTF = Não é necessário aviso prévio (dispensável)\nCF/88 = é necessário aviso prévio (indispensável)')
        janela19=janela_questao7C()
        janela18.hide()
    if window==janela19 and event==sg.WINDOW_CLOSED:
        break
    if window==janela19 and event=='Certo':
        erro+=1
        sg.popup('Você errou!\nComentário:\nSTF.Plenário.ADI 4411-É INCONSTITUCIONAL A CRIAÇÃO DE TAXA DE COMBATE A INCÊNDIOS\n A atividade desenvolvida pelo Estado no âmbito da segurança pública\né mantida ante impostos, sendo imprópria a substituição, para tal fim, de taxa.')
        janela20=janela_questao8C()
        janela19.hide()
    elif window==janela19 and event=='Errado':
        acerto+=1
        sg.popup('Você acertou!\nComentário:\nSTF.Plenário.ADI 4411-É INCONSTITUCIONAL A CRIAÇÃO DE TAXA DE COMBATE A INCÊNDIOS\n A atividade desenvolvida pelo Estado no âmbito da segurança pública\né mantida ante impostos, sendo imprópria a substituição, para tal fim, de taxa.')
        janela20=janela_questao8C()
        janela19.hide()
    if window==janela20 and event==sg.WINDOW_CLOSED:
        break
    if window==janela20 and event=='Errado':
        acerto+=1
        sg.popup('Você acertou!\nComentário:\nArt. 5º, VIII, CF: ninguém será privado de direitos por motivo de crença religiosa ou de convicção filosófica ou política,\nsalvo se as invocar para eximir-se de obrigação legal a todos imposta e recusar-se\na cumprir prestação alternativa, fixada em lei;')
        janela21=janela_questao9C()
        janela20.hide()
    elif window==janela20 and event=='Certo':
        erro+=1
        sg.popup('Você errou!\nComentário:\nArt. 5º, VIII, CF: ninguém será privado de direitos por motivo de crença religiosa ou de convicção filosófica ou política,\nsalvo se as invocar para eximir-se de obrigação legal a todos imposta e recusar-se\na cumprir prestação alternativa, fixada em lei;')
        janela21=janela_questao9C()
        janela20.hide()
    if window==janela21 and event==sg.WINDOW_CLOSED:
        break
    if window==janela21 and event=='Certo':
        acerto+=1
        sg.popup('Você acertou!\nComentário:\nArt 144 CF: § 1º A polícia federal, instituída por lei como órgão permanente, estruturado em carreira, destina-se a:\nIV - exercer, com exclusividade, as funções de polícia judiciária da União.')
        pontos=acerto-erro
        if pontos<1:
            pontos=0
            sg.popup('Você conseguiu' ,pontos,'ponto!')
            break
        else:
            sg.popup('Parabéns, você conseguiu' ,pontos,'pontos!')
            break
    elif window==janela21 and event=='Errado':
        erro+=1
        sg.popup('Você errou!\nComentário:\nArt 144 CF: § 1º A polícia federal, instituída por lei como órgão permanente, estruturado em carreira, destina-se a:\nIV - exercer, com exclusividade, as funções de polícia judiciária da União.')
        pontos=acerto-erro
        if pontos<1:
            pontos=0
            sg.popup('Você conseguiu' ,pontos,'ponto!')
            break
        else:
            sg.popup('Parabéns, você conseguiu' ,pontos,'pontos!')
            break
    ##Daqui pra baixo é só as questões de Direito Penal
    elif window == janela1 and event== 'Direito Penal':
        janela3=janela_questaoP()
        janela1.hide()
    if window == janela3 and event == sg.WINDOW_CLOSED:
        break
    if window == janela3 and event == 'Certo':
        erro+=1
        sg.popup('Você errou!\nComentário:\nConcussão: Exigir, para si ou para outrem, direta ou indiretamente, ainda que fora da função ou antes de assumi-la, mas em razão dela, vantagem indevida.')
        janela4=janela_questao1P()
        janela3.hide()
    if window == janela4 and event== sg.WINDOW_CLOSED:
        break
    elif window == janela3 and event =='Errado':
        acerto+=1
        sg.popup('Você acertou!\nComentário:\nConcussão: Exigir, para si ou para outrem, direta ou indiretamente, ainda que fora da função ou antes de assumi-la, mas em razão dela, vantagem indevida.')
        janela4=janela_questao1P()
        janela3.hide()
    if window == janela4 and event== sg.WINDOW_CLOSED:
        break
    if window == janela4 and event=='Certo':
        erro+=1
        sg.popup('Você errou!\nComentário:\nO crime de resistência consuma-se com a prática da violência ou da ameaça.\nO que torna a questão FALSA.')
        janela5=janela_questao2P()
        janela4.hide()
    if window == janela5 and event == sg.WINDOW_CLOSED:
        break
    elif window==janela4 and event=='Errado':
        acerto+=1
        sg.popup('Você acertou!\nComentário:\nO crime de resistência consuma-se com a prática da violência ou da ameaça.\nO que torna a questão FALSA.')
        janela5=janela_questao2P()
        janela4.hide()
    if window == janela5 and event == sg.WINDOW_CLOSED:
        break
    if window == janela5 and event =='Certo':
        erro+=1
        sg.popup('Você errou!\nComentário:\nO crime de corrupção passiva caracteriza-se solicitar ou receber, para si ou para outros, direta ou indiretamente,\nainda que fora da função ou antes de assumi-la, mas em razão dela, vantagem indevida, ou aceitar promessa de tal vantagem.')
        janela6=janela_questao3P()
        janela5.hide()
    if window == janela6 and event == sg.WINDOW_CLOSED:
        break
    elif window == janela5 and event=='Errado':
        acerto+=1
        sg.popup('Você acertou!\nComentário:\nExigir para si ou para outrem, direta ou indiretamente, ainda que fora da função ou antes de assumi-la, mas em razão dela, vantagem indevida.\nCaracteriza CONCUSÃO, NÃO CORRUPÇÃO.')
        janela6=janela_questao3P()
        janela5.hide()
    if window == janela6 and event == sg.WINDOW_CLOSED:
        break
    if window== janela6 and event== 'Certo':
        acerto+=1
        sg.popup('Você acertou!\nComentário:\nArt. 334. Iludir, no todo ou em parte, o pagamento de direito ou imposto devido pela entrada, pela saída ou pelo consumo de mercadoria. (Pena: Reclusão de 1 a 4 anos).\nA partir do julgamento do HC n. 218.961/SP, a Quinta Turma do Superior Tribunal de Justiça assentou o entendimento de que o delito de descaminho é formal, se configurando com o simples ato de iludir o pagamento do imposto devido pela entrada de mercadoria no país.')
        janela7=janela_questao4P()
        janela6.hide()
    if window == janela7 and event == sg.WINDOW_CLOSED:
        break
    elif window== janela6 and event=='Errado':
        erro+=1
        sg.popup('Você errou!\nComentário:\nArt. 334. Iludir, no todo ou em parte, o pagamento de direito ou imposto devido pela entrada, pela saída ou pelo consumo de mercadoria. (Pena: Reclusão de 1 a 4 anos).\nA partir do julgamento do HC n. 218.961/SP, a Quinta Turma do Superior Tribunal de Justiça assentou o entendimento de que o delito de descaminho é formal, se configurando com o simples ato de iludir o pagamento do imposto devido pela entrada de mercadoria no país.')
        janela7=janela_questao4P()
        janela6.hide()
    if window == janela7 and event == sg.WINDOW_CLOSED:
        break
    if window== janela7 and event=='Certo':
        erro+=1
        sg.popup('Você errou!\nComentário:\nA súmula vinculante não é lei nem ato normativo, de forma que a SV 24-STF não inovou no ordenamento jurídico. O enunciado apenas espelhou (demonstrou) o que a jurisprudência já vinha decidindo.\nAssim, a SV pode ser aplicada aos crimes cometidos antes da sua vigência, tendo em vista que não se está diante de norma mais gravosa, mas de consolidação de interpretação judicial.')
        janela8=janela_questao5P()
        janela7.hide()
    if window == janela8 and event== sg.WINDOW_CLOSED:
        break
    elif window== janela7 and event=='Errado':
        acerto+=1
        sg.popup('Você acertou!\nComentário:\nA súmula vinculante não é lei nem ato normativo, de forma que a SV 24-STF não inovou no ordenamento jurídico. O enunciado apenas espelhou (demonstrou) o que a jurisprudência já vinha decidindo.\nAssim, a SV pode ser aplicada aos crimes cometidos antes da sua vigência, tendo em vista que não se está diante de norma mais gravosa, mas de consolidação de interpretação judicial.')
        janela8=janela_questao5P()
        janela7.hide()
    if window == janela8 and event== sg.WINDOW_CLOSED:
        break
    if window == janela8 and event == 'Certo':
        acerto+=1
        sg.popup('Você acertou!\nComentário:\nL8137, Art. 15. Os crimes previstos nesta lei são de ação penal pública, aplicando-se-lhes o disposto no  art. 100 do Decreto-Lei n° 2.848, de 7 de dezembro de 1940 - Código Penal.\nCP, Art. 100 - A ação penal é pública, salvo quando a lei expressamente a declara privativa do ofendido.\nSTF - A propositura da ação penal não depende de representação fiscal para fins penais, se o MP dispuser, por outros meios, de elementos que lhe permitam comprovar a definitividade da constituição do crédito tributário.')
        janela9=janela_questao6P()
        janela8.hide()
    elif window== janela8 and event== 'Errado':
        erro+=1
        sg.popup('Você errou!\nComentário:\nL8137, Art. 15. Os crimes previstos nesta lei são de ação penal pública, aplicando-se-lhes o disposto no  art. 100 do Decreto-Lei n° 2.848, de 7 de dezembro de 1940 - Código Penal.\nCP, Art. 100 - A ação penal é pública, salvo quando a lei expressamente a declara privativa do ofendido.\nSTF - A propositura da ação penal não depende de representação fiscal para fins penais, se o MP dispuser, por outros meios, de elementos que lhe permitam comprovar a definitividade da constituição do crédito tributário.')
        janela9=janela_questao6P()
        janela8.hide()
    if window== janela9 and event== sg.WINDOW_CLOSED:
        break
    if window== janela9 and event== 'Certo':
        acerto+=1
        sg.popup('Você acertou!\nComentário:\nArt. 16 do CP - Nos crimes cometidos sem violência ou grave ameaça à pessoa, reparado o dano ou restituída a coisa, até o recebimento da denúncia ou da queixa,\npor ato voluntário do agente, A PENA SERÁ reduzida de um a dois terços (redução igual dos crimes tentado)')
        janela10=janela_questao7P()
        janela9.hide()
    if window== janela10 and event==sg.WINDOW_CLOSED:
        break
    if window== janela9 and event== sg.WINDOW_CLOSED:
        break
    elif window== janela9 and event== 'Errado':
        erro+=1
        sg.popup('Você errou!\nComentário:\nArt. 16 do CP - Nos crimes cometidos sem violência ou grave ameaça à pessoa, reparado o dano ou restituída a coisa, até o recebimento da denúncia ou da queixa,\npor ato voluntário do agente, A PENA SERÁ reduzida de um a dois terços (redução igual dos crimes tentado)')
        janela10=janela_questao7P()
        janela9.hide()
    if window== janela10 and event==sg.WINDOW_CLOSED:
        break
    if window== janela10 and event=='Certo':
        acerto+=1
        sg.popup('Você acertou!\nComentário:\nArt. 111, CP - A prescrição, antes de transitar em julgado a sentença final, começa a correr:\n (...)IV - nos de bigamia e nos de falsificação ou alteração de assentamento do registro civil, da data em que o fato se tornou conhecido.')
        janela11=janela_questao8P()
        janela10.hide()
    elif window==janela10 and event=='Errado':
        erro+=1
        sg.popup('Você errou!\nComentário:\nArt. 111, CP - A prescrição, antes de transitar em julgado a sentença final, começa a correr:\n (...)IV - nos de bigamia e nos de falsificação ou alteração de assentamento do registro civil, da data em que o fato se tornou conhecido.')
        janela11=janela_questao8P()
        janela10.hide()
    if window==janela11 and event == sg.WINDOW_CLOSED:
        break
    if window==janela11 and event =='Certo':
        erro+=1
        sg.popup('Você errou!\nComentário:\nPreso que praticar fato definido como crime doloso ou falta grave, deverá ser transferido para regime mais rigoroso\nNão se admite contravenção penal ou modalidade culposa.')
        janela12=janela_questao9P()
        janela11.hide()
    elif window==janela11 and event =='Errado':
        acerto+=1
        sg.popup('Você acertou!\nComentário\nPreso que praticar fato definido como crime doloso ou falta grave, deverá ser transferido para regime mais rigoroso\nNão se admite contravenção penal ou modalidade culposa.')
        janela12=janela_questao9P()
        janela11.hide()
    if window==janela12 and event== sg.WINDOW_CLOSED:
        break
    if window==janela12 and event == 'Certo':
        erro+=1
        sg.popup('Você errou!\nComentário:\nCrimes imprescritiveís: RAÇÃO-Racismo e Ação de grupos armados.')
        pontos=acerto-erro
        if pontos<1:
            pontos=0
            sg.popup('Você conseguiu' ,pontos,'ponto!')
            break
        else:
            sg.popup('Parabéns, você conseguiu' ,pontos,'pontos!')
            break
    elif window==janela12 and event=='Errado':
        acerto+=1
        sg.popup('Você acertou!\nComentário:\nCrimes imprescritiveís: RAÇÃO-Racismo e Ação de grupos armados.')
        pontos=acerto-erro
        if pontos<1:
            pontos=0
            sg.popup('Você conseguiu', pontos,'ponto!')
            break
        else:
            sg.popup('Parabéns, você conseguiu' ,pontos,'pontos!')
            break