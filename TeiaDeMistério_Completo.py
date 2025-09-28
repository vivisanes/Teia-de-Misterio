import time
import sys
import os

# FUNC PRA DIGITAR TEXTO DE UM JEITO BONITINHO
def digitar_texto(texto):
    estilo_cor = "\033[1;32m"
    reset_cor = "\033[0m"

    for char in texto:
        sys.stdout.write(estilo_cor + char + reset_cor)
        sys.stdout.flush()
        time.sleep(0.05)
    print()

# FUNC PRA EXIBIR A FALA DE UM JEITO BONITINHO
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
'''
FASE 1 - 2.0
'''

#COMEÇO FASE 1
localCasaMarcos = [
    'SÃO PAULO, 04 DE FEVEREIRO DE 2000',
    'RUA DOS MAGNATAS, 389 - 23H07'
]
for linha in localCasaMarcos:
    digitar_texto(linha)
    time.sleep(0.5)
print()

EntraDaCasa = [
    'Você chega na cena do crime, uma casa de alto nível.',
    'Há vários policiais no local coletando evidências, um deles se aproxima de você.'
]
narra(EntraDaCasa)

laurentino = '[POLICIAL LAURENTINO]'
lau_f1 = [
    'Boa noite detetive Isaac. A vítima é aquele modelo famoso, Marcos Matarazzo.',
    'Ele e a esposa estavam voltando de um jantar no centro da cidade, quando chegaram em casa foram abordados por um ladrão que disparou dois tiros:', 
    'Um na testa de Marcos e outro na bochecha da esposa, Yara, que já foi levada para o hospital.',
    'O pessoal já separou umas pistas. Essa é a ficha da vítima:'
]
exibir_fala(laurentino, lau_f1, 36)
print()

#FICHA MARCOS MATARAZZO
ficha_marcos =  """
 ____________________________________________
|                                            |
|           FICHA DA VÍTIMA:                 |
|____________________________________________|
|                                            |
| Nome: Marcos Matarazzo                     |
| Data de nascimento: 08/08/1971             |
| Estado Civil: Casado                       |
| Aparência: Homem alto, cabelos pretos      |
|            e olhos castanhos               |
| Nascido na capital de São Paulo            |
|____________________________________________|
"""
print(ficha_marcos)
print()
print()

#DENTRO DA CASA DO MARCOS MATARAZZO
DentroDaCasaM = [
    'Você tem alguns cômodos para investigar:',
    'SALA, JARDIM e QUARTO da vítima.'
]

opcoesCasa1 = ['SALA', 'QUARTO', 'JARDIM', 'SAIR']

