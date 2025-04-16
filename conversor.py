import requests

class Conversor:
    def __init__(self, chave_api):
        self.chave_api = chave_api
        self.url = f"https://v6.exchangerate-api.com/v6/{self.chave_api}/latest/USD"

    def obter_taxas(self):
        response = requests.get(self.url)
        if response.status_code == 200:
            return response.json()["conversion_rates"]
        else:
            print("Erro ao obter dados da API.")
            return None
        
        def converter(self, valor, moeda_origem, moeda_destino):
            taxas = self.obter_taxas()
            if taxas:
                if moeda_origem != "USD":
                    valor_em_usd = valor / taxas[moeda_origem]
                else:
                    valor_em_usd = valor

                valor_convertido = valor_em_usd * taxas[moeda_destino]
                return round(valor_convertido, 2)
            else:
                return None