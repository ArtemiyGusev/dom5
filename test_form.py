from controls.dropdown import dropdown
from controls.check_table_text import check_table_text
from controls.datepicker import datepicker
from controls.subject import subject
from selene.support.shared.jquery_style import s, ss
from env import *
from helper.acceptance_test_modul import url_open_size, add_file


def test_case_practice_form():
    url_open_size('/automation-practice-form')

    s('#firstName').type('Jack')

    s('#lastName').type('Shepard')

    s('#userEmail').type('Jack@mail.ru')

    s('#userNumber').type('4815162342')

    s('#currentAddress').type('Oceanic')

    subject(s(subjects_input)).select_element_in_list('g', select_element_in_subject)

    datepicker(s(date_of_birth_input)).select_date_in_datepicker(date_of_birth)

    s(gender_select_male).click()

    s(hobbies_select_sports).click()

    dropdown(s(list_state)).select_element_in_dropdown(element_in_list_state)

    dropdown(s(list_city)).select_element_in_dropdown(element_in_list_city)

    add_file(send_picture_button, file_name=file_name)

    s(send_data).click()

    check_table_text(ss(table_name)).check_expected_result_in_table(*expected_result_in_table)
