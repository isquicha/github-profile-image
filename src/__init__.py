from bs4 import BeautifulSoup
from requests import get
from requests.models import Response

from src.errors import ProfileNotFoundError, ProfilePageUnavailabeError

URL = "https://github.com"


def _get_profile_page(uri: str) -> Response.content:
    """Get user profile page

    Parameters
    ----------
    uri : str
        The user's github profile page URI (https://github.com/username)

    Returns
    -------
    Response.content
        The page content: an HTML page

    Raises
    ------
    ProfileNotFoundError
        If user does not exits
    ProfilePageUnavailabeError
        If any other error occurs
    """

    response = get(uri)
    if response.status_code == 404:
        raise ProfileNotFoundError
    if response.status_code != 200:
        raise ProfilePageUnavailabeError
    return response.content


def _get_image_link_from_page(page) -> str:
    soup = BeautifulSoup(page, "html.parser")
    image = soup.find(
        name="img",
        attrs={
            "class": lambda classes: all(
                [
                    _class in classes.split()
                    for _class in ["avatar-user", "width-full"]
                ]
            )
        },
    )
    image_link = image.get("src")
    return image_link


def get_user_image_link(user: str) -> str:
    uri = f"{URL}/{user}"
    page = _get_profile_page(uri=uri)
    return _get_image_link_from_page(page)
