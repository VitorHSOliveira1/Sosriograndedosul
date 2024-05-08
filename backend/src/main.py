# Importações
import google_search
import reviews_analysis
import sentiment_analysis

# Funções
def fetch_ongs_data():
    """Busca dados das ONGs usando o módulo google_search."""
    ongs = google_search.search_ongs_in_rs()
    return ongs

def analyze_reviews(ongs):
    """Analisa as avaliações das ONGs usando o módulo reviews_analysis."""
    reviews_data = reviews_analysis.process_reviews(ongs)
    return reviews_data

def display_results(results):
    """Exibe os resultados no console ou os salva em um arquivo."""
    for result in results:
        print(f"ONG: {result['name']}, Avaliações Positivas: {result['positive_reviews']}")

# Execução
if __name__ == "__main__":
    try:
        ongs = fetch_ongs_data()
        reviews_data = analyze_reviews(ongs)
        display_results(reviews_data)
    except Exception as e:
        print(f"Erro ao executar o script: {e}")
