from selene import be
from selene.support.conditions import have
from selene.support.jquery_style_selectors import s, ss


def test_case1():

    # Заполняем форму
    s('#firstName').type('Jack')

    s('#lastName').type('Shepard')

    s('#userEmail').type('Jack@mail.ru')

    s('#userNumber').type('4815162342')

    s('#currentAddress').type('Oceanic')

    s('#subjectsInput').type('H')

    s('#react-select-2-option-0').click()

    s('#dateOfBirthInput').click()
    s('[aria-label*="20th"]').click()

    s('[for=gender-radio-1]').click()

    s('[for=hobbies-checkbox-1]').click()

    #select state
    s('#state').click()
    s('#react-select-3-option-0').click()
    #select city
    s('#city').click()
    s('#react-select-4-option-0').click()
    # Отправка картинки
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
                                      '20 June,2022',
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
