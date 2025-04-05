from cProfile import label
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Treeview, Style
import sqlite3
import webbrowser

# ContactUs page----------------------------
def Contact():
#design---------------------------------
    contact=Toplevel()
    contact.title('home page')
    screen_height=contact.winfo_screenheight()
    screen_width=contact.winfo_screenwidth()
    w=screen_width
    h=screen_height
    contact.geometry(f"{w}x{h}")
    bg_img=PhotoImage(file='readers.png')
    bg_lbl=Label(contact,image=bg_img,width=w-10,height=h)
    bg_lbl.place(anchor="center",relx=0.5,rely=0.5)
#---------------------------------
    def open_link01():
        webbrowser.open("https://github.com/David-Emil")
    def open_link02():
        webbrowser.open("")
#main labels------------------------------------
    con_img=PhotoImage(file='communication.png')
    con_lbl=Label(contact,text='for Contact',font=('bold',30),bg='white',image=con_img,compound='left')
    con_lbl.place(relx=0.4,rely=0)


    GH_img=PhotoImage(file='GitHup.png')
    GH_btn=Button(contact,text='GitHup',image=GH_img,compound='left',command=open_link01,cursor='hand2',height=35,width=200,font=('bold',25),bg='blue')
    GH_btn.place(relx=0.20,rely=0.3)
    
    Li_img=PhotoImage(file='LinkedIn.png')
    Li_btn=Button(contact,text='LinkedIn',image=Li_img,compound='left',command=open_link02,cursor='hand2',height=35,width=200,font=('bold',25),bg='blue')
    Li_btn.place(relx=0.40,rely=0.3)

    def back():
        contact.destroy()

    back_img=PhotoImage(file='back.png')
    back_btn=Button(contact,image=back_img,compound='left',width=100,height=30,font=('arial',20),command=back,bg='orange',cursor='hand2')
    back_btn.place(anchor='center',relx=0.03,rely=0.015)

    contact.mainloop()

# about page----------------------------
def about():
    # design---------------------------------
    about = Toplevel()
    about.title("About page")
    screen_height = about.winfo_screenheight()
    screen_width = about.winfo_screenwidth()
    w = screen_width
    h = screen_height
    about.geometry(f"{w}x{h}")
    bg_img = PhotoImage(file="readers.png")
    bg_lbl = Label(about, image=bg_img, width=w - 10, height=h)
    bg_lbl.place(anchor="center", relx=0.5, rely=0.5)
    # ---------------------------------

    # main labels------------------------------------
    about_lbl = Label(about, text="About Us Page", font=("bold", 30), bg="white")
    about_lbl.place(relx=0.4, rely=0)
    ans_lbl = Label(about, font=("bold", 20), bg="white", text="Welcome to ""Dav BookStore"", a haven for book lovers of all kinds.\nWhether you’re searching for the latest bestsellers, timeless classics, or hidden gems,\nwe’ve curated a diverse collection to inspire and delight readers of all ages.\nOur mission is to foster a community of passionate readers by offering a wide range of\n[genres, personalized recommendations, and a cozy] environment where you can explore the world of books.\nAt ""Dav Bookstore"", we believe in the power of stories to connect us, and we’re here to help you find your next great read.\nVisit us today and discover the joy of reading!")
    ans_lbl.place(anchor="center",relx=0.50, rely=0.35)
    ans2_lbl = Label(
        about,
        font=("areal", 20),
        bg="black",
        fg="white",
        text='Our Library System Makes It Easy To You To Lend a Book OR Restore It.\n See How Much Books You Lended .\n Add New Book To The Library , Delete Or Edit\n a Book And It Helps You To See The Readers\n "your customers"',
    )
    ans2_lbl.place(anchor="center", relx=0.500, rely=0.75)

    def back():
        about.destroy()

    back_img = PhotoImage(file="back.png")
    back_btn = Button(
        about,
        image=back_img,
        compound="left",
        width=100,
        height=30,
        font=("arial", 20),
        command=back,
        bg="orange",
        cursor="hand2",
    )
    back_btn.place(anchor="center", relx=0.03, rely=0.015)

    about.mainloop()

