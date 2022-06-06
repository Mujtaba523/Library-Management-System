from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import datetime

#List Of Books
ListBooks = ["I Feel Bad About My Neck", "Broken Glass", "Harry Potter and the Goblet of Fire", "A Little Life", "Chronicles: Volume One", "The Tipping Point",
"Darkmans", "Light", "Visitation", "Noughts & Crosses", "The God Delusion", "The Cost of Living", "Tell Me How It Ends", "Ideas And Opinions",
"The Structure of Scientific Revolutions", "A Brief History of Time", "What is Life?", "Coming of Age in the Milky Way", "ABC of Relativity"]

#Merge Sort Implementation for sorting books
class MergeSort(object):
    def __init__(self, array):
        self.array = array
    def merge_sort(self):
        if len(self.array) > 1:
            m = len(self.array)//2
            left = self.array[:m]
            right = self.array[m:]
            leftsorter = MergeSort(left)
            leftsorter.merge_sort()
            rightsorter = MergeSort(right)
            rightsorter.merge_sort()
            i = 0
            j = 0
            k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    self.array[k] = left[i]
                    i += 1
                else:
                    self.array[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                self.array[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                self.array[k] = right[j]
                j += 1
                k += 1
        return self.array

#Main class of Library Management
class LibraryManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("1550x800+0+0")
        #----------------------------------Variables-----------------------------------------
        self.Member=StringVar()
        self.ID=StringVar()
        self.Name=StringVar()
        self.Address=StringVar()
        self.Book_ID=StringVar()
        self.Book_Title=StringVar()
        self.Author=StringVar()
        self.Date_Borrowed=StringVar()
        self.Due_Date=StringVar()
        self.Reserve=StringVar()

        #--------------------------------Title----------------------------------------------
        Title = Label(root, text="Library Database Management System", font=("Poppins", 35, "italic"),
              bg="black", fg="white", bd=12, relief=RIDGE)
        Title.pack(side=TOP, fill=X)
        frame = Frame(self.root, bd=12, relief=RIDGE,padx=0,bg="light blue")
        frame.place(x=0, y=110, width=1550, height=400)

        #---------------------------------Data Frame Left-------------------------------------
        DataFrameLeft=LabelFrame(frame,text="Library Member Information", font=("Times New Roman", 20, "bold"),
              bg="light blue", fg="blue", bd=8 )
        DataFrameLeft.place(x=10, y=5, width = 900, height = 350)
        Label_of_Member = Label(DataFrameLeft, text="Member Type", font=("times new roman", 16, "bold"), bg="light blue",
                      fg="dark blue")
        Label_of_Member.grid(row=0, column=0, sticky=W)
        comMember = ttk.Combobox(DataFrameLeft, font=("times new roman", 12, "bold"), state="readonly", textvariable=self.Member, width=25)
        comMember["value"] = ("Admin Staff", "Student", "Lecturer")
        comMember.grid(row=0, column=1, pady=12)

        Label_of_ID = Label(DataFrameLeft, text="ID Number", font=("times new roman", 16, "bold"), bg="light blue",
                      fg="dark blue", padx=2, pady=12)
        Label_of_ID.grid(row=1, column=0, sticky=W)
        self.entry_of_ID = Entry(DataFrameLeft, font=("times new roman", 12, "bold"), bg="white", fg="black", textvariable=self.ID, relief=GROOVE, width=25)
        self.entry_of_ID.grid(row=1, column=1)

        Label_of_Name = Label(DataFrameLeft, text="Name",  font=("times new roman", 16, "bold"), bg="light blue",
                      fg="dark blue", padx=2, pady=12)
        Label_of_Name.grid(row=2, column=0, sticky=W)
        self.entry_of_Name = Entry(DataFrameLeft, font=("times new roman", 12, "bold"),textvariable=self.Name,bg="white", fg="black", relief=GROOVE, width=25)
        self.entry_of_Name.grid(row=2, column=1)

        Label_of_Address = Label(DataFrameLeft, text="Address", font=("times new roman", 16, "bold"), bg="light blue",
                      fg="dark blue", padx=2, pady=12)
        Label_of_Address.grid(row=3, column=0, sticky=W)
        self.entry_of_Address = Entry(DataFrameLeft, font=("times new roman", 12, "bold"), bg="white", textvariable=self.Address, fg="black", relief=GROOVE, width=25)
        self.entry_of_Address.grid(row=3, column=1)

        Label_of_Book_ID = Label(DataFrameLeft, text="Book ID", font=("times new roman", 16, "bold"), bg="light blue",
                      fg="dark blue", padx=2, pady=12)
        Label_of_Book_ID.grid(row=4, column=0, sticky=W)
        self.entry_of_Book_ID = Entry(DataFrameLeft, font=("times new roman", 12, "bold"), bg="white", fg="black", textvariable=self.Book_ID, relief=GROOVE, width=25)
        self.entry_of_Book_ID.grid(row=4, column=1)

        Label_of_Book_Title = Label(DataFrameLeft, text="Book Title", font=("times new roman", 16, "bold"), bg="light blue",
                      fg="dark blue", padx=2, pady=12)
        Label_of_Book_Title.grid(row=0, column=3, sticky=W, padx=15)
        self.entry_of_Book_Title = Entry(DataFrameLeft, font=("times new roman", 12, "bold"), bg="white", fg="black", textvariable=self.Book_Title, relief=GROOVE, width=25)
        self.entry_of_Book_Title.grid(row=0, column=4)

        Label_of_Author = Label(DataFrameLeft, text="Author", font=("times new roman", 16, "bold"), bg="light blue",
                      fg="dark blue", padx=2, pady=12)
        Label_of_Author.grid(row=1, column=3, sticky=W,padx=15)
        self.entry_of_Author = Entry(DataFrameLeft, font=("times new roman", 12, "bold"), bg="white", fg="black", relief=GROOVE, textvariable=self.Author, width=25)
        self.entry_of_Author.grid(row=1, column=4)

        Label_of_Date_Borrowed = Label(DataFrameLeft, text="Date Borrowed", font=("times new roman", 16, "bold"), bg="light blue",
                      fg="dark blue", padx=2, pady=12)
        Label_of_Date_Borrowed.grid(row=2, column=3, sticky=W,padx=15)
        self.entry_of_Date_Borrowed = Entry(DataFrameLeft, font=("times new roman", 12, "bold"), bg="white", fg="black", textvariable=self.Date_Borrowed, relief=GROOVE, width=25)
        self.entry_of_Date_Borrowed.grid(row=2, column=4)

        Label_of_Date_Due = Label(DataFrameLeft, text="Due Date", font=("times new roman", 16, "bold"), bg="light blue",
                      fg="dark blue", padx=2, pady=12)
        Label_of_Date_Due.grid(row=3, column=3, sticky=W, padx=15)
        self.entry_of_Date_Due= Entry(DataFrameLeft, font=("times new roman", 12, "bold"), bg="white", fg="black", textvariable=self.Due_Date, relief=GROOVE, width=25)
        self.entry_of_Date_Due.grid(row=3, column=4)

        Label_of_Reserve_Book= Label(DataFrameLeft, text="Reserve Non-Available Book", font=("times new roman", 16, "bold"), bg="light blue",
                      fg="dark blue", padx=2, pady=12)
        Label_of_Reserve_Book.grid(row=4, column=3, sticky=W, padx=15)
        self.entry_of_Reserve_Book= Entry(DataFrameLeft, font=("times new roman", 12, "bold"), bg="white", fg="black", textvariable=self.Reserve, relief=GROOVE, width=25)
        self.entry_of_Reserve_Book.grid(row=4, column=4)

        #---------------------------------Data Frame Right-------------------------------------
        DataFrameRight=LabelFrame(frame,text="Book Details", font=("Times New Roman", 20, "bold"),
              bg="light blue", fg="blue", bd=8 )
        DataFrameRight.place(x=920, y=5, width =300, height = 350)

        listScrollbar = Scrollbar(DataFrameRight)
        listScrollbar.grid(row=0, column=1, sticky="ns")

        def select_book(event=""):
            value = str(self.listBox.get(self.listBox.curselection()))
            x = value
            if x == "I Feel Bad About My Neck":
                self.Book_ID.set("HS-444")
                self.Book_Title.set("I Feel Bad About My Neck")
                self.Author.set("Nora Ephron")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.Date_Borrowed.set(d1)
                self.Due_Date.set(d3)
            elif x == "Broken Glass":
                self.Book_ID.set("HS-443")
                self.Book_Title.set("Broken Glass")
                self.Author.set("Alain Mabanckou")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.Date_Borrowed.set(d1)
                self.Due_Date.set(d3)
            elif x == "Harry Potter and the Goblet of Fire":
                self.Book_ID.set("HS-442")
                self.Book_Title.set("Harry Potter and the Goblet of Fire")
                self.Author.set("J.K. Rowling")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.Date_Borrowed.set(d1)
                self.Due_Date.set(d3)
            elif x == "A Little Life":
                self.Book_ID.set("HS-418")
                self.Book_Title.set("A Little Life")
                self.Author.set("Hanya Yanagihara")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.Date_Borrowed.set(d1)
                self.Due_Date.set(d3)
            elif x == "Chronicles: Volume One":
                self.Book_ID.set("HS-423")
                self.Book_Title.set("Chronicles: Volume One")
                self.Author.set("Bob Dylan")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.Date_Borrowed.set(d1)
                self.Due_Date.set(d3)
            elif x == "The Tipping Point":
                self.Book_ID.set("HS-490")
                self.Book_Title.set("The Tipping Point")
                self.Author.set("Malcolm Gladwell")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.Date_Borrowed.set(d1)
                self.Due_Date.set(d3)
            elif x == "Darkmans":
                self.Book_ID.set("HS-450")
                self.Book_Title.set("Darkmans")
                self.Author.set("Nicola Barker")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.Date_Borrowed.set(d1)
                self.Due_Date.set(d3)
            elif x == "Light":
                self.Book_ID.set("HS-433")
                self.Book_Title.set("Light")
                self.Author.set("Alex Light")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.Date_Borrowed.set(d1)
                self.Due_Date.set(d3)
            elif x == "Visitation":
                self.Book_ID.set("HS-445")
                self.Book_Title.set("Visitation")
                self.Author.set("Don Cushman")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.Date_Borrowed.set(d1)
                self.Due_Date.set(d3)
            elif x == "Noughts & Crosses":
                self.Book_ID.set("HS-446")
                self.Book_Title.set("Noughts & Crosses")
                self.Author.set("Malorie Blackman")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.Date_Borrowed.set(d1)
                self.Due_Date.set(d3)
            elif x == "The God Delusion":
                self.Book_ID.set("HS-201")
                self.Book_Title.set("The God Delusion")
                self.Author.set("Richard Dawkins")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.Date_Borrowed.set(d1)
                self.Due_Date.set(d3)
            elif x == "The Cost of Living":
                self.Book_ID.set("HS-120")
                self.Book_Title.set("The Cost of Living")
                self.Author.set("Deborah Levy")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.Date_Borrowed.set(d1)
                self.Due_Date.set(d3)
            elif x == "Tell Me How It Ends":
                self.Book_ID.set("HS-342")
                self.Book_Title.set("Tell Me How It Ends")
                self.Author.set("Valeria Luiselli")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.Date_Borrowed.set(d1)
                self.Due_Date.set(d3)
            elif x == "Ideas And Opinions":
                self.Book_ID.set("HS-653")
                self.Book_Title.set("Ideas And Opinions")
                self.Author.set("Albert Einstein")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.Date_Borrowed.set(d1)
                self.Due_Date.set(d3)
            elif x == "The Structure of Scientific Revolutions":
                self.Book_ID.set("HS-476")
                self.Book_Title.set("The Structure of Scientific Revolutions")
                self.Author.set("Thomas Kuhn")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.Date_Borrowed.set(d1)
                self.Due_Date.set(d3)
            elif x == "A Brief History of Time":
                self.Book_ID.set("HS-867")
                self.Book_Title.set("A Brief History of Time")
                self.Author.set("Stephen Hawking")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.Date_Borrowed.set(d1)
                self.Due_Date.set(d3)
            elif x == "Broken Glass":
                self.Book_ID.set("HS-443")
                self.Book_Title.set("Broken Glass")
                self.Author.set("Alain Mabanckou")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.Date_Borrowed.set(d1)
                self.Due_Date.set(d3)
            elif x == "What is Life?":
                self.Book_ID.set("HS-768")
                self.Book_Title.set("What is Life?")
                self.Author.set("Erwin Schrödinger")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.Date_Borrowed.set(d1)
                self.Due_Date.set(d3)
            elif x == "Coming of Age in the Milky Way":
                self.Book_ID.set("HS-863")
                self.Book_Title.set("Coming of Age in the Milky Way")
                self.Author.set("Timothy Ferris")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.Date_Borrowed.set(d1)
                self.Due_Date.set(d3)
            elif x == "ABC of Relativity":
                self.Book_ID.set("HS-756")
                self.Book_Title.set("ABC of Relativity")
                self.Author.set("Bertrand Russell")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.Date_Borrowed.set(d1)
                self.Due_Date.set(d3)
            else:
                self.Book_ID.set("")
                self.Book_Title.set("")
                self.Author.set("")

                d1 = datetime.datetime.today()
                d2 = datetime.timedelta(days = 15)
                d3 = d1+d2
                self.Date_Borrowed.set(d1)
                self.Due_Date.set(d3)
                

        self.listBox = Listbox(DataFrameRight, font=("poppins", 12, "normal"), width = 25, height = 10)
        self.listBox.grid(row=0, column=0, padx=4)
        self.listBox.bind("<<ListboxSelect>>", select_book)
        listScrollbar.config(command=self.listBox.yview)
        for item in ListBooks:
            self.listBox.insert(END, item)

         #---------------------------------Data Frame Last-------------------------------------
        DataFrameLast=LabelFrame(frame,text="Operations", font=("Times New Roman", 20, "bold"),
              bg="light blue", fg="blue", bd=8 )
        DataFrameLast.place(x=1230, y=5, width =280, height = 350)
    
        Label_of_New_Book = Label(DataFrameLast, text="Book Name", font=("times new roman", 16, "bold"), bg="light blue",
                      fg="dark blue", padx=2, pady=12)
        Label_of_New_Book.grid(row=0, column=1, sticky=W, padx=8)
        self.entry_of_New_Book= Entry(DataFrameLast, font=("times new roman", 12, "bold"), bg="white", fg="black", relief=GROOVE, width=15)
        self.entry_of_New_Book.grid(row=0, column=2)
        #----------------------------------Button Frame for Books operation-------------------
        ButtonFrameBooks=LabelFrame(DataFrameLast, bg="light blue", fg="blue", bd=5)
        ButtonFrameBooks.place(x=5, y=50, width =250, height = 250)

        Add_Books = Button(ButtonFrameBooks, text = "Add Book",font=("poppins", 8, "normal"), width=18, bg="blue", fg="white", command=self.add_books).grid(row=2, padx=50,column=3, pady=10)
        Delete_Books = Button(ButtonFrameBooks, text = "Delete Book",font=("poppins", 8, "normal"), width=18, bg="blue", fg="white", command=self.delete_books).grid(row=3, padx=50,column=3, pady=10)
        Sort_Books = Button(ButtonFrameBooks, text = "Sort Book",font=("poppins", 8, "normal"), width=18, bg="blue", fg="white", command=self.sort_books).grid(row=4, padx=50,column=3, pady=10)
        Search_Books = Button(ButtonFrameBooks, text = "Search Book",font=("poppins", 8, "normal"), width=18, bg="blue", fg="white", command=self.search_books).grid(row=5, padx=50,column=3, pady=10)

        #---------------------------------Button Frame for Member operation-------------------
        ButtonFrame=LabelFrame(self.root, bg="light blue", fg="blue", bd=8 )
        ButtonFrame.place(x=0, y=530, width =1550, height = 70)

        button_of_add = Button(ButtonFrame, text = "Add Data",font=("poppins", 8, "normal"), width=25, bg="blue", fg="white", command=self.add_data).grid(row=0, padx=50,column=0, pady=10)
        Button_of_delete = Button(ButtonFrame, text = "Delete Data",font=("poppins", 8, "normal"), width=25, bg="blue", fg="white", command=self.delete_data).grid(row=0, padx=50,column=1, pady=10)
        Button_of_reset = Button(ButtonFrame, text = "Reset Data",font=("poppins", 8, "normal"), width=25, bg="blue", fg="white", command=self.clear_data).grid(row=0, padx=50,column=2, pady=10)
        Button_of_quit = Button(ButtonFrame, text = "Exit",font=("poppins", 8, "normal"), command=self.root.destroy, width=25, bg="blue", fg="white").grid(row=0, padx=50,column=4, pady=10)
        Button_of_show = Button(ButtonFrame, text = "Show Data",font=("poppins", 8, "normal"), command=self.fetch_data, width=25, bg="blue", fg="white").grid(row=0, padx=50,column=3, pady=10)
        #---------------------------------Information Frames-----------------------------------
        FrameDetails=LabelFrame(self.root, bg="light blue", fg="blue", bd=8 )
        FrameDetails.place(x=0, y=600, width =1550, height = 200)
        xscroll= ttk.Scrollbar(FrameDetails,orient=HORIZONTAL)
        yscroll= ttk.Scrollbar(FrameDetails,orient=VERTICAL)
        self.library_table=ttk.Treeview(FrameDetails, column=("Member Type", "ID Number", 
        "Name", "Address", "Book ID", "Book Title", "Author", 
        "Date Borrowed", "Due Date", "Reserve Non-Available Book"), xscrollcommand=xscroll.set, yscrollcommand=yscroll.set)
        xscroll.pack(side=BOTTOM, fill=X)
        yscroll.pack(side=RIGHT, fill=Y)
        xscroll.config(command=self.library_table.xview)
        yscroll.config(command=self.library_table.yview)
        columns = ["Member Type", "ID Number", 
        "Name", "Address", "Book ID", "Book Title", "Author", 
        "Date Borrowed", "Due Date", "Reserve Non-Available Book"]
        for i in columns:
            self.library_table.heading(i, text=i)
        self.library_table["show"]="headings"
        self.library_table.pack(fill=BOTH, expand=1)

        #-------------------------------Functionalities Behind All Buttons---------------------
    def add_books(self):
        new_book = self.entry_of_New_Book.get()
        ListBooks.append(new_book)
        for item in ListBooks:
            self.listBox.insert(END, item)
    
    def delete_books(self):
        self.listBox.delete(ANCHOR)
    
    def sort_books(self):
        sort = MergeSort(ListBooks)
        x = sort.merge_sort()
        self.listBox.delete(0,END)
        for item in x:
            self.listBox.insert(END, item)

    def search_books(self):
        new_book = self.entry_of_New_Book.get()
        for i in ListBooks:
            if str(i) == new_book:
                messagebox.showinfo("SEARCH SUCCESFULL", "GIVEN BOOK IS PRESENT!!!")
        if new_book not in ListBooks:
            messagebox.showinfo("SEARCH UNSUCCESFULL", "GIVEN BOOK IS NOT PRESENT!!!")
    
    def add_data(self):
        conn = sqlite3.connect("Data.db")
        my_cursor=conn.cursor()
        my_cursor.execute("INSERT INTO AllData(Member, ID_No, Name, Address, Book_ID, Book_Title, Author, Date_Borrowed, Due_Date, Reserved) VALUES(?,?,?,?,?,?,?,?,?,?)", (self.Member.get(),
        self.ID.get(),
        self.Name.get(),
        self.Address.get(),
        self.Book_ID.get(),
        self.Book_Title.get(),
        self.Author.get(),
        self.Date_Borrowed.get(),
        self.Due_Date.get(),
        self.Reserve.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("SUCCESFULL", "DATA HAS BEEN SUCCESSFULLY SAVED")
        
    def delete_data(self):
        self.library_table.delete(*self.library_table.get_children())
        conn = sqlite3.connect("Data.db")
        my_cursor=conn.cursor()
        x = str(self.ID.get())
        my_cursor.execute("DELETE from AllData")
        conn.commit()
        conn.close()

    def fetch_data(self):
        conn = sqlite3.connect("Data.db")
        my_cursor=conn.cursor()
        my_cursor.execute("SELECT * FROM AllData")
        rows = my_cursor.fetchall()

        if len(rows)!=0:
            self.library_table.delete(*self.library_table.get_children())
            for i in rows:
                self.library_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def clear_data(self):
        self.entry_of_ID.delete(0,END)
        self.entry_of_Name.delete(0,END)
        self.entry_of_Address.delete(0,END)
        self.entry_of_Book_ID.delete(0,END)
        self.entry_of_Book_Title.delete(0,END)
        self.entry_of_Date_Borrowed.delete(0,END)
        self.entry_of_Date_Due.delete(0,END)
        self.entry_of_Author.delete(0,END)
        self.entry_of_Reserve_Book.delete(0,END)

if __name__=="__main__":
    root = Tk()
    obj = LibraryManagementSystem(root)
    root.mainloop()
