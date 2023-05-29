from tkinter import *
from libclass import *
from tkinter import messagebox
    
class LibraryControl:
    def __init__(self,library):
        self.library=library
        self.admin_role=False
        self.win=Tk()
        self.win.title("Library Control System")
        self.loginGUI()
        print(Mylib.admin)
        self.win.mainloop()
    
    def loginGUI(self):
        self.win.geometry("300x300")
        self.loginlab=Label(self.win,text="Login",font=("Arial",30))
        self.loginlab.grid(row=0,column=0,columnspan=2,padx=10,pady=10)
        self.usernamelab=Label(self.win,text="Username: ")
        self.usernamelab.grid(row=1,column=0,padx=10,pady=10)
        self.UNentry=Entry(self.win)
        self.UNentry.grid(row=1,column=1)
        
        self.passwordlab=Label(self.win,text="Password: ")
        self.passwordlab.grid(row=2,column=0,padx=10,pady=10)
        self.PWentry=Entry(self.win,show="*")
        self.PWentry.grid(row=2,column=1,padx=10,pady=10)
        
        self.loginbut=Button(self.win,text="Login",command=self.ValidLogin)
        self.loginbut.grid(row=3,column=0,columnspan=2)
        Label(self.win,text="Quit if wrong username or password")
        
    def ValidLogin(self):
        self.password=self.PWentry.get()
        self.username=self.UNentry.get()
 
        if Mylib.login(self.username,self.password,user_data,admin_data):
            self.admin_role=Mylib.admin
            self.ShowLibrary()
        else:
            self.win.quit()
    def ShowLibrary(self):
        self.loginlab.destroy()
        self.usernamelab.destroy()
        self.passwordlab.destroy()
        self.UNentry.destroy()
        self.PWentry.destroy()
        self.loginbut.destroy()
        self.win.geometry("900x900")
        Label(self.win,text="Library control",font=("Arial",30)).pack()
        self.entry=Entry(self.win,font=("Arial",20))
        self.entry.pack(pady=40)
        self.entrytext=""
        self.menuframe=Frame(self.win)
        self.menuframe.pack()
        if self.admin_role:
            Label(self.menuframe,text="Logined as admin ",font=("Arial",20)).grid(row=4,column=0,columnspan=3)
        else:
            Label(self.menuframe,text="Logined as user",font=("Arial",20)).grid(row=4,column=0,columnspan=3)
        #menu frame
        self.info_but=Button(self.menuframe,text="Book information",padx=10,pady=10,command=self.Infor)
        self.check_avai_but=Button(self.menuframe,text="Available Book",padx=10,pady=10,command=self.Checkavai)
        self.check_out_book_but=Button(self.menuframe,text="Check out book",padx=10,pady=10,command=self.Checkout)
        self.return_book_but=Button(self.menuframe,text="Return book",padx=10,pady=10,command=self.Return)
        self.find_book_by_title_but=Button(self.menuframe,text="Find book by title",padx=10,pady=10,command=self.FindByTitle)
        self.find_book_by_author_but=Button(self.menuframe,text="Find book by author",padx=10,pady=10,command=self.FindByAuthor)
        self.show_all_book_but=Button(self.menuframe,text="Show all books",padx=10,pady=10,command=self.ShowAllBook)
        self.show_all_avai_books_but=Button(self.menuframe,text="Show all available books",padx=10,pady=10,command=self.ShowAllAvaiBook)
        self.show_history_but=Button(self.menuframe,text="Show history",padx=10,pady=10,command=self.ShowHisto)
        self.add_book_but=Button(self.menuframe,text="Add book",padx=10,pady=10,command=self.AddBook)
        self.remove_book_but=Button(self.menuframe,text="Remove book",padx=10,pady=10,command=self.RemoveBook)
        self.quit_but=Button(self.menuframe,text="Quit",command=self.Quit,padx=10,pady=10)

        self.info_but.grid(row=0,column=0,padx=10,pady=10)
        self.check_avai_but.grid(row=0,column=1,padx=10,pady=10)
        self.check_out_book_but.grid(row=0,column=2,padx=10,pady=10)
        self.return_book_but.grid(row=1,column=0,padx=10,pady=10)
        self.find_book_by_title_but.grid(row=1,column=1,padx=10,pady=10)
        self.find_book_by_author_but.grid(row=1,column=2,padx=10,pady=10)
        self.show_all_book_but.grid(row=2,column=0,padx=10,pady=10)
        self.show_all_avai_books_but.grid(row=2,column=1,padx=10,pady=10)
        self.show_history_but.grid(row=2,column=2,padx=10,pady=10)
        self.quit_but.grid(row=3,column=1,padx=10,pady=10)
        if self.admin_role:
            self.add_book_but.grid(row=3,column=0,padx=10,pady=10)
            self.remove_book_but.grid(row=3,column=2,padx=10,pady=10)

        self.textbox=Text(self.win,width=900)
        self.textbox.pack()

    def ClearOutput(self):
        self.textbox.delete("1.0",END)
    def GetInput(self):
        self.entrytext=nice(self.entry.get())
    def GetAndClear(self):
        self.ClearOutput()
        self.GetInput()
    def Infor(self):
        self.GetAndClear()
        i=0
        for book in self.library:
            if book.title.lower()==self.entrytext.lower():
                i+=1
                self.textbox.insert(f"{i}.0",book.infor())
                i+=1
        if i==0:
            self.textbox.insert("1.0","Can't find this book!")
    def Checkavai(self):
        self.GetAndClear()
        i=0
        for book in self.library:
            if book.title.lower()==self.entrytext.lower():
                i+=1
                self.textbox.insert(f"{i}.0",book.is_available())
                i+=1
        if i==0:
            self.textbox.insert("1.0","Can't find this book!")
    def Checkout(self):
        self.GetAndClear()
        i=0
        for book in self.library:
            if book.title.lower()==self.entrytext.lower():
                i+=1
                self.textbox.insert(f"{i}.0",book.check_out(history,self.username,book))
                break
        if i==0:
            self.textbox.insert("1.0","Can't find this book!")
    def Return(self):
        self.GetAndClear()
        i=0
        for book in self.library:
            if book.title.lower()==self.entrytext.lower():
                i=1
                self.textbox.insert(f"{i}.0",book.return_book(history,self.username,book))
                
        if i==0:
            self.textbox.insert("1.0","Can't find this book!")
    def FindByAuthor(self):
        self.GetAndClear()
        text=Mylib.search_book_by_author(self.entrytext)
        self.textbox.insert("1.0",text)
    def FindByTitle(self):
        self.GetAndClear()
        text=Mylib.search_book_by_title(self.entrytext)
        self.textbox.insert("1.0",text)
    def ShowAllBook(self):
        self.GetAndClear()
        text=Mylib.display_book()
        self.textbox.insert("1.0",text)
    def ShowAllAvaiBook(self):
        self.GetAndClear()
        text=Mylib.display_available_book()
        self.textbox.insert("1.0",text)
    def ShowHisto(self):
        self.GetAndClear()
        text=""
        for line in histo:
            text=text+line+"\n"
        self.textbox.insert("1.0",text)
    def AddBook(self):
        self.ClearOutput()
        self.GetInput()
        book=self.entrytext.split(", ")
        if len(book)==5 and book[3].isdigit() and book[4].isdigit():
            b=Book(book[0],book[1],book[2],book[3],book[4])
            if b not in Mylib.books:
                Mylib.books.append(b)
                messagebox.showinfo(title="Notice",message="Book add to library")
            else:
                messagebox.showerror(title="Error",message="Book was in Library!\n")
        else:
            messagebox.showinfo(title="Notice",message="Enter Book infomation in fomrat (title, author, isbs number, quantity,checkoutbook) to the entry")
    def RemoveBook(self):
        self.GetAndClear()
        check=1
        for book in Mylib.books:
            if book.title.lower()==self.entrytext.lower():
                check=0
                messagebox.showinfo(title="Removed book",message= f"Removed {self.entrytext.title()}\n")
                Mylib.remove_book(book)
        if check==1:
            messagebox.showinfo(title="Removed book",message= f"Can't find the book\n")
    def Quit(self):
            
        with open('books.txt', 'w') as file:
            for book in Mylib.books:
                file.write(f"{book.title}, {book.author}, {book.ibsn}, {book.quantity}, {book.checkoutbook}\n") #ghi lại dữ liệu hiện tại của Mylib
        with open("checkout_history.txt","a",encoding="utf-8") as f:
            for i in history:
                f.write(i+"\n") #ghi tiếp lịch sử mượn trả phiên làm việc
        self.win.quit()

screen=LibraryControl(Mylib.books)
