import requests

class Boleto:
    def __init__(self, sh_cnpj=None, sh_token=None, cedente_cnpj=None, testing=True):
        self.sh_cnpj = sh_cnpj
        self.sh_token = sh_token
        self.cedente_cnpj = cedente_cnpj
        self.testing = testing
        self.headers = {
            "Content-Type": "application/json",
            "cnpj-sh": self.sh_cnpj,
            "token-sh": self.sh_token,
            "cnpj-cedente": self.cedente_cnpj
        }
        if testing:
            self.url = "http://homologacao.plugboleto.com.br/api/v1"
        else:
            self.url = "http://plugboleto.com.br/api/v1"

    def cadastrar_cedente(self, payload):
        cedenteHeader = {
            "Content-Type": "application/json",
            "cnpj-sh": self.sh_cnpj,
            "token-sh": self.sh_token
        }
        response = requests.post(self.url + "/cedentes",headers=cedenteHeader, json=payload)
        return response.json()

    def cadastrar_conta(self, payload):
        response = requests.post(self.url + "/cedentes/contas", headers=self.headers, json=payload)
        return response.json()

    def cadastrar_convenio(self, payload):
        response = requests.post(self.url + "/cedentes/contas/conveniosz", headers=self.headers, json=payload)
        return response.json()

    def alterar_cedente(self, id):
        url = "{base_url}/cedentes/{id}".format(base_url=self.url, id=id)
        response = requests.put(url, headers=self.headers)

    def alterar_conta(self, id):
        url = "{base_url}/cedentes/contas/{id}".format(base_url=self.url, id=id)
        response = requests.put(url, headers=self.headers)

    def alterar_convenio(self, id):
        url = "{base_url}/cedentes/contas/convenios/{id}".format(base_url=self.url, id=id)
        response = requests.put(url, headers=self.headers)

    def consultar_boletos(self, id=None):
        if id:
            url = "{base_url}/boletos?idintegracao={idintegracao}".format(
                base_url=self.url, idintegracao=id)
        else:
            url = "{url}/boletos".format(url=self.url)
        response = requests.get(url, headers=self.headers)
        return response.json()

    def gerar_boleto(self, payload):
        response = requests.post(self.url + "/boletos/lote", headers=self.headers, json=payload)
        return response.json()

    def gerar_remessa(self, payload):
        response = requests.post(self.url + "/remessas/lote", headers=self.headers, json=payload)
        return response.json()

    def solicitar_impressao(self, payload):
        response = requests.post(self.url + "/boletos/impressao/lote", headers=self.headers, json=payload)
        return response.json()

    def consultar_impressao(self, protocolo):
        url = "{base_url}/boletos/impressao/lote/{protocolo}".format(base_url=self.url, protocolo=protocolo)
        response = requests.get(url, headers=self.headers)
        return response.content

    def enviar_email(self, payload):
        response = requests.post(self.url + "/email/lote", headers=self.headers, json=payload)
        return response.json()

    def consultar_email(self, protocolo):
        url = "{base_url}/email/lote/{protocolo}".format(base_url=self.url, protocolo=protocolo)
        response = requests.get(url, headers=self.headers)
        return response.json()

    def gerar_remessa_alteracao(self, payload):
        response = requests.post(self.url + "/boletos/altera/lote", headers=self.headers, json=payload)
        return response.json()

    def consultar_remessa_alteracao(self, protocolo):
        url = "{base_url}/boletos/altera/lote/{protocolo}".format(base_url=self.url, protocolo=protocolo)
        response = requests.get(url, headers=self.headers)
        return response.json()

    def gerar_remessa_baixa(self, payload):
        response = requests.post(self.url + "/boletos/baixa/lote", headers=self.headers, json=payload)
        return response.json()

    def consultar_remessa_baixa(self, protocolo):
        url = "{base_url}/boletos/baixa/lote/{protocolo}".format(base_url=self.url, protocolo=protocolo)
        response = requests.get(url, headers=self.headers)
        return response.json()

    def processar_retorno(self, payload):
        response = requests.post(self.url + "/retornos", headers=self.headers, json=payload)
        return response.json()

    def consultar_retorno(self, protocolo):
        url = "{base_url}/retornos/{protocolo}".format(base_url=self.url, protocolo=protocolo)
        response = requests.get(url, headers=self.headers)
        return response.json()

    def descartar_boleto(self, payload):
        response = requests.post(self.url + "/boletos/descarta/lote", headers=self.headers, json=payload)
        return response.json()

    def cadastrar_email(self, payload):
        response = requests.post(self.url + "/email/config", headers=self.headers, json=payload)
        return response.json()

    def cadastrar_notificao_eventp(self, payload):
        response = requests.post(self.url + "/eventos/agendamentos", headers=self.headers, json=payload)
        return response.json()
