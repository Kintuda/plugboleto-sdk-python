from Boleto import Boleto
import json
import base64

# Instanciando a classe
boleto = Boleto('CPNJ-SH',
                'TOKEN-SH', 'CEDENTE-CPFCNPJ', 2)

def cadastrar_cedente():
    with open('jsonExample.json') as examples:
        payload = json.load(examples)
        data = payload["cedente_cadastro_exemplo"]
        boleto.cadastrar_cedente(data)


def cadastrar_conta():
    with open('jsonExample.json') as examples:
        payload = json.load(examples)
        data = payload["conta_exemplo"]
        boleto.cadastrar_conta(data)


def cadastrar_convenio():
    with open('jsonExample.json') as examples:
        payload = json.load(examples)
        data = payload["convenio_exemplo"]
        boleto.cadastrar_convenio(data)


def incluir_boleto():
    with open('jsonExample.json') as examples:
        payload = json.load(examples)
        data = payload["boleto_exemplo"]
        boleto = boleto.gerar_boleto(data)
        print(boleto)


def consultar_boleto(idintegracao=None):
    boleto = boleto.consultar_boletos(idintegracao)
    print(boleto)


def gerar_remessa(idintegracao):
    if isinstance(idintegracao, list):
        remessa = boleto.gerar_remessa(idintegracao)
        print(remessa["_dados"]["_sucesso"])
    else:
        remessa = boleto.gerar_remessa([idintegracao])
    for rem in remessa["_dados"]["_sucesso"]:
        f = open(rem["arquivo"], "w+")
        content = rem["remessa"]
        f.write(base64.b64decode(content))
        f.close()


def gerar_impressao():
    with open('jsonExample.json') as examples:
        payload = json.load(examples)
        data = payload["impressao_exemplo"]
        resposta = boleto.solicitar_impressao(data)


def arquivo_impressao(protocolo):
    f = open("impressao.pdf", "wb")
    file = boleto.consultar_impressao(protocolo)
    f.write(file)
    f.close()

def enviar_email():
     with open('jsonExample.json') as examples:
        payload = json.load(examples)
        data = payload["email_exemplo"]
        resposta = boleto.enviar_email(data)
        print(resposta)

def remessa_alteracao():
    with open('jsonExample.json') as examples:
        payload = json.load(examples)
        data = payload["remessa_alteracao_exemplo"]
        resposta = boleto.gerar_remessa_alteracao(data)
        print(resposta)

def arquivo_alteracao(protocolo):
    remessa = boleto.consultar_remessa_alteracao(protocolo)
    for rem in remessa["_dados"]["_sucesso"]:
        f = open(rem["arquivo"], "w+")
        content = rem["remessa"]
        f.write(base64.b64decode(content))
        f.close()

def remessa_baixa():
    with open('jsonExample.json') as examples:
        payload = json.load(examples)
        data = payload["baixa_exemplo"]
        resposta = boleto.gerar_remessa_baixa(data)
        print(resposta)

def arquivo_baixa(protocolo):
    remessa = boleto.consultar_remessa_baixa(protocolo)
    for rem in remessa["_dados"]["_sucesso"]:
        f = open(rem["arquivo"], "w+")
        content = rem["remessa"]
        f.write(base64.b64decode(content))
        f.close()
    
def upload_retorno(path):
    with open("retornoExemplo.ret", "r") as file:
        content = file.read()
        print(type(content))
        base64Content = base64.b64encode(bytes(content, 'utf-8'))
        payload = {
            "arquivo": base64Content.decode('ascii')
        }
        retorno = boleto.processar_retorno(payload)
        print(retorno)

def consultar_retorno(protocolo):
        retorno = boleto.consultar_retorno(protocolo)
        print(retorno)
