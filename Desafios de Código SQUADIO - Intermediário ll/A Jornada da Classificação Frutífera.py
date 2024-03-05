# Descrição
# Nesta missão, sua tarefa é mais desafiadora do que nunca! Em um pomar mágico, as frutas têm características únicas que as diferenciam. Seu objetivo é criar um modelo de machine learning capaz de classificar frutas com base em três características: peso, textura (suave ou áspera) e cor (vermelha, laranja ou amarela). Cada tipo de fruta tem limites específicos para essas características.

# Maçã:

# Peso mínimo: 130 gramas
# Textura: Ápera (rough)
# Cor: Vermelha (red)
# Laranja:

# Peso mínimo: 120 gramas
# Textura: Suave (smooth)
# Cor: Laranja (orange)
# Morango:

# Peso mínimo: 150 gramas
# Textura: Suave (smooth)
# Cor: Vermelha (red)
# Banana:

# Peso mínimo: 150 gramas
# Textura: Áspera (rough)
# Cor: Amarela (yellow)


# Função para prever a classe da fruta
def prever_fruta(peso, textura, cor):
    # Lógica de decisão baseada nas características fornecidas
    if peso >= 150 and textura == "smooth" and cor == "red":
        return "A fruta é um morango!"
    elif peso >= 130 and textura == "rough" and cor == "red":
        return "A fruta é uma maçã!"
    elif peso >= 120 and textura == "smooth" and cor == "orange":
        return "A fruta é uma laranja!"
    elif peso >= 150 and textura == "rough" and cor == "yellow":
        return "A fruta é uma banana!"
    else:
        return "Não foi possível classificar a fruta."

# Entrada do usuário
peso_fruta = float(input())
textura_fruta = input()
cor_fruta = input()

# Chamada da função de previsão
resultado = prever_fruta(peso_fruta, textura_fruta, cor_fruta)

# Saída da previsão
print(resultado)
