import yfinance as yf
import openai
import os


def get_stock_history(ticker_symbol, start_date, end_date, period):
    stock = yf.Ticker(ticker_symbol)
    history = stock.history(start=start_date, end=end_date)
    return history

def calculate_statistics(data):
    return max(data), min(data), sum(data) / len(data)

def create_summary(ticker_symbol, data, analysis_type):
    max_val, min_val, avg_val = calculate_statistics(data)
    return (
        f"Para {ticker_symbol}, en los datos {analysis_type}, "
        f"el valor máximo es {max_val}, el valor mínimo es {min_val}, "
        f"y el valor promedio es {avg_val}.\n"
        "Basado en estos valores y el volumen de operaciones, dime la tendencia mas probable que puede continuar. Solo dame la respuesta tecnica de como llegas a esa conclusión"
    )

# Configuración
ticker_symbol = "^GSPC"
start_date = "2024-01-01"
end_date = "2024-03-20"
api_key = ("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")

if api_key is None:
    raise ValueError("La API key no está configurada correctamente")

# Obtener datos de la acción
history = get_stock_history(ticker_symbol, start_date, end_date, period="1mo")
volume_summary = create_summary(ticker_symbol, history['Volume'], "de volumen")
price_summary = create_summary(ticker_symbol, history['Close'], "históricos")

# Crea el cliente de OpenAI
client = openai.OpenAI(api_key=api_key)

# Función para hacer la solicitud a OpenAI
def get_openai_analysis(summary):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": summary}],
    )
    return response.choices[0].message.content.strip() if response.choices and response.choices[0].message else "No se recibió respuesta válida del API"

# Imprimir las respuestas de OpenAI
print(get_openai_analysis(volume_summary))
print(get_openai_analysis(price_summary))
