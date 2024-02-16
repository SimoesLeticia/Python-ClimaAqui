# Python ClimaAqui
O *Python-ClimaAqui* é um programa que realiza previsões meteorológicas para os próximos cinco dias através da geolocalização do usuário.

## Estrutura do Repositório
Este repositório está organizado da seguinte forma:
| **Diretórios/Arquivos**            | **Descrição**                                                                                     |
|:-----------------------------------|:--------------------------------------------------------------------------------------------------|
| **fontes**                         |                                                                                                   |
| `ClimaAqui_Funcoes.py`             | Este arquivo contém funções que interagem com as APIs para obter as informações meteorológicas.   |
| `ClimaAqui_Principal.py`           | Este arquivo contém a chamada da função principal responsável por exibir as previsões climáticas. |
| **exemplos**                       |                                                                                                   |
| `ClimaAqui_Exemplo_Terminal.txt`   | Um arquivo de texto que demonstra como as previsões são exibidas no terminal.                     |
| `ClimaAqui_Exemplo_Notebook.ipynb` | Um notebook que demonstra as previsões meteorológicas de forma mais interativa.                   |

## Pré-requisitos
Antes de executar *Python-ClimaAqui*, certifique-se de ter instaladas as seguintes bibliotecas Python: **`requests`**, **`datetime`**.

Você pode instalá-las executando o seguinte comando em seu terminal:
```
pip install requests datetime
```
- Também é essencial obter uma **API Key** registrando-se gratuitamente no site [AccuWeather Developer](https://developer.accuweather.com). Sem essa chave, não será possível realizar as requisições. É importante observar que existe um limite de requisições por **API Key**.

## Recursos Utilizados
O *Python-ClimaAqui* utiliza duas APIs:
### [IPInfo](https://ipinfo.io)
É um serviço de geolocalização que fornece informações sobre a localização de um dispositivo com base no seu endereço IP, incluindo latitude, longitude, cidade, país e provedor de internet.
### [AccuWeather](https://www.accuweather.com)
É um serviço de previsão do tempo. Sua API oferece uma ampla gama de dados climáticos, incluindo previsões horárias, diárias e de longo prazo, alertas meteorológicos e informações históricas.

## Contribuições
Contribuições são sempre bem-vindas! Se você tem sugestões de melhorias, encontrou algum bug ou simplesmente quer dizer "olá 👋🏽", sinta-se à vontade para abrir uma issue ou enviar um pull request.
