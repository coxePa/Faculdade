import random

print(
    'Depois de muito tempo vivendo sob domínio tirânico das capivaras que ganharam consciência,\n'
    'a resistência humana vive sob constante ameaça do exército capivara que ronda quase todos os lugares.\n'
    'Esses rebeldes humanos vivem em bunkers subterrâneos espalhados por vários lugares, eles funcionam como um grande sistema metroviário,\n'
    'mas, diferente de um metrô normal, são usados trens manuais, normalmente feito artesanalmente de restos de metais e materiais do gênero. \n'
    'A comida e água é escassa, requerendo cooperação entre as partes rebeldes para se manterem, os coletores, como são chamadas as pessoas que \n'
    'vão para a superfície, são essênciais na sobrevivência rebelde, e você é um desses coletores que foi pego por guardas capivaras enquanto buscava por\n'
    'suprimentos. Você acorda dentro de uma cela suja e com um cheiro forte de sangue, você não sabe de onde vem esse cheiro, mas ouve barulhos de\n'
    'batidas e algo se partindo, você percebe que as condições do portão que prende você são precárias e decide arrombar a fechadura com uns\n'
    'grampos que escondeu no seu calçado. Após algumas tentativas, você consegue escapar.\n'
    'Você tem dois caminhos de escolha, podendo ir para direita ou para esquerda...\n'
)

escolha_corredor = input('Para qual lado você vai? ').lower()
if escolha_corredor == 'direita':
    print(
        'Você vai pela direita passando pelas outras celas e não vê nada além de corpos em decomposição. No final, à sua esquerda, você vê uma entrada.\n'
          'Ao espiar pela entrada você vê uma capivara grande, de aproximadamente 2 metros, usando um avental sujo de sangue e na mesa há pedaços de carne fresca.\n'
          'Como ela está de costas para você, você pode tentar se esgueirar por trás dela, mas claro que há uma chance de dar errado')
elif escolha_corredor == 'esquerda': 
    print('Você decide ir para a esquerda e encontra uma porta de metal, mas infelizmente ela está trancada e é impossível de abrir usando grampos.\n'
          'Sua única opção é ir pela direita. Sendo assim, você vai pela direita passando pelas outras celas e não vê nada além de corpos em decomposição,\n'
          'No final, à sua esquerda, você vê uma entrada. Ao espiar pela entrada você vê uma capivara grande, de aproximadamente 2 metros de altura e\n' 
          'de costas para você, usando um avental sujo de sangue e na mesa há pedaços de carne fresca.\n')
else:
    print("Opção inválida, apenas 'direita' ou 'esquerda'!")

print('Você pode se esgueirar por ela sem fazer barulho ou tentar imobilizá-la ela dando-lhe uma panelada na cabeça com uma panela que encontrou no chão...')
print()


while True:
    escolha_açougueiro = input('O que você decide fazer? ').lower()
    if escolha_açougueiro == 'esgueirar':
        luck = random.random() #Gera um numero entre 0 e 1
        if luck <= 0.3:
            print('\nVocê tenta se esgueirar, mas o açougueiro percebe e joga o cutelo em você acertando a sua cabeça te matando instântaneamente')
            print()
            print('Você morreu. Tente novamente!') #Permite 'reviver' e tentar novamente. - Vinicius
            print()
            continue
        else:
            print('\nVocê consegue se esgueirar pelo açougueiro, abrindo a porta encontrando uma escada. Ao subi-la, chegando no andar de cima\n'
                  'você percebe que está numa casa antiga no meio de uma cidade, está de noite e está tudo silencioso. Você vê a porta da frente\n'
                  'e tenta abrir, mas está trancada, nisso você ouve passos vindo da direita, você se esconde debaixo de uma mesa e espera. E então, \n'
                  'surge uma capivara menor, ela está desarmada e desatenta, parece estar procurando por algo.\n' 
                  'você pode imobilizar ela com a sua panela...')
            escolha_desatenta=input('Você quer tentar imobilizá-la? ').lower()
            if escolha_desatenta=='sim':
                print('') #Continuação da história if 'sim' - Vinicius

            elif escolha_desatenta=='não':
                print('') #Continuação da história if 'não' - Vinicius
            
            else: 
                print()
                print("Opção inválida, apenas 'sim' ou 'não'!")
                print()
            continue
    elif escolha_açougueiro == 'imobilizar':
        luck = random.random()
        if luck <= 0.7:
            print('Você tenta imobilizar o açougueiro mas ele é muito mais forte que você, jogando você no chão, pegando-lhe pelo pescoço e golpeando-lhe\n'
                  'na barriga, fazendo suas entranhas cair no chão enquanto você morre de dor e agonia')
            print()
            print('Você morreu. Tente novamente!') #Permite 'reviver' e tentar novamente. - Vinicius
            print()
            continue
        else:
            print('Você conseguiu imobilizar o açougueiro, assim conseguindo pegar o seu cutelo. Você percebe que esse cutelo é muito afiado e é\n'
                  'uma opção perfeita para se defender de inimigos. Abrindo a porta ao lado você encontra uma escada e decide subir, chegando no andar de cima\n'
                  'você percebe que está numa casa antiga no meio de uma cidade, está de noite e está tudo silencioso, a iluminação é mais amena,\n'
                  'ficando perfeito para se esconder no escuro, você vê a porta da frente e tenta abrir, mas está trancada. Nisso, você ouve passos\n'
                  'vindo da direita. Você se esconde debaixo de uma mesa e espera.\n'
                  'Após esperar, surge uma capivara menor, ela está desarmada e desatenta, parece estar procurando por algo, e você pode matar ela\n'
                  ' com o seu cutelo...')
            escolha_desatenta=input('Você quer tentar matá-la? ').lower()
            if escolha_desatenta=='sim':
                print('') #Continuação da história if 'sim' - Vinicius

            elif escolha_desatenta=='não':
                print('') #Continuação da história if 'não' - Vinicius
            
            else: 
                print()
                print("Opção inválida, apenas 'sim' ou 'não'!")
                print()
            continue

    else: print("Opção inválida, apenas 'esgueirar' ou 'imobilizar'!")
    continue
