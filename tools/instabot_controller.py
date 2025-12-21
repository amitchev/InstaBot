from playwright.sync_api import sync_playwright
import time
import random
import json

username = 'cava.bot97'
password = 'Ozzie1174@'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.instagram.com/accounts/login/")

    page.fill('input[name="username"]', username)
    page.fill('input[name="password"]', password)
    page.click('button[type="submit"]')
    time.sleep(5 + random.random() * 4)

    page.goto("https://www.instagram.com/gabbymitchev/")
    posts = page.query_selector_all('article a')
    for post in posts[:5]:
        post.click()
        time.sleep(2)
        page.click('svg[aria-label="Like"]')
        page.fill('textarea[aria-label="Add a comment…"]', "MY WIFEEEEE!")
        page.click('button[type="submit"]')
        page.go_back()
        time.sleep(random.randint(3,6))

class InstabotController():
    def __init__(self):
        with open("C:\Users\amitc\OneDrive\Documents\Insta-Bot\settings.json", "r", encoding="utf-8") as f:
            self.json_data = json.load(f)

        self.username = self.json_data["username"]
        self.password = self.json_data["password"]
