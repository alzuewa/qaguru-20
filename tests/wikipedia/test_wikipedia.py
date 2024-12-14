from allure import step
from selene import be, have

from screens import main_screen, onboarding_screen


def test_search_article():
    with step('Skip onboarding'):
        onboarding_screen.skip_button.click()
    with step('Type search query'):
        main_screen.search_field.click()
        main_screen.input_field.type('Appium')
    with step('Verify content found'):
        main_screen.search_results.should(have.size_greater_than(0))
        main_screen.search_results.first.should(have.text('Appium'))


def test_open_article():
    with step('Skip onboarding'):
        onboarding_screen.skip_button.click()
    with step('Type search query'):
        main_screen.search_field.click()
        main_screen.input_field.type('Python')

    with step('Verify content found'):
        main_screen.search_results.should(have.size_greater_than(0))
        main_screen.search_results.first.click()


def test_onboarding_screen():
    with step('Verify screen-1 content'):
        onboarding_screen.add_language_button.should(be.visible)
        onboarding_screen.skip_button.should(be.visible)
        onboarding_screen.paginator.should(be.visible)
        onboarding_screen.paginator.should(have.attribute('content-desc', 'Page 1 of 4'))
        onboarding_screen.page_title.should(have.text('The Free Encyclopedia'))

    with step('Go to the screen-2'):
        onboarding_screen.continue_button.click()

    with step('Verify screen-2 content'):
        onboarding_screen.add_language_button.should(be.not_.visible)
        onboarding_screen.skip_button.should(be.visible)
        onboarding_screen.paginator.should(be.visible)
        onboarding_screen.paginator.should(have.attribute('content-desc', 'Page 2 of 4'))
        onboarding_screen.page_title.should(have.text('New ways to explore'))

    with step('Go to the screen-3'):
        onboarding_screen.continue_button.click()

    with step('Verify screen-3 content'):
        onboarding_screen.add_language_button.should(be.not_.visible)
        onboarding_screen.skip_button.should(be.visible)
        onboarding_screen.paginator.should(be.visible)
        onboarding_screen.paginator.should(have.attribute('content-desc', 'Page 3 of 4'))
        onboarding_screen.page_title.should(have.text('Reading lists with sync'))

    with step('Go to the screen-4'):
        onboarding_screen.continue_button.click()

    with step('Verify screen-4 content'):
        onboarding_screen.add_language_button.should(be.not_.visible)
        onboarding_screen.skip_button.should(be.not_.visible)
        onboarding_screen.paginator.should(be.visible)
        onboarding_screen.paginator.should(have.attribute('content-desc', 'Page 4 of 4'))
        onboarding_screen.page_title.should(have.text('Data & Privacy'))
        onboarding_screen.get_started_button.should(be.clickable)
