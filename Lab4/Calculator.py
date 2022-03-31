
class Calculator:
    def __init__(self, shops_cut: [int, float]):
        self.__shops_cut = shops_cut
        self._PLN_to_USD_rate = 4.7
        self._PLN_to_EU_rate = 4.8

    def calculate_price_usd_eu(self, price: [int, float]) -> list:
        return [price / self._PLN_to_USD_rate, price / self._PLN_to_EU_rate]

    def calculate_price_usd_eu_with_shops_cut(self, price: [int, float]) -> list:
        price_including_cut = price / (1.0 - self.__shops_cut)
        return [price_including_cut / self._PLN_to_USD_rate, price_including_cut / self._PLN_to_EU_rate]