# books page--------------------
def books():
    # page design -----------------------------------------------------
    books = Toplevel()

    books.title("Books Page")
    screen_height = books.winfo_screenheight()
    screen_width = books.winfo_screenwidth()
    w = screen_width
    h = screen_height

    books.geometry(f"{w-10}x{h}")

    bg_img = PhotoImage(file="readers.png")
    bg_lbl = Label(books, image=bg_img, width=w - 10, height=h)
    bg_lbl.place(anchor="center", relx=0.5, rely=0.5)

    # coonection---------------
    con = sqlite3.connect("library.db")
    cur = con.cursor()
    cur.execute('select * from books order by "book name" ')
    books_list = cur.fetchall()
    con.close()

    # treeview--------------------------------------------------------------------

    columns = ["id", "book name", "book amount", "book rate", "book type"]

    btree = Treeview(books, columns=columns, show="headings", selectmode="none")
    btree.column("id", anchor="center", width=80)
    btree.column("book name", anchor="center")
    btree.column("book amount", anchor="center")
    btree.column("book rate", anchor="center")
    btree.column("book type", anchor="center")

    btree.heading("id", text="Id")
    btree.heading("book name", text="Book Name")
    btree.heading("book amount", text="Book Amount")
    btree.heading("book rate", text="Book rate")
    btree.heading("book type", text="Book type")

    for book in books_list:
        btree.insert("", "end", iid=book[0], values=book)

    # treeview-----------------------------------------------------

    # scrollbar-------------------------------------------------------------
    bscrollbar = Scrollbar(books, orient="vertical", command=btree.yview)
    btree.configure(yscrollcommand=bscrollbar.set)

    # style-----------
    style = Style()
    style.configure(
        "Treeview",
        font=("arial", 15),
        rowheight=30,
        foreground="black",
        background="white",
    )
    # ------------------
    reader_lbl = Label(
        books, font=("arial", 20), bg="white", text="this is the books we have : "
    )
    # _________-------------------------

    # getuser-------------------------------
    def get_book():
        get = Toplevel()
        get.title("addition page")

        # form  design-----
        w = 500
        h = 500
        screen_height = get.winfo_screenheight()
        screen_width = get.winfo_screenwidth()
        x = int((screen_height - h) / 2)
        y = int((screen_width - w) / 2)

        a = "black"
        b = "#808080"
        get.geometry(f"{w}x{h}+{y}+{x}")
        get.resizable(False, False)

        get.config(background="white")

        add_lbl = Label(
            get, text="Addition form", width=20, font=("bold", 25), bg=b, fg=a
        )
        add_lbl.place(x=50, y=53)

        name_txt = Entry(get, width=20, fg=a, bg=b)
        name_txt_lbl = Label(
            get, text="enter the book name :", width=20, font=("bold", 10), fg=a, bg=b
        )

        books_txt = Entry(get, width=20, fg=a, bg=b)
        books_txt_lbl = Label(
            get,
            text="enter the books number :",
            width=20,
            font=("bold", 10),
            fg=a,
            bg=b,
        )

        books_rate_txt = Entry(get, width=20, fg=a, bg=b)
        books_rate_txt_lbl = Label(
            get, text="enter the book rate :", width=20, font=("bold", 10), fg=a, bg=b
        )

        books_type_txt = Entry(get, width=20, fg=a, bg=b)
        books_type_txt_lbl = Label(
            get, text="enter the book type :", width=20, font=("bold", 10), fg=a, bg=b
        )

        name_txt_lbl.place(x=70, y=130)
        name_txt.place(x=240, y=130)

        books_txt_lbl.place(x=70, y=180)
        books_txt.place(x=240, y=180)

        books_rate_txt_lbl.place(x=70, y=230)
        books_rate_txt.place(x=240, y=230)

        books_type_txt_lbl.place(x=70, y=280)
        books_type_txt.place(x=240, y=280)

        def add():
            name = name_txt.get()
            books = books_txt.get()
            rate = books_rate_txt.get()
            type = books_type_txt.get()

            con = sqlite3.connect("library.db")
            cur = con.cursor()
            cur.execute(
                'INSERT into "books"("book name" , "book amount" ,"book rate","book type")values(?,?,?,?)',
                [name, books, rate, type],
            )
            con.commit()
            con.close()
            messagebox.showinfo("info", "addition complete")
            get.destroy()

        add_btn = Button(
            get,
            text="Add",
            height=2,
            fg="black",
            bg="white",
            width=20,
            font=("bold", 10),
            command=add,
            cursor="hand2",
        )
        add_btn.place(x=200, y=330)
        get.mainloop()

    # ---------------------------------------------

    # delete user------------------------------------------
    def dele():
        dele = Toplevel()
        dele.title("delete page")

        # form  design-----
        w = 500
        h = 500
        screen_height = dele.winfo_screenheight()
        screen_width = dele.winfo_screenwidth()
        x = int((screen_height - h) / 2)
        y = int((screen_width - w) / 2)

        a = "black"
        b = "#808080"
        dele.geometry(f"{w}x{h}+{y}+{x}")
        dele.resizable(False, False)

        dele.config(background="white")
        dele_lbl = Label(
            dele, text="Deletion form", width=20, font=("bold", 25), bg=b, fg=a
        )
        dele_lbl.place(x=50, y=53)

        name_txt = Entry(dele, width=20, fg=a, bg=b)
        name_txt_lbl = Label(
            dele, text="enter the name :", font=("arial", 10), width=20, fg=a, bg=b
        )
        name_txt_lbl.place(anchor="center", relx=0.245, rely=0.5)
        name_txt.place(anchor="center", relx=0.55, rely=0.5, height=30)

        def delete():
            name = name_txt.get()
            x = messagebox.askyesno("info", "are you sure you want to delete " + name)
            if x:

                con = sqlite3.connect("library.db")
                cur = con.cursor()
                cur.execute('DELETE from books where "book name" like ?', [name])
                con.commit()
                con.close()
                messagebox.showinfo("info", "deletion complete")
                dele.destroy()

        dele_btn = Button(
            dele,
            text="Delete",
            width=30,
            height=2,
            fg="black",
            bg="white",
            font=("arial", 15),
            command=delete,
            cursor="hand2",
        )
        dele_btn.place(relx=0.2, rely=0.6)

    # -----------------------------------------------------------

    # edit info--------------------------------------
    def edit():

        edit = Toplevel()
        edit.title("edit page")

        # form  design-----
        w = 500
        h = 500
        screen_height = edit.winfo_screenheight()
        screen_width = edit.winfo_screenwidth()
        x = int((screen_height - h) / 2)
        y = int((screen_width - w) / 2)

        a = "black"
        b = "#808080"
        edit.geometry(f"{w}x{h}+{y}+{x}")
        edit.resizable(False, False)

        edit.config(background="white")

        edit_lbl = Label(
            edit, text="Edit form", width=20, font=("bold", 25), bg=b, fg=a
        )
        edit_lbl.place(x=50, y=53)

        name_txt = Entry(edit, width=20, fg=a, bg=b)
        name_txt_lbl = Label(
            edit, text="enter the book name :", width=20, font=("bold", 10), fg=a, bg=b
        )
        name_txt_lbl.place(anchor="center", relx=0.245, rely=0.45)
        name_txt.place(anchor="center", relx=0.6, rely=0.45, height=30)

        books_txt = Entry(edit, width=20, fg=a, bg=b)
        books_txt_lbl = Label(
            edit,
            text="enter the new books number :",
            width=22,
            font=("bold", 10),
            fg=a,
            bg=b,
        )
        books_txt_lbl.place(anchor="center", relx=0.245, rely=0.55)
        books_txt.place(anchor="center", relx=0.6, rely=0.55, height=30)

        def edi():
            x = messagebox.askyesno("info", "are you sure you want to edit")
            if x:
                name = name_txt.get()
                books = int(books_txt.get())

                con = sqlite3.connect("library.db")
                cur = con.cursor()
                cur.execute(
                    'UPDATE books SET "book amount" = ? where "book name" like ?',
                    [books, name],
                )
                con.commit()
                con.close()
                messagebox.showinfo("info", "edit complete")
                edit.destroy()

        edit_btn = Button(
            edit,
            text="Edit",
            width=30,
            height=2,
            fg="black",
            bg="white",
            font=("arial", 15),
            command=edi,
            cursor="hand2",
        )
        edit_btn.place(relx=0.2, rely=0.6)
        edit.mainloop()

    # -------------------------------------------------------

    # search------------------------------------------------------------
    def search():

        sere = Toplevel()
        sere.title("search page")

        # form  design-----
        w = 1000
        h = 550
        screen_height = sere.winfo_screenheight()
        screen_width = sere.winfo_screenwidth()
        x = int((screen_height - h) / 2)
        y = int((screen_width - w) / 2)

        a = "black"
        b = "#808080"
        sere.geometry(f"{w}x{h}+{y}+{x}")
        sere.resizable(False, False)

        sere.config(background="white")

        ser_lbl = Label(
            sere, text="Searching form", width=20, font=("bold", 25), bg=b, fg=a
        )
        ser_lbl.place(x=300, y=43)

        sern_lbl = Label(
            sere, text="search by book name :", width=22, font=("bold", 12), fg=a, bg=b
        )

        name_txt = Entry(sere, width=25, fg=a, bg=b)
        name_txt_lbl = Label(
            sere, text="enter the book name :", width=25, font=("bold", 12), fg=a, bg=b
        )
        name_txt_lbl.place(anchor="center", relx=0.25, rely=0.3)
        name_txt.place(anchor="center", relx=0.45, rely=0.3)
        sern_lbl.place(anchor="center", relx=0.082, rely=0.2)

        sert_lbl = Label(
            sere, text="search by book type :", width=25, font=("bold", 12), fg=a, bg=b
        )
        books_type_txt = Entry(sere, width=25, fg=a, bg=b)
        books_type_txt_lbl = Label(
            sere, text="enter the book type :", width=25, font=("bold", 12), fg=a, bg=b
        )
        books_type_txt_lbl.place(anchor="center", relx=0.25, rely=0.5)
        books_type_txt.place(anchor="center", relx=0.45, rely=0.5)
        sert_lbl.place(anchor="center", relx=0.078, rely=0.4)

        serr_lbl = Label(
            sere,
            text="search book rate greater than :",
            width=25,
            font=("bold", 12),
            fg=a,
            bg=b,
        )
        books_rate_txt = Entry(sere, width=25, fg=a, bg=b)
        books_rate_txt_lbl = Label(
            sere, text="enter the book rate :", width=25, font=("bold", 12), fg=a, bg=b
        )
        books_rate_txt_lbl.place(anchor="center", relx=0.25, rely=0.7)
        books_rate_txt.place(anchor="center", relx=0.45, rely=0.7)
        serr_lbl.place(anchor="center", relx=0.11, rely=0.6)

        def ser1():

            name = name_txt.get()

            con = sqlite3.connect("library.db")
            cur = con.cursor()
            cur.execute('SELECT * from books where "book name" like ? ', [f"%{name}%"])
            z = cur.fetchall()

            tre = Toplevel()
            tre.title("search result")
            w = 900
            h = 500
            screen_height = tre.winfo_screenheight()
            screen_width = tre.winfo_screenwidth()
            x = int((screen_height - h) / 2)
            y = int((screen_width - w) / 2)

            tre.geometry(f"{w}x{h}+{y}+{x}")
            tre.resizable(False, False)

            tre.config(background="white")

            columns = ["id", "book name", "book amount", "book rate", "book type"]

            stree = Treeview(tre, columns=columns, show="headings", selectmode="browse")
            stree.column("id", anchor="center", width=80)
            stree.column("book name", anchor="center")
            stree.column("book amount", anchor="center")
            stree.column("book rate", anchor="center")
            stree.column("book type", anchor="center")

            stree.heading("id", text="Id")
            stree.heading("book name", text="Book Name")
            stree.heading("book amount", text="Book Amount")
            stree.heading("book rate", text="Book rate")
            stree.heading("book type", text="Book type")

            for book in z:
                stree.insert("", "end", iid=book[0], values=book)

            # treeview-----------------------------------------------------

            # style-----------
            style = Style()
            style.configure(
                "Treeview",
                font=("arial", 15),
                rowheight=30,
                foreground="white",
                background="black",
            )

            con.close()
            stree.place(anchor="center", relx=0.5, rely=0.5)
            sscrollbar = Scrollbar(tre, orient="vertical", command=stree.yview)
            stree.configure(yscrollcommand=sscrollbar.set)
            sscrollbar.pack(side="right", fill=Y)

        def ser2():

            typ = books_type_txt.get()

            con = sqlite3.connect("library.db")
            cur = con.cursor()
            cur.execute('SELECT * from books where "book type" like ? ', [f"%{typ}%"])
            z = cur.fetchall()
            tre = Toplevel()
            tre.title("search result")
            w = 900
            h = 500
            screen_height = tre.winfo_screenheight()
            screen_width = tre.winfo_screenwidth()
            x = int((screen_height - h) / 2)
            y = int((screen_width - w) / 2)

            tre.geometry(f"{w}x{h}+{y}+{x}")
            tre.resizable(False, False)

            tre.config(background="white")

            columns = ["id", "book name", "book amount", "book rate", "book type"]

            stree = Treeview(tre, columns=columns, show="headings", selectmode="browse")
            stree.column("id", anchor="center", width=80)
            stree.column("book name", anchor="center")
            stree.column("book amount", anchor="center")
            stree.column("book rate", anchor="center")
            stree.column("book type", anchor="center")

            stree.heading("id", text="Id")
            stree.heading("book name", text="Book Name")
            stree.heading("book amount", text="Book Amount")
            stree.heading("book rate", text="Book rate")
            stree.heading("book type", text="Book type")

            for book in z:
                stree.insert("", "end", iid=book[0], values=book)

            # treeview-----------------------------------------------------

            # style-----------
            style = Style()
            style.configure(
                "Treeview",
                font=("arial", 15),
                rowheight=30,
                foreground="black",
                background="white",
            )

            con.close()
            stree.place(anchor="center", relx=0.5, rely=0.5)
            sscrollbar = Scrollbar(tre, orient="vertical", command=stree.yview)
            stree.configure(yscrollcommand=sscrollbar.set)
            sscrollbar.pack(side="right", fill=Y)

        def ser3():

            rate = int(books_rate_txt.get())

            con = sqlite3.connect("library.db")
            cur = con.cursor()
            cur.execute('SELECT * from books where  "book rate" >= ?', [rate])
            z = cur.fetchall()
            tre = Toplevel()
            tre.title("search result")
            w = 900
            h = 500
            screen_height = tre.winfo_screenheight()
            screen_width = tre.winfo_screenwidth()
            x = int((screen_height - h) / 2)
            y = int((screen_width - w) / 2)

            tre.geometry(f"{w}x{h}+{y}+{x}")
            tre.resizable(False, False)

            tre.config(background="white")

            columns = ["id", "book name", "book amount", "book rate", "book type"]

            stree = Treeview(tre, columns=columns, show="headings", selectmode="browse")
            stree.column("id", anchor="center", width=80)
            stree.column("book name", anchor="center")
            stree.column("book amount", anchor="center")
            stree.column("book rate", anchor="center")
            stree.column("book type", anchor="center")

            stree.heading("id", text="Id")
            stree.heading("book name", text="Book Name")
            stree.heading("book amount", text="Book Amount")
            stree.heading("book rate", text="Book rate")
            stree.heading("book type", text="Book type")

            for book in z:
                stree.insert("", "end", iid=book[0], values=book)

            # treeview-----------------------------------------------------

            # style-----------
            style = Style()
            style.configure(
                "Treeview",
                font=("arial", 15),
                rowheight=30,
                foreground="black",
                background="white",
            )

            con.close()
            stree.place(anchor="center", relx=0.5, rely=0.5)
            sscrollbar = Scrollbar(tre, orient="vertical", command=stree.yview)
            stree.configure(yscrollcommand=sscrollbar.set)
            sscrollbar.pack(side="right", fill=Y)

        search_btnn = Button(
            sere,
            text="Search",
            width=20,
            height=1,
            fg="white",
            bg="black",
            font=("arial", 15),
            command=ser1,
            cursor="hand2",
        )
        search_btnn.place(anchor="center", relx=0.85, rely=0.35)

        search_btnt = Button(
            sere,
            text="Search",
            width=20,
            height=1,
            fg="white",
            bg="black",
            font=("arial", 15),
            command=ser2,
            cursor="hand2",
        )
        search_btnt.place(anchor="center", relx=0.85, rely=0.55)

        search_btnr = Button(
            sere,
            text="Search",
            width=20,
            height=1,
            fg="white",
            bg="black",
            font=("arial", 15),
            command=ser3,
            cursor="hand2",
        )
        search_btnr.place(anchor="center", relx=0.85, rely=0.75)
        sere.mainloop()

    def lend():
        lene = Toplevel()
        lene.title("lending page")

        # form  design-----
        w = 500
        h = 500
        screen_height = lene.winfo_screenheight()
        screen_width = lene.winfo_screenwidth()
        x = int((screen_height - h) / 2)
        y = int((screen_width - w) / 2)

        a = "black"
        b = "#808080"
        lene.geometry(f"{w}x{h}+{y}+{x}")
        lene.resizable(False, False)

        lene.config(background="white")
        lene_lbl = Label(
            lene, text="Lending form", width=20, font=("bold", 25), bg=b, fg=a
        )
        lene_lbl.place(x=50, y=53)

        name_txt = Entry(lene, width=20, fg=a, bg=b)
        name_txt_lbl = Label(
            lene, text="enter the name :", font=("arial", 10), width=20, fg=a, bg=b
        )
        name_txt_lbl.place(anchor="center", relx=0.245, rely=0.5)
        name_txt.place(anchor="center", relx=0.55, rely=0.5, height=30)

        def len():
            name = name_txt.get()
            x = messagebox.askyesno("info", "are you sure you want to lend " + name)
            if x:

                con = sqlite3.connect("library.db")
                cur = con.cursor()
                cur.execute(
                    'update books set "book amount" = "book amount" -1 where "book name" like ?',
                    [name],
                )
                con.commit()
                con.close()
                messagebox.showinfo("info", "lending complete")
                lene.destroy()

        lend_btn = Button(
            lene,
            text="lend",
            width=30,
            height=2,
            fg="white",
            bg="black",
            font=("arial", 15),
            command=len,
            cursor="hand2",
        )
        lend_btn.place(relx=0.3, rely=0.6)

    # restore ------------------------------
    def restore():

        res = Toplevel()
        res.title("Returning page")

        # form  design-----
        w = 500
        h = 500
        screen_height = res.winfo_screenheight()
        screen_width = res.winfo_screenwidth()
        x = int((screen_height - h) / 2)
        y = int((screen_width - w) / 2)

        a = "black"
        b = "#808080"
        res.geometry(f"{w}x{h}+{y}+{x}")
        res.resizable(False, False)

        res.config(background="white")
        res_lbl = Label(
            res, text="Returining form", width=20, font=("bold", 25), bg=b, fg=a
        )
        res_lbl.place(x=50, y=53)

        name_txt = Entry(res, width=20, fg=a, bg=b)
        name_txt_lbl = Label(
            res, text="enter the name :", font=("arial", 10), width=20, fg=a, bg=b
        )
        name_txt_lbl.place(anchor="center", relx=0.245, rely=0.5)
        name_txt.place(anchor="center", relx=0.55, rely=0.5, height=30)

        def rest():
            name = name_txt.get()
            x = messagebox.askyesno("info", "are you sure you want to return " + name)
            if x:

                con = sqlite3.connect("library.db")
                cur = con.cursor()
                cur.execute(
                    'update books set "book amount" = "book amount" +1 where "book name" like ?',
                    [name],
                )
                con.commit()
                con.close()
                messagebox.showinfo("info", "restoring complete")
                res.destroy()

        res_btn = Button(
            res,
            text="restore",
            width=30,
            height=2,
            bg="white",
            fg="black",
            font=("arial", 15),
            command=rest,
            cursor="hand2",
        )
        res_btn.place(relx=0.3, rely=0.6)

        res.mainloop()

    #  members info mangment-----------------

    add_btn = Button(
        books,
        text="Add book",
        relief="ridge",
        bg="white",
        fg="black",
        font=("arial", 15),
        width=15,
        command=get_book,
        cursor="hand2",
    )
    add_btn.place(relx=0.8, rely=0.45)

    del_btn = Button(
        books,
        text="Delete book",
        relief="ridge",
        bg="white",
        fg="black",
        font=("arial", 15),
        width=15,
        command=dele,
        cursor="hand2",
    )
    del_btn.place(relx=0.8, rely=0.55)

    edit_btn = Button(
        books,
        text="Edit book",
        relief="ridge",
        bg="white",
        fg="black",
        font=("arial", 15),
        width=15,
        command=edit,
        cursor="hand2",
    )
    edit_btn.place(relx=0.8, rely=0.6)

    search_btn = Button(
        books,
        text="search for book",
        relief="ridge",
        bg="white",
        fg="black",
        font=("arial", 15),
        width=15,
        command=search,
        cursor="hand2",
    )
    search_btn.place(relx=0.8, rely=0.4)

    lend_btn = Button(
        books,
        text="lend book",
        relief="ridge",
        bg="white",
        fg="black",
        font=("arial", 15),
        width=15,
        command=lend,
        cursor="hand2",
    )
    lend_btn.place(relx=0.8, rely=0.5)

    res_btn = Button(
        books,
        text="Return book",
        relief="ridge",
        bg="white",
        fg="black",
        font=("arial", 15),
        width=15,
        command=restore,
        cursor="hand2",
    )
    res_btn.place(relx=0.8, rely=0.65)
    # -----------------------------------------

    def back():
        books.destroy()

    # show elements-----------------
    bscrollbar.pack(side="right", fill=Y)
    btree.place(relx=0.4, rely=0)
    reader_lbl.place(relx=0.179, rely=0)

    back_img = PhotoImage(file="back.png")
    back_btn = Button(
        books,
        image=back_img,
        compound="left",
        width=100,
        height=30,
        font=("arial", 20),
        command=back,
        bg="orange",
        cursor="hand2",
    )
    back_btn.place(anchor="center", relx=0.03, rely=0.015)

    # --------------------------------------------------------
    books.mainloop()

