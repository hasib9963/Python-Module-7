class Shopping:
    cart = [] # class attribute or static attribute
    origin = 'china'

    def __init__(self, name, location) -> None:
        self.name = 'Jamuna future park' # instance attribute
        self.location = 'Bashundhara city'

    def purchase(self, item, price, amount):
        remaining = amount - price 
        print(f'Buying: {item} for price: {price} and remaining: {remaining}')

    @staticmethod
    def multifly(a, b):
        result = a * b 
        print(result) 

    @classmethod
    def hudai_dekhi(self, item):
        print('Hudai dekhmu kintu kinmu na just ac er hawa khaite asci', item)


basundara = Shopping('Jamuna future park', 'Badda')
# basundara.purchase('Google pixel 8 pro', 104000, 150000)
basundara.hudai_dekhi('lungi')
# Shopping.purchase(2, 3, 3)
Shopping.hudai_dekhi('Lungi')

Shopping.multifly(12, 13) # static method
# basundara.multifly(88, 12)