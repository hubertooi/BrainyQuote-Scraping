
# Project

Python web scraper for scraping quotes by topic from BrainyQuotes website: https://www.brainyquote.com/

### Before starting

1) Install Intellij IDEA Community version 2020.3.1 or visual studio code Version: 1.52.1 which I use the two. It is up to your personal preference.

2) I uses windows's version python 3.8.0 64 bit link: https://www.python.org/downloads/release/python-380/

3) i) Intellij IDEA: download python plugins by downloading it within Intellij. 
   ii) VScode: download python extensions. 

4) If you are familiar of setting virtual environment for each project, you can set up virtual environment. Intellij IDEA has it own way to set up virtual environment when you set up a project. Virtual environment needed to be set up using terminal with VScode.

5) Install pip and packages listed in requirement.txt with the its recpective versions.

6) Within .vscode, the settings.json is meant for my specific virtual environment. If you are not planning to use virtual environment, then just make use the path of the python is your default location of python.exe (global python location)

7) The .idea and BrainyQuote-scraping.iml are meant for Intellij IDEA.

### Before running quote_scraping.py

1) At codeline 40: you will need to specify the path you intend to save csv file of the quotes scraped from the python file. You only need to change to path directory within path = 'C:\\Users\\Hubert\\Desktop\\'. The back portion is set up for csv file naming unless you want to change the naming format.

2) You can refer to Quote Topics BrainyQuote.pdf for topics that you can input when you run quote_scraping.py

### Example output
1) quotes_success.csv is an example of the quotes saved into csv file format.
# Enjoy and happy scraping quotes



