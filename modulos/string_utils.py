# Módulo de operações com strings


def capitalize(texto: str) -> str:
    if not texto:
        return texto
    primeira = texto[0].upper()
    restante = texto[1:].lower()

    return primeira + restante


def reverse_string(texto: str) -> str:
    if not texto:
        return texto
    inverso_texto = texto[::-1]

    return inverso_texto


def count(texto: str) -> str:
    return len(texto)
