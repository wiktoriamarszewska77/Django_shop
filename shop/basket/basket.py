class Basket():
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('session_key')
        if 'session_key' not in request.session:
            basket = self.session['session_key'] = {}

        self.basket = basket

    def add(self, product):
        product_id = str(product.id)

        if product_id in self.basket:
            pass
        else:
            self.basket[product_id] = {'price': str(product.price)}

        self.session.modified = True
