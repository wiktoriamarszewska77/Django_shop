from products.models import Product

class Basket():
    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('session_key')
        if 'session_key' not in request.session:
            basket = self.session['session_key'] = {}

        self.basket = basket

    def add(self, product, quantity):
        product_id = str(product.id)
        product_qty = str(quantity)

        if product_id in self.basket:
            pass
        else:
            # self.basket[product_id] = {'price': str(product.price)}
            self.basket[product_id] = int(product_qty)

        self.session.modified = True

    def __len__(self):
        return len(self.basket)

    def get_prods(self):
        product_ids = self.basket.keys()

        products = Product.objects.filter(id__in=product_ids)
        return products

    def get_quants(self):
        quantities = self.basket
        return quantities
