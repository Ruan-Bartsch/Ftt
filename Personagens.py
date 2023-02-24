print("="*30)
print("Vamos criar um personagem")
print("="*30)

name = []
desc = []
img = []
program = []
anim = []
  


while True:
    nome = input("Digite o nome do personagem:") 
    name.append(nome)  
    descricao = input("Digite a descrição do personagem:")
    desc.append(descricao)
    imagem = input("Coloque o link da imagem do personagem caso tenha uma:")
    img.append(imagem)
    programa = input("Digite o nome do programa do personagem:")
    program.append(programa)
    animador = input("Digite o nome do animador do personagem:")
    anim.append(animador)
    print("="*30)
    print("Personagem", nome, "criado com sucesso!!")
    print("="*30)
    novo = input("Deseja criar outro personagem? y/n?")
    if novo == "n":
        break



while True:
    print()
    pesquisa = input("Digite o nome do personagem para visualiza-lo:")
    if pesquisa in name:
        posicao = name.index(pesquisa)
        print("Nome:", name[posicao])
        print("Descrição:", desc[posicao])
        print("Imagem:", img[posicao])
        print("Programa:", program[posicao])
        print("Animador:", anim[posicao])
        break
    else :
        print("Personagem não encontrado")



    



        









   
