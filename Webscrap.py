# def Scrapping():
#     from bs4 import BeautifulSoup
#     import requests
#     import pyrebase
#
#     # connectivity to the fire base
#     config = {
#         'apiKey': "AIzaSyBdpemUwtU64fJNVVhTubjQSUyCybtOc5w",
#         'authDomain': "college-connectivity.firebaseapp.com",
#         'databaseURL': "https://college-connectivity.firebaseio.com",
#         'storageBucket': "college-connectivity.appspot.com",
#     }
#     connection = pyrebase.initialize_app(config)
#
#     db = connection.database()
#
#     ## create a global list, that contains all the books dictionaries
#     all_books_details = []
#
#     # To write Into firebase
#     def entry(name, price, avail, book_id, img_url, book_upc):
#         # Book_Id = 100+c
#
#         record = {
#             "Book-name":  name, "Book-price": price, "Book-avail": avail,"Book-image": img_url,
#             "Book-upc": book_upc,"Book-Id": book_id
#         }
#         db.child("college-connectivity").child("details").push(record)
#
#     # Web scrapping code bellow
#     link = ["http://books.toscrape.com/index.html"]
#
#     # Used to get all webpage address
#
#     image_url = []
#     for i in range(1, 51):
#       url = "http://books.toscrape.com/catalogue/page-"+str(i)+".html"
#       link.append(url)
#     c = 1
#
#
#     #   Iterating through Each page
#
#     for pages in range(len(link)):
#         index = requests.get(link[pages])
#         soup = BeautifulSoup(index.text,"html.parser")
#         Book_Category = soup.find_all("div", {"class": "image_container"})
#
#         # Used to iterate to inner web-pages
#         for i in range(len(Book_Category)):
#             new1 = Book_Category[i].find("a", href=True)
#             x = new1["href"]
#
#
#             # Doing this Because Link were not proper
#             if x[0:9] == "catalogue":
#                 url = "http://books.toscrape.com/"+new1["href"]
#             else:
#                 url = "http://books.toscrape.com/catalogue/"+new1["href"]
#
#
#             # Reaching the final web-page
#             final_page = requests.get(url, verify=False)
#             final_soup = BeautifulSoup(final_page.text, "html.parser")
#
#             book_name = final_soup.find("h1")
#             name = book_name.getText()
#
#             book_price = final_soup.find("p", {"class": "price_color"})
#             price = book_price.getText()[1:]
#
#             book_avail = final_soup.find("p", {"class": "instock availability"})
#             avail = (book_avail.getText())[15:40]
#
#             book_img = final_soup.find("img")
#             img_url = "http://books.toscrape.com"+book_img["src"][5:]
#
#             book_upc = final_soup.find("td").getText()
#
#             ## use this method to save the data on firebase server
#             entry(name, price, avail, c, img_url, book_upc)
#
#             ## create a new book dictionary, that has all the details of a
#             ## particular book.
#             Book_ID = 100 + c
#             book_dict = {'Name': name,
#                          'Price': price,
#                          'Availability': avail,
#                          'Book_ID': Book_ID,
#                          'img_url': img_url,
#                          'UPC_Code': book_upc}
#
#             ## save the newly created book dictionary to 'all_books_details' list.
#             all_books_details.insert(book_dict)
#
#             c = c+1
#
#         ## save all the details on firebase server
#         for i in range(len(all_books_details)):
#             book = all_books_details[i]
#             entry(name = book['Name'], price = book['Price'],
#                   avail = book['Availability'], book_id = book['Book_ID'],
#                   book_upc = book['UPC_Code'], img_url = book['img_url'])

# def Scrapping():
from bs4 import BeautifulSoup
import requests
import pyrebase

# connectivity to the fire base
config = {
    'apiKey': "AIzaSyBdpemUwtU64fJNVVhTubjQSUyCybtOc5w",
    'authDomain': "college-connectivity.firebaseapp.com",
    'databaseURL': "https://college-connectivity.firebaseio.com",
    'storageBucket': "college-connectivity.appspot.com",
}
connection = pyrebase.initialize_app(config)

db = connection.database()

## create a global list, that contains all the books dictionaries
all_books_details = []

# To write Into firebase
def entry(name, price, avail, book_id, img_url, book_upc):
    # Book_Id = 100+c

    record = {
        "Book-name":  name, "Book-price": price, "Book-avail": avail,"Book-image": img_url,
        "Book-upc": book_upc,"Book-Id": book_id
    }
    db.child("college-connectivity").child("details").push(record)

# Web scrapping code bellow
link = ["http://books.toscrape.com/index.html"]

# Used to get all webpage address

image_url = []
for i in range(1, 51):
    url = "http://books.toscrape.com/catalogue/page-"+str(i)+".html"
    link.append(url)
c = 1

## save all the details on firebase server
def push_the_details():

    for i in range(len(all_books_details)):
        book = all_books_details[i]
        entry(name=book['Name'], price=book['Price'],
              avail=book['Availability'], book_id=book['Book_ID'],
              book_upc=book['UPC_Code'], img_url=book['img_url'])

#   Iterating through Each page
for pages in range(len(link)):
    index = requests.get(link[pages])
    soup = BeautifulSoup(index.text,"html.parser")
    Book_Category = soup.find_all("div", {"class": "image_container"})

    # Used to iterate to inner web-pages
    for i in range(len(Book_Category)):
        new1 = Book_Category[i].find("a", href=True)
        x = new1["href"]


        # Doing this Because Link were not proper
        if x[0:9] == "catalogue":
            url = "http://books.toscrape.com/"+new1["href"]
        else:
            url = "http://books.toscrape.com/catalogue/"+new1["href"]


        # Reaching the final web-page
        final_page = requests.get(url, verify=False)
        final_soup = BeautifulSoup(final_page.text, "html.parser")

        book_name = final_soup.find("h1")
        name = book_name.getText()

        book_price = final_soup.find("p", {"class": "price_color"})
        price = book_price.getText()[1:]

        book_avail = final_soup.find("p", {"class": "instock availability"})
        avail = (book_avail.getText())[15:40]

        book_img = final_soup.find("img")
        img_url = "http://books.toscrape.com"+book_img["src"][5:]

        book_upc = final_soup.find("td").getText()

        ## use this method to save the data on firebase server
        # entry(name, price, avail, c, img_url, book_upc)

        ## create a new book dictionary, that has all the details of a
        ## particular book.
        Book_ID = 100 + c
        book_dict = {'Name': name,
                     'Price': price,
                     'Availability': avail,
                     'Book_ID': Book_ID,
                     'img_url': img_url,
                     'UPC_Code': book_upc}

        ## save the newly created book dictionary to 'all_books_details' list.
        all_books_details.append(book_dict)

        c = c+1

    ## scrape only 20 pages.
    if (pages == (len(link)-1)):
        push_the_details()
