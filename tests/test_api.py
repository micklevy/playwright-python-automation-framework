from playwright.sync_api import sync_playwright


def test_api_example_domain():
    with sync_playwright() as p:
        request = p.request.new_context(ignore_https_errors=True)
        response = request.get("https://example.com")
        assert response.status == 200