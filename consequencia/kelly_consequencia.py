'''
Definir onde os arquivos serão salvos;
será definido o nome do arquivo;
o app será escrito e lido;
usando o log win+. se cria os emoji;
a lista SEMPRE começa vazia;
ao escrever o itém será colocado em novas linhas;

'''

NOME_ARQUIVO = "meus_desejos.txt"
desejos = []

try: 
    with open(meus_desejos, 'r', encoding= 'utf-8') as arquivo:
        for linha in arquivo:

            desejos.append(linha.strip())
    print(f"Meus desejos foram carregados do arquivo '{meus_desejos}'!\n")
except FileNotFoundError:
    print("Parece que é sua primeia vez! Vamos cias sua lista de desejos. \n")
except Exception as e:
    print(f"Ocorreu um erro ao carregar os desejos: {e}")

def salvar_desejos(lista_de_desejos):
    try: 
        with open(meus_desejos, 'w', encoding='utf-8') as arquivo:
            for desejo in lista_de_desejos: 
                arquivo.write(desejo + "n")
    print("\n✅ Seus desejos foram salvos com suceso!")
except Exception as e:
    print(f"\n❌ Erro ao salvar os desejos: {e}")

while True: 
    print("\n--- O que voc~e quer fazer? ---")
    print("1 - Adicionar um novo desejo")
    print("2 - Ver meus desejos")
    print("3 - Sair")

opcao = input("Digite sua opção (1,2 ou 3): ")


     