from django.urls import resolve
from django.test import TestCase
from lists.views import home_page
from django.http import HttpRequest
#

class HomePageTest(TestCase):
    '''Тест домашней страницы'''
    def test_uses_home_template(self):
        '''тест: используется домашний шаблон'''
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')




    #def test_root_url_resolves_to_home_page_view(self):
    #    '''тест: корневой url преобразуется в представление домашней страницы'''
    #    found = resolve('/')
    #    self.assertEqual(found.func, home_page)


    #def test_home_page_returns_correct_html(self):
    #    '''тест: домашняя страница возвращает правильный html'''
        
    #    response = self.client.get('/')
    #    html = response.content.decode('utf8')

    #    self.assertTrue(html.startswith('<html>'))
    #    self.assertIn('<title>To-Do lists</title>', html)
    #    self.assertTrue(html.strip().endswith('</html>'))

    #    self.assertTemplateUsed(response, 'home.html')

    