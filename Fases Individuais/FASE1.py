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
#----------------------------------------------------------
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