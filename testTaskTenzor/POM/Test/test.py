from POM.Pages.startPage import StartPage
from POM.Pages.searchPage import SearchPage
from POM.Pages.imagePage import ImagePage
from POM.Pages.firsrResultPage import FirstResultPage
from POM.Pages.modalMenuServicesPage import ModalMenuServicesPage
from POM.Pages.modalMenuWithPicturesPage import ModalMenuWithPicturesPage
from POM.Test import log_app as log


class TestTenzor:

    log.log_open()

    def test_search_of_yandex(self, browser, url):

        browser.get(url)

        start_page = StartPage(browser)
        start_page.assert_general_search_box()
        start_page.send_text()
        start_page.assert_suggest_input()
        start_page.click_enter()

        search_page = SearchPage(browser)
        search_page.assert_result_search()
        search_page.first_page_of_search_click()

        first_page = FirstResultPage(browser)
        first_page.go_to_new_windows()
        first_page.assert_first_link()


    def test_yandex_img(self, browser, url):

        browser.get(url)

        start_page = StartPage(browser)
        start_page.assert_button_menu()
        start_page.button_menu_click()

        modal_menu_services = ModalMenuServicesPage(browser)
        modal_menu_services.pictures_click()
        modal_menu_services.switch_to_img_page()

        img_page = ImagePage(browser)
        img_page.assert_link_new_windows()
        img_page.first_category_click()
        img_page.assert_category_display_in_the_search_field()
        img_page.first_img_click()

        modal_menu_pictures = ModalMenuWithPicturesPage(browser)
        modal_menu_pictures.assert_picture_opened_after_click()
        modal_menu_pictures.safe_link_first_pic()
        modal_menu_pictures.press_forward_button()
        modal_menu_pictures.safe_link_second_pic()
        modal_menu_pictures.assert_picture_changed()
        modal_menu_pictures.press_back_button()
        modal_menu_pictures.assert_returned_the_first_picture()
