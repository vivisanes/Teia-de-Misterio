import time
import sys
import os

def digitar_texto(texto):
    estilo_cor = "\033[1;32m"
    reset_cor = "\033[0m"

    for char in texto:
        sys.stdout.write(estilo_cor + char + reset_cor)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

def exibir_fala(nome_personagem, fala, cor):
    estilo_fala = f"\033[1;{cor}m"
    reset_cor = "\033[0m"

    print(f"{estilo_fala}{nome_personagem}:{reset_cor}")

    for linha in fala:
        for char in linha:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.05)
        print()
        time.sleep(0.5)

#FUNCAO PARA EXIBIR AS NARRAÇÕES
def narra(texto):
    for linha in texto:
        print(linha)
        time.sleep(1)
    print()

#FUNCAO PARA OS CREDITOS
def fim():
    creditos = [
        'TEIA DE MISTÉRIO',
        'Por - Saturn Games',
        'Obrigado por jogar!'
    ]

    largura_tela = os.get_terminal_size().columns

    for linha in creditos:
        espacos = (largura_tela - len(linha)) // 2
        linha_formatada = ' ' * espacos + linha

        print(linha_formatada)
        time.sleep(2)
# --------------------------------------------------------- #
localDelegacia2 = [
    'FLORIANÓPOLIS, 9 DE JULHO DE 2007',
    'DELEGACIA - 12H03'
]
for linha in localDelegacia2:
    digitar_texto(linha)
    time.sleep(0.5)

delegacia1 = [
    'Você continua sua investigação sobre o caso de Kauan Queiroz, sem muito sucesso,',
    'até que um dia na sua delegacia, você escuta uma comoção do lado de fora da sua sala.'
]
narra(delegacia1)

eloise = '[ELOISE]'
elo_f1 = [
    'Preciso falar com o detetive Isaac! Me deixem passar!',
    'Faz um mês que soltaram ele! Soltaram o homem que me deu essa cicatriz!',
    'Ele matou Kauan! Aqui, veja!'
    ]
exibir_fala(eloise, elo_f1, 35)
print()

delegacia2 = [
    'Ela te entrega uma folha'
]
narra(delegacia2)

fichaRafa = """
╔════════════════════════════════════════════════════════════╗
║                       FICHA INDIVIDUAL                     ║
╠════════════════════════════════════════════════════════════╣
║ Nome: Rafael Teixeira                                      ║
║ Data de Nascimento: 05/04/1970                             ║
║ Estado Civil: Divorciado                                   ║
╠════════════════════════════════════════════════════════════╣
║ APARÊNCIA                                                  ║
║ - Estatura: Alta                                           ║
║ - Cabelos: Loiros curtos                                   ║
║ - Olhos: Azuis                                             ║
╠════════════════════════════════════════════════════════════╣
║ FICHA CRIMINAL                                             ║
║ - Preso em: 04/03/2000                                     ║
║ - Crime: Violência doméstica contra Eloise Teixeira        ║
║ - Condenação: 10 anos de prisão                            ║
║ - Liberação por bom comportamento: 31/05/2007              ║
╚════════════════════════════════════════════════════════════╝
"""
print(fichaRafa)
print()

#PERGUNTAS NA DELEGACIA
perguntasDlg = [
    'Você pode fazer algumas perguntas para Eloise.',
    '1 - Você acredita que ele sabia do seu novo casamento?',
    '2 - Você tem alguma ideia de onde ele mora agora?',
    'Quando você terminar, você pode SAIR'
]
narra(perguntasDlg)
detetive = '[VOCÊ]'

