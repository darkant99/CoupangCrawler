import requests

from domain.CoupangClient import CoupangClient

HOST = "https://www.coupang.com"
DEFAULT_HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "ko-KR,ko;q=0.9",
    "sec-ch-ua": '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36"
}


class CoupangHttpClient(CoupangClient):
    @staticmethod
    def __path2Url(path):
        return HOST + path

    # noinspection PyMethodMayBeStatic
    def __get(self, url):
        return requests.get(url, headers=DEFAULT_HEADERS)

    def __loadHtml(self, url):
        return self.__get(url).text

    def requestProducts(self, categoryId) -> str:
        response = self.__get(
            self.__path2Url("/np/categories/" + categoryId)
        )
        return response.text

    def requestProductDetail(self, href) -> str:
        response = self.__get(
            self.__path2Url(href)
        )
        return response.text
