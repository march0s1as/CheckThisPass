# -*- coding: utf-8 -*-
# imports aqui, meu bem.
import sys
import hashlib
import requests
from time import sleep
import os
# cores aqui.
fVermelho = "\033[1;31m"
tVerde = "\033[1;32m"
tAmarelo = "\033[1;33m"
tBranco = "\033[1;97m"
# início do script.
def senhas(pwd):
    sha1pwd = hashlib.sha1(pwd.encode('utf-8')).hexdigest().upper()
    head, tail = sha1pwd[:5], sha1pwd[5:]
    url = 'https://api.pwnedpasswords.com/range/' + head
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError('Erro encontrado: "{}": {}'.format(
            url, res.status_code))
    hashes = (line.split(':') for line in res.text.splitlines())
    count = next((int(count) for t, count in hashes if t == tail), 0)
    return sha1pwd, count
            
def menu_principal(args):
  pwd = args.strip()
  if pwd == "":
    print(fVermelho + "Campo não preenchido! >:(")
  else:
    try:
      sha1pwd, count = senhas(pwd)
      if count:
        inicio()
        deubom = fVermelho + """┌─ {0} foi identificada com {1} ocorrências.
└──╼ {2}"""
        print(deubom.format(pwd, count, sha1pwd))
      else:
        inicio()
        print(tVerde + """┌─ {} não foi encontrada.
└──╼ https://discord.gg/v5d3PZ9""".format(pwd))
    except UnicodeError:
      erro = sys.exc_info()[1]
      inicio()
      print(fVermelho + "{0} não pôde ser verificada: {1}".format(pwd, erro))

def inicio():
  os.system(['clear', 'cls'][os.name == 'nt'])
  print(tAmarelo + """
  ┌─┐┬ ┬┌─┐┌─┐┬┌─  ┌┬┐┬ ┬┬┌─┐  ┌─┐┌─┐┌─┐┌─┐
  │  ├─┤├┤ │  ├┴┐   │ ├─┤│└─┐  ├─┘├─┤└─┐└─┐
  └─┘┴ ┴└─┘└─┘┴ ┴   ┴ ┴ ┴┴└─┘  ┴  ┴ ┴└─┘└─┘""")
  print(tBranco + "        https://github.com/march0s1as")
  print(" ")
  sleep(1)
inicio()
Password = input(tBranco + """┌─Insira a senha
└──╼ """)
menu_principal(Password)
