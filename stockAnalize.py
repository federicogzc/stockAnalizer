import yfinance as yf
import os
import openai 
                                    #yahoo finances
#obtenemos los datos de la acción
ticker_symbol = "MSFT"
stock = yf.Ticker(ticker_symbol)

#Extraemos la información
info = stock.info

#Aquí vamos a seleccionar los datos especificos que deseemos analizar
#por ejemplo los ultimos precios de cierre
history= stock.history(period="1mo")['Close']

#Preparamos un resumen de los datos para la solicitud de OpenAI
#Por ejemplo un resumen textual de los datos
import yfinance as yf
import os
import openai 
                                    #yahoo finances
#obtenemos los datos de la acción
ticker_symbol = "^GSPC"
stock = yf.Ticker(ticker_symbol)

#Extraemos la información
info = stock.info

#Aquí vamos a seleccionar los datos especificos que deseemos analizar
#por ejemplo los ultimos precios de cierre
history= stock.history(period="1mo")['Close']

#Preparamos un resumen de los datos para la solicitud de OpenAI
#Por ejemplo un resumen textual de los datos
max_price = max(history)
min_price = min(history)
avg_price = sum(history) / len(history)
historical_data_summary = (
    f"analiza los datos historicos de {ticker_symbol} del ultimo mes: {history.tolist()}\n y analizalos como si fueras el mejor trader del mundo, para decirme caul es la tendencia"
)

                                      #OpenAI

# Establece la API key (asegúrate de que tu clave de API esté configurada en las variables de entorno)
api_key = ("Tu Apykey de OpenAI")
if api_key is None:
    raise ValueError("La API key no está configurada correctamente")

# Crea el cliente de OpenAI
client = openai.OpenAI(api_key=api_key)

# Hacemos la solicitud a OpenAI para analizar los datos
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": historical_data_summary,
        }
    ],
)

# Imprimimos la respuesta
if response.choices and response.choices[0].message:
    print(response.choices[0].message.content.strip())
else:
    print("No se resibió respuesta válida del API")

                                      #OpenAI

# Establece la API key (asegúrate de que tu clave de API esté configurada en las variables de entorno)
api_key = ("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")
if api_key is None:
    raise ValueError("La API key no está configurada correctamente")

# Crea el cliente de OpenAI
client = openai.OpenAI(api_key=api_key)

# Hacemos la solicitud a OpenAI para analizar los datos
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": historical_data_summary,
        }
    ],
)

# Imprimimos la respuesta
if response.choices and response.choices[0].message:
    print(response.choices[0].message.content.strip())
else:
    print("No se resibió respuesta válida del API")