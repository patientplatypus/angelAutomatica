# angelAutomatica

# What this is
- This is a selenium driver for angel List jobs that will automatically go through the website and apply for jobs based on your requirements. This is firmly in `grey hat` territory - perhaps not entirely kind, but there is **NO** handling for getting around recaptchas. This cannot be considered a DOS as there exists automatic `time.sleeps` of large intervals.

# How to make it work
## Install Selenium driver
  - First go and grab the Firefox selenium driver (I got the one for mac, but you will need to grab the one that works with your chosen OS) here: https://github.com/mozilla/geckodriver/releases. You will then need to make sure that you place the driver in the correct path. For mac, this defaults to /usr/local/bin.
## Install Virtal Environment and packages
  - Set up the virtal env and install the required packages : `virtualvenv venv`
  `pip install time`
  `pip install re`
  `pip install selenium`
  (I should later go back and put in a `requirements.text` file, but there are not enough packages at the momement)
## Configure to Taste
  You now need to configure the code to apply for jobs to taste (Note, I do not have environment variables set up **expressly** as this does stupid things very fast, you need to go through the code to understand it, or you risk sending stupid things to many companies):
  - Lines 27-28 comment in to run in *headless mode*: This will not display the browser as the Selenium app is running. Not recommended for first time users or those unfamiliar with Selenium.
  - Line 12 in `database.py` needs to be changed to handle your mlab database (you need to set this up on your own). **IMPORTANT** This makes sure you don't apply to the same job twice.
  - Lines 239, and 241 handle your username and login information for angelList. If you don't log in, you can't apply for jobs.
  - Line 189 is the message your going to write to companies.
  - Lines 95 - 120 are the requirements you are looking for in the job title.
## Running
  - Make sure everything you have written so far is correct!
  - `python main.py`
