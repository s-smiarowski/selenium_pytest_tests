'''
Example of Python | Selenium webdriver | pytest 
Test covering IMDB search
'''
from pages.main import ImdbMainPage
from pages.find import ImdbFindPage
from pages.selected import ImdbSelectedPage


def test_imdb_search(browser):
    
    main_page = ImdbMainPage(browser)
    find_page = ImdbFindPage(browser)
    selected_page = ImdbSelectedPage(browser)
    
    # Here you can change the searchphrase
    PHRASE = "Baahubali"

    # Given the IMDB home page is displayed
    main_page.load()


    # When the users searches for "Baahubali"
    main_page.search(PHRASE)


    # Then the text: Results for (...) contains search PHRASE
    assert PHRASE.lower() in find_page.search_input_value().lower()


    # Then the search result list contains search PHRASE
    titles = find_page.result_link_titles()
    no_results = [i for i in titles if PHRASE.lower() in i.lower()]
    assert len(no_results)>0


    # Then the search for PHRASE is in selected_page title
    find_page.select_title()
    assert PHRASE.lower() in selected_page.title().lower()


    # Then the PHRASE is in "title" text field
    assert PHRASE.lower() in selected_page.movie_name().lower()