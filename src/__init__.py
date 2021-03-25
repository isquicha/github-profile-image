from bs4 import BeautifulSoup
from requests import get
from requests.models import Response

URL = "https://github.com"


def _get_profile_page(uri: str) -> Response.content:
    return get(uri).content


def _get_image_link_from_page(page) -> str:
    soup = BeautifulSoup(page, "html.parser")
    image = soup.find("img", {"class": "avatar-user"})
    image_link = image.get("src")
    return image_link


def get_user_image_link(user: str) -> str:
    uri = f"{URL}/{user}"
    page = _get_profile_page(uri=uri)
    return _get_image_link_from_page(page)
