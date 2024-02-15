import ClimaAqui_Funcoes as funcoes

# Chamada da API
visualizacao = funcoes.montar_previsoes_5Dias()

# Saída
if visualizacao:
    print(visualizacao)