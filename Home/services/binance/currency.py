from currency_converter import CurrencyConverter

class Currency:
    def __init__(self, USD_value):
        self.currencyConverter = CurrencyConverter()
        self.USD = round(USD_value,2)
        self.AUD = round(self.currencyConverter.convert(USD_value,"USD", "AUD"),2)



#print(c.convert(100, 'AUD','USD'))