while True:
    pergunta = input('QUAL PERGUNTA VOCÊ QUER FAZER? (1, 2, SAIR): ').upper()
    print()

    opcoes = ['1', '2', 'SAIR']
    if pergunta not in opcoes:
        print()
        print('Digite uma opção válida! (1, 2 ou SAIR)')
        print()
        continue

    if pergunta == '1':
        det_p1 = [
            'Acha que ele sabia que você tinha se casado de novo?'
        ]
        exibir_fala(detetive, det_p1, 33)

        elo_r1 = [
            'Definitivamente sim! Ele era tão ciumento... Foi por isso que ele me deixou essa cicatriz.',
            'Eu tenho certeza que foi ele! Vocês precisam prendê-lo!'
        ]
        exibir_fala(eloise, elo_r1, 35)
        print()

    elif pergunta == '2':
        det_p2 = [
            'Você sabe onde ele está agora? Onde ele mora?'
        ]
        exibir_fala(detetive, det_p2, 33)

        elo_r2 = [
            'Eu não tenho ideia, mas ele sabe onde eu moro e ele vai me matar!',
            'Eu tenho certeza disso, vocês precisam fazer alguma coisa!'
        ]
        exibir_fala(eloise, elo_r2, 35)
        print()

    elif pergunta == 'SAIR':
        sairDlg = [
            'Você tenta acalmar Eloise e manda alguns oficiais procurarem por Rafael perto da casa dela e nas redondezas.'
        ]
        narra(sairDlg)
        break

# TIME SKIP
localCasaE = [
    'FLORIANÓPOLIS, 10 DE JULHO DE 2007',
    'RUA TEODORO DA FONSSECA, 208 - 18H47'
]
for linha in localCasaE:
    digitar_texto(linha)
    time.sleep(0.5)

#CASA DA ELOISE
EntradaCasaE = [
    'Você vai à casa de Eloise para discutir sobre o caso de Kauan e verificiar se Rafael havia feito algum mal a ela.',
    'Você bate na porta, e quando é atendido seus olhos veem uma mulher deslumbrante.'
]
narra(EntradaCasaE)

elo_f2 = ['Detetive! Entre, o jantar está quase pronto.']
exibir_fala(eloise, elo_f2, 35)
print()

respostaEntrar = input('Você quer entrar? (SIM ou NÃO):').upper()
print()

opcoesEntrar = ['SIM', 'NÃO']
if respostaEntrar not in opcoesEntrar:
    print()
    print('Digite uma opção válida! (SIM ou NÃO)')
    print()
    respostaEntrar = input('Você quer entrar?:').upper()
    print()

if respostaEntrar == 'SIM':
    entrei = [
        'Você entra para jantar, a comida estava ótima.',
        'Você se diverte tanto com Eloise que mal se lembra que ela ficou viúva há pouco mais de um mês.'
    ]
    narra(entrei)
elif respostaEntrar == 'NÃO':
    elo_f3 = ['Oh detetive, por favor eu insisto! Entre, já está tudo quase pronto.']
    exibir_fala(eloise, elo_f3, 35)
    print()
    naoEntrei = [
        'Você acaba aceitando o convite da bela moça e entra para jantar. A comida estava ótima.',
        'Você se diverte tanto com Eloise que mal se lembra que ela ficou viúva há pouco mais de um mês.'
    ]
    narra(naoEntrei)

#DENTRO DA CASA DE ELOISE
dentroDaCasaE = [
    'Após o jantar, você se lembra o motivo da visita.',
    'Você pega seu caderno de anotações e começa a fazer perguntas para Eloise.'
]
narra(dentroDaCasaE)

perguntasE = [
    'Você pode fazer algumas perguntas:',
    '1 - Aconteceu algo estranho com você recentemente?',
    '2 - O que aconteceu entre você e Rafael Teixeira?',
    'Quando terminar, você pode SAIR'
]
narra(perguntasE)

while True:
    pergunta = input('QUAL PERGUNTA VOCÊ QUER FAZER? (1, 2, SAIR): ').upper()
    print()

    opcoes = ['1', '2', 'SAIR']
    if pergunta not in opcoes:
        print()
        print('Digite uma opção válida! (1, 2 ou SAIR)')
        print()
        continue
    
    if pergunta == '1':
        det_p1 = [
            'Como você está? Algo estranho aconteceu recentemente?'
        ]
        exibir_fala(detetive, det_p1, 33)

        elo_r1 = [
            'Ah, estou bem, nada aconteceu. Obrigada pela preocupação, detetive.',
            'Eu reforcei a segurança da casa, mas me sinto mais segura só com sua presença.'
        ]
        exibir_fala(eloise, elo_r1, 35)
        print()

    elif pergunta == '2':
        det_p2 = [
            'Por que você e Rafael se separaram? O que aconteceu entre vocês?'
        ]
        exibir_fala(detetive, det_p2, 33)

        elo_r2 = [
            'No começo, Rafael era um homem tão gentil, mas era tão ciumento...',
            'Só quando ele me agrediu eu percebi que ele era o homem raivoso, rude e egoísta que ele escondia.'
        ]
        exibir_fala(eloise, elo_r2, 35)
        print()

    elif pergunta == 'SAIR':
        sairCasaE = [
            'Após as perguntas, você e Eloise ainda conversam um pouco antes de você decidir ir embora.'
        ]
        narra(sairCasaE)
        break

