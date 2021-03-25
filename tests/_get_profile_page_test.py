from src import URL, _get_profile_page as get_page

# from .. import _get_profile_page as get_page


def test_page_exists_on_existing_profile():
    assert get_page(f"{URL}/isquicha") != b"Not Found"


def test_page_not_found_on_non_existing_profile():
    assert get_page(f"{URL}/asodhaiusldhaisudghaislgaiusgduya") == b"Not Found"
