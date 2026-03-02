from pages.base_page import BasePage


class HomePage(BasePage):

    def open(self, base_url):
        self.navigate(base_url)

    def get_header_text(self):
        return self.page.locator("h1").inner_text()