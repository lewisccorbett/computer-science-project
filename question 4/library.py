# Question 4: Adyan, Lewis, Emmanuel, Aryan

# importing modules
import time # used to add delays
import datetime # used to record exact date & time for transactions

# declaring files to be used throughout the program
users_file = "users.txt"
books_file = "books.csv"
transactions_file = "transactions.txt"

# creating user file if not present
try:
    with open (users_file, "r") as users: # will throw an error if file not found
        pass
except FileNotFoundError:
    with open (users_file, "a") as users: # creates file if not present
        pass

# creating books file if not present
try:
    with open (books_file, "r") as books: # will throw an error if file not found
        pass
except FileNotFoundError:
    with open (books_file, "a") as books: # creates file if not present
        pass

# creating transactionf ile if not present
try:
    with open (transactions_file, "r") as transactions: # will throw an error if file not found
        pass
except FileNotFoundError:
    with open(transactions_file, "a") as transasctions: # creates file if not present
        pass

LOGGED_IN = False # boolean variable used throughout program to check if the user has logged in
admin_mode = 0 # variable to determine whether the user can access the admin menu or not 

# a class which determines the layout of a book
class Book:
    def __init__(self, title, author, ID, status):
        self.title = title
        self.author = author
        self.ID = ID
        self.status = status

    def __str__(self):
        return f"Book Title: {self.title},Author: {self.author},ID: {self.ID},Status: {self.status}"


# a class for logging in or registering user
class LoginSystem:
    def __init__(self):
        # creating a dictionary to store the users, assigning admin or user to them
        self.users = {
            # example: user: "[username]" level: "[admin/user]"}
        }
        self.username = ''
    
    def __str__(self):
        return self.username
    
    # a function for registering users
    def register_user(self):
        global user
        try:
            current_account = user.username # this is used to prevent errors when registering new accounts as an admin
        except:
            pass
        while True:
            first_name = input("Enter your FIRST NAME:  ")
            if first_name != "": # ensures the user types something
                break
        while True:
            surname = input("Enter your SURNAME:     ")
            if surname != "":
                break
        level = input("Is the user an (a)dmin or a (u)ser:   ").strip().lower()
        while level not in ["a","u"]: # ensures the user types a or u
            level = input("Is the user an (a)dmin or a (u)ser:   ").strip().lower()
        x=0  # if a user with the same username is present, a number will be added to the end of the username
        self.username = f"{first_name[:3]}{surname[:2]}" # the username is the first 3 letters of the first name, and first 2 of the surname
        while True:
            with open(users_file, "r") as users:
                contents = users.read()
            if self.username in contents: # checks if a user already has the username
                x+=1
                self.username = f"{first_name[:3]}{surname[:2]}{x}" # adds a number if the username is taken
            else:
                break
        if level == "a":
            user = Admin(self.username) # makes the user an admin using the admin calss
        else:
            user = User(self.username) # makes the user a user using the user class
        print(f"Your username is: {self.username}") # this username is essential for logging in

        self.users[self.username] = {"level": "admin" if level == "a" else "user"} # adds the user data to the dictionary
        with open (users_file, "r") as users:
            temp_contents = users.read() # temporarily storing already registered users
        with open (users_file, "w+") as users:
            users.write(f"{temp_contents}{self.users}\n") # clears the file, and writes all previous users including the new user in the file
        if LOGGED_IN: # this is to prevent errors when registering a new account as an admin
            user.username = current_account # makes the username the admin's user to prevent errors
            time.sleep(0.7)
        else:
            self.login() # redirects to login menu
    
    # a function for logging in users
    def login(self):
        global user, LOGGED_IN
        LOGGED_IN = False # variable for whether the user is logged in or not
        with open (users_file, "a+") as users:
            users.seek(0) # files opened in a+ mode starts at the end, so this starts it from the beginning
            temp_list = []
            temp_list.append(users.read()) # adds the existing users to a temp list to check if there are any
            if temp_list == ['']: # if there are no users, redirect to register menu
                print("There are no users! Redirecting to register menu...")
                self.register_user() # redirects to register menu if no users are present
            else:
                while not LOGGED_IN:
                    self.username = input("Enter your username:  ").strip() # asks for username (CASE SENSITIVE)
                    with open (users_file, "r") as users:
                        for line in users:
                            try:
                                user_data = eval(line.strip()) # checks if the username matches data from the file
                                if self.username in user_data: # if the username is found
                                    if 'admin' in line and self.username in line: # if the user is an admin
                                        user = Admin(self.username) # open an admin account for that user
                                        user.select_admin()
                                    else:
                                        user = User(self.username) # open a user account for the user
                                    LOGGED_IN = True # the user is now logged in
                                    print(f"Logged in as {self.username}.")
                                    return # stop execution once found
                            except:
                                continue
                            else:
                                continue
                        if not LOGGED_IN:
                            print("Invalid!") # if the user is not found or any other errors arise


