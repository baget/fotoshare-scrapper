"""A script to scrape images from fotoshare.co and download them."""

from urllib.parse import urlparse, urlunparse
import time
import requests
from playwright.sync_api import sync_playwright

BASE_URL = "https://fotoshare.co"
INDEX_PAGE = "WHAT_EVER_YOU_WANT_TO_SCRAPE"  # Replace with the actual page you want to scrape
PHOTOS_FOLDER = "photos"


def main():
    """A script to scrape images from a specific page on fotoshare.co and download them.
    It uses Playwright to navigate the site and requests to download images.
    """
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = get_images(browser, f"{BASE_URL}{INDEX_PAGE}")

        divs = page.query_selector_all("div[data-url]")
        for div in divs:
            data_url = div.get_attribute("data-url")
            if data_url and ".svg" not in data_url:
                get_images(browser, f"{BASE_URL}{data_url}")

        browser.close()


def get_images(browser, url: str):
    """Get images from a given URL using Playwright.
    This function navigates to the specified URL, finds all image elements,
    Args:
        browser (Broswer): A Playwright browser instance to use for navigation.
        url (str): The URL to scrape for images.

    Returns:
        Page: The Playwright page object after navigating to the URL.
    """
    page = browser.new_page()
    page.goto(url)
    img_elements = page.query_selector_all("img")
    for img in img_elements:
        src = img.get_attribute("src")
        if src and ".svg" not in src:
            clean_url = urlunparse(urlparse(src)._replace(query=""))
            print(clean_url)
            if "_thumb" not in clean_url:
                download_image(clean_url)
                time.sleep(0.3)  # To avoid overwhelming the server

    return page


def download_image(url: str):
    """Download an image from a given URL and save it to the photos folder.
    This function sends a GET request to the image URL and saves the content to a file.

    Args:
        url (str): The URL of the image to download.
    """
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        filename = url.split("/")[-1]
        with open(f"{PHOTOS_FOLDER}/{filename}", "wb") as file:
            file.write(response.content)
        print(f"Downloaded {filename}")
    else:
        print(f"Failed to download {url}, status code: {response.status_code}")


if __name__ == "__main__":
    main()
