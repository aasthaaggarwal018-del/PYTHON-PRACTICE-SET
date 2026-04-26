class res():
    resturant_name='maharaja paradise'
    location='mumbai'


    def __init__(self,order_no,amount):
        self.order_no=order_no
        self.amount=amount


    def info(self):
        print(f'resturant : {self.resturant_name} \nlocation : {self.location} ' )
        print(f'order number : {self.order_no} \nbill amount {self.amount}' )


order1=res(5,700)
order1.info()


order2=res(8,1500)
order2.info()

        

    