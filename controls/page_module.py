import datetime
from helper.acceptance_test_modul import *

now_date = datetime.datetime.now()
str(now_date)


class page_module:
    def __init__(self, element):
        self.element = element

    def select_element_in_list(self, element_text, element_select=None):
        if element_select is None:
            self.element.type(element_text).press_enter()
        else:
            self.element.type(element_text)
            self.element.click()
            s(element_select).click()

    def select_element_in_dropdown(self, select_element):
        self.element.click()
        s(select_element).click()

    def select_date_in_datepicker(self, elements_in_datepicker=None):
        if elements_in_datepicker is None:
            self.element.set_value(now_date.strftime("%d %b %Y")).click()
        else:
            self.element.click()
            s(elements_in_datepicker).s('[value="%d' % now_date.year + '"]').click()
            s(elements_in_datepicker).s('[value="%d' % now_date.month + '"]').click()
            s(elements_in_datepicker).s('[value="%d' % now_date.day + '"]').click()

    def check_expected_result_in_table(self, *args):
        self.element.should(have.texts(*args))
