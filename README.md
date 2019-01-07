# Book Inventory Management

## Web Scrapping using Beautiful Soup 4

```
final_page = requests.get(url, verify=False)
final_soup = BeautifulSoup(final_page.text, "html.parser")
```

## Tkinter GUI

```
if __name__ == "__main__":
    root = Tk()
    top = index(root)
```
##### Used Framing

```
container = tk.Frame(self.master)
container.pack(side="top", expand=True, fill="both")
container.grid_rowconfigure(0, weight=1)
container.grid_columnconfigure(0, weight=1)
```

##### Used Threading

Creating Thread
```
Thread.__init__(self)
self.queue = queue
```

Calling Thread
```
self.master.wait_window(d.top)
```

### ScreenShots

Home Page
![alt welcome](https://github.com/rahuljadli/Book-Inventory-Management/blob/master/screen_shots/start.png)

Displaying All Records

![alt welcome](https://github.com/rahuljadli/Book-Inventory-Management/blob/master/screen_shots/all_records.png)

Login Page

![alt welcome](https://github.com/rahuljadli/Book-Inventory-Management/blob/master/screen_shots/login.png)

Email Verification Mail

![alt welcome](https://github.com/rahuljadli/Book-Inventory-Management/blob/master/screen_shots/email_verification.png)

Forget Password Mail

![alt welcome](https://github.com/rahuljadli/Book-Inventory-Management/blob/master/screen_shots/forget_password.png)

Particular Page Record

![alt welcome](https://github.com/rahuljadli/Book-Inventory-Management/blob/master/screen_shots/particular_book_record.png)


## Steps Taken To Complete This Project

###### Made a Python Script to extract all information regarding a book from books.toscrape.com which is a free practice purpose scraping website having 1000+ records regarding books.

###### Used Google Firebase NoSQL database to store information on cloud and usedn its storage bucket and its authetication system to authenticate the user based on gmail account.

###### Used Tkinter for GUI purpose and used concept of framming and followed OOP approach to make the projects .

###### Used concept of threading to make the desktop app Fast.