# readers page---------------------
def readers():
    # page design -----------------------------------------------------
    readers = Toplevel()

    readers.title("Readers Page")
    screen_height = readers.winfo_screenheight()
    screen_width = readers.winfo_screenwidth()
    w = screen_width
    h = screen_height

    readers.geometry(f"{w-10}x{h}")

    bg_img = PhotoImage(file="readers.png")
    bg_lbl = Label(readers, image=bg_img, width=w - 10, height=h)
    bg_lbl.place(anchor="center", relx=0.5, rely=0.5)
    # connection---------------------------
    con = sqlite3.connect("library.db")
    cur = con.cursor()
    cur.execute("select * from readers order by books desc")
    result = cur.fetchall()
    con.close()
    # treeview--------------------------------------------------------------------

    columns = ["name", "books"]

    rtree = Treeview(readers, columns=columns, show="headings", selectmode="none")

    rtree.column("name", anchor="center")
    rtree.column("books", anchor="center")

    rtree.heading("name", text="Name")
    rtree.heading("books", text="Books")

    for reader in result:
        rtree.insert("", "end", values=reader)

    # treeview-----------------------------------------------------

    # scrollbar-------------------------------------------------------------
    rscrollbar = Scrollbar(readers, orient="vertical", command=rtree.yview)
    rtree.configure(yscrollcommand=rscrollbar.set)

    # style-----------
    style = Style()
    style.configure(
        "Treeview",
        font=("arial", 15),
        rowheight=30,
        foreground="white",
        background="black",
    )
    # ------------------
    reader_lbl = Label(
        readers, font=("arial", 20), bg="white", text="this is our members system : "
    )
    # _________-------------------------

    # getuser-------------------------------
    def get_user():

        get = Toplevel()
        get.title("addition page")

        # form  design-----
        w = 500
        h = 500
        screen_height = get.winfo_screenheight()
        screen_width = get.winfo_screenwidth()
        x = int((screen_height - h) / 2)
        y = int((screen_width - w) / 2)

        a = "black"
        b = "#808080"
        get.geometry(f"{w}x{h}+{y}+{x}")
        get.resizable(False, False)

        get.config(background="white")

        add_lbl = Label(
            get, text="Addition form", width=20, font=("bold", 25), bg=b, fg=a
        )
        add_lbl.place(x=50, y=53)

        name_txt = Entry(get, width=20, fg=a, bg=b)
        name_txt_lbl = Label(
            get, text="enter the member name :", width=20, font=("bold", 10), fg=a, bg=b
        )

        books_txt = Entry(get, width=20, fg=a, bg=b)
        books_txt_lbl = Label(
            get,
            text="enter the books number :",
            width=20,
            font=("bold", 10),
            fg=a,
            bg=b,
        )
        
        id_txt = Entry(get, width=20, fg=a, bg=b)
        id_txt_lbl = Label(
            get,
            text="enter your id based on table sequence :",
            width=20,
            font=("bold", 10),
            fg=a,
            bg=b,
        )

        name_txt_lbl.place(x=70, y=180)
        name_txt.place(x=300, y=180)

        books_txt_lbl.place(x=70, y=230)
        books_txt.place(x=300, y=230)

        id_txt_lbl.place(x=70, y=280)
        id_txt.place(x=300, y=280)

        def add():
            name = name_txt.get()
            books = books_txt.get()
            id = id_txt.get()

            con = sqlite3.connect("library.db")
            cur = con.cursor()
            cur.execute("insert into readers values(?,?,?)", [name, books, id])
            con.commit()

            con.close()
            messagebox.showinfo("info", "addition complete")
            get.destroy()

        add_btn = Button(
            get,
            text="Add",
            width=20,
            height=2,
            fg="black",
            bg="darkred",
            font=("arial", 15),
            command=add,
            cursor="hand2",
        )
        add_btn.place(relx=0.29, rely=0.8)

    # ---------------------------------------------

    # delete user------------------------------------------
    def deluser():
        dele = Toplevel()
        dele.title("delete page")

        # form  design-----
        w = 500
        h = 500
        screen_height = dele.winfo_screenheight()
        screen_width = dele.winfo_screenwidth()
        x = int((screen_height - h) / 2)
        y = int((screen_width - w) / 2)

        a = "black"
        b = "#808080"
        dele.geometry(f"{w}x{h}+{y}+{x}")
        dele.resizable(False, False)

        dele.config(background="white")
        dele_lbl = Label(
            dele, text="Deletion form", width=20, font=("bold", 25), bg=b, fg=a
        )
        dele_lbl.place(x=50, y=53)

        name_txt = Entry(dele, width=20, fg=a, bg=b)
        name_txt_lbl = Label(
            dele, text="enter the name :", font=("arial", 10), width=20, fg=a, bg=b
        )
        name_txt_lbl.place(anchor="center", relx=0.245, rely=0.5)
        name_txt.place(anchor="center", relx=0.55, rely=0.5, height=30)

        def delete():
            name = name_txt.get()
            x = messagebox.askyesno(
                "info", "are you sure you want to delete" + " " + name
            )
            if x:

                con = sqlite3.connect("library.db")
                cur = con.cursor()
                cur.execute('DELETE from readers where "nick name" like ?', [name])
                con.commit()
                con.close()
                messagebox.showinfo("info", "deletion complete")
                dele.destroy()

        dele_btn = Button(
            dele,
            text="Delete",
            width=30,
            height=2,
            fg="black",
            bg="darkred",
            font=("arial", 15),
            command=delete,
            cursor="hand2",
        )
        dele_btn.place(relx=0.3, rely=0.55)
        dele.mainloop()

    # -----------------------------------------------------------

    # edit info--------------------------------------
    def edit():

        edit = Toplevel()
        edit.title("edit page")

        # form  design-----
        w = 500
        h = 500
        screen_height = edit.winfo_screenheight()
        screen_width = edit.winfo_screenwidth()
        x = int((screen_height - h) / 2)
        y = int((screen_width - w) / 2)

        a = "black"
        b = "#808080"
        edit.geometry(f"{w}x{h}+{y}+{x}")
        edit.resizable(False, False)

        edit.config(background="white")

        edit_lbl = Label(
            edit, text="Edit form", width=20, font=("bold", 25), bg=b, fg=a
        )
        edit_lbl.place(x=50, y=53)

        msg_lbl = Label(
            edit,
            text="you must enter a name even if it's the same name",
            font=("bold", 12),
            bg=b,
            fg="darkblue",
        )
        msg_lbl.place(x=80, y=100)

        name_txt = Entry(edit, width=20, fg=a, bg=b)
        name_txt_lbl = Label(
            edit, text="enter the nick name :", width=20, font=("bold", 10), fg=a, bg=b
        )
        name_txt_lbl.place(anchor="center", relx=0.245, rely=0.35)
        name_txt.place(anchor="center", relx=0.6, rely=0.35, height=30)

        newname_txt = Entry(edit, width=20, fg=a, bg=b)
        newname_txt_lbl = Label(
            edit, text="enter the new name :", width=20, font=("bold", 10), fg=a, bg=b
        )
        newname_txt_lbl.place(anchor="center", relx=0.245, rely=0.45)
        newname_txt.place(anchor="center", relx=0.6, rely=0.45, height=30)

        books_txt = Entry(edit, width=20, fg=a, bg=b)
        books_txt_lbl = Label(
            edit,
            text="enter the new books number :",
            width=22,
            font=("bold", 10),
            fg=a,
            bg=b,
        )
        books_txt_lbl.place(anchor="center", relx=0.245, rely=0.55)
        books_txt.place(anchor="center", relx=0.6, rely=0.55, height=30)

        def edi():
            x = messagebox.askyesno("info", "are you sure you want to edit")
            if x:
                name = name_txt.get()
                newname = newname_txt.get()
                books = int(books_txt.get())

                con = sqlite3.connect("library.db")
                cur = con.cursor()
                cur.execute(
                    'UPDATE readers SET "books" = ? where "nick name" like ?',
                    [books, name],
                )
                con.commit()
                con.close()
                con = sqlite3.connect("library.db")
                cur = con.cursor()
                cur.execute(
                    'UPDATE readers SET "nick name" = ? where "nick name" like ?',
                    [newname, name],
                )
                con.commit()
                con.close()
                messagebox.showinfo("info", "edit complete")
                edit.destroy()

        edit_btn = Button(
            edit,
            text="Edit",
            width=30,
            height=2,
            bg="white",
            fg="black",
            font=("arial", 15),
            command=edi,
            cursor="hand2",
        )
        edit_btn.place(relx=0.2, rely=0.6)
        edit.mainloop()

    # -------------------------------------------------------
    def search():

        sere = Toplevel()
        sere.title("search page")

        # form  design-----
        w = 500
        h = 500
        screen_height = sere.winfo_screenheight()
        screen_width = sere.winfo_screenwidth()
        x = int((screen_height - h) / 2)
        y = int((screen_width - w) / 2)

        a = "black"
        b = "#808080"
        sere.geometry(f"{w}x{h}+{y}+{x}")
        sere.resizable(False, False)

        sere.config(background="white")
        name_txt = Entry(sere, width=25, fg=a, bg=b)
        name_txt_lbl = Label(
            sere, text="enter the name :", width=25, font=("bold", 12), fg=a, bg=b
        )
        name_txt_lbl.place(anchor="center", relx=0.25, rely=0.5)
        name_txt.place(anchor="center", relx=0.7, rely=0.5)
        sf_lbl = Label(
            sere, text="Searching Form", width=20, font=("bold", 25), bg=b, fg=a
        )
        sf_lbl.place(x=50, y=53)

        def ser():
            name = "none"
            name = name_txt.get()
            tre = Toplevel()
            tre.title("search result")
            w = 400
            h = 100
            screen_height = tre.winfo_screenheight()
            screen_width = tre.winfo_screenwidth()
            x = int((screen_height - h) / 2)
            y = int((screen_width - w) / 2)

            tre.geometry(f"{w}x{h}+{y}+{x}")
            tre.resizable(False, False)

            tre.config(background="white")

            con = sqlite3.connect("library.db")
            cur = con.cursor()
            cur.execute(
                'SELECT * from readers where "nick name" like ? ', [f"%{name}%"]
            )
            z = cur.fetchall()
            columns = ["nick name", "books"]

            stree = Treeview(tre, columns=columns, show="headings", selectmode="none")

            stree.column("nick name", anchor="center")
            stree.column("books", anchor="center")

            stree.heading("nick name", text="Nick Name")
            stree.heading("books", text="Books")

            for book in z:
                stree.insert("", "end", values=book)

            # treeview-----------------------------------------------------

            # style-----------
            style = Style()
            style.configure(
                "Treeview",
                font=("arial", 15),
                rowheight=30,
                foreground="white",
                background="black",
            )

            con.close()
            stree.place(anchor="center", relx=0.5, rely=0.34, height=120)
            sscrollbar = Scrollbar(tre, orient="vertical", command=stree.yview)
            stree.configure(yscrollcommand=sscrollbar.set)
            sscrollbar.pack(side="right", fill=Y)

        search_btn = Button(
            sere,
            text="Search",
            width=30,
            height=2,
            bg="white",
            fg="black",
            font=("arial", 15),
            command=ser,
            cursor="hand2",
        )
        search_btn.place(relx=0.2, rely=0.65)
        sere.mainloop()

    #  members info mangment-----------------

    add_btn = Button(
        readers,
        text="Add member",
        relief="ridge",
        bg="white",
        fg="black",
        font=("arial", 15),
        width=15,
        command=get_user,
        cursor="hand2",
    )
    add_btn.place(relx=0.8, rely=0.45)

    del_btn = Button(
        readers,
        text="Delete member",
        relief="ridge",
        bg="white",
        fg="black",
        font=("arial", 15),
        width=15,
        command=deluser,
        cursor="hand2",
    )
    del_btn.place(relx=0.8, rely=0.55)

    edit_btn = Button(
        readers,
        text="Edit member",
        relief="ridge",
        bg="white",
        fg="black",
        font=("arial", 15),
        width=15,
        command=edit,
        cursor="hand2",
    )
    edit_btn.place(relx=0.8, rely=0.5)
    search_btn = Button(
        readers,
        text="Search for member",
        relief="ridge",
        bg="white",
        fg="black",
        font=("arial", 15),
        width=15,
        command=search,
        cursor="hand2",
    )
    search_btn.place(relx=0.8, rely=0.4)
    # -----------------------------------------

    def back():
        readers.destroy()

    # show elements-----------------
    rscrollbar.pack(side="right", fill=Y)
    rtree.place(relx=0.7, rely=0)
    reader_lbl.place(relx=0.46, rely=0)
    back_img = PhotoImage(file="back.png")
    back_btn = Button(
        readers,
        image=back_img,
        compound="left",
        width=100,
        height=30,
        font=("arial", 20),
        command=back,
        bg="orange",
        cursor="hand2",
    )
    back_btn.place(anchor="center", relx=0.03, rely=0.015)

    # --------------------------------------------------------
    readers.mainloop()

