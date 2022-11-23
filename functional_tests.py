from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time



class NewVisitorTest(unittest.TestCase):
    ''' Тест нового пользователя'''

    def setUp(self):
        '''установка'''
        self.browser = webdriver.Firefox()

    def tearDown(self):
        '''демонтаж'''
        self.browser.quit()


    def test_can_start_a_list_and_retrieve_it_later(self):
        ''' тест: можно начать список и получить его позже'''

        #Эдит слышала про крутое новое онлайн-приложение со списком
        #неотложныйх дел. Она решает оценить его домашнюю страницу
        self.browser.get('http://localhost:8000')


        #Она видит, что заголовок и шапка страницы говорят о списках неотложных дел
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        #self.fail('Закончить тест!')

        #Ей сразу же предлагается ввести элемент списка
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )


        #Она набирает в текстовом поле "Купить павлиньи перья"
        inputbox.send_keys('Купить павлинья перья')


        #Когда она нажимает enter, страница обновляется, и теперь страница
        #содержит "1: Купить павлинья перья" в качестве элемента списка
        inputbox.sens_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Купить павлинья перья' for row in rows)
        )

        
        #Текстовое поле по-прежнему предлагает ее добавить еще один элемент, Она вводит еще один


        #После этого она видит что сайт сгенериорвал уникальный УРЛ адрес для нее( с ее списком)
        self.fail('Закончить тест!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')