while True:
    narra(DentroDaCasaM)
    escolhaCasa1 = input('PARA ONDE VOCÊ QUER IR? (SALA, QUARTO, JARDIM ou SAIR): ').upper()
    print()

    while escolhaCasa1 not in opcoesCasa1:
        print()
        print('Digite uma opção válida! (SALA, QUARTO, JARDIM ou SAIR)')
        print()
        escolhaCasa1 = input('PARA ONDE VOCÊ QUER IR? (SALA, QUARTO, JARDIM ou SAIR): ').upper()
        print()

    if escolhaCasa1 == 'SAIR':
        break

    # SALA DO MARCOS MATARAZZO
    if escolhaCasa1 == 'SALA':
        sala_marcos = [
            'Ao entrar na sala você vê o corpo de Marcos, ele está usando um PALETÓ de grife. Olhando no rosto dele, você vê uma expressão de choque.',
            'Você também vê algumas marcas de sangue no CHÃO, uma ESTANTE com algumas fotos do casal e um APARADOR com algumas decorações que parecem mais caras que sua casa.',
            'Você também pode VOLTAR.'
        ]
        narra(sala_marcos)

        opcoesSala1 = ['PALETÓ', 'CHÃO', 'ESTANTE', 'APARADOR', 'VOLTAR']
        escolhaSala1 = input('ONDE VOCÊ QUER OLHAR? (PALETÓ, CHÃO, ESTANTE, APARADOR ou VOLTAR): ').upper()
        print()
        
        while escolhaSala1 != 'VOLTAR':
            if escolhaSala1 == 'PALETÓ':
                recibo_marcos = """
                +-----------------------------------------------------------------------+
                |                        RECIBO DE ESTACIONAMENTO                       |
                |                                                                       |
                |                          Estacionamento Seguro                        |
                |-----------------------------------------------------------------------|
                | Data de entrada:      04/02/2000       Horário de entrada:   20:10    |
                | Data de saída:        04/02/2000       Horário de saída:     21:47    |
                |-----------------------------------------------------------------------|
                | Tempo estacionado:                   1 hora e 37 minutos              |
                |                                                                       |
                | Valor cobrado:                       R$ 32,00                         |
                |                                                                       |
                +-----------------------------------------------------------------------+
                """
                paleto = ['Checando os bolsos do paletó do corpo frio de Marcos, você encontra um recibo de estacionamento:']
                narra(paleto)
                print(recibo_marcos)
            elif escolhaSala1 == 'CHÃO':
                chaoMarcos = ['Em meio às marcas de sangue próximas do corpo e vários policiais analisando provas, você encontra uma cápsula de bala calibre 9mm']
                narra(chaoMarcos)
            elif escolhaSala1 == 'ESTANTE':
                estanteMarcos = ['Você encontra várias revistas de moda, livros de publicidade e arte moderna.',
                                  'Nada que vai te ajudar agora.']
                narra(estanteMarcos)
            elif escolhaSala1 == 'APARADOR':
                certidaoMarcos = """
                +-----------------------------------------------------------------------+
                |                        CERTIDÃO DE CASAMENTO                          |
                |                                                                       |
                | Data do casamento:       04 de fevereiro de 1995                      |
                |                                                                       |
                | Esposo:                  Marcos Matarazzo                             |
                | Esposa:                  Yara ██████████                              |
                |                                                                       |
                | Testemunhas:                                                          |
                |                 Victor Matarazzo      Isabela Vieira                  |
                |                                                                       |
                |                                                                       |
                | Assinatura do Esposo            Assinatura da Esposa                  |
                |   Marcos Matarazzo                 Yara ██████████                    |
                +-----------------------------------------------------------------------+
                """
                aparadorMarcos = [
                    'Você abre as gavetas do aparador.',
                    'Em meio a alguns panfletos e alguns documentos muito bem organizados, você encontra a certidão de casamento de Marcos e Yara'
                ]
                narra(aparadorMarcos)
                print(certidaoMarcos)

            print('Você pode checar PALETÓ, CHÃO, ESTANTE e o APARADOR, ou você pode VOLTAR.')
            escolhaSala1 = input('ONDE VOCÊ QUER OLHAR? (PALETÓ, CHÃO, ESTANTE, APARADOR ou VOLTAR): ').upper()
            print()
            
            while escolhaSala1 not in opcoesSala1:
                print()
                print('Digite uma opção válida! (PALETÓ, CHÃO, ESTANTE, APARADOR ou VOLTAR)')
                print()
                escolhaSala1 = input('ONDE VOCÊ QUER OLHAR? (PALETÓ, CHÃO, ESTANTE, APARADOR ou VOLTAR): ').upper()
                print()

    # JARDIM DO MARCOS MATARAZZO
    elif escolhaCasa1 == 'JARDIM':
        jardimMarcos = [
            'Ao sair pelo jardim, você vê um espaço muito agradável para lazer.',
            'Você vê algumas flores, um balanço e um gazebo.',
            'Olhando para a casa, você percebe que uma das janelas está quebrada,',
            'os cacos do antigo vidro da janela estão para o lado de dentro.'
        ]
        narra(jardimMarcos)

    # QUARTO DO MARCOS MATARAZZO
    elif escolhaCasa1 == 'QUARTO':
        quartoMarcos = [
            'Ao entrar no quarto, você vê um ARMÁRIO bem bagunçado e uma das portas está quebrada.',
            'Você também vê uma penteadeira cheia de maquiagens e perfumes.',
            'Olhando na cabeceira da cama você vê uma foto de aparentemente Marcos e Yara sorrindo.'
        ]
        narra(quartoMarcos)

        lau_f2 = ['A empregada deu falta de um colar, o dinheiro que estava no cofre e uma arma 9mm que Marcos tinha por segurança.']
        exibir_fala(laurentino, lau_f2, 36)
        print('Você pode checar ARMÁRIO ou você pode SAIR.')
        escolhaQuartoM = input('ONDE VOCÊ QUER OLHAR? (ARMÁRIO ou SAIR): ').upper()
        print()
        opcoesQuartoM = ['ARMÁRIO', 'SAIR']

        while escolhaQuartoM not in opcoesQuartoM:
            print()
            print('Digite uma opção válida! (ARMÁRIO ou SAIR)')
            print()
            escolhaQuartoM = input('ONDE VOCÊ QUER OLHAR? (ARMÁRIO ou SAIR): ').upper()
            print()

        # ARMÁRIO DO MARCOS MATARAZZO
        while escolhaQuartoM != 'SAIR':
            if escolhaQuartoM == 'ARMÁRIO':
                armarioMarcos = [
                    'Você vê muitas roupas de marcas que você nem sabe pronunciar.',
                    'No meio da bagunça do armário, você encontra um cofre.'
                ]
                narra(armarioMarcos)
                
                # COFRE
                cofreMarcos = [
                    'Você afasta algumas roupas para alcançar o cofre.',
                    'Ao olhar a fechadura, você percebe que já foi arrombada.',
                    'Olhando dentro do cofre, você vê que o ladrão ainda deixou algumas jóias e certa quantidade de dinheiro.'
                ]
                narra(cofreMarcos)

            print('Você pode checar o ARMÁRIO, ou você pode SAIR.')
            escolhaQuartoM = input('ONDE VOCÊ QUER OLHAR? (ARMÁRIO ou SAIR): ').upper()
            print()

            while escolhaQuartoM not in opcoesQuartoM:
                print()
                print('Digite uma opção válida! (ARMÁRIO ou SAIR)')
                print()
                escolhaQuartoM = input('ONDE VOCÊ QUER OLHAR? (ARMÁRIO ou SAIR): ').upper()
                print()

