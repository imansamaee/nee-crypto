from currency_converter import CurrencyConverter

class Currency:
    def __init__(self, USD_value):
        self.currencyConverter = CurrencyConverter()
        self.USD = USD_value
        self.USD_round = round(USD_value,2)
        self.AUD = self.currencyConverter.convert(USD_value,"USD", "AUD")
        self.AUD_round = round(self.AUD,2)




#print(c.convert(100, 'AUD','USD'))