import pytest
from src import URL, _get_profile_page as get_page
from src.errors import ProfileNotFoundError


def test_page_exists_on_existing_profile():
    assert get_page(f"{URL}/isquicha") != b"Not Foun"


def test_page_not_found_on_non_existing_profile():
    with pytest.raises(ProfileNotFoundError):
        get_page(f"{URL}/asodhaiusldhaisudghaislgaiusgduya")
