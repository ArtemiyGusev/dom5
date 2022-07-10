from selene.support.conditions import have


class check_table_text:
    def __init__(self, element):
        self.element = element

    def check_expected_result_in_table(self, *args):
        self.element.should(have.texts(*args))