# home page-----------
def home_page():
    home = Toplevel()

    home.title("Home Page")
    screen_height = home.winfo_screenheight()
    screen_width = home.winfo_screenwidth()
    w = screen_width
    h = screen_height
    home.geometry(f"{w}x{h}")

    # logout function
    def logout():
        home.destroy()

    # background photo-----------
    bg_img = PhotoImage(file="library-app-background.png")
    bg_lbl = Label(home, image=bg_img, width=w, height=h)

    bg_lbl.place(anchor="center", relx=0.5, rely=0.5)

    # ------upper buttons of the design
    reader_img = PhotoImage(file="man-sitting-and-reading-book.png")
    btn_readers = Button(
        home,
        text="readers",
        width=110,
        height=30,
        bg="Cyan",
        font=("tahoma", 15),
        image=reader_img,
        compound="left",
        command=readers,
        cursor="hand2",
    )

    books_img = PhotoImage(file="books-stack-of-three.png")
    btn_books = Button(
        home,
        text="books",
        width=110,
        height=30,
        bg="Cyan",
        font=("tahoma", 15),
        image=books_img,
        compound="left",
        command=books,
        cursor="hand2",
    )

    about_img = PhotoImage(file="information-button.png")
    about_btn = Button(
        home,
        text="About Us",
        width=120,
        height=30,
        bg="Cyan",
        font=("tahoma", 15),
        image=about_img,
        compound="left",
        command=about,
        cursor="hand2",
    )
    
    contact_img = PhotoImage(file="customer-service.png")
    contact_btn = Button(
        home,
        text="Contact Us",
        width=120,
        height=30,
        bg="Cyan",
        font=("tahoma", 15),
        image=contact_img,
        compound="left",
        command=Contact,
        cursor="hand2",
    )

    logout_img = PhotoImage(file="log-out.png")
    btn_logout = Button(
        home,
        text="logout",
        width=150,
        height=30,
        bg="orange",
        font=("tahoma", 15),
        image=logout_img,
        compound="left",
        command=logout,
        cursor="hand2",
    )

    btn_readers.place(x=0, y=0)
    btn_books.place(x=110, y=0)
    about_btn.place(x=220, y=0)
    contact_btn.place(x=340, y=0)
    btn_logout.place(relx=0.89, rely=0.91)

    # ------------------------

    # welcome labels-----

    hello_txt = Label(home, font=("bold", 25), text="Welcome to Dav BookStore", bg = "white")
    hello_txt.place(x=720, y=40)

    hello_txt2 = Label(
        home,
        font=("arial", 15),
        text="welcome to Dav BookStore . we have a large connection to carter reading needs of all kinds of readers ",
         bg = "white"
    )
    hello_txt2.place(x=400, y=100)

    # ------------------------

    # main labels------------
    whhy_lbl = Label(home, text="Why Reading Is Important?", font=("bold", 25),  bg = "white")
    whhy_ans = Label(
        home,
        font=("arial", 15),
        bg="orange",
        text="Reading expands knowledge, enhances cognitive skills, and fosters empathy by exposing us to\n diverse perspectives and experiences. It also improves language proficiency and provides both relaxation and entertainment.",
    )

    id_lbl = Label(home, font=("bold", 20), bg="orange", text="Credits to David Emile")

    whhy_lbl.place(x=150, y=300)
    whhy_ans.place(x=0, y=400)

    id_lbl.place(relx=0, rely=0.91)
    # -----------------------
    home.mainloop()

