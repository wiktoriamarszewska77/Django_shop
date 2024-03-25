from products.models import Product


class Basket:
    def __init__(self, request):
        self.session = request.session
        if "session_key" not in self.session:
            self.session["session_key"] = {}

        self.basket = self.session["session_key"]

    def add(self, product_id: int, quantity: int):
        if product_id not in self.basket:
            # self.basket[product_id] = {'price': str(product.price)}
            self.basket[product_id] = quantity
            self.session.modified = True

    def basket_total(self):
        products_ids = self.basket.keys()
        products = Product.objects.filter(id__in=products_ids)

        quantities = self.basket
        total = 0
        for key, value in quantities.items():
            key = int(key)
            for product in products:
                if product.id == key:
                    total = total + (product.price * value)

        return total

    def __len__(self):
        return len(self.basket)

    def get_prods(self):
        product_ids = self.basket.keys()
        return Product.objects.filter(id__in=product_ids)

    def get_quants(self):
        return self.basket

    def update(self, product_id: int, quantity: int):
        self.basket[product_id] = quantity
        self.session.modified = True

        return self.basket

    def delete(self, product: str):
        if str(product) in self.basket:
            del self.basket[str(product)]

        self.session.modified = True

    def remove_basket(self):
        self.basket = {}
        self.session["session_key"] = {}
        self.session.modified = True
