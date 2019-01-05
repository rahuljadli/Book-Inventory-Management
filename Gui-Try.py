import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from tkinter.font import Font
from tkinter import font
from tkinter.ttk import Combobox
from PIL import ImageTk, Image
import pyrebase
from tkinter import simpledialog
import connect as st
# import Webscrap as ws
import queue as q
from threading import Thread

globaldata : dict

class index:

    def __init__(self, master):
        # tk.Tk.__init__(self)
        self.master = master

        # Making a frame
        container = tk.Frame(self.master)
        container.pack(side="top", expand=True, fill="both")

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # Will contain all the pages'
        self.frames = {}
        for F in (StartPage, LogInPage, SignInPage, SearchPage, DisplayPage):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        ## create event generator - DisplayData that should be called whenever we show the frame.
        ## frame.event_generate("<<DisplayData>>")
        frame.tkraise()

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        back = Label(self, bg="powder blue", width=1800, height=2)
        back.pack(side=TOP)

        font_Title = Font(family="Georgia", weight="bold", size=28)
        font_Button = Font(family="Sylfaen")
        font_Bottom = Font(family="sylfaen", weight="bold", size=22)

        label = tk.Label(self, text="Welcome To Book Shell", font=font_Title, bg="red")
        label.pack(fill=X)

        button1 = tk.Button(self, text="Log In", bg="yellow", fg="red",
                            font=font_Button, command=lambda: controller.show_frame(LogInPage))

        button1.place(x=250, y=190)

        button2 = tk.Button(self, text="Sign Up",
                            bg ="yellow", fg="red", font=font_Button, command=
                            lambda: controller.show_frame(SignInPage))

        button2.place(x=430, y=190)

        bottom_frame = Label(self, text="We Love Web Scrapping", font=font_Bottom,
                             fg="green", bg="orange")

        bottom_frame.pack(side=BOTTOM, fill=X)


class SignInPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        font_Title = Font(family="Georgia", weight="bold", size=28)
        font_Button = Font(family="Sylfaen")
        font_Bottom = Font(family="sylfaen", weight="bold", size=22)
        font_Details = Font(family="Georgia", weight="bold", size=14)

        Detail_Block = Label(self, text="Welcome Fill Your Details", font=font_Title,
                             bg ="red")
        Detail_Block.pack(fill=X)
        Label_UserEmail = tk.Label(self, text="Email Id", font=font_Details)
        Label_UserEmail.place(x=150, y=136)

        Label_Password = tk.Label(self, text = "Password", font = font_Details)
        Label_Password.place(x=150, y=176)

        UserEmail = Entry(self, font = font_Details)
        UserEmail.place(x = 300, y = 136)

        Password = Entry(self, font = font_Details, show = "*", fg = "black")
        Password.place(x = 300, y = 176)

        SignInButton = Button(self, text = "Sign Up", font = font_Button, fg = "red"
                              , command = lambda: self.create(UserEmail.get(), Password.get(), controller))

        SignInButton.place(x = 320, y = 235)

        HomeButton = Button(self, text = "Home", font = font_Button,
                            fg = "red", command = lambda: controller.show_frame(StartPage))

        HomeButton.place(x = 400, y = 235)
        bottom_frame = Label(self, text = "We Love Web Scrapping", font = font_Bottom,
                             fg = "green", bg = "orange")

        bottom_frame.pack(side = BOTTOM, fill = X)

    def create(self, UserEmail, Password, controller):

        b = st.CreateAccount(UserEmail, Password)

        if b == 1:
            controller.show_frame(LogInPage)
        else:
            messagebox.showinfo("Info", "Invalid Password Or Email")


class LogInPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        font_Title = Font(family="Georgia", weight="bold", size=28)
        font_Button = Font(family="Sylfaen")
        font_Bottom = Font(family="sylfaen", weight="bold", size=22)
        font_Details = Font(family="Georgia", weight="bold", size=14)

        DetailBlock = Label(self, text="Enter Your Details", font=font_Title, bg="red")
        DetailBlock.pack(fill=X)
        LabelUserName = tk.Label(self, text="User Name", font=font_Details)
        LabelUserName.place(x=150, y=136)

        LabelPassword = tk.Label(self, text="Password", font=font_Details)
        LabelPassword.place(x=150, y=176)

        UserName = Entry(self, font=font_Details, show="")
        UserName.place(x=300, y=136)

        Password = Entry(self, font=font_Details, show="*", fg="black")
        Password.place(x=300, y=176)

        LogInButton = Button(self, text="Log In", font=font_Button, fg="red"
                             , command=lambda: self.LogInaccount(UserName.get(), Password.get(), controller))

        LogInButton.place(x=320, y=235)

        HomeButton = Button(self, text="Home", font=font_Button, fg="red"
                            , command=lambda: controller.show_frame(SearchPage))

        HomeButton.place(x=400, y=235)

        Forget_Button = Button(self, text="Forget password", fg="black"
                               , height=1, command=lambda: self.Reset_Password())

        Forget_Button.place(x=330, y=285)

        bottom_frame = Label(self, text="We Love Web Scrapping", font=font_Bottom,
                             fg="green", bg="orange")

        bottom_frame.pack(side=BOTTOM, fill=X)

    def Reset_Password(self):
        s = simpledialog.askstring("Input", "Enter Your Email-Id")
        b = st.ResetPassword(s)
        if b == 1:
            messagebox.showinfo("Info", "reset link send to your Email")

    def LogInaccount(self, UserName, Password, controller):

        b = st.LogAccount(UserName, Password)
        if b == 1:
            controller.show_frame(SearchPage)
        else:
            messagebox.showinfo("Info", "Invalid Password Or Email")


class SearchPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        back = Label(self, bg="powder blue", width=1800)
        back.pack(side=TOP)
        font_Title = Font(family="Georgia", weight="bold", size=28)
        font_Button = Font(family="Sylfaen")
        font_Bottom = Font(family="sylfaen", weight="bold", size=22)
        font_box = Font(family="Georgia", weight="bold", size=16)

        # rahuljadli19@gmail.com
        label = tk.Label(self, text = "Welcome To Search Shell", font = font_Title, bg = "red")
        label.pack(fill = X)
        labe2 = tk.Label(self, text = "Enter the Details",
                         font = font_Title, bg = "powder blue")
        labe2.pack(fill = X)

        search_label = Label(self, text = "Search By:", font = font_box)
        search_label.place(x = 110, y = 144)

        search_list = ["Book Name", "Book Id", "Book UPC", "Book price", "Book Genre"]
        self.combobox = Combobox(self, values = search_list, height = 5, width = 14, font = font_box)
        self.combobox.place(x = 280, y = 144)

        enter = Label(self, text = "Enter Detail:", font = font_box)
        enter.place(x = 110, y = 190)
        self.entrybox = Entry(self, font = font_box, show = "", fg = "black", width = 16)
        self.entrybox.place(x = 280, y = 190)

        search_button = Button(self, text = "Search", font = font_box, bg = "#47d147",
                               width = 7, command = lambda: self.getEnteredDetails())
        search_button.place(x = 545, y = 160)

        scriptbox = Label(self, text = "Run Script:", font = font_box)
        scriptbox.place(x = 110, y = 250)  # 47d147

        run_button = Button(self, text = "Run", font = font_box, bg = "#47d147",
                            width = 7, command = lambda: self.message())
        run_button.place(x = 335, y = 240)

        view_label = Label(self, text = "View All Records", font = font_box
                           )
        view_label.place(x = 110, y = 320)

        viewall_button: Button = Button(self, text="View", font=font_box,
                                        bg="#47d147", width=7,
                                        command=lambda: controller.show_frame(DisplayPage))
        viewall_button.place(x=335, y=310)
        button2 = tk.Button(self, text="Home", bg="#47d147", width=7
                            , font=font_box, command=lambda: controller.show_frame(StartPage))

        button2.place(x=463, y=420)
        bottom_frame = Label(self, text="We Love Web Scrapping", font=font_Bottom,
                             fg="green", bg="orange")
        bottom_frame.pack(side=BOTTOM, fill=X)

    ## this function is used to run the script....
    def message(self):
        messagebox.showinfo("Fetching Data from Website", "Script running successfully in Background")

    ## get the entered details of the user
    def getEnteredDetails(self):
        selected_item_list = self.combobox.get()
        details = self.entrybox.get()

        ## check if the details are empty or not
        if ((selected_item_list != '') & (details != '')) :
            # self.refinedStartSearchingWithThreaded(selected_item_list, details)

            d = MyDialog(self.master, selected_item_list, details)

            self.master.wait_window(d.top)
            self.callNewFrame(single_book_detail=globaldata)
        else:
            messagebox.showerror("Error", "Please enter any detail to search.")

    ## @args : single_book_detail : show the details of a single book at a time.
    ## description : call this method to show the details of the book
    def callNewFrame(self, single_book_detail):
        displaySingleBookDetails = tk.Tk()
        displaySingleBookDetails.geometry("780x520+160+80")
        displaySingleBookDetails.title(single_book_detail['Book-name'])

        self.font_box = font.Font(family="Georgia", weight="bold", size=16)
        self.font_data = font.Font(family="Sylfaen", size=16)

        label = tk.Label(displaySingleBookDetails, text="Displaying Book Details", bg="red", font=self.font_box)
        label.pack(fill=X)
        # label.grid(row=0, columnspan=6)

        search_label = Label(displaySingleBookDetails, text="Book Name", font=self.font_box)
        search_label.place(x=110, y=144)
        # search_label.grid(row=1, column=0)

        book_name = Label(displaySingleBookDetails, text=single_book_detail['Book-name'], height=5, width=14,
                          font=self.font_data)
        book_name.place(x=525, y=90)
        # book_name.grid(row=1, column=1)

        enter = Label(displaySingleBookDetails, text="Book Price", font=self.font_box)
        enter.place(x=110, y=190)
        # enter.grid(row=2, column=0)

        book_price = Label(displaySingleBookDetails, text=single_book_detail['Book-price'], fg="black", width=16,
                           font=self.font_data)
        book_price.place(x=485, y=190)
        # book_price.grid(row=2, column=1)

        scriptbox = Label(displaySingleBookDetails, text="Number of Books Available", font=self.font_box)
        scriptbox.place(x=110, y=250)  # 47d147
        # scriptbox.grid(row=3, column=0)

        run_button = Label(displaySingleBookDetails, text=single_book_detail['Book-avail'], font=self.font_data)
        run_button.place(x=550, y=250)
        # run_button.grid(row=3, column=1)

        view_label = Label(displaySingleBookDetails, text="Book UPC Code", font=self.font_box)
        view_label.place(x=110, y=320)
        # view_label.grid(row=4, column=0)

        viewall_button = Label(displaySingleBookDetails, text=single_book_detail['Book-upc'], font=self.font_data)
        viewall_button.place(x=550, y=320)
        # viewall_button.grid(row=4, column=1)

        displaySingleBookDetails.mainloop()

## use this view to show the details of all the books
class DisplayPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        tree = ttk.Treeview(self)
        xsb = ttk.Scrollbar(self, orient='horizontal', command=tree.xview)
        tree.configure(xscroll=xsb.set)
        # xsb.pack(side=RIGHT, fill=Y)

        back = Label(self, bg="powder blue", width=1800, height=2)
        back.pack(side=TOP)

        font_Title = Font(family="Georgia", weight="bold", size=28)
        font_Button = Font(family="Sylfaen")
        font_Bottom = Font(family="sylfaen", weight="bold", size=22)

        label = tk.Label(self, text="Book Records:", font=font_Title, bg="red")
        label.pack(fill=X)

        # filename = Image.open("C:\\Users\\Rahul jadli\\PycharmProjects\\College-Project\\graphicera.png")
        # filename = Image.open("Age-Distribution.png")
        # render: PhotoImage = ImageTk.PhotoImage(filename)
        # render = ImageTk.PhotoImage(filename)

        tree["columns"] = ("one", "two", "three", "four", "five")
        tree.column("one", width=120)
        tree.column("two", width=267)
        tree.column("three", width=160)
        tree.column("four", width=80)
        tree.column("five", width=330)

        tree.heading("one", text="Book Number", anchor='center')
        tree.heading("two", text="Book Title", anchor='center')
        tree.heading("three", text="genre", anchor='center')
        tree.heading("four", text="Price", anchor='center')
        tree.heading("five", text="Image", anchor='center')

        tree.config(height=15)
        i = 1
        # Call to function

        Record = st.All_Record()

        for book in Record.each():
            record = book.val()

            tree.insert('', i, text=str(i),
                        values=(record["Book-Id"], record["Book-name"],
                                record["Book-avail"], record["Book-price"], record["Book-image"]))

            # tree.insert('', i, text=str(i), open=True, image=render)

            i = i + 1

        tree.pack()

        # vsb = ttk.Scrollbar(self, orient="vertical",
        #                     command=tree.yview)

        # tree.config(yscrollcommand=vsb.set)
        # tree.grid(row=0, column=0)
        # # ysb.grid(row=0, column=1, sticky='ns')
        # xsb.grid(row=1, column=0, sticky='ew')
        # self.grid()

        bottom_frame = Label(self, text="We Love Web Scrapping", font=font_Bottom,
                             fg="green", bg="orange")

        bottom_frame.pack(side=BOTTOM, fill=X)
        button2 = tk.Button(self, text="Home", bg="#47d147", fg="red"
                , font=font_Button, command=lambda: controller.show_frame(StartPage))

        button2.place(x=463, y=420)



