from src.scraping import get_download_page


def test_response():
    response = get_download_page()
    assert response is not None
    assert response.split("\n")[0] == "<!DOCTYPE html>"
