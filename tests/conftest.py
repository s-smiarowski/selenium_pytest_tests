import pytest
import selenium.webdriver

@pytest.fixture
def browser():

    # initialize ChromeDriver isntance
    b = selenium.webdriver.Chrome()

    # weit up to 10 sec for elements to appear
    b.implicitly_wait(10)

    #Return the webDriver instance for the setup
    yield b

    # Quit webdriver isntance and cleanup
    b.quit()