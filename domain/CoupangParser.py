from abc import *

from domain.Goods import Goods


class CoupangParser:
    @abstractmethod
    def parseHrefInGoodsList(self, html) -> list[str]:
        pass

    @abstractmethod
    def parseGoodsDetail(self, html) -> Goods:
        pass
