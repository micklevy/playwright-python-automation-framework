from pages.home_page import HomePage


def test_homepage_loads(page):
    home = HomePage(page)
    home.open("https://example.com")
    assert "Example Domain" in home.get_header_text()