# a class for the main library, including the main menus and functions available for all users despite being an admin or not
class Library:
    def __init__(self):
        self.books = [] # a list of all books
    
    # a function to print out all the books
    def display_books(self):
        with open(books_file, "r") as books:
            contents = books.read()
            if contents == "": # if there are no books
                print("No books available")
            else:
                print(contents)
    
    # a function to search for books
    def search_books(self):
        found = False # a boolean variable which changes if the search term is located
        search_method = input("""Would you like to search by:
1. Book title
2. Author
3. ID
""").strip()
        while search_method not in ["1", "2", "3"]: # loops the input if invalid
            search_method = input("""Would you like to search by:
1. Book title
2. Author
3. ID
""").strip()
        with open(books_file, "r") as books:
            if search_method == "1": # searching for book title
                search_term = input("Enter search term:  ").lower().strip()
                for line in books:
                    book_name, book_author, identification, book_status = line.split(",")
                    if f"book title: {search_term}" == book_name.lower(): # if found
                        found = True
                        print(line)
            elif search_method == "2": # searching for author
                search_term = input("Enter search term:  ").lower().strip()
                for line in books:
                    book_name, book_author, identification, book_status = line.split(",")
                    if f"author: {search_term}" == book_author.lower(): # if found
                        found = True
                        print(line)
            elif search_method == "3": # searching for ID
                search_term = input("Enter search term:  ").lower().strip()
                for line in books:
                    book_name, book_author, identification, book_status = line.split(",")
                    if f"id: {search_term}" == identification.lower(): # if found
                        found = True
                        print(line)
            time.sleep(0.3)
        if not found: # if no results were found
            print("No results returned.")
            time.sleep(0.3)

    # main function which presents the user with a main menu depending on whether they are an admin or a user
    def run(self):
        user = User(self) # makes a reference to the user class
        while True:
            time.sleep(0.3)
            if admin_mode == 1: # if the user is an admin present admin menu
                menu = input("""Admin Menu:
1. Add Book
2. Display Books
3. Remove a Book
4. Search Books
5. Register new user
6. List all users
7. Delete a user
8. Search users
9. Exit
""")
                if menu == "1":
                    Admin(user).add_book()
                elif menu == "2":
                    self.display_books()
                elif menu == "3":
                    Admin(user).remove_book()
                elif menu == "4":
                    self.search_books()
                elif menu == "5":
                    LoginSystem().register_user()
                elif menu == "6":
                    Admin(user).list_users()
                elif menu == "7":
                    Admin(user).delete_user()
                elif menu == "8":
                    Admin(user).search_users()
                elif menu == "9":
                    print("Exiting...")
                    break
                else:
                    print("Invalid!")
                    time.sleep(0.3)

            else: # if the user is a normal user present the user menu
                menu = input("""User Menu:
1. Borrow Book
2. Return Book
3. Display Books
4. Search Books
5. Check Books Taken
6. Exit
""")

                if menu == "1":
                    User(user).borrow_book()
                elif menu == "2":
                    User(user).return_book()
                elif menu == "3":
                    self.display_books()
                elif menu == "4":
                    self.search_books()
                elif menu == "5":
                    User(user).number_of_books(False)
                elif menu == "6":
                    print("Exiting...")
                    break
                else:
                    print("Invalid!")
                    time.sleep(0.3)


