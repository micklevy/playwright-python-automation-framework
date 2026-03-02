from pages.home_page import HomePage


def test_homepage_loads(page, config):
    home = HomePage(page)
    home.open(config["base_url"])
    assert "Example Domain" in home.get_header_text()