import re


def validar_contatos(contatos):
    padrao_nome = r"Nome:\s*([A-Z][a-z]+(?:\s[A-Z][a-z]+)?)"
    padrao_email = r"Email:\s*([a-zA-Z0-9.%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})"
    padrao_telefone = r"Telefone:\s*(\(\d{2}\)\s\d{5}-\d{4}|\d{5}-\d{4})"

    for contato in contatos:
        nome_match = re.search(padrao_nome, contato)
        email_match = re.search(padrao_email, contato)
        telefone_match = re.search(padrao_telefone, contato)

        if nome_match and email_match and telefone_match:
            nome = nome_match.group(1)
            email = email_match.group(1)
            telefone = telefone_match.group(1)
            print(f"Contato válido: Nome:{nome}, Email:{email}, Telefone:{telefone}")
        else:
            print(f"Contato Inválido: {contato}")


contatos_exemplo = [
    "Nome: Alice Silva, Email: alice.silva@example.com, Telefone: (11) 98765-4321",
    "Nome: Bob Santos, Email: bobSantos@example.com, Telefone: (11) 98865-4321",
    "Nome: Jorge , Email: jorge@example.com, Telefone: (11) 98764-4321",
    "Nome: Contato Errado Teste, Email: contato.silva@example.com, Telefone: (11) 9876-4321",
    "Nome: Contato Errado Email: contato.silvaexample.com, Telefone: (11) 99876-4321",
]

validar_contatos(contatos_exemplo)
