from domain.Goods import Goods


class Coupang:
    def __init__(self, client, parser):
        self.client = client
        self.parser = parser

    def getHrefInGoodsList(self, categoryId) -> list[str]:
        html = self.client.requestGoodsList(categoryId)
        return self.parser.parseHrefInGoodsList(html)

    def getGoodsDetail(self, href) -> Goods:
        html = self.client.requestGoodsDetail(href)
        return self.parser.parseGoodsDetail(html)
