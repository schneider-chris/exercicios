import json

arquivo_cadastros = "cadastros.json"

def exibir_menu():
    print("\n ---- MENU CADASTROS ----")
    print("1 - Novo cadastro")
    print("2 - Ver cadastros")
    print("3 - Sair")
    print("----------------------")

def salvar_cadastros (cadastros):
    with open (arquivo_cadastros, "w", encoding="utf-8") as arquivo:
        json.dump(cadastros, arquivo, indent=4, ensure_ascii=False)

def carregar_cadastros():
    try:
        with open (arquivo_cadastros, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

def cadastrar_pessoa(cadastros):
    nome = input("Nome: ")
    idade = input("Idade: ")
    turma = input("Turma: ")
    curso = input("Curso: ")
    cadastros.append({"Nome": nome, "Idade": idade, "Turma": turma, "Curso": curso})
    salvar_cadastros(cadastros)
    print("Cadastro finalizado com sucesso")

    def ver_cadastros(cadastros):
        if not cadastros:
            print("\n Nenhum cadastro no sistema")
        else:
            print("\n-------Lista de Cadastros------")
            for i, pessoa in enumerate(cadastros, 1):
                print(f"{i} . Nome: {pessoa['Nome']}, Idade: 
{pessoa['Idade']}, Turma: {pessoa['Turma']}, Curso: {pessoa['Curso']}")
    input("\n Pressione Enter para voltar ao menu...")

def main():
    cadastros = carregar_cadastros()
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção:")
        if opcao == "1":
            cadastrar_pessoa(cadastros)
        elif opcao == "2":
            ver_cadastros(cadastros)
        elif opcao == "3":
            print("Obrigado por usar o sistema de cadastro!")
            break
        else:
            print("Opção inválida! Tente Novamente.")

if __name__=="__main__":
    main()