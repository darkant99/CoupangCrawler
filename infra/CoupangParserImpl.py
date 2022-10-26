from domain.CoupangParser import CoupangParser

import re
import json
from bs4 import BeautifulSoup as soup

from domain.Product import Product


class CoupangParserImpl(CoupangParser):
    def parseHrefInProducts(self, html) -> list[str]:
        parser = soup(html, "html.parser")
        result = map(
            lambda it: it.find("a")["href"],
            parser.select("#productList > li")
        )
        return list(result)

    def parseProductDetail(self, html) -> Product:
        matched = re.findall("exports.sdp = (.*);", html)
        sdp = json.loads(matched[0])
        return Product(sdp.get("itemName"))
