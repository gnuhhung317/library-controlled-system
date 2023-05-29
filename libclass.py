import hashlib

import time

def nice(book_name):
        return " ".join(book_name.split())
def get_sha256_hash(data):
    hash_object = hashlib.sha256(data.encode())
    return hash_object.hexdigest()
class Book:
    def __init__(self,title,author,ibsn,quantity,checkoutbook):
        self.title =title
        self.author = author
        self.ibsn = ibsn
        self.quantity=int(quantity) #số lượng sách
        self.checkoutbook=int(checkoutbook) #số lượng sách đã bị mượn
    def infor(self):
        return f"Tựa đề sách là {self.title} của {self.author} với số ibs là {self.ibsn}\n"
    def is_available(self):
        if self.quantity-self.checkoutbook>0: #kiểm tra số sách hiện tại
            return f"{self.title} có sẵn {self.quantity-self.checkoutbook}!\n"
        else:
            return f"{self.title} không có sẵn!\n"
    def check_out(self,history,username,book):
        if int(self.quantity)-self.checkoutbook>0:
            self.checkoutbook+=1 #tăng số sách self bị mượn thêm 1
            history.append(f"{time.ctime(time.time())} {username} đã mượn {book.title}") #lưu lịch sử mượn vào list để thêm vào lưu vào csdl sau phiên làm việc
            return f"{self.title} của bạn đây!\nLịch sử mượn trả sẽ được cập nhật sau phiên làm việc"
        else:
            return f"{self.title} đã bị mượn hết!\n"
    def return_book(self,history,username,book):
        if self.checkoutbook>0:
            history.append(f"{time.ctime(time.time())} {username} đã trả {book.title}") #lưu lịch sử mượn vào list để thêm vào lưu vào csdl sau phiên làm việc
            self.checkoutbook-=1 #giảm số sách self bị giảm thêm 1#
            return f"{self.title} đã được trả!\nlịch sử mượn trả sẽ được cập nhật sau phiên làm việc\n"   
        else:
            return f"{self.title} chưa được mượn cuốn nào cả!\n"
class Library:
    def __init__(self):
        self.books=[]
        self.admin=False
    def login(self,username,password,user_data,admin_data):
        if username in user_data and user_data[username]==get_sha256_hash(password): #kiểm tra mật khẩu sau khi hash có giống trong từ điển dữ liệu người dúng không
            return True
        elif username in admin_data and admin_data[username]==get_sha256_hash(password):
            self.admin=True
            return True
        return False
    
    def add_book(self,book):
        self.books.append(book)

    def remove_book(self,book):
        self.books.remove(book)
        return f"Đã xóa sách {book.title}"
    def search_book_by_title(self,keyword=str):
        matched_book = [book for book in self.books if keyword.lower() in book.title.lower()]
        if not matched_book:
            return "can't find the book"
        else:
            find="Tìm được:\n"
            i=1
            for book in matched_book:
                find+=f"\n{i}. {book.title} của {book.author} với số ibs là {book.ibsn}: {int(book.quantity)-book.checkoutbook} quyển\n"
                i+=1
        return find
    
    def search_book_by_author(self,keyword=str):
        matched_book = [book for book in self.books if keyword.lower() in book.author.lower()]
        if len(matched_book)==0:
            return "Can't find the author"
        else:
            find="Tìm được:\n"
            i=1
            for book in matched_book:
                find+=f"\n{i}. {book.title} của {book.author} với số ibs là {book.ibsn}: {int(book.quantity)-book.checkoutbook} quyển\n"
                i+=1
        return find
    
    def display_book(self):
        i=1
        display=""
        for book in self.books:
            display+=f"{i}. {book.title} của {book.author}: {book.quantity} quyển\n"
            i+=1
        return display
    
    def display_available_book(self):
        available_book=[book for book in self.books if book.quantity-book.checkoutbook>0] #tạo danh sách sách có số quyển sách hiện có lớn hơn 0
        if len(available_book)==0:
            return "Không có sách nào có sẵn!"
        else:
            show=""
            i=1
            for book in available_book:
                show+=f"{i}. {book.title} của {book.author}: {book.quantity} quyển\n"
                i += 1
            return show
Mylib=Library()
#tạo một từ điển chứa tài khoản và mật khẩu (sau khi đã hash) của người dùng từ file user.txt
with open("user.txt","r") as f:
    data=f.read()
data=data.split("\n")
for i in range(len(data)):
    data[i]=data[i].split(", ")
user_data={username: password for [username,password] in data }
#tạo một từ điển chứa tài khoản và mật khẩu(sau khi đã hash của người dùng từ file admin.txt
with open("admin.txt","r") as f:
    data=f.read()
    data=data.split("\n")
    for i in range(len(data)):
        data[i]=data[i].split(", ")
    admin_data={admin: password for [admin,password] in data }
#mở lịch sử đến phiên làm việc lần trước
f=open("checkout_history.txt",'r',encoding="utf-8")
histo=f.read()
histo=histo.split("\n")
# tạo danh sách rỗng lưu lại lịch sử mượn trả từng tiến trình để ghi vào checkout_history
history=[]
with open('books.txt','r',encoding="utf-8") as file:
    file=file.read()
    file=file.split("\n")
    for i in range(len(file)):
        file[i]=file[i].split(", ")
    for row in file:
        if len(row) == 5:
            book = Book(row[0].strip(), row[1].strip(), row[2].strip(), row[3].strip(),row[4].strip())
            Mylib.add_book(book)
        elif len(row)>5:    #chia 2 trường hợp vì tiêu đề sách có thể chứa dấu phẩy
            for i in range(1,len(row)-5):
                row[0]= row[0]+row[i]
            book = Book(row[0].strip(),row[-4].strip(),row[-3].strip(), row[-2].strip(),row[-1].strip())
            Mylib.add_book(book)
    
    
    