# register page-------------------------------------
def register():
    register = Toplevel()

    # page design------------------------
    w = 500
    h = 500
    screen_height = register.winfo_screenheight()
    screen_width = register.winfo_screenwidth()
    x = int((screen_height - h) / 2)
    y = int((screen_width - w) / 2)

    register.title("register page")
    register.geometry(f"{w}x{h}+{y}+{x}")
    register.resizable(False, False)
    register.config(background="white")
    # ---------------------------------------------

    # page gui-----------------------------------------------
    Register_img = PhotoImage(file="download.png")
    Register_lbl = Label(register, image =Register_img, width=100, height=150)
    Register_lbl.place(x=0,y=40)
    
    reg_lbl = Label(register, text="Registration form", width=20, font=("bold", 20))
    reg_lbl.place(x=90, y=53)

    name_lbl = Label(register, text="UserName", width=10, font=("bold", 10))
    name_lbl.place(x=110, y=130)

    name_entry = Entry(register)
    name_entry.place(x=240, y=130)

    email_lbl = Label(register, text="Email", width=20, font=("bold", 10))
    email_lbl.place(x=68, y=180)

    email_entry = Entry(register)
    email_entry.place(x=240, y=180)

    gender_lbl = Label(register, text="Gender", width=20, font=("bold", 10))
    gender_lbl.place(x=70, y=230)
    var = IntVar()
    male_radio = Radiobutton(
        register, text="Male", padx=5, variable=var, value=1
    ).place(x=235, y=230)
    female_radio = Radiobutton(
        register, text="Female", padx=20, variable=var, value=2
    ).place(x=290, y=230)

    age_lbl = Label(register, text="Age:", width=20, font=("bold", 10))
    age_lbl.place(x=70, y=280)

    age_entry = Entry(register)
    age_entry.place(x=240, y=280)

    pass_lbl = Label(register, text="password", width=20, font=("bold", 10))
    pass_lbl.place(x=70, y=330)
    pass_entry = Entry(register)
    pass_entry.place(x=240, y=330)

    # -----------------------------------------------------------

    def reg():

        name = name_entry.get()
        password = pass_entry.get()
        con = sqlite3.connect("library.db")
        cur = con.cursor()
        cur.execute("insert into users values(?,?)", [name, password])
        con.commit()
        con.close()
        register.destroy()

    sub_btn = Button(
        register,
        text="Submit",
        width=20,
        bg="brown",
        fg="white",
        command=reg,
        cursor="hand2",
    ).place(x=180, y=380)

    register.mainloop()