saidaCasaE = [
    'Ao sair da casa de Eloise, você sente dentro de você que sente algo diferente por Eloise.',
    'Com Rafael ainda à solta, as visitas à casa de Eloise foram ficando cada vez mais frequentes e as discussões sobre o caso cada vez mais raras.',
    'Você percebe que o sentimento diferente que sentia por Eloise era amor. Você sabe que isso não é o certo.'
]
narra(saidaCasaE)

#ABANDONAR OU FICAR?
abandonarOuFicar = [
    'Você passa algumas noites em claro pensando nos seus sentimentos por Eloise.',
    'Você nunca esteve tão confuso, deve separar o profissional do pessoal?'
]
narra(abandonarOuFicar)

decisaoAF = input('Você quer desistir dos seus sentimentos e ABANDONAR Eloise ou quer FICAR com ela e corre o risco?: ').upper()
print()

opcoesAF = ['ABANDONAR', 'FICAR']
if decisaoAF not in opcoesAF:
    print()
    print('Digite uma opção válida! (ABANDONAR ou FICAR)')
    print()
    decisaoAF = input('Você quer desistir dos seus sentimentos e ABANDONAR Eloise ou quer FICAR com ela e corre o risco?: ').upper()
    print()

decisaoAbandonaOuFica = [
    'Você decide ir contar à Eloise sobre sua decisão.',
    'Você chega na casa dela e enquanto você se enrola nas palavras para explicar seus sentimentos, Eloise te dá um beijo.',
    'Antes que você possa ter uma reação e processar o que aconteceu, seu telefone toca.'
]
narra(decisaoAbandonaOuFica)

camargo = '[POLICAL CAMARGO]'
cam_f1 = ['Detetive Isaac? Lembra do Rafael Teixeira, chefe? Achamos o cara!']
exibir_fala(camargo, cam_f1, 36)

det_f1 = ['Certo, estou indo para a delegacia.']
exibir_fala(detetive, det_f1, 33)
print()
print('Você desliga o telefone.')
print()

elo_f4 = ['O que aconteceu? Quem era?']
exibir_fala(eloise, elo_f4, 35)
print()

#CONTAR OU NÃO CONTAR
contarOuN = input('Você vai CONTAR para Eloise o que aconteceu ou NÃO?: ').upper()
opcoesCouN = ['CONTAR', 'NÃO']
if contarOuN not in opcoesCouN:
    print()
    print('Digite uma opção válida! (CONTAR ou NÃO): ')
    print()
    contarOuN = input('Você vai CONTAR para Eloise o que aconteceu ou NÃO?: ').upper()
    print()

if contarOuN == 'CONTAR':
    det_r1 = ['Meus oficiais encontraram o Rafael, ele está na delegacia.']
    exibir_fala(detetive, det_r1, 33)
    elo_f5 = ['Oh, que ótimo! O que está esperando, Isaac? Vai para delegacia interrogá-lo!']
    exibir_fala(eloise, elo_f5, 35)
    print()
    contei = [
        'Antes que vocês possam conversar sobre o que acabou de acontecer entre vocês dois,'
        'você entra no seu carro e vai direto para a delegacia.'
    ]
    narra(contei)
elif contarOuN == 'NÃO':
    det_r2 = ['Preciso ir à delegacia resolver algumas burocracias.']
    exibir_fala(detetive, det_r2, 33)
    print()
    naoContei = [
        'Antes que Eloise possa te impedir e antes que vocês possam conversar sobre o que acabou de acontecer,',
        'você vira as costas e vai direto para a delegacia.'
    ]
    narra(naoContei)

#INTERROGATORIO RAFAEL
localDelegacia2 = [
    'FLORIANÓPOLIS, 12 DE JULHO DE 2007',
    'DELEGACIA - 14H16'
]
for linha in localDelegacia2:
    digitar_texto(linha)
    time.sleep(0.5)

