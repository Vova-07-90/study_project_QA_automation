from POM.Test import log_app as log

class FirstResultPage:

    def __init__(self, browser):
        self.browser = browser
        self.expected_link_search = 'https://tensor.ru/'

    def go_to_new_windows(self):
        self.browser.switch_to.window(self.browser.window_handles[1])

    def assert_first_link(self):
        link_first_of_search = self.browser.current_url
        assert link_first_of_search == self.expected_link_search, log.logger.error(f'URL not {self.expected_link_search}')
        log.logger.info(f'Correct URL {self.expected_link_search}')