## different thread class is used to download the data
## description : this class will start the thread for different arguments.
class ThreadedTask(Thread):

    ## description : initialize the thread class
    def __init__(self, queue, selected_item_list, details):
        Thread.__init__(self)
        self.queue = queue
        self.selected_item_list = selected_item_list
        self.details = details

    ## description : this method will start the thread that downloads the data from firebase-realtime database
    def run(self):
        data = st.searchRecord(self.selected_item_list, self.details)
        self.queue.put(data)


## Dialog class, to show dialog box containing the progress bar
class MyDialog:

    def __init__(self, parent, selected_item_list, details):
        top = self.top = Toplevel(parent)
        top.title("Downloading Data..")

        self.selected_item_list = selected_item_list
        self.details = details

        # Label(top, text="Downloading Data").pack()

        self.progress_bar = ttk.Progressbar(top, orient="horizontal",
                                        length=200, mode="determinate")
        self.progress_bar.pack()

        # b = Button(top, text="OK", command=lambda : self.ok())
        # b.pack(pady=5)
        self.progress_bar.start(interval=10)
        self.refinedStartSearchingWithThreaded(self.selected_item_list, self.details)


    # def ok(self):
    #     # print("Data downloaded successfully")
    #     # data =
    #     self.top.destroy()
    #     # return data

    ## @args : selected_item_list - search the book by this parameter
    ## @args : detail - value of the selected parameter to search
    ## description : this method will give control to the thread class to download contents from firebase-realtime database
    def refinedStartSearchingWithThreaded(self, selected_item_list, details):
        self.queue = q.Queue()
        ThreadedTask(self.queue, selected_item_list, details).start()
        self.top.after(100, self.process_queue)
        # return data

    ## start the queue to download the data from firebase-realtime database
    ## description : this method will keep on checking if the queue process has been completed or not
    ## and once it's done, it will show error or info message based on the data received.
    def process_queue(self):
        global globaldata
        try:
            msg = self.queue.get(0)

            ## class another class to show the data
            if (len(msg.each()) == 0):
                print("Nothing found...")
                messagebox.showerror("Error", "Nothing found.. Please try another parameters.")
            else:
                ## iterate through the data
                self.progress_bar.stop()
                messagebox.showinfo("Success", "Data Downloaded successfully.")
                single_book_detail: dict
                for detail in msg.each():
                    single_book_detail = detail.val()

                # self.callNewFrame(single_book_detail)
                # return single_book_detail
                globaldata = single_book_detail
                self.top.destroy()

        except q.Empty:
            self.top.after(100, self.process_queue)

    '''
        Entry Point to the program
    '''
if __name__ == "__main__":
    root = Tk()
    top = index(root)
    root.geometry("780x520+160+80")
    root.title("Book Shell")
    root.maxsize(width=1000, height=550)
    root.minsize(width=1000, height=550)
    # root.iconbitmap("open_book_vug_icon.ico")
    root.mainloop()