interrogaRafa = [
    'Você chega na delegacia, com um pouco de raiva do homem que fez a mulher, que você acabou de descobrir que ama, sofrer.',
    'Você entra na sala de interrogatório sem muitas apresentações e já começa as perguntas.'
]
narra(interrogaRafa)

interrogatorio = [
    'Você pode fazer algumas perguntas para Rafael Teixeira:',
    '1 - O nome Kauan Queiroz te lembra alguém?',
    '2 - Você queria vingança depois de sair da prisão?',
    'Quando acabar, você pode SAIR'
]
narra(interrogatorio)

rafa = '[RAFAEL TEIXEIRA]'

while True:
    pergunta = input('QUAL PERGUNTA VOCÊ QUER FAZER? (1, 2, SAIR): ').upper()
    print()

    opcoes = ['1', '2', 'SAIR']
    if pergunta not in opcoes:
        print()
        print('Digite uma opção válida! (1, 2 ou SAIR)')
        print()
        continue

    if pergunta == '1':
        det_p1 = ['O nome Kauan Queiroz te lembra alguém?']
        exibir_fala(detetive, det_p1, 33)

        rafa_r1 = ['Eu sei lá quem é esse cara! Por que eu deveria saber?!']
        exibir_fala(rafa, rafa_r1, 31)
        
        det_re1 = [
            'Kauan Queiroz foi o juiz do seu caso, não lembra?',
            'Ele se casou com sua ex depois do caso e foi assassinado no dia 2 de junho'
        ]
        exibir_fala(detetive, det_re1, 33)
        print()

    elif pergunta == '2':
        det_p2 = [
            'Depois que você saiu da cadeia você queria vingança?',
            'Se você não pudesse ter Eloise, ninguém mais poderia?'
        ]
        exibir_fala(detetive, det_p2, 33)

        rafa_r2 = [
            'Vingança? Primeiro que eu não me lembro nem da minha última refeição, muito menos o juiz que me condenou.'
            'Além do mais, no dia 2 de junho eu estava num café com a própria Eloise. Queria me desculpar com ela,',
            'achei que isso nos ajudaria a deixar tudo isso para trás. Eu queria mostrar para ela que eu mudei!'
        ]
        exibir_fala(rafa, rafa_r2, 31)

        det_re2 = [
            'Estava com ela?',
            'Ela vai confirmar isso se eu perguntar?'
        ]
        exibir_fala(detetive, det_re2, 33)

        rafa_r3 = [
            'Pode perguntar à ela!',
            'Ou você pode olhar as câmeras do café ou da praça que tem do lado!'
        ]
        exibir_fala(rafa, rafa_r3, 31)

    elif pergunta == 'SAIR':
        sairInte = [
            'Você estranha as respostas de Rafael.',
            'Porque Eloise o acusaria se estava com ele no dia do assassinato de Kauan?',
            'Você decide procurar mais sobre Eloise no banco de dados da polícia e vai atrás das gravações que Rafael mencionou.'
        ]
        narra(sairInte)
        break

#TIME SKIP INVESTIGAÇÃO
localDelegacia2 = [
    'FLORIANÓPOLIS, 12 DE JULHO DE 2007',
    'DELEGACIA - 17h34'
]
for linha in localDelegacia2:
    digitar_texto(linha)
    time.sleep(0.5)

investigaFim = [
    'Após mexer alguns pauzinhos, você consegue as gravações do café onde Rafael e Eloise haviam se encontrado.',
    'Você consegue ver nas filmagens Rafael e Eloise conversando no café, assim como o ex-prisioneiro tinha dito.',
    'Mas, se aquela era Eloise e Rafael estava com ela na hora da morte de Kauan, quem era a viúva?',
    'Você decide investigar mais a fundo sobre quem é a Eloise, ou quem é a verdadeira mulher por trás desse nome...',
    'Você encontra uma ficha específica.'
]
narra(investigaFim)
fichaElo = """
╔════════════════════════════════════════════════════════════╗
║                     FICHA DE CIDADÃO                       ║
╠════════════════════════════════════════════════════════════╣
║ Nome: Eloise Vieira                                        ║
║ Data de Nascimento: 24/05/1973                             ║
║ Estado Civil: Divorciada                                   ║
╠════════════════════════════════════════════════════════════╣
║ APARÊNCIA                                                  ║
║ - Estatura: Baixa                                          ║
║ - Cabelos: Castanhos                                       ║
║ - Olhos: Verdes                                            ║
╠════════════════════════════════════════════════════════════╣
║ OBSERVAÇÃO                                                 ║
║ - Fez uma denúncia de violência doméstica contra           ║
║   seu ex-marido Rafael Teixeira no dia 03/01/2000.         ║
╚════════════════════════════════════════════════════════════╝
"""
print(fichaElo)
print()