# a class for a user with default permissions
class User:
    def __init__(self, username):
        self.username = username

    # a function to tell the number of books taken by the user (5 max books), or to check the number of books for another function
    def number_of_books(self, check):
        count = 0 # an integer variable to count for every book the user has borrowed
        temp_list = [] # a temp list which will store each book the user has borrowed
        with open(books_file, "r") as books:
            for line in books:
                if user.username in line:
                    book_name, book_author, identification, book_status = line.split(",")
                    count += 1 # increments the count if the book is borrowed by the user
                    temp_name = book_name.replace("Book Title: ", "")
                    temp_author = book_author.replace("Author: ","")
                    temp_id = identification.replace("ID: ","")
                    temp_list.append(f"{temp_name} by {temp_author} (ID: {temp_id})")
        if check: # if the number of books is to be used by another function
            return count # return the number of books taken out
        else: # if the number of books is to be presented to the user
            if count > 0:
                print(f"{user.username}, you have taken out {count} books:\n{temp_list}")
            else:
                print(f"{user.username}, you haven't taken out any books")

    # a function for users to borrow books
    def borrow_book(self):
        books_taken = User.number_of_books(self, True)
        if books_taken == 5: # maximum books
            print("You cannot borrow anymore books! Return a book to borrow more.")
            time.sleep(0.4)
            return # stops execution
        with open(books_file, "r") as books:
            if books.read() == "":
                print("There are no books to borrow!") # checks if there are any books in the file
                return # stops execution

        borrowed = False # a boolean variable to check if a book has been succesfully borrowed or not
        ID = input("Enter the ID of the book you would like to borrow:  ")
        temp_list = [] # temporary list
        with open(books_file, "r+") as books:
            books.seek(0)
            for line in books:
                book_name, book_author, identification, book_status = line.split(",") # splits data in the books file into separate variables
                if identification != f"ID: {ID}": # if the ID does not match the input add it to the temporary array
                    temp_list.append(line) 
                else:
                    if book_status.strip() != "Status: Available": # if the book is not available
                        print("This book is already taken!")
                        return # stops execution
                    borrowed = True # declares the book borrowed
                    updated_info = f"{book_name},{book_author},{identification},Status: {user.username}\n" # changes status to the username
                    temp_list.append(updated_info) # adds the new info the the temporary array
                    borrowed_book = book_name
                    borrowed_book_author = book_author
                    continue
            if borrowed: 
                with open(books_file, "w") as books:
                    for line in temp_list:
                        books.write(line) # writes the contents of the temporary list into the books to update it successfully
                print(f"You have borrowed {borrowed_book}")
                Transactions().record_transaction(user.username,True,False,borrowed_book,borrowed_book_author)
    
    # a function for returning books borrowed by a user
    def return_book(self):
        with open(books_file, "r") as books:
            if books.read() == "":
                print("There are no books to return!") # checks if there any books in the file
                return # stops exection
            
        returned = False # a boolean variable to determine whether a book has been successfully returned or not
        ID = input("Enter the ID of the book you would like to return:  ")
        temp_list = [] 
        with open(books_file, "r+") as books:
            books.seek(0)
            for line in books: # goes through each line of the file
                book_name, book_author, identification, book_status = line.split(",")
                if identification != f"ID: {ID}": # if the current line does not include the requested ID
                    temp_list.append(line) # the line is added to the temp list
                else:
                    if book_status.strip() == "Status: Available": # if the book is available, it cannot be returned
                        print("You can't return a book which you haven't taken out!")
                        return # stops execution
                    if book_status.strip() == f"Status: {user.username}": # checks that the book has been taken out by the current user
                        returned = True # declares the book returned
                        updated_info = f"{book_name},{book_author},{identification},Status: Available\n" # updates the status to available
                        temp_list.append(updated_info)
                        returned_book = book_name
                        returned_book_author = book_author
                        continue
                    else:
                        print("You can't return a book which you haven't taken out!")
                        return
            if returned: 
                with open(books_file, "w") as books:
                    for line in temp_list:
                        books.write(line)
                print(f"You have returned {returned_book}")  
                Transactions().record_transaction(user.username,False,True,returned_book,returned_book_author)      