# ---------------------------------------------------
def login():

    def check_login():
        con = sqlite3.connect("library.db")
        cur = con.cursor()
        cur.execute("SELECT * from users")
        z = cur.fetchall()
        con.close()

        for x in z:
            user = x[0]
            pas = x[1]

            user1 = user_txt.get()
            pas1 = pass_txt.get()
            if user == user1 and pas == pas1:
                messagebox.showinfo(
                    "info", "hello " + user1 + " welcome back on our page"
                )
                home_page()
                break
        else:
            messagebox.showerror("eror", "wrong password or user name")

    login = Tk()
    w = 500
    h = 300
    screen_height = login.winfo_screenheight()
    screen_width = login.winfo_screenwidth()
    x = int((screen_height - h) / 2)
    y = int((screen_width - w) / 2)

    login.title("login page")
    login.geometry(f"{w}x{h}+{y}+{x}")
    login.resizable(False, False)

    log_img = PhotoImage(file="1.png")

    reg_img = PhotoImage(file="registration.png")

    frame = Frame(login)
    
    hello_lbl = Label(
        frame,
        text="Hello to Dav BookStore \nSignIn please",
        font=("tahoma", 15),
    )

    user_lbl = Label(frame, text="UserName", font=("tahoma", 16))
    user_txt = Entry(frame, font=("tahoma", 12))

    pass_lbl = Label(frame, text="Password", font=("tahoma", 16))
    pass_txt = Entry(frame, show="*", font=("tahoma", 12))

    log_btn = Button(
        frame,
        text="SignIn",
        fg="#F982F1",
        command=check_login,
        font=("tahoma", 15),
        image=log_img,
        compound="left",
        relief="raised",
        cursor="hand2",
    )
    log_btn.config(width=100, height=30)
    signup_lbl = Label(frame, text="If you don't have ann account, you can SignUp", bg="white", font=("tahome",14))
    reg_btn = Button(
        frame,
        text="SignUp",
        command=register,
        fg="#F982F1",
        font=("tahoma", 15),
        image=reg_img,
        compound="left",
        relief="raised",
        cursor="hand2",
    )
    reg_btn.config(width=100, height=30)

    hello_lbl.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
    user_lbl.grid(row=1, column=0, padx=5, pady=5)
    user_txt.grid(row=1, column=1, padx=5, pady=5)

    pass_lbl.grid(row=2, column=0, padx=5, pady=5)
    pass_txt.grid(row=2, column=1, padx=5, pady=5)
    log_btn.grid(row=3, column=0, columnspan=2, padx=5, pady=5)
    signup_lbl.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
    reg_btn.grid(row=5, column=0, columnspan=2, padx=5, pady=5)
    frame.place(anchor="center", relx=0.5, rely=0.5)
    login.mainloop()

login()