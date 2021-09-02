import re
import pyautogui
import selenium.common.exceptions
from selenium import webdriver
from bs4 import BeautifulSoup


def center(top, bottom, left, right, state):
    if state == "AREA_CONNECTICUT":
        yyy = ((top + bottom) / 2) + 15
        xx = (left + right) / 2 - 20
    elif state == "AREA_MICHIGAN":
        yyy = ((top + bottom) / 2) + 60
        xx = ((left + right) / 2) + 10
    else:
        yyy = ((top + bottom) / 2) + 50
        xx = (left + right) / 2
    return xx, yyy


driver = webdriver.Chrome('C:/Users/dondo/Desktop/Coding/YiMian/chromedriver')

driver.set_page_load_timeout(3)

try:
    driver.get('https://online.seterra.com/en/vgp/3003')
except selenium.common.exceptions.TimeoutException:
    pass

soup = BeautifulSoup(driver.page_source, "html.parser")
html_coords = {}
areas = ['AREA_ALASKA', 'AREA_ALABAMA', 'AREA_ARKANSAS', 'AREA_ARIZONA', 'AREA_CALIFORNIA', 'AREA_COLORADO', 'AREA_CONNECTICUT', 'AREA_DELAWARE', 'AREA_FLORIDA', 'AREA_GEORGIA', 'AREA_HAWAII', 'AREA_IOWA', 'AREA_IDAHO', 'AREA_ILLINOIS', 'AREA_INDIANA', 'AREA_KANSAS', 'AREA_KENTUCKY', 'AREA_LOUISIANA', 'AREA_MASSACHUSETTS', 'AREA_MARYLAND', 'AREA_MAINE', 'AREA_MICHIGAN', 'AREA_MINNESOTA', 'AREA_MISSOURI', 'AREA_MISSISSIPPI', 'AREA_MONTANA', 'AREA_NORTHCAROLINA', 'AREA_NORTHDAKOTA', 'AREA_NEBRASKA', 'AREA_NEWHAMPSHIRE', 'AREA_NEWJERSEY', 'AREA_NEWMEXICO', 'AREA_NEVADA', 'AREA_NEWYORK', 'AREA_OHIO', 'AREA_OKLAHOMA', 'AREA_OREGON', 'AREA_PENNSYLVANIA', 'AREA_RHODEISLAND', 'AREA_SOUTHCAROLINA', 'AREA_SOUTHDAKOTA', 'AREA_TENNESSEE', 'AREA_TEXAS', 'AREA_UTAH', 'AREA_VIRGINIA', 'AREA_VERMONT', 'AREA_WASHINGTON', 'AREA_WISCONSIN', 'AREA_WESTVIRGINIA', 'AREA_WYOMING']
driver.fullscreen_window()
pyautogui.scroll(-900)

for area in areas:
    coords = driver.execute_script(f"var element = document.getElementById('{area}'); var locationOfTheStateButIHaveToMakeThisVariableNameSuperLong = element.getBoundingClientRect(); return locationOfTheStateButIHaveToMakeThisVariableNameSuperLong")
    x, y = center(coords.get("top"), coords.get("bottom"), coords.get("left"), coords.get("right"), area)
    html_coords[area] = (x, y)


for i in range(50):
    soup = BeautifulSoup(driver.page_source, "html.parser")
    a = "AREA_" + str(re.search('Click on (.+?)</span>', str(soup.find('span', {'id': 'currQuestion'}))).group(1)).replace(" ", "").upper()
    pyautogui.leftClick(html_coords[a])