#SAINDO DA CASA DO MARCOS MATARAZZO
saida_casaM = [
    'Você sente que coletou todas as provas que podia.',
    'Você vai em direção da entrada da casa e vê o policial Laurentino vindo em sua direção'
]
narra(saida_casaM)

lau_f3 = [
    'A viúva do senhor Marcos está internada no Hospital Esperança, aqui perto. Poderíamos fazer uma visita amanhã, ver se ela pode nos ajudar...'
    ]
exibir_fala(laurentino, lau_f3, 36)
print()

#HOSPITAL
localHospital = [
    'SÃO PAULO, 05 DE FEVEREIRO DE 2000',
    'HOSPITAL ESPERANÇA - 9H47'
]
for linha in localHospital:
    digitar_texto(linha)
    time.sleep(0.5)
print()

hosp = [
    'Você chega ao hospital com o objetivo de fazer algumas perguntas para a viúva de Marcos, Yara.', 
    'Você chega a recepção e a recepcionista logo pede para alguma enfermeira te levar até Yara.'
    ]
narra(hosp)

enfermeira = '[ENFERMEIRA]'
enf_f1 = [
    'A senhora Yara passou por uma cirurgia muito complicada, ela acordou faz algumas horas. Ninguém veio fazer visita. Detetive Isaac, peço para que o senhor seja delicado. O trauma dela ainda é recente.'
]

exibir_fala(enfermeira, enf_f1, 34)
print()

hospQuarto = [
    'Ao entrar no quarto de Yara, ela se ajeita na maca.',
    'Ela sorri.',
    'Ou pelo menos tenta...'
]
narra(hospQuarto)

