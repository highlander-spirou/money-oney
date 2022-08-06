from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromiumService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from bs4 import BeautifulSoup
from bs4.element import Tag
from time import sleep
from extract.retry_decorator import retry_on_min_len, retry_on_none

def create_driver(url:str) -> Chrome:
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument("--window-size=1920,1080")

    driver = Chrome(service=ChromiumService(ChromeDriverManager(version="103.0.5060.134", chrome_type=ChromeType.CHROMIUM, path = r"driver").install()), options=chrome_options)
    driver.set_page_load_timeout(30)
    print('driver instantiated')
    driver.get(url)
    print('driver created')
    return driver

@retry_on_min_len(20)
def crawl_table(driver:Chrome) -> list:
    print('crawling table')
    soup = BeautifulSoup(driver.page_source, 'lxml')
    table_src = soup.find('table')
    data = []
    rows: Tag = table_src.find_all('tr')[3:] # bắt đầu từ số 3
    driver.get_screenshot_as_file(f"screenshots/screenshot.png")

    for row in rows:
        data.append([value.text.strip() for value in row.children if isinstance(value, Tag)])
    
    return data

@retry_on_none
def crawl_fund(fund:str, driver) -> Tag:
    print(f'crawling {fund}')
    link = driver.find_element("xpath", f'//a[contains(text(), "{fund}")]')
    link.click()
    driver.get_screenshot_as_file(f"screenshots/screenshot-{fund}.png")
    block_up = driver.find_elements(by=By.CSS_SELECTOR, value=".block-up")
    block_up = block_up[0]
    block_up_html = block_up.get_attribute('innerHTML')
    block_up_soup = BeautifulSoup(block_up_html, 'lxml')
    fund_page_src = block_up_soup.find("div", {"class":"row"})
    
    driver.find_elements(by=By.CSS_SELECTOR, value=".close-btn")[0].click()
    sleep(2)
    return fund_page_src



def run_crawler(url):
        print('start crawling process')
        with create_driver(url) as driver:
            table = crawl_table(driver)
            data = [i[0] for i in table]
            returned_table = {}
            for i in data:
                returned_table[i] = crawl_fund(i, driver)
            
        return table, returned_table
