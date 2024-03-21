import yfinance as yf
import os
import openai 

# Obtenemos los datos de la acción
ticker_symbol = "^GSPC"
stock = yf.Ticker(ticker_symbol)

# Extraemos la información
info = stock.info

# Seleccionamos los datos específicos a analizar, como los últimos precios de cierre
history = stock.history(period="1mo")['Close']

# Calculamos el resumen de los datos históricos
max_price = max(history)
min_price = min(history)
avg_price = sum(history) / len(history)
historical_data_summary = (
    f"Analiza los datos históricos de {ticker_symbol} del último mes: {history.tolist()}\n"
    "y analízalos como si fueras el mejor trader del mundo, para decirme cuál es la tendencia."
)

# Establece la API key (asegúrate de que tu clave de API esté configurada en las variables de entorno)
api_key = os.getenv("Tu API key de OpenAI")
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
    print("No se recibió respuesta válida del API")
