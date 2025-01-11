from PIL import Image
import pytesseract
import cv2
import requests
from bs4 import BeautifulSoup

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('Tester5.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, threshold = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

cv2.imwrite("processed_image.png", threshold)

title = pytesseract.image_to_string(Image.open("processed_image.png"))
print(title)

def get_rating(title):

    base_url = "https://www.goodreads.com/search"
    params = {"q": title, "search_type": "books"}

    response = requests.get(base_url, params=params)

    if response.status_code != 200:
        print("Could not find title:" + title)
        return None

    soup = BeautifulSoup(response.text, 'html.parser')

    rating = soup.find('span', class_='minirating')
    if rating:
        print("The rating of {title} is {rating}")
        return None
    else:
        print("Could not find rating for " + title)
        return None
    
get_rating(title)