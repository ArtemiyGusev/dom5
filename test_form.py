from selene import be
from selene.support.conditions import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s, ss


def url_open_size(url, width=1920, height=1080):
    browser.open(url)
    browser.config.driver.set_window_size(width, height)


def test_case1():
    url_open_size('/automation-practice-form')

    # Заполняем форму
    s('#firstName').type('Jack')

    s('#lastName').type('Shepard')

    s('#userEmail').type('Jack@mail.ru')

    s('#userNumber').type('4815162342')

    s('#currentAddress').type('Oceanic')

    s('#subjectsInput').type('H')

    s('#react-select-2-option-0').click()

    browser.execute_script('document.querySelector("#dateOfBirthInput").value = "27 Jun 2022";')

    s('[for=gender-radio-1]').click()

    s('[for=hobbies-checkbox-1]').click()

    s('#state').click()
    s('#react-select-3-option-0').click()

    s('#city').click()
    s('#react-select-4-option-0').click()
    # Либо: s('#uploadPicture').type(os.path.abspath('123.png')), но будет импорт 'os'
    s('#uploadPicture').type('C:\\123.png')
    s('#submit').click()

    s('.table-responsive').should(be.visible)

    ss('.table td').should(have.texts('Student Name',
                                      'Jack Shepard',
                                      'Student Email',
                                      'Jack@mail.ru',
                                      'Gender',
                                      'Male',
                                      'Mobile',
                                      '4815162342',
                                      'Date of Birth',
                                      '27 June,2022',
                                      'Subjects',
                                      'Hindi',
                                      'Hobbies',
                                      'Sports',
                                      'Picture',
                                      '123.png',
                                      'Address',
                                      'Oceanic',
                                      'State and City',
                                      'NCR Delhi'))
