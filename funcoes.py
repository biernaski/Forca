from palavra import *

def jogar():
    indice = random.randint(0,len(palavra_secreta))
    adivinhar = palavra_secreta[indice].lower()
    adivinhar = ['_'] * len(adivinhar)
    chances = 0
    letras_digitadas = []
    
    while chances < 6:
        os.system('cls')
        print(boneco[chances])
        print(f"---  {"".join(adivinhar)}  ---\n")
        print(f"Letras já digitadas: {letras_digitadas}")
        letra = input("Digite uma letra: ").lower() # Deixa a letra sempre minuscula
    
        if letra in letras_digitadas:
            print("Você já digitou essa letra")
        
        letras_digitadas.append(letra) # Lista das letras já digitadas
        
        if letra.isalpha() and len(letra) == 1:
            if letra in palavra_secreta[indice].lower(): # Verifica se a letra digitada está na palavra secreta, caso sim, altera a letra na variável adivinhar
                for i, char in enumerate(palavra_secreta[indice].lower()): 
                    if letra == char:
                        adivinhar[i] = letra
            else:
                chances += 1
                if chances >= 6: # Verifica se o usuário perdeu ou não
                    os.system('cls')
                    print(boneco[chances])
                    print(f"A palavra era : {palavra_secreta[indice].lower()}")
                    print("Você perdeu :(\n")
                    break
        else:
            print(f"'{letra}' não é uma letra.")
            letras_digitadas.pop() # Remove o último valor digitado que não foi uma letra
            time.sleep(3)

        if "".join(adivinhar) == palavra_secreta[indice].lower(): # Verifica se o usuário ganhou ou não acertando a palavra
            os.system('cls')
            print(f"---  {"".join(adivinhar)}  ---\n")
            print("Você venceu :) \n")
            break

def menu():
    while True:
        print("\nSeja bem vindo ao jogo da forca.")
        print("Selecione a opção:\n1 - Jogar\n2 - Sair")
        opcao = input("Digite o numero: ")

        if opcao == '2':
            os.system('cls')
            print("Obrigado por jogar.\n")
            break
        elif opcao != '1':
            os.system('cls')
            print("Opção inváilida. Tente novamente...\n")
        else:
            os.system('cls')
            jogar()