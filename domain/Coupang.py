from domain.Product import Product


class Coupang:
    def __init__(self, client, parser):
        self.client = client
        self.parser = parser

    def getHrefInProducts(self, categoryId) -> list[str]:
        html = self.client.requestProducts(categoryId)
        return self.parser.parseHrefInProducts(html)

    def getProductDetail(self, href) -> Product:
        html = self.client.requestProductDetail(href)
        return self.parser.parseProductDetail(html)
