from abc import *


class CoupangClient:
    @abstractmethod
    def requestGoodsList(self, categoryId) -> str:
        pass

    @abstractmethod
    def requestGoodsDetail(self, href) -> str:
        pass
