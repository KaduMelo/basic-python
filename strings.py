argumento = "www.facebook.com.br?moedaorigem=real"
index = argumento.find("=")
print(argumento[index + 1:])

list_argumento = argumento.split("=")
print(list_argumento)

url = 'www.bytebank.com.br/cambio?valor=1500&moedaOrigem=real&moedaDestino=dolar'
pega_argumentos_url = url.find("?")
list_argumentos = url[pega_argumentos_url + 1:].split("&")

for argumento in list_argumentos:
    index = argumento.find("=")
    print(argumento[index + 1:])
