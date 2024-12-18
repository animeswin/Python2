nome = input("Insira o nome do contato: ")
telefone = input("Insira o número de telefone: ")
email = input("Insira o endereço de email: ")

contato = {
    "Nome": nome,
    "Telefone": telefone,
    "Email": email
}

print("\nInformações do Contato:")
print(f"Nome: {contato['Nome']}")
print(f"Telefone: {contato['Telefone']}")
print(f"Email: {contato['Email']}")