yara = '[YARA]'
yara_f1 = [
    'Ah, você é o detetive que está cuidando do caso do Marcos? Por favor entre!',
    'Pode perguntar qualquer coisa, vou tentar lembrar de tudo *ri*',
    'Pelo meu Marcos, eu ajudo o máximo que puder.'
]
exibir_fala(yara, yara_f1, 35)
print()

# INTERROGATORIO YARA
interrogatorioY = [
    'Você pode fazer algumas perguntas para Yara.',
    '1 - Você se lembra de como o ladrão era?',
    '2 - Você acha que o ladrão sabia que vocês estavam fora?',
    '3 - Seu marido tinha alguém que não gostasse dele?',
    'Quando terminar, você pode SAIR'
]
narra(interrogatorioY)
opcoesPerguntaY = ['1', '2', '3', 'SAIR']

perguntaY = input('QUAL PERGUNTA VOCÊ QUER FAZER? (1, 2, 3 ou SAIR): ').upper()
print()
detetive = '[VOCÊ]'

while perguntaY not in opcoesPerguntaY:
    print()
    print('Digite uma opção válida! (1, 2, 3 ou SAIR)')
    print()
    perguntaY = input('QUAL PERGUNTA VOCÊ QUER FAZER? (1, 2, 3 ou SAIR): ').upper()
    print()

#LOOP DAS PERGUNTAS
while perguntaY != 'SAIR':
    # PERGUNTA 1
    if perguntaY == '1':
        det_p1 = ['Você se lembra de alguma característica do ladrão? Cor da pele, dos olhos ou algo assim?']
        exibir_fala(detetive, det_p1, 33)
        print()
        yara_r1 = ['Não... Foi tudo muito rápido. Ele também estava usando uma daquelas bandanas no rosto, não consigo me lembrar... Desculpe.']
        exibir_fala(yara, yara_r1, 35)
        print()
    # PERGUNTA 2
    elif perguntaY == '2':
        det_p2 = ['Você acha que o ladrão, de algum jeito, saberia que você estariam fora?']
        exibir_fala(detetive, det_p2, 33)
        print()
        yara_r2 = [
            'O jantar com o Marcos foi surpresa para mim. Estávamos comemorando nosso aniversário de casamento.',
            'Alguém pode ter visto em algum blog a data do nosso casamento e, provavelmente, imaginou que iríamos comemorar fora...'
        ]
        exibir_fala(yara, yara_r2, 35)
        print()
    # PERGUNTA 3
    elif perguntaY == '3':
        det_p3 = ['Você consegue pensar em alguém que não gosta do Marcos, algum inimigo?']
        exibir_fala(detetive, det_p3, 33)
        print()
        yara_r3 = [
            'Oh não! Todos adoram- adoravam o Marcos *lacrimeja*...',
            'Ele era tão gentil e tranquilo. Talvez algum outro modelo sem tanto sucesso quanto ele? Não sei...'
        ]
        exibir_fala(yara, yara_r3, 35)
        print()

    # Solicitar nova escolha após responder
    perguntaY = input('QUAL PERGUNTA VOCÊ QUER FAZER? (1, 2, 3 ou SAIR): ').upper()
    print()

    # Validar nova escolha
    while perguntaY not in opcoesPerguntaY:
        print()
        print('Digite uma opção válida! (1, 2, 3 ou SAIR)')
        print()
        perguntaY = input('QUAL PERGUNTA VOCÊ QUER FAZER? (1, 2, 3 ou SAIR): ').upper()
        print()

# SAIDA DO HOSPITAL
hospSaida = [
    'Depois da conversa com Yara, você ainda não tem muitas respostas.',
    'Ela tentou, mas não foi muito útil...'
]
narra(hospSaida)

localCasoArq = [
    'SÃO PAULO, 10 DE AGOSTO DE 2000',
    'DELEGACIA - 10H04'
]
for linha in localCasoArq:
    digitar_texto(linha)
    time.sleep(0.5)
print()

