from pyrebase.pyrebase import Firebase, Database


def CreateAccount(email, password):

    b=0
    import pyrebase

    # connectivity to the fire base
    config = {
        'apiKey': "#########",
        'authDomain': "######.firebaseapp.com",
        'databaseURL': "https://#####.firebaseio.com",
        'storageBucket': "#####.appspot.com",
    }
    connection: Firebase = pyrebase.initialize_app(config)
    auth = connection.auth()
    try:

        user = auth.create_user_with_email_and_password(email, password)
        security=auth.send_email_verification(user['idToken'])
        return 1

    except:
        b=0
    return b


def LogAccount(username, password):

    b = 0
    import pyrebase

    # connectivity to the fire base
    config = {
        'apiKey': "######",
        'authDomain': "#####.firebaseapp.com",
        'databaseURL': "https://#####.firebaseio.com",
        'storageBucket': "####.appspot.com",
    }
    connection = pyrebase.initialize_app(config)
    auth = connection.auth()
    try:

        user = auth.sign_in_with_email_and_password(username, password)

        b=1
    except:
        b = 0

    return b

def ResetPassword(email) :

    b = 0
    import pyrebase

    # connectivity to the fire base
    config = {
        'apiKey': "######",
        'authDomain': "#####.firebaseapp.com",
        'databaseURL': "https://#####.firebaseio.com",
        'storageBucket': "####.appspot.com",
    }

    connection = pyrebase.initialize_app(config)
    auth = connection.auth()
    try:

        user = auth.send_password_reset_email(email)
        b = 1

    except:
        b = 0
    return b

def All_Record():

    import pyrebase
    config = {
        'apiKey': "######",
        'authDomain': "#####.firebaseapp.com",
        'databaseURL': "https://#####.firebaseio.com",
        'storageBucket': "####.appspot.com",
    }

    connection = pyrebase.initialize_app(config)
    firebase: Database = connection.database()

    book_record = firebase.child("#####").child("details").get()

    return book_record

def searchRecord(key, value):
    import pyrebase
    config = {
        'apiKey': "######",
        'authDomain': "#####.firebaseapp.com",
        'databaseURL': "https://#####.firebaseio.com",
        'storageBucket': "####.appspot.com",
    }

    connection = pyrebase.initialize_app(config)
    firebase: Database = connection.database()

    key_map_dict = {
        "Book Name": "Book-name",
        "Book Id" : "Book-Id",
        "Book UPC" : "Book-upc",
        "Book price": "Book-price"
    }

    key = key_map_dict.get(key, "Not Found")

    book_details = firebase.child("####").child("details").order_by_child(key).equal_to(value).get()
    # if (book_details.key())
    # print(book_details)
    return book_details
