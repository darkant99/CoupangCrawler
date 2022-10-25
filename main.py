from domain.Coupang import Coupang
from infra.CoupangHttpClient import CoupangHttpClient
from infra.CoupangParserImpl import CoupangParserImpl

coupang = Coupang(
    CoupangHttpClient(),
    CoupangParserImpl()
)

products = list(map(
    coupang.getGoodsDetail,
    coupang.getHrefInGoodsList("118900")
))