chefe = '[CAPITÃO DA DELEGACIA]'
chefe_f1 = [
    'Você não conseguiu nenhuma prova nova em cinco meses com esse caso aberto, Isaac!',
    'O caso vai ser arquivado!'
]
exibir_fala(chefe, chefe_f1, 34)
print()

finalFase1 = [
    'Seu superior arquiva o caso',
    'Você não tem o suficiente para achar o suspeito do assassinato de Marcos Matarazzo.'
]
narra(finalFase1)
# --------------------------------------------------------- #

'''
FASE 2 - 2.0
'''

# --------------------------------------------------------- #

localCasaKauan = [
    "FLORIANÓPOLIS, 3 DE JUNHO DE 2007",
    "RUA TEODORO DA FONSSECA, 208 - 17h48"    
]
for linha in localCasaKauan:
    digitar_texto(linha)
    time.sleep(0.5)
print()

caso2 = ['Você foi chamado para investigar um caso de assassinato em Florianópolis.']
narra(caso2)

ramos = '[POLICIAL RAMOS]'
ram_f1 = [
    'Boa tarde detetive Isaac,espero que o senhor tenha feito uma boa viagem.',
    'A vítima é o juiz Kauan Queiroz, o corpo dele estava em casa quando chegamos.',
    'Nada da casa foi roubado e a casa estava bem arrumada, sem sinal de invasão. Isso tirando a mancha de sangue no quarto da vítima e da esposa, Eloise.',
    'Aparentemente os vizinhos não viram e nem ouviram nada de suspeito.',
    'Aqui a ficha dele...'
]
exibir_fala(ramos, ram_f1, 36)

ficha_kauan = """
            ____________________________________________
            |                                            |
            |           FICHA DA VÍTIMA:                 |
            |____________________________________________|
            |                                            |
            | Nome: Kauan Queiroz                        |
            | Data de nascimento: 24/10/1968             |
            | Estado Civil: Casado                       |
            | Aparência: Homem de estatura média,        |
            | cabelos castanhos levemente grisalhos e    |
            | olhos azuis                                |               
            | Nascido Carazinho, interior do Rio         |
            | Grande do Sul, se mudou para Florianópolis |
            | em 1986.                                   |
            |____________________________________________|
            """
print(ficha_kauan)
print()

DentroDaCasaK = [
    'Você tem alguns cômodos para investigar:',
    'SALA e QUARTO da vítima.',
    'Ao terminar, você pode SAIR.'
]
opcoesCasa2 = ['SALA', 'QUARTO', 'SAIR']

