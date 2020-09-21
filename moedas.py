import locale

locale.setlocale(locale.LC_MONETARY, 'en_US.UTF-8')
valor_em_dolar_formatado_baixo = locale.currency(12.4593681, grouping=True)
valor_em_dolar_formatado_alto = locale.currency(15000.0, grouping=True)
print(valor_em_dolar_formatado_baixo)
print(valor_em_dolar_formatado_alto)

locale.setlocale(locale.LC_MONETARY, 'pt_BR.UTF-8')
valor_em_reais_formatado_baixo = locale.currency(12.4593681, grouping=True)
valor_em_reais_formatado_alto = locale.currency(15000.0, grouping=True)
print(valor_em_reais_formatado_baixo)
print(valor_em_reais_formatado_alto)



