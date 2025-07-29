# chat gpt project !
class Book : 
    def __init__(self,book_id,title,author,quantity): 
        self.book_id = book_id 
        self.title = title 
        self.author = author 
        self.quantity = quantity
class User : 
    def __init__(self, user_id, name ,borrowed_books ): 
        self.user_id = user_id 
        self.name = name 
        self.borrowed_books = borrowed_books
class Libary : 
    def __init__(self): 
        self.books = []
        self.users = []
    def add_book(self): 
        while True : 
            try: 
                book_id = int(input('gives us book id: ')) #you msut make it auto !
                title = input('Gives us book title : ')
                author = input('Gives us the book author: ')
                quanity = int(input('gives book queniti : '))
                break 
            except ValueError : 
                print('gives us a valid value !')
        book = Book(book_id, title, author, quanity)
        self.books.append(book)
    def show_books(self): 
        if not self.books : 
            print('no books avaliable right knew !')
        else : 
            print('this is the lsit of book in our libary bro !')
            for book in self.books : 
                print(f'book id : {book.book_id} | book title : {book.title} | book author : {book.author} | book quantity : {book.quantity}')
    def edit_book(self): 
        try :
            book_id_edit = int(input('Gives us the id of book you wnna change ?'))
        except ValueError : 
            print('plz gives us a vlaid value bro !')
            return 
        for book in self.books : 
            if book_id_edit == book.book_id : # books was found !
                try : 
                    new_title = input('Gives us new title : ')
                    new_author = input('Gives us the new author of book !'); 
                    new_quantity = int(input('Gives us new Quantity : '))
                except ValueError : 
                    print('Gives us a valid values !')
                    return
                book.title = new_title 
                book.author = new_author
                book.quantity = new_quantity
                print('the book was edited Succefely !')  # books was edited !
                return 
            
        print(" Book with that ID was not found.")   # book was  not found bro !   
         
    # delet book function : 
    def delete_book(self): 
        try : 
            delete_book_id = int(input('gives us the id of book you wanna delet'))
        except ValueError : 
            print('gives us a valid id plz !')
            return
        for book in self.books: 
            if book.book_id == delete_book_id : 
                self.books.remove(book)
                print('The boook was delet succefely !')
                return
                
        print(" Book with that ID was not found.")   # book was  not found bro !   
        
    #adding a user : 
    def add_user(self): 
        try :
            user_id = int(input('gives us the user id : '))
            user_name = input('gives us your name : ')
            books_borrowed = []
            while True : 
                print('**Menu**')
                print('1-add book to your borrowed books')
                print('2-Exit')
                user_choise = int(input('give us yrou choise bro : '))
                if user_choise == 1 : 
                    book_borrowed_name = input('gives us the book name !')
                    books_borrowed.append(book_borrowed_name)
                elif user_choise == 2 : 
                    print('okey !')
                    break
                else: 
                    print('Invalid choise !')
            
            user = User(user_id, user_name, books_borrowed)
            self.users.append(user)     
            print('the book was added succrfelly !')     
        except ValueError :
            print('plz gives us a valid values !')
        
        
                
              
        
                
     
        
            
