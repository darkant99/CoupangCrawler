from abc import *

from domain.Product import Product


class CoupangParser:
    @abstractmethod
    def parseHrefInProducts(self, html) -> list[str]:
        pass

    @abstractmethod
    def parseProductDetail(self, html) -> Product:
        pass
