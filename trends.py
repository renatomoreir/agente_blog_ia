from pytrends.request import TrendReq
import matplotlib.pyplot as plt

def tendencias_topicos(palavras_chave):
    pytrends = TrendReq(hl='pt-BR', tz=360)
    pytrends.build_payload(palavras_chave, cat=0, timeframe='today 3-m', geo='BR', gprop='')
    tendencias = pytrends.interest_over_time()

    # pytrends.build_payload(["destinos turísticos"], cat=0, timeframe="today 3-m", geo="BR", gprop="")
    # related_queries = pytrends.rGelated_queries()

    # trending_searches = pytrends.trending_searches(pn="brazil")

    plt.figure(figsize=(12,6))
    for destino in palavras_chave:
        plt.plot(tendencias.index, tendencias[destino], label=destino)

    plt.title("Interesse por Destinos (Últimos 3 meses)")
    plt.xlabel("Data")
    plt.ylabel("Interesse")
    plt.legend()
    plt.grid()
    plt.show()

    
    return tendencias