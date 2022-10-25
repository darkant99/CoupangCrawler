from domain.CoupangParser import CoupangParser

import re
import json
from bs4 import BeautifulSoup as soup

from domain.Goods import Goods


class CoupangParserImpl(CoupangParser):
    def parseHrefInGoodsList(self, html) -> list[str]:
        parser = soup(html, "html.parser")
        result = map(
            lambda it: it.find("a")["href"],
            parser.select("#productList > li")
        )
        return list(result)

    def parseGoodsDetail(self, html) -> Goods:
        matched = re.findall("exports.sdp = (.*);", html)
        sdp = json.loads(matched[0])
        return Goods(sdp.get("itemName"))