investigaE = [
    'A descrição da ficha bate perfeitamente com a mulher da gravação.',
    'Você não para de pensar em uma única pergunta: Quem era a mulher que você amava?',
    'Você se sente traído, Eloise estava mentindo para você, tinha te manipulado.',
    'Porque ela teria feito isso? Fingir ser outra pessoa?',
    'Por quanto tempo ela tem planejado isso?',
    'Movido pela raiva, você decide invadir a casa dela furtivamente para investigar.'
]

#INVASÃO DA CASA DA ELOISE
localCasaE = [
    'FLORIANÓPOLIS, 12 DE JULHO DE 2007',
    'RUA TEODORO DA FONSSECA, 208 - 22H49'
]
for linha in localCasaE:
    digitar_texto(linha)
    time.sleep(0.5)

invasaoCasa = [
    'Você entra pela janela furtivamente, não fazendo barulho algum.',
    'Você olha ao redor e percebe que a casa está vazia.',
    'Você, de uma vez por todas, decide por um ponto final em toda essa investigação.'
]

opcoesInvasao = ['SALA', 'QUARTO']

while True:
    narra(invasaoCasa)
    investigaCasa = input('PARA ONDE VOCÊ QUER IR? (SALA ou QUARTO): ').upper()
    print()

    while investigaCasa not in opcoesInvasao:
        print()
        print('Digite uma opção válida! (SALA ou QUARTO)')
        print()
        investigaCasa = input('PARA ONDE VOCÊ QUER IR? (SALA ou QUARTO): ').upper()
        print()

    # SALA ELOISE
    if investigaCasa == 'SALA':
        investigaSala = [
            'Você vê uma ESTANTE com livros e um APARADOR com algumas decorações.',
            'Você pode VOLTAR para a entrada.'
        ]
        opcoesSala = ['ESTANTE', 'APARADOR', 'VOLTAR']
        while True:
            narra(investigaSala)
            investigarS = input('ONDE VOCÊ QUER OLHAR? (ESTANTE, APARADOR ou você pode VOLTAR.): ').upper()
            print()

            while investigarS not in opcoesSala:
                print()
                print('Digite uma opção válida! (ESTANTE, APARADOR ou você pode VOLTAR.)')
                print()
                investigarS = input('ONDE VOCÊ QUER OLHAR?: ').upper()
                print()

            if investigarS == 'ESTANTE':
                estanteE = [
                    'Você vasculha a estante.',
                    'Não há nada de interessante fora o sentimento de amargura que você sente ao lembrar das conversas sobre os diversos livros com "Eloise".',
                    'Você se pergunta se "Eloise" leu mesmo todos aqueles livros.'
                ]
                narra(estanteE)
            elif investigarS == 'APARADOR':
                aparadorE = [
                    'Você encontra algumas contas de luz e água.',
                    'Obviamente, todas no nome de "Eloise Queiroz".',
                    'Você se pergunta há quanto tempo essa mulher mudou sua identidade.'
                ]
                narra(aparadorE)
            elif investigarS == 'VOLTAR':
                break

    # QUARTO DA ELOISE
    if investigaCasa == 'QUARTO':
        investigaQuarto = [
            'Você vê uma MESA com vários papéis e cadernos em cima,',
            'o ARMÁRIO com várias roupas de grife e a CAMA, que está bagunçada.',
            'Você pode VOLTAR para a entrada.'
        ]
        opcoesQuarto = ['MESA', 'ARMÁRIO', 'CAMA', 'VOLTAR']
        while True:
            narra(investigaQuarto)
            investigarQ = input('ONDE VOCÊ QUER OLHAR? (MESA, ARMÁRIO, CAMA ou você pode VOLTAR.): ').upper()
            print()

            while investigarQ not in opcoesQuarto:
                print()
                print('Digite uma opção válida! (MESA, ARMÁRIO, CAMA ou você pode VOLTAR.)')
                print()
                investigarQ = input('ONDE VOCÊ QUER OLHAR?: ').upper()
                print()

            if investigarQ == 'MESA':
                mesaE = [
                    'Você olha no meio dos cadernos e anotações.',
                    'Você só encontra algumas listas de mercado e alguns recibos de compras.',
                    'A única coisa que chama sua atenção é a data do seu aniversário marcada em vermelho no calendário dela.'
                ]
                narra(mesaE)
            elif investigarQ == 'ARMÁRIO':
                armarioE = [
                    'Em meio as diversas roupas chiques, você acha algumas caixas com fotos antigas.',
                    'Você encontra uma foto de uma mulher que você poderia dizer ser "Eloise".',
                    'Ela está completamente diferente, mas mesmo assim, familiar.'
                ]
                narra(armarioE)
            elif investigarQ == 'CAMA':
                camaE = [
                    'Desesperado por uma única resposta sequer, você revira a cama na esperança de encontrar alguma coisa.',
                    'Qualquer coisa.',
                    'Olhando debaixo da cama com o auxílio de uma lanterna você encontra uma certa irregularidade no carpete.',
                    'Iluminando melhor, você percebe a porta de um alçapão escondido.'
                ]
                narra(camaE)
                # ALCAPAO
                alcapao = input('Você quer abrir o alçapão? (SIM ou NÃO): ').upper()
                print()

                while alcapao not in ['SIM', 'NÃO']:
                    print()
                    print('Digite uma opção válida! (SIM ou NÃO)')
                    print()
                    alcapao = input('Você quer abrir o alçapão?: ').upper()
                    print()

                if alcapao == 'SIM':
                    abri = [
                        'Você abre o alçapão e encontra uma escada que desce para um porão secreto.',
                        'Ao descer, você percebe que há muitos documentos e objetos de valor guardados lá.',
                        'Parece que Eloise estava escondendo muito mais do que você imaginava.'
                    ]
                    narra(abri)

                    abriAlca = [
                            'Você desce as velhas escadas de madeira com sua lanterna em mãos.',
                            'O lugar é muito empoeirado, você vê armários de metal, uma pequena prateleira com alguns arquivos e alguns outros móveis consumidos pelo tempo.',
                            'O que realmente chama sua atenção é um quadro de teia, cheio de fotos e documentos.',
                            'Você vê uma foto de Kauan Queiroz, ligada a uma notícia do seu assassinato.',
                            'Você vê uma foto de Marcos Matarazzo, também ligada a uma notícia do seu assassinato.',
                            'E por último,',
                            'Você vê uma foto sua. Não tem nada ligado a ela.',
                            '',
                            '',
                            'Você finalmente liga os pontos na sua cabeça.',
                            'A mulher que você amava, não era só manipuladora.',
                            'Ela também era uma assassina.',
                            'Ela enganou Marcos Matarazzo como Yara e o matou.',
                            'Enganou você e Kauan como Eloise.',
                            'Você agora percebe,',
                            'você vai ter o mesmo fim de Kauan e Marcos.',
                            'Com isso, uma grande teia de mistério parecia ter se resolvido na sua cabeça.',
                            '',
                            '',
                            '',
                            '',
                            'Olhando pela bagunça de documentos numa mesa perto do quadro de teia, você encontra um RG muito velho e desgastado.'
                    ]
                    narra(abriAlca)

                    docNath = """
                                _______________________________________________________________
                                |                                                             |
                                |                  REPÚBLICA FEDERATIVA DO BRASIL             |
                                |_____________________________________________________________|
                                |                                 |                           |
                                |        IDENTIDADE               |           RG              |
                                |_________________________________|___________________________|
                                |                                 |                           |
                                |    Nome: Nathalia Salazar       |                           |
                                |    Data de Nascimento: ■■/■■/■■ |      ■■.■■■.■■■-■         |
                                |_________________________________|___________________________|                                    
                                |                                 |                           |
                                |    CPF:                         |      Órgão Emissor:       |
                                |   ■■■■■■■■■■■■■                 |          ■■■-■■           |
                                |                                 |                           |                                    
                                |       [Nathalia Salazar]        |      Validade: ■■/■■      |
                                |_________________________________|___________________________|
                                |                                                             |
                                |                       _._                                   |                                    
                                |                     ,"-._"-.                                |
                                |                     ;"-._"-."-.                             |
                                |                     :.   "-.`. |                            |
                                |                     (;`-._  `.  ;                           |
                                |                      :_  _".    :                           |
                                |                      ;o: o` |   ;                           |
                                |                      : ;     )-. `.                         |
                                |                       ;=-  .:|     "-._                     |
                                |                       :_.-" ; `.       "-.                  |
                                |                 _._   ( :   :   "-._      "-.               |
                                |                |   `._.='    |               `.             |
                                |               :    |:         `-.__ _._   "-.  |            |
                                |                |    '.    _      ",' ` ",    |  ;           |
                                |                 )-.   `j"^,L_..--"      ; ,-. : :           |
                                |_____________________________________________________________|
                                """
                    print(docNath)
                    print()
                    nath = '[NATHALIA SALAZAR]'

                    saindoAlca = [
                        'Você decide sair do porão para poder voltar a investigar e poder prender Nathalia por seus crimes.',
                        'Antes que você pudesse abrir a porta do quarto, você ouve uma porta sendo destrancada.',
                        'Você saca sua arma.',
                        '',
                        'Você vê algumas opções para se esconder:',
                        'Você pode voltar para debaixo da CAMA',
                        'Você pode se esconder num pequeno espaço entre a ESTANTE e a parede do quarto.',
                        'Ou você pode FUGIR pela janela.'
                    ]

                    escolha = input("ONDE VOCÊ VAI SE ESCONDER? (CAMA, ESTANTE ou FUGIR): ").upper()

                    if escolha == 'CAMA' or escolha == 'ESTANTE':
                        esconder = [
                            'Você se esconde',
                            'Com o nervosismo você atira antes da hora e acaba acertado a parede.',
                            'Você sai do esconderijo.',
                            '',
                            '',
                            'Enquanto você sai do seu esconderijo, Nathalia volta para a sala.',
                            'Quando você vai atrás dela, ela te da um tiro no braço pelas suas costas.',
                            'Você pega cobertura em uma parede.'
                        ]
                        narra(esconder)

                        nath_f1 = [
                            'As coisas não precisam ser assim, Isaac!',
                            'Eu realmente não quero lutar com você.',
                            'Você é diferente dos outros, você é especial!',
                            'Acredite em mim!'
                        ]
                        exibir_fala(nath, nath_f1, 35)

                        det_l1 = [
                            'Eu não consigo acreditar em você!',
                            'Você vai me matar igual fez com Marcos e com Kauan! Você Mentiu para mim esse tempo todo!'
                        ]
                        exibir_fala(detetive, det_l1, 33)

                        nath_f2 = [
                            'Mas você é diferente! Eu nunca menti para você!',
                            'Tudo o que eu disse sobre você, todas as nossas conversas, foi tudo real!',
                            'As coisas não precisam terminar assim, eu realmente te amo!'
                        ]
                        exibir_fala(nath, nath_f2, 35)
                        print()
                        #DECISAO FINAL
                        decFinal = [
                            'Você pode ACREDITAR ou ATIRAR em Nathalia'
                            ]
                        narra(decFinal)
                        final = input('O QUE VOCÊ VAI FAZER?(ACREDITAR ou ATIRAR):').upper()
                        if final not in ['ACREDITAR', 'ATIRAR']:
                            print()
                            print('Digite uma opção válida! (ACREDITAR ou ATIRAR)')
                            print()
                            final = input('O QUE VOCÊ VAI FAZER?: ').upper()
                        
                        if final == 'ACREDITAR':
                            detCre = [
                                'Eu...',
                                'Eu não consigo fazer isso! Não posso te entregar para a polícia!',
                                'Você é o amor da minha vida!'
                                ]
                            exibir_fala(detetive, detCre, 33)

                            nathCre = [
                                'Sabia que você me entenderia...',
                                'Eu te amo, Isaac.'
                            ]
                            exibir_fala(nath, nathCre, 35)
                            final2 = [
                                'Nathalia se aproxima de você.',
                                'Ela te beija e você sente que fez a escolha certa.',
                                'Nathalia é o amor da sua vida.'
                                'Vocês fogem juntos para um novo recomeço.'
                                ]
                            narra(final2)

                            print()
                            print('FINAL 2/4')
                            fim()
                            exit()
                        
                        elif final == 'ATIRAR':
                            atirei = [
                                'Você aproveita um certo momento de fraqueza de Nathalia e atira na direção dela.',
                                'Você erra.'
                            ]
                            narra(atirei)

                            nathAtira = [
                                'Desgraçado!',
                                'HOJE EU TE MATO!'
                            ]
                            exibir_fala(nath, nathAtira, 35)

                            luta = [
                                'Nathalia avança em sua direção, ela usa alguns móveis para se proteger.',
                                'Você pode AVANCAR também ou pode ESPERAR, o que você vai fazer?'
                            ]
                            narra(luta)

                            avancaEspera = input('AVANÇAR ou ESPERAR?: ').upper()
                            if avancaEspera not in ['AVANÇAR', 'ESPERAR']:
                                print()
                                print('Digite uma opção válida! (AVANÇAR ou ESPERAR)')
                                print()
                                avancaEspera = input('AVANÇAR ou ESPERAR?: ').upper()    
                                print()
                            
                            if avancaEspera == 'AVANÇAR':
                                final3 = [
                                    'Com raiva, você se aproxima de Nathalia, numa distância onde você tem certeza que não vai mais errar nenhum tiro.',
                                    'Você segura firme sua arma e mira em direção a Nathalia.',
                                    'Quando você pensa em puxar o gatilho você sente um tiro no seu peito.',
                                    'Ela foi mais rápida.',
                                    'Em seus últimos momentos de vida, você vê aquela mulher que você pensou que pudesse amar virando as costas e indo embora.',
                                    'Ela conseguiu o que queria. Seu propósito acabou para ela.'
                                    ]
                                narra(final3)
                                print()
                                print('FINAL 3/4')
                                fim()
                                exit()
                            
                            elif avancaEspera == 'ESPERAR':
                                final4 = [
                                        'Você espera parado, se concentrando apenas nas movimentações de Nathalia.',
                                        'Ela tenta atirar em você, mas você pega cobertura no sofá da sala.',
                                        'Aproveitando a brecha, você atira. Dessa vez você precisa acertar.',
                                        'Você sem hesitar atira.',
                                        'Ao procurar por Nathalia, você a encontra.',
                                        'Dura, fria e caída, com um tiro bem na testa.',
                                        'Enquanto você se aproxima do cadáver da mulher que você acreditou que um dia te amasse.',
                                        'As sirenes ecoam ao seu redor. Acabou.',
                                        'Você conseguiu'
                                    ]
                                narra(final4)
                                print()
                                print('FINAL 4/4')
                                fim()
                                exit()


                    elif escolha == 'FUGIR':
                        fuga = [
                            'Você pula pela janela, desesperado para chamar reforços.',
                            'Você alcança um lugar seguro e chama reforços.',
                            'Enquanto você espera, você consegue ver uma mulher te olhando pela janela da casa.',
                            'Assim que os reforços chegam, eles se preparam para arrombar a porta.',
                            'Antes que você pudesse fazer qualquer coisa, a casa simplesmente explode.',
                            'Enquanto você corre pela rua em busca de algum resquício de justiça, você recebe uma mensagem.'
                        ]

                        celular = """
                            ⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⠿⠿⠿⠿⠿⠿⢿⣿⠿⢿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⢸⣿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⣿⡇⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀() Eloise   ⣿⡇⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⢸⣿-------------⣿⡇⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⢸⣿()    Boa    ⣿⡇⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⢸⣿  tentativa  ⣿⡇⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀detetive. ;)⣿⡇⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣿⡇⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣿⡇⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣿⡇⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⣿⡇⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⢸⣿⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣿⡇⠀⠀⠀⠀⠀⠀⠀
                            ⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣦⣤⣤⣤⣤⣤⣴⣿⣿⣿⡿⠃⠀⠀⠀⠀⠀⠀⠀
                                    """
                        print(celular)
                        print()
                        print('FINAL 1/4')
                        fim()
                        exit()



                else:
                    narra(['Você decide não abrir o alçapão por enquanto.',
                           'Mas você sente que não vai prosseguir se não entrar aqui.'])
            elif investigarQ == 'VOLTAR':
                break