while True:
    narra(DentroDaCasaK)
    escolhaCasa2 = input('PARA ONDE VOCÊ QUER IR? (SALA, QUARTO ou SAIR): ').upper()
    print()

    while escolhaCasa2 not in opcoesCasa2:
        print()
        print('Digite uma opção válida! (SALA, QUARTO ou SAIR)')
        print()
        escolhaCasa2 = input('PARA ONDE VOCÊ QUER IR? (SALA, QUARTO ou SAIR): ').upper()
        print()

    if escolhaCasa2 == 'SAIR':
        break

    # SALA DO KAUAN QUEIROZ
    if escolhaCasa2 == 'SALA':
        sala_kauan = [
            'Ao entrar pela porta da frente, você se depara com alguns diplomas da Universidade Federal de Santa Catarina.',
            'Os diplomas estavam no nome de Kauan Queiroz, datados em 20/01/1999'
        ]
        narra(sala_kauan)

        investigaSala2 = [
            'Você pode olhar em alguns lugares:',
            'Um ARMÁRIO pequeno, as JANELAS e uma ESTANTE cheia de livros.',
            'Você também pode VOLTAR.'
        ]
        narra(investigaSala2)

        opcoesSala2 = ['ARMÁRIO', 'JANELAS', 'ESTANTE', 'VOLTAR']
        escolhaSala2 = input('ONDE VOCÊ QUER OLHAR? (ARMÁRIO, JANELAS, ESTANTE ou VOLTAR): ').upper()
        print()
        
        while escolhaSala2 not in opcoesSala2:
            print()
            print('Digite uma opção válida! (ARMÁRIO, JANELAS, ESTANTE ou VOLTAR)')
            print()
            escolhaSala2 = input('ONDE VOCÊ QUER OLHAR? (ARMÁRIO, JANELAS, ESTANTE ou VOLTAR): ').upper()
            print()

        while escolhaSala2 != 'VOLTAR':
            if escolhaSala2 == 'ARMÁRIO':
                armario = [
                    'Você procura por algum tipo de rastro deixado pelo assassino.',
                    'Você encontra algumas contas e folhetos.',
                    'Nada que vá te ajudar agora.'
                ]
                narra(armario)
            elif escolhaSala2 == 'ESTANTE':
                estanteKauan = [
                    'Em meio a diversos livros sobre leis nacionais e internacionais e matérias em jornais sobre alguns casos que Kauan foi juiz, você encontra uma certidão de casamento'
                ]
                narra(estanteKauan)
                certidaoKauan = '''
                +-----------------------------------------------------------------------+
                |                        CERTIDÃO DE CASAMENTO                          |
                |                                                                       |
                | Data do casamento:       10 de fevereiro de 2002                      |
                |                                                                       |
                | Esposo:                  Kauan Queiroz                                |
                | Esposa:                  Eloise Bittencourt                           |
                |                                                                       |
                | Testemunhas:                                                          |
                |                 Joanna Queiroz      Rozana Amadeuz                    |
                |                                                                       |
                |                                                                       |
                | Assinatura do Esposo            Assinatura da Esposa                  |
                |    Kauan Queiroz                 Eloise Bittencourt                   |
                +-----------------------------------------------------------------------+
                '''
                print(certidaoKauan)
                print()
            elif escolhaSala2 == 'JANELAS':
                janelaKauan = [
                    'Você tenta procurar por algum rastro deixado por algo ou alguém.',
                    'Tudo parece normal.'
                ]
                narra(janelaKauan)
            
            print('Você pode checar ARMÁRIO, a ESTANTE e as JANELAS ou você pode VOLTAR.')
            escolhaSala2 = input('ONDE VOCÊ QUER OLHAR? (ARMÁRIO, JANELAS, ESTANTE ou VOLTAR): ').upper()
            print()

            while escolhaSala2 not in opcoesSala2:
                print()
                print('Digite uma opção válida! (ARMÁRIO, JANELAS, ESTANTE ou VOLTAR)')
                print()
                escolhaSala2 = input('ONDE VOCÊ QUER OLHAR? (ARMÁRIO, JANELAS, ESTANTE ou VOLTAR): ').upper()
                print()

    # QUARTO DO KAUAN QUEIROZ
    elif escolhaCasa2 == 'QUARTO':
        quartoKauan = [
            'Entrando no quarto, a porta do ARMÁRIO está aberta, mas você também se depara com o CORPO de Kauan.',
            'Ele está sentado em sua ESCRIVANINHA.'
        ]
        narra(quartoKauan)

        opcoesQuarto2 = ['CORPO', 'ESCRIVANINHA', 'ARMÁRIO', 'VOLTAR']
        escolhaQuarto2 = input('ONDE VOCÊ QUER OLHAR? (CORPO, ESCRIVANINHA, ARMÁRIO ou VOLTAR): ').upper()
        print()
        
        while escolhaQuarto2 not in opcoesQuarto2:
            print()
            print('Digite uma opção válida! (CORPO, ESCRIVANINHA, ARMÁRIO ou VOLTAR)')
            print()
            escolhaQuarto2 = input('ONDE VOCÊ QUER OLHAR? (CORPO, ESCRIVANINHA, ARMÁRIO ou VOLTAR): ').upper()
            print()

        while escolhaQuarto2 != 'VOLTAR':
            if escolhaQuarto2 == 'CORPO':
                corpoKauan = [
                    'Ao olhar mais de perto o cadáver de Kauan você percebe algumas coisas:',
                    'O tiro veio de trás da cabeça, atravessando-a e saindo pela testa.',
                    'A segunda coisa que você percebe é que claramente Kauan não sabia que iria morrer.'
                ]
                narra(corpoKauan)
            elif escolhaQuarto2 == 'ESCRIVANINHA':
                escrivaninhaKauan = [
                    'Kauan parecia estar lendo alguns papéis antes de morrer. Agora estão todos manchados de sangue.',
                    'Algo sobre o que você vê te faz pensar que ele estava trabalhando em algum caso de roubo.'
                ]
                narra(escrivaninhaKauan)
            elif escolhaQuarto2 == 'ARMÁRIO':
                armarioKauan = [
                    'Você vê muitas roupas em cores variadas de preto e cinza na parte masculina do armário.',
                    'Em contraste, você olha para o lado feminino você vê roupas em diversas cores, bem diversificado.',
                    'Não parece ter nada interessante aqui.'
                ]
                narra(armarioKauan)

            print('Você pode checar o CORPO, a ESCRIVANINHA e o ARMÁRIO ou você pode VOLTAR.')
            escolhaQuarto2 = input('ONDE VOCÊ QUER OLHAR? (CORPO, ESCRIVANINHA, ARMÁRIO ou VOLTAR): ').upper()
            print()

            while escolhaQuarto2 not in opcoesQuarto2:
                print()
                print('Digite uma opção válida! (CORPO, ESCRIVANINHA, ARMÁRIO ou VOLTAR)')
                print()
                escolhaQuarto2 = input('ONDE VOCÊ QUER OLHAR? (CORPO, ESCRIVANINHA, ARMÁRIO ou VOLTAR): ').upper()
                print()

entradaK = [
    'Você sente que não consegue muitas informações só investigando a casa.',
    'Você decide se encontrar com o policial Ramos para ver se consegue mais informações'
]

ram_f2 = [
    'A viúva ainda está muito abalada, não quis falar muito nem responder as perguntas que fizemos...',
    'Mas peguei o número de contato dela no caso de querer tentar de novo mais tarde.'
]
exibir_fala(ramos, ram_f2, 36)
print()
entradaK = [
    'Você sente que não consegue muitas informações só investigando a casa.',
    'Você decide se encontrar com o policial Ramos para ver se consegue mais informações'
]

ram_f2 = [
    'A viúva ainda está muito abalada, não quis falar muito nem responder as perguntas que fizemos...',
    'Mas peguei o número de contato dela no caso de querer tentar de novo mais tarde.'
]
exibir_fala(ramos, ram_f2, 36)
print()

finalCasaK = [
    'Você decide ir embora da casa e trabalhar mais no caso na delegacia.'
]
narra(finalCasaK)

#CAFETERIA 
localCafeteria = [
    'FLORIANÓPOLIS, 05 DE JUNHO DE 2007',
    'CAFETERIA CAFÉ REFÚGIO - 10H32'
]
for linha in localCafeteria:
    digitar_texto(linha)
    time.sleep(0.5)

cafeteria = [
    'Após não conseguir muitas pistas investigando a cena do crime, você decide recorrer à última pista que você não conseguiu checar:',
    'A viúva de Kauan Queiroz, Eloise.',
    'Vocês decidem se encontrar numa cafeteria do bairro onde Eloise mora, um ambiente mais amigável do que a delegacia.'
]
narra(cafeteria)

detetive = '[VOCÊ]'
eloise = '[ELOISE]'
elo_f1 = [
    'Detetive Isaac? Sou Eloise, é você que está no comando do caso do meu marido Kauan?'
]
exibir_fala(eloise, elo_f1, 35)
print()

det_f1 = [
    'Ah, sim, sou eu que estou cuidado do caso.',
    'Antes de tudo meus sentimentos pelo seu marido, ele parecia ser um bom homem.',
    'Tenho algumas perguntas para você, tudo bem?'
]
exibir_fala(detetive, det_f1, 33)
print()

