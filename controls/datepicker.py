import datetime
from selene.support.shared.jquery_style import s

now_date = datetime.datetime.now()
str(now_date)


class datepicker:

    def __init__(self, element):
        self.element = element

    def select_date_in_datepicker(self, elements_in_datepicker=None):
        if elements_in_datepicker is None:
            self.element.set_value(now_date.strftime("%d %b %Y")).click()
        else:
            self.element.click()
            s(elements_in_datepicker).s('[value="%d' % now_date.year + '"]').click()
            s(elements_in_datepicker).s('[value="%d' % now_date.month + '"]').click()
            s(elements_in_datepicker).s('[value="%d' % now_date.day + '"]').click()
