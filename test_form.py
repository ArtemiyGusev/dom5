from controls.page_module import *
from env import *


def test_case_practice_form():
    url_open_size('/automation-practice-form')

    s('#firstName').type('Jack')

    s('#lastName').type('Shepard')

    s('#userEmail').type('Jack@mail.ru')

    s('#userNumber').type('4815162342')

    s('#currentAddress').type('Oceanic')

    element = page_module(s(subjects_input))
    element.select_element_in_list('g', select_element_in_subject)

    element = page_module(s(date_of_birth_input))
    element.select_date_in_datepicker(date_of_birth)

    s(gender_select_male).click()

    s(hobbies_select_sports).click()

    element = page_module(s(list_state))
    element.select_element_in_dropdown(element_in_list_state)

    element = page_module(s(list_city))
    element.select_element_in_dropdown(element_in_list_city)

    add_file(send_picture_button, file_name=file_name)

    s(send_data).click()

    check_expected_result_in_table(table_name, *expected_result_in_table)
