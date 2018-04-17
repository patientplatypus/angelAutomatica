# -*- coding: utf-8 -*-

# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# IMPORT BLOCK
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

import time
import re

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


from database import *

# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# SET UP SELENIUM BROWSER
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

opts = Options()
# here you can set if you want Selenium to run headless or not (comment in next 2 lines)
# opts.set_headless()
# assert opts.headless  # operating in headless mode
browser = Firefox(options=opts,executable_path="/usr/local/bin/geckodriver")
browser.get('https://www.angel.co')


# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# SET UP DATERBASE
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

print('Initialize DBHandler db')
DBHandlerInstance = DBHandler()
DBHandlerInstance.init_db()

# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# START SELENIUM NAVIGATION
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# FUNCTION HOLDER
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

def isascii(mystring):
    try:
        mystring.decode('ascii')
    except UnicodeDecodeError:
        print "it was not a ascii-encoded unicode string"
        return False
    else:
        print "It may have been an ascii-encoded unicode string"
        return True

def applyForJob():
    time.sleep(3)

    print('attempting to open new tab')

    browser.execute_script("window.open('', '_blank');")
    browser.switch_to_window(browser.window_handles[1])
    browser.get(job_links_href)

    print('now defining click_listing, job_listings_match_text and linkHolder')

    click_listing = None
    job_listings_match_text = None
    linkHolder = [];

    print('trying to find divs by class')

    title_divs = browser.find_elements_by_class_name("listing-title")

    print('value of title divs')

    print(title_divs)

    links = []

    for div in title_divs:
        print('inside divs')
        anchor = div.find_element_by_css_selector("a")
        print('value of anchor')
        print(anchor)
        print(anchor.get_attribute('href'))
        print(anchor.get_attribute('text'))
        links.append(anchor)

    found_match = False

    if found_match == False:
        for link in links:
            print("links linky")
            print(link.get_attribute("text"))
            if link.get_attribute("text").find("Fullstack")!=-1 or link.get_attribute("text").find("Full stack")!=-1 or link.get_attribute("text").find("Full Stack")!=-1 or link.get_attribute("text").find("fullstack")!=-1 or link.get_attribute("text").find("full stack")!=-1 or link.get_attribute("text").find("Full-stack")!=-1 or link.get_attribute("text").find("Full-Stack")!=-1 or link.get_attribute("text").find("full-stack")!=-1:
                click_listing = link
                found_match = True
                break

    if found_match == False:
        for link in links:
            print("links linky")
            print(link.get_attribute("text"))
            if link.get_attribute("text").find("frontend")!=-1 or link.get_attribute("text").find("Front end")!=-1 or link.get_attribute("text").find("Front End")!=-1 or link.get_attribute("text").find("front end")!=-1 or link.get_attribute("text").find("Front-end")!=-1 or link.get_attribute("text").find("front-end")!=-1 or link.get_attribute("text").find("Front-End")!=-1 or link.get_attribute("text").find("Frontend")!=-1 or link.get_attribute("text").find("FrontEnd")!=-1:
                click_listing = link
                found_match = True
                break

    if found_match == False:
        for link in links:
            print("links linky")
            print(link.get_attribute("text"))
            if link.get_attribute("text").find("web")!=-1 or link.get_attribute("text").find("javascript")!=-1 or link.get_attribute("text").find("Javascript")!=-1 or link.get_attribute("text").find("Python")!=-1 or link.get_attribute("text").find("React")!=-1 or link.get_attribute("text").find("react")!=-1 or            link.get_attribute("text").find("python")!=-1 or link.get_attribute("text").find("Web")!=-1 or link.get_attribute("text").find("Node.js")!=-1 :
                click_listing = link
                found_match = True
                break

    if found_match == False:
        for link in links:
            print("links linky")
            print(link.get_attribute("text"))
            if link.get_attribute("text").find("Software Engineer")!=-1:
                click_listing = link
                found_match = True
                break

    if click_listing!=None:
        print("there was a match for click listing")
        print(click_listing.get_attribute("text"))
        print(click_listing.get_attribute("href"))
        click_listing.click()

        time.sleep(10)

        print('Attempting to click on Apply to COMPANYNAME button')
        xPathstring = "//a[contains(text(),"+"'Apply to "+job_links_text+"'"+")]"
        element = browser.find_element_by_xpath(xPathstring)
        print('value of element')
        print(element)
        element.click()


        # NOTE - sleep until the text area is loaded so we can search through all textareas and find the one that is displayed

        time.sleep(10)

        text_area = None

        text_areas = browser.find_elements_by_css_selector("textarea")

        for area in text_areas:
            print('here are the values of the area')
            print(area)
            print('here is the class')
            print(area.get_attribute('class'))
            print('here is the maxlength')
            print(area.get_attribute('maxlength'))
            if area.is_displayed():
                print("This textarea is displayed, use this one")
                text_area = area
                break
            else:
                print('not displayed')

        placeholder_text = text_area.get_attribute("placeholder")
        capitalized_words = re.findall('([A-Z][a-z]+)', placeholder_text)

        full_name_intro = None

        for word in capitalized_words:
            if word == "Write" or word == "What" or word == "Why" or job_links_text.find(word)!=-1:
                print('in word lookup cycle for text_area and found unimportant word. Skipping...')
            else:
                if full_name_intro == None:
                    print('found first name and it is')
                    print(word)
                    full_name_intro = word
                else:
                    print('found last name and it is')
                    print(word)
                    full_name_intro = full_name_intro + " " + word
                    print('now value of full_name_intro is:')
                    print(full_name_intro)
        #
        text_to_insert = 'Dear '+str(full_name_intro)+',\n\n'+'I am writing to apply for your consideration as a developer at '+str(job_links_text)+'.\n \n'+'YOUR MESSAGE GOES HERE'

        print('value of text_to_insert')
        print(text_to_insert)

        print('now attempting to clear the textarea')
        text_area.clear()
        print('now attempting to insert text into the textarea')
        text_area.send_keys(text_to_insert)


        print('findind application button')
        paper_plane = browser.find_element_by_class_name('fontello-paper-plane')
        application_button = paper_plane.find_element_by_xpath('..')

        print('sending application and writing company to mlab database')
        DBHandlerInstance.add_name(job_links_text)
        application_button.click()

        time.sleep(5)

        print('applied to job now closing tab')
        browser.close()
        print('put focus on saved window instance')
        browser.switch_to.window(main_window)


    else:
        print("there was no match for click listing")
        print('no suitable positions found, closing tab')
        browser.close()
        print('put focus on saved window instance')
        browser.switch_to.window(main_window)


# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# ENTRYPOINT FOR CODE EXECUTION
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# GO TO LOGIN PAGE AND LOGIN
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

time.sleep(1)

browser.find_element_by_class_name('login').click()

time.sleep(1)

search_email = browser.find_element_by_id('user_email')
search_email.send_keys('<YOUR EMAIL>')

search_password = browser.find_element_by_id('user_password')
search_password.send_keys('<YOUR PASSWORD>')

browser.find_element_by_xpath("//input[@value='Log In']").click()

# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# NAVIGATE TO JOBS PAGE BASED ON SEARCH CRITERIA
# alter search paramaters to taste
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

time.sleep(1)

browser.get('https://angel.co/jobs#find/f!%7B%22locations%22%3A%5B%221688-United%20States%22%5D%2C%22last_active%22%3A%227%22%2C%22types%22%3A%5B%22full-time%22%5D%2C%22roles%22%3A%5B%22Full-Stack%20Developer%22%2C%22Frontend%20Developer%22%5D%7D')

time.sleep(5)


# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# BOUNCE SELENIUM TO BOTTOM FOR INFINITE SCROLL
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

bouncePage = True
job_links = None
job_links_href = None
job_links_text = None

while bouncePage:
    print("trying to scroll")
    job_links = browser.find_elements_by_class_name('startup-link')
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(10)
    afterBounce_job_links = browser.find_elements_by_class_name('startup-link')
    print('value of job_links last item:')
    print(job_links[len(job_links)-1].text)
    print('value of afterBounce_job_links last item:')
    print(afterBounce_job_links[len(afterBounce_job_links)-1].text)
    if job_links[len(job_links)-1].text == afterBounce_job_links[len(afterBounce_job_links)-1].text:
        bouncePage = False

# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
# APPLY FOR JOBS BUT ONLY IF HAVENT APPLIED BEFORE
# &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&

for company in job_links:
    job_links_href = company.get_attribute('href')
    job_links_text = company.get_attribute('text')
    print('value of company name:')
    print(job_links_text)

    print('checking if this company has already been applied to: ')

    appliedForJobPrior = True

    textDecodable = True

    # isascii = lambda s: len(s) == len(s.encode())

    # if isascii(job_links_text): #make sure no non-unicode characters in company name
    print("Company name is all in ascii characters")
    appliedForJobPrior = DBHandlerInstance.check_name(job_links_text)
    if appliedForJobPrior == True:
        print('You have applied to this job before! Skipping...')
    elif job_links_text.find("'") != -1 or job_links_text.find("tik") != -1 or job_links_text.find("Hiveel") != -1: #stupid edge case - Obsess has a funky name - who puts a ' in their name?
        print('You suck Obsess, go away')
        print('Also Lotik you blow')
    else:
        print('You have not applied to this job before! Applying...')
        print('save current instance of browser window')
        main_window = browser.current_window_handle
        applyForJob()
    # else:
    #     print("Company name is not all in ascii characters. Skipping...")
