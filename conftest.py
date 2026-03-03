import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    context = browser.new_context()
    page = context.new_page()
    yield page
    context.close()


def pytest_runtest_setup(item):
    print(f"\n🚀 Starting test: {item.name}")


def pytest_runtest_teardown(item):
    print(f"✅ Finished test: {item.name}")