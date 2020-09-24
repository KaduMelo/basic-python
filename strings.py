argumento = "www.facebook.com.br?moedaorigem=real"
index = argumento.find("=")
print(argumento[index + 1:])

list_argumento = argumento.split("=")
print(list_argumento)