elo_f2 = [
    'Ah, obrigada, ele era sim!',
    'Estou pronta para responder qualquer pergunta, quero justiça pelo meu Kauan!'
]
exibir_fala(eloise, elo_f2, 35)
print()

perguntasCafe = [
    'Você pode fazer algumas perguntas para Eloise:',
    '1 - Onde você estava quando tudo aconteceu?',
    '2 - Você reparou algo estranho na sua casa?',
    '3 - Seu marido tinha algum inimigo, ou teve alguma briga recentemente?',
    'Quando terminar, você pode SAIR.'
]
narra(perguntasCafe)

opcoesCafe = ['1', '2', '3', 'SAIR']
perguntaC = input('QUAL PERGUNTA VOCÊ QUER FAZER? (1, 2, 3 ou SAIR): ').upper()
print()

while perguntaC not in opcoesCafe:
    print()
    print('Digite uma opção válida! (1, 2, 3 ou SAIR)')
    print()
    perguntaY = input('QUAL PERGUNTA VOCÊ QUER FAZER?: ').upper()
    print()

#LOOP DAS PERGUNTAS
while perguntaC != 'SAIR':
    # PERGUNTA 1
    if perguntaC == '1':
        det_p1 = ['Eloise, onde você estava quando o Kauan faleceu?']
        exibir_fala(detetive, det_p1, 33)
        print()
        elo_r1 = [
            'Eu tinha saído para ir ao mercado naquela noite...',
            'Quando cheguei em casa o Kauan estava morto no nosso quarto...'
            ]
        exibir_fala(eloise, elo_r1, 35)
        print()
    # PERGUNTA 2
    elif perguntaC == '2':
        det_p2 = ['Tinha algo de diferente na sua casa quando você voltou? Algo fora do comum?']
        exibir_fala(detetive, det_p2, 33)
        print()
        elo_r2 = [
            'Não, tudo parecia normal até eu entrar no nosso quarto.'
        ]
        exibir_fala(eloise, elo_r2, 35)
        print()
    # PERGUNTA 3
    elif perguntaC == '3':
        det_p3 = ['Consegue pensar em alguém que queria o mal do seu marido? Alguma briga recente ou algo assim?']
        exibir_fala(detetive, det_p3, 33)
        print()
        elo_r3 = [
            'Não consigo nem imaginar quem poderia odiar tanto o Kauan ao ponto de fazer uma coisa dessas com ele...'
        ]
        exibir_fala(eloise, elo_r3, 35)
        print()

    perguntaC = input('QUAL PERGUNTA VOCÊ QUER FAZER? (1, 2, 3 ou SAIR): ').upper()
    print()

    while perguntaC not in opcoesCafe:
        print()
        print('Digite uma opção válida! (1, 2, 3 ou SAIR)')
        print()
        perguntaC = input('QUAL PERGUNTA VOCÊ QUER FAZER? (1, 2, 3 ou SAIR): ').upper()
        print()

cicatriz = [
    'Apesar de toda a beleza de Eloise ser desconsertante, você percebe uma cicatriz na bochecha dela.'
]
narra(cicatriz)

det_p4 = [
    'Dona Eloise, me desculpa pela minha indelicadeza, mas como conseguiu essa cicatriz?'
]
exibir_fala(detetive, det_p4, 33)
print()

elo_r4 = [
    'Ah... Eu tive um ex muito abusivo...',
    'Ele me socou no rosto. Eu o denunciei e ele foi preso.',
    'Foi no julgamento dele que eu conheci o Kauan...'
]
exibir_fala(eloise, elo_r4, 35)
print()

finalCafe = [
    'Após finalizar a conversa, Eloise se despede de você com um beijo no rosto.',
    'Você ainda fica no café, ainda sem muitas respostas.',
    'A cicatriz de Eloise te lembrou um caso antigo que você não resolveu, isso te faz temer que não consiga resolver esse também.'
]
narra(finalCafe)
# --------------------------------------------------------- #

'''
FASE 3 - 2.0
'''

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
                        narra(fuga)

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