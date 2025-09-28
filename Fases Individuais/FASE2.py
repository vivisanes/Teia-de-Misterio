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
FASE 2 - 2.0
'''
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