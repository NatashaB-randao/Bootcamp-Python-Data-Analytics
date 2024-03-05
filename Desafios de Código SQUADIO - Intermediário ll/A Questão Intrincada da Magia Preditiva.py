# Descrição
# No reino mágico onde cada feiticeiro possui uma afinidade elemental única, seu desafio é criar um modelo de machine learning para prever essa afinidade. Os feiticeiros podem pertencer a um dos quatro elementos mágicos: Fogo, Água, Terra ou Ar. A predição será baseada em cinco atributos mágicos: intensidade do feitiço, presença de componente raro, fase lunar, idade do feiticeiro e afinidade com animais mágicos.

# Aqui estão os critérios mágicos para cada elemento:

# Elemento Fogo:

# Intensidade do feitiço maior ou igual a 5.
# Fase lunar durante o feitiço é crescente.
# Idade do feiticeiro é superior a 100 anos.
# Elemento Água:

# Intensidade do feitiço maior ou igual a 7.
# Presença de componente raro.
# Fase lunar durante o feitiço é cheia.
# Idade do feiticeiro é igual ou inferior a 100 anos.
# Afinidade com animais mágicos.
# Elemento Terra:

# Intensidade do feitiço maior ou igual a 7.
# Presença de componente raro.
# Fase lunar durante o feitiço é cheia.
# Idade do feiticeiro é igual ou inferior a 100 anos.
# Afinidade com animais mágicos.
# Elemento Ar:

# Caso não se encaixe nos critérios anteriores.



# Função para prever a afinidade elemental do feiticeiro
def prever_afinidade_elemental(intensidade, componente_raro, fase_lunar, idade_feiticeiro, afinidade_animais):
    # Convertendo a resposta do componente raro e afinidade com animais para booleanos
    componente_raro = componente_raro.strip().lower() == "sim"
    afinidade_animais = afinidade_animais.strip().lower() == "sim"

    # Desenvolvendo a Lógica de decisão para prever a afinidade elemental
    if intensidade >= 5 and fase_lunar.strip() == "crescente" and idade_feiticeiro > 100:
        return "A afinidade elemental do feiticeiro é com o elemento Fogo!"
    elif intensidade >= 7 and componente_raro and fase_lunar.strip() == "cheia":
        if idade_feiticeiro <= 100 and afinidade_animais:
            return "A afinidade elemental do feiticeiro é com o elemento Terra!"
        else:
            return "A afinidade elemental do feiticeiro é com o elemento Água!"
    else:
        return "A afinidade elemental do feiticeiro é com o elemento Ar!"

# Entrada do usuário
intensidade_feitico = int(input())
componente_raro_feitico = input()
fase_lunar_feitico = input()
idade_feiticeiro = int(input ())
afinidade_animais_feiticeiro = input()

# Fazendo a previsão
resultado = prever_afinidade_elemental(intensidade_feitico, componente_raro_feitico, fase_lunar_feitico, idade_feiticeiro, afinidade_animais_feiticeiro)

# Saída da previsão