# a class for a user with administrator permissions
class Admin:
    def __init__(self, username):
        self.username = username

    # a function to ensure the user is an admin
    def select_admin(self):
        global admin_mode
        admin_mode = 1

    # a function to add books to the library
    def add_book(self):
        while True:
            book_title = input("Enter the book name: ")
            if "," in book_title:
                print("Please do not include commas!")
            elif book_title != "": # ensures the book name has characters
                break
        while True: # loops until valid
            author = input("Enter the author of the book: ")
            if author != "":
                break
        while True:
            try:
                ID = int(input("Enter the ID of the book: "))
                valid = True # a variable to check if the id is valid orw not
                with open(books_file, "r") as books:
                    for line in books:
                        book_name, book_author, identification, book_status = line.split(",")
                        if identification == f"ID: {ID}": # if a book already has the id
                            print("A book already has this ID!")
                            valid = False
                        else:
                            continue
                if ID < 0: # ensuring the id is a positive number
                    print("ID must be positive!")
                    valid = False
                if valid:
                    break
            except ValueError: # if the id is not in integer format
                print("Invalid format!")
        status = "Available"

        book = Book(book_title, author, ID, status) # the book class is used to format the new book
        print(f"Added {book_title} by {author}!")
        
        with open(books_file, "a+") as books:
            books.write(f"{Book.__str__(book)}\n") # adds the new book to the file

    # a function for removing books
    def remove_book(self):
        removed = False # a boolean variable to determine if a book has been successfully removed or not
        cancel = False # a boolean variable to check if the operation has been cancelled
        temp_list = []
        while True:
            try:
                ID = int(input("Enter the ID of the book you want to remove, or press ENTER to cancel:  "))
                break
            except ValueError: # if the user inputs nothing or a wrong value, the operation stops
                cancel = True
                break
        if not cancel: # if the operation is ongoing
            with open(books_file, "r+") as books:
                books.seek(0)
                for line in books:
                    book_name, author, identification, status = line.split(",")
                    if identification != f"ID: {ID}": # checks if the id matches any in the file
                        temp_list.append(line) # if it does not match, it is added to a temporary list
                    else:
                        removed = True # if the id is found, declare it removed
                        removed_book_name = book_name
                        continue
            if removed == True: 
                with open(books_file, "w") as books:
                    for line in temp_list:
                        books.write(line) # clears the books and writes the updated version with the removed book
                print(f"{removed_book_name} has been removed.")

    # a function for listing all users
    def list_users(self):
        with open(users_file, "r") as users:
            print("{'Username'}: {'level': [admin/user]} <-- FORMAT") # shows the user the format
            print(users.read())
            time.sleep(1)
    
    # a function for searching all the users for a term
    def search_users(self):
        found = False # a boolean variable to determine whether the search term has been located in the file or not
        with open(users_file, "r") as users:
            search_term = input("Enter search term: ")
            for line in users:
                if search_term.lower() in line.lower(): # if the search term is found in a line
                    found = True
                    print(line) # the line is printed
            time.sleep(0.6)
        if not found: # if no results were found at all
            print("No results returned.")
            time.sleep(0.3)

    # a function for deleting a user
    def delete_user(self):
        global user
        user_to_delete = input("Enter the username of the user to delete:  ")

        if user_to_delete == user.username: # if the input is the current user, stop execution
            print("You can't delete an account currently in use!")
            return # stops execution

        deleted = False # a boolean variable to determine whether an account has been deleted or not
        temp_list = []

        with open(users_file, "a+") as users:
            users.seek(0)
            for line in users: # goes through every line in the user file
                user_data = eval(line.strip()) 
                if user_to_delete not in user_data: # if the user requested is not found in the current line
                    temp_list.append(line)
                else:
                    deleted = True # declare the user deleted
                    continue
        
        if deleted:
            with open(users_file, "w") as users: # clears the file 
                for line in temp_list:
                    users.write(line) # adds updated user list to file
            print(f"{user_to_delete} has been deleted!") 
        else:
            print("User not found.")
                

# a class used to record the date and time for all books borrowed and returned
class Transactions:
    def __init__(self):
        self.transactions_file = "transactions.txt"
    
    # a function used to record transactions in a file
    def record_transaction(self,user,borrowed,returned,title,author):
        with open(self.transactions_file, "a") as transactions:
            if borrowed:
                transactions.write(f"{datetime.datetime.now()}: {user} borrowed {title} by {author}\n")
            elif returned:
                transactions.write(f"{datetime.datetime.now()}: {user} returned {title} by {author}\n")



# main
new_user = input("To register, type 'register', otherwise press ENTER to continue\n").strip().lower()
if new_user == "register":
    LoginSystem().register_user()
else:
    LoginSystem().login()
Library().run()
