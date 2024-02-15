import requests
import json
from datetime import datetime, timedelta, timezone

ACCUWEATHER_API_KEY = "[Digite aqui sua API Key	do AccuWeather]"

def consultar_geolocalizacao():
    # ipinfo.io: Retorna a geolocalização com base no IP do usuário.
    try:
        IPINFO_API_URL = "https://ipinfo.io/json"

        response = requests.get(IPINFO_API_URL)
        response.raise_for_status()

        localizacao = json.loads(response.text)

        if "loc" not in localizacao:
            print("Não foi possível obter a localização do usuário.")
            return None

        return localizacao
    except requests.exceptions.RequestException as e:
        print(f"Falha na requisição para obter localização. Erro: {e}")
    return None

def consultar_chave_geolocalizacao(geolocalizacao):
    # AccuWeather - Geoposition Search: Retorna uma chave específica de localização com base na latitude e longitude.
    try:
        ACCUWEATHER_GEOPOSITION_URL = "http://dataservice.accuweather.com/locations/v1/cities/geoposition/search"

        latitude, longitude = geolocalizacao["loc"].split(",")
        params = {
            "apikey"  : ACCUWEATHER_API_KEY,
            "q"       : f"{latitude},{longitude}",
            "language": "pt-br",
            "details" : "false"
        }

        response = requests.get(ACCUWEATHER_GEOPOSITION_URL, params=params)
        response.raise_for_status()

        localizacao_chave = json.loads(response.text)

        if "Key" not in localizacao_chave:
            print("Não foi possível obter código da localização do usuário.")
            return None

        return localizacao_chave["Key"]
    except requests.exceptions.RequestException as e:
        print(f"Falha na requisição para obter código da localização. Erro: {e}")
    return None

def consultar_previsoes_5Dias(geolocalizacao):
    # AccuWeather - 5 Days of Daily Forecasts: Retorna previsões diárias para os próximos 5 dias em uma localização específica.
    try:
        geolocalizacao_chave = consultar_chave_geolocalizacao(geolocalizacao)

        if geolocalizacao_chave is None:
            return None

        ACCUWEATHER_FORECAST_URL = "http://dataservice.accuweather.com/forecasts/v1/daily/5day/"
        URL = f"{ACCUWEATHER_FORECAST_URL}{geolocalizacao_chave}"

        params = {
            "apikey"  : ACCUWEATHER_API_KEY,
            "language": "pt-br",
            "details" : "true",
            "metric"  : "true"
        }

        response = requests.get(URL, params=params)
        response.raise_for_status()

        previsoes_5Dias = json.loads(response.text)

        if "DailyForecasts" not in previsoes_5Dias:
            print("Não foi possível obter as previsões meteorológicas para a localização do usuário.")
            return None

        return previsoes_5Dias
    except requests.exceptions.RequestException as e:
        print(f"Falha na requisição para obter as previsões meteorológicas. Erro: {e}")
    return None

def converter_data(epochdate):
    # Mapear dias da semana
    dias_semana = ["Domingo", "Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado"]

    data_atual  = datetime.today().date()
    data        = datetime.fromtimestamp(epochdate, timezone.utc).date()

    dia_atual = ""
    if data == data_atual:
        dia_atual = "Hoje, "
    elif data == data_atual + timedelta(days=1):
        dia_atual = "Amanhã, "

    data_convertida = {
        "dia_atual" : dia_atual,
        "data"      : data.strftime("%d/%m/%Y"),
        "dia_semana": dias_semana[int(data.strftime("%w"))]
    }
    return data_convertida

def montar_previsoes_5Dias():
    geolocalizacao  = consultar_geolocalizacao()
    previsoes_5Dias = consultar_previsoes_5Dias(geolocalizacao)

    if not geolocalizacao or not previsoes_5Dias:
        print("Não foi possível obter as informações necessárias.")
        return None

    lista_previsoes_5Dias = []
    for dia in previsoes_5Dias["DailyForecasts"]:
        data_convertida = converter_data(dia["EpochDate"])
        previsao_diaria = {
            "data"      : data_convertida["data"],
            "dia_atual" : data_convertida["dia_atual"],
            "dia_semana": data_convertida["dia_semana"],
            "minima"    : dia["Temperature"]["Minimum"]["Value"],
            "maxima"    : dia["Temperature"]["Maximum"]["Value"],
            "clima"     : dia["Day"]["IconPhrase"],
            "chuva"     : dia["Day"]["RainProbability"],
            "umidade"   : dia["Day"]["RelativeHumidity"]["Average"],
            "vento"     : dia["Day"]["Wind"]["Speed"]["Value"]
        }
        lista_previsoes_5Dias.append(previsao_diaria)

    # Monta texto das previsões meteorológicas
    cidade = geolocalizacao["city"]
    regiao = geolocalizacao["region"]

    linha_separador = "____________________________________________________________"
    linha_cabecalho = f"Previsão para {cidade}, {regiao}."
    linha_corpo = linha_cabecalho

    for dia in lista_previsoes_5Dias:
        linha_corpo += (
            f"\n{linha_separador}\n"
            f"{dia["dia_atual"]}{dia["dia_semana"]}, {dia["data"]}\n"
            f"Temperatura : ⬇️ {dia["minima"]}ºC ⬆️ {dia["maxima"]}ºC\n"
            f"Clima       : {dia["clima"]}\n"
            f"Chuva       : {dia["chuva"]}%\n"
            f"Umidade     : {dia["umidade"]}%\n"
            f"Vento       : {dia["vento"]} km/h"
        )

    linha_corpo += f"\n{linha_separador}"
    return linha_corpo