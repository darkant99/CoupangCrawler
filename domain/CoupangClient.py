from abc import *


class CoupangClient:
    @abstractmethod
    def requestProducts(self, categoryId) -> str:
        pass

    @abstractmethod
    def requestProductDetail(self, href) -> str:
        pass
