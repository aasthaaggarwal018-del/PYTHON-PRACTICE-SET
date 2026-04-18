class laptop:
    brand='default'
    ram='8 gb'
    price='2 lakh'


laptop_1=laptop()
laptop_1.brand='hp'
laptop_1.ram='16 gb'

laptop_2 =laptop
laptop_2.brand='macbook'
laptop_2.price='3lakh'



print(laptop_1.brand  , laptop_1.ram , laptop_1.price , sep='\n')
print(laptop_2.brand  , laptop_2.ram , laptop_2.price , sep='\n')
print(laptop_2)