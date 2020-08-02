from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from tinderBackend import *


class TinderGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Tinder App")
        self.root.maxsize(800, 500)
        self.root.minsize(800, 500)
        self.root['bg'] = 'Pink'
        self.tinderBackend = Tinder()

        self.lblWelcome = Label(self.root, text=("Welocme to Tinder App "), font=("Impact", 50), bg="light green")
        self.lblWelcome.grid(row=0, column=0)

        self.lblafterWelcome = Label(self.root, text=(""), font=("Impact", 40), bg="pink")
        self.lblafterWelcome.grid(row=2, column=0)

        self.btnLogin = Button(self.root, width=7, height=1, text="Login", font=("Arial", 20), bg="light blue",
                               command=lambda: self.loginWindow())
        self.btnLogin.grid(row=3, column=0)

        self.lblafterLogin = Label(self.root, text=(""), font=("Impact", 10), bg="pink")
        self.lblafterLogin.grid(row=4, column=0)

        self.btnRegister = Button(self.root, width=7, height=1, text="Register", font=("Arial", 20), bg="light blue",
                                  command=lambda: self.registerWindow())
        self.btnRegister.grid(row=5, column=0)

        self.lblafterRegister = Label(self.root, text=(""), font=("Impact", 10), bg="pink")
        self.lblafterRegister.grid(row=6, column=0)

        self.btnExit = Button(self.root, width=7, height=1, text="Exit", font=("Arial", 20), bg="Light blue",
                              command=lambda: self.root.destroy())
        self.btnExit.grid(row=7, column=0)

        self.root.mainloop()

    def loginWindow(self):
        if (self.tinderBackend.currentUserId != 0):
            self.showUserMenu()
        else:
            child = Toplevel(self.root)
            child.title("Login Window")
            child.maxsize(680, 250)
            child.minsize(680, 250)
            child['bg'] = 'Pink'

            lblLogin = Label(child, text="Email:", width=8, height=1, font=('Arial', 15), bg='pink')
            lblLogin.grid(row=0, column=0, pady=20)
            entEmail = Entry(child, width=29, font=('Arial', 20))
            entEmail.grid(row=0, column=1, pady=20)

            lblPassword = Label(child, text="Password:", width=8, height=1, font=('Arial', 15), bg='pink')
            lblPassword.grid(row=1, column=0, pady=10)
            entPassword = Entry(child, width=29, font=('Arial', 20))
            entPassword.grid(row=1, column=1, pady=10)

            btnLogin = Button(child, text="Login", width=7, height=1, bg='light blue', font=('Arial', 20),
                              command=lambda: self.validate(child, entEmail.get(), entPassword.get()))
            btnLogin.grid(row=3, column=1, pady=20)

    def validate(self, child, email, password):
        result = self.tinderBackend.userLogin(email, password)
        if result:
            messagebox.showinfo('Success', 'Successfully Logged in !')
            self.showUserMenu()
            child.destroy()
        else:
            messagebox.showinfo('Error', 'Logged in failed !')

    def registerWindow(self):
        child = Toplevel(self.root)
        child.title("Registration Window")
        child.maxsize(800, 400)
        child.minsize(800, 400)

        child['bg'] = 'Pink'

        lblName = Label(child, text="Name:", width=12, height=1, font=('Arial', 15), background='Pink')
        lblName.grid(row=0, column=0, pady=10)
        entName = Entry(child, width=30, font=('Arial', 20))
        entName.grid(row=0, column=1, pady=10)

        lblGender = Label(child, text="Gender:", width=12, height=1, font=('Arial', 15), background='Pink')
        lblGender.grid(row=1, column=0, pady=10)
        entGender = Entry(child, width=30, font=('Arial', 20))
        entGender.grid(row=1, column=1, pady=10)

        lblCity = Label(child, text="City:", width=12, height=1, font=('Arial', 15), background='Pink')
        lblCity.grid(row=2, column=0, pady=10)
        entCity = Entry(child, width=30, font=('Arial', 20))
        entCity.grid(row=2, column=1, pady=10)

        lblEmail = Label(child, text="Email:", width=12, height=1, font=('Arial', 15), background='Pink')
        lblEmail.grid(row=3, column=0, pady=10)
        entEmail = Entry(child, width=30, font=('Arial', 20))
        entEmail.grid(row=3, column=1, pady=10)

        lblPassword = Label(child, text="Password:", width=12, height=1, font=('Arial', 15), background='Pink')
        lblPassword.grid(row=4, column=0, pady=10)
        entPassword = Entry(child, width=30, font=('Arial', 20))
        entPassword.grid(row=4, column=1, pady=10)

        btnRegister = Button(child, width=8, height=1, text="Register", font=('Arial', 20), background='light blue',
                             command=lambda: self.addUser(child, entName.get(), entGender.get(), entCity.get(),
                                                          entEmail.get(), entPassword.get()))
        btnRegister.grid(row=5, column=1, pady=10)

    def addUser(self, child, name, gender, city, email, password):
        self.tinderBackend.userRegister(name, gender, city, email, password)
        messagebox.showinfo('Success', 'Registration Successful !')
        child.destroy()

    def showUserMenu(self):
        child = Toplevel(self.root)
        child.title("User Window")
        child.maxsize(460, 460)
        child.minsize(460, 460)
        child['bg'] = 'Pink'

        username = self.tinderBackend.fetchUserName()

        lblWelcome = Label(child, width=30, height=1, text=("Welcome %s !" % username[0][0]), bg='pink',
                           font=('Arial', 15))
        lblWelcome.grid(row=0, column=0, pady=20)

        btn1 = Button(child, width=20, height=1, text="View All Users", bg='light blue', font=('Arial', 15),
                      command=lambda: self.showUsers())
        btn1.grid(row=1, column=0, pady=10)

        btn2 = Button(child, width=20, height=1, text="View Sent Proposals", bg='light blue', font=('Arial', 15),
                      command=lambda: self.viewSent())
        btn2.grid(row=2, column=0, pady=10)

        btn3 = Button(child, width=20, height=1, text="View Received Proposals", bg='light blue', font=('Arial', 15),
                      command=lambda: self.viewReceived())
        btn3.grid(row=3, column=0, pady=10)

        btn4 = Button(child, width=20, height=1, text="View Matches", bg='light blue', font=('Arial', 15),
                      command=lambda: self.viewMatches())
        btn4.grid(row=4, column=0, pady=10)

        btn5 = Button(child, width=20, height=1, text="Log Out", bg='light blue', font=('Arial', 15),
                      command=lambda: self.logout(child))
        btn5.grid(row=5, column=0, pady=10)

    def showUsers(self):
        child = Toplevel(self.root)
        child.title("User List")
        child.maxsize(1366, 768)
        child.minsize(1366, 768)
        child['bg'] = 'Pink'

        # Create a Main Frame
        main_frame = Frame(child)
        main_frame.pack(fill=BOTH, expand=1)
        # Create a Canvas
        my_canvas = Canvas(main_frame, background='Pink')
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        # Add a scrollbar to the canvas
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)
        # Configure the canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        # Create Another Frame inside the canvas
        second_frame = Frame(my_canvas, background='Pink')
        # Add that new frame to a window in the canvas
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")



        userlist = self.tinderBackend.viewAllUsers()

        lblWelcome = Label(second_frame, text="User List", width=35, height=3, font=('Courier,16'), bg="pink", padx=15,
                           pady=10)
        lblWelcome.grid(row=0, column=0)

        lblgender = Label(second_frame, text="Gender", width=35, height=3, font=('Courier,16'), bg="pink", padx=15,
                          pady=10)
        lblgender.grid(row=0, column=1)

        lblcity = Label(second_frame, text="City", width=35, height=3, font=('Courier,16'), bg="pink", padx=15, pady=10)
        lblcity.grid(row=0, column=2)

        i = 1
        k = 0
        for user in userlist:
            if user[0] != self.tinderBackend.currentUserId:
                lblName = Label(second_frame, text=user[1], width=15, height=1, font=('Arial', 15), padx=15, pady=5,
                                bg="pink")
                lblName.grid(row=i, column=0, pady=10)
                lblGender = Label(second_frame, text=user[2], width=6, height=1, font=('Arial', 15), padx=15, pady=5,
                                  bg="pink")
                lblGender.grid(row=i, column=1, pady=10)
                lblCity = Label(second_frame, text=user[3], width=15, height=1, font=('Arial', 15), padx=15, pady=5,
                                bg="pink")
                lblCity.grid(row=i, column=2, pady=10)
                if (self.tinderBackend.checkPropose(user[0])):
                    btnPropose = Button(second_frame, text="Propose", width=8, height=1, font=('Arial', 15),
                                        bg="light blue",
                                        padx=15, pady=5,
                                        command=lambda k=i: self.sendProposal(userlist[k - 1][0]))
                    btnPropose.grid(row=i, column=3, pady=10)
            i = i + 1

    def sendProposal(self, userid):
        self.tinderBackend.propose(userid)
        messagebox.showinfo("Sent", " Proposal Sent ")

    def viewSent(self):
        child = Toplevel(self.root)
        child.title("Sent Proposals List")
        child.maxsize(1366, 768)
        child.minsize(1366, 768)
        child['bg'] = 'Pink'

        # Create a Main Frame
        main_frame = Frame(child)
        main_frame.pack(fill=BOTH, expand=1)
        # Create a Canvas
        my_canvas = Canvas(main_frame, background='Pink')
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        # Add a scrollbar to the canvas
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)
        # Configure the canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        # Create Another Frame inside the canvas
        second_frame = Frame(my_canvas, background='Pink')
        # Add that new frame to a window in the canvas
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        userlist = self.tinderBackend.viewSentProposals()
        lblWelcome = Label(second_frame, text="Crush List", width=35, height=3, font=('Courier,16'), bg="pink")
        lblWelcome.grid(row=0, column=0)

        lblname = Label(second_frame, text="Name", width=35, height=3, font=('Courier,16'), bg="pink", padx=15, pady=5)
        lblname.grid(row=0, column=1)

        lblgender = Label(second_frame, text="Gender", width=35, height=3, font=('Courier,16'), bg="pink", padx=15,
                          pady=5)
        lblgender.grid(row=0, column=2)

        lblcity = Label(second_frame, text="City", width=35, height=3, font=('Courier,16'), bg="pink", padx=15, pady=5)
        lblcity.grid(row=0, column=3)

        i = 1
        for user in userlist:
            lblId = Label(second_frame, text=user[3], width=2, height=1, font=('Arial', 15), bg="pink")
            lblId.grid(row=i, column=0)
            lblName = Label(second_frame, text=user[4], width=15, height=1, font=('Arial', 15), bg="pink")
            lblName.grid(row=i, column=1)
            lblGender = Label(second_frame, text=user[5], width=6, height=1, font=('Arial', 15), bg="pink")
            lblGender.grid(row=i, column=2)
            lblCity = Label(second_frame, text=user[6], width=15, height=1, font=('Arial', 15), bg="pink")
            lblCity.grid(row=i, column=3)
            i = i + 1

    def viewReceived(self):
        child = Toplevel(self.root)
        child.title("Received List")
        child.maxsize(1366, 768)
        child.minsize(1366, 768)
        child['bg'] = 'Pink'

        # Create a Main Frame
        main_frame = Frame(child)
        main_frame.pack(fill=BOTH, expand=1)
        # Create a Canvas
        my_canvas = Canvas(main_frame, background='Pink')
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        # Add a scrollbar to the canvas
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)
        # Configure the canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        # Create Another Frame inside the canvas
        second_frame = Frame(my_canvas, background='Pink')
        # Add that new frame to a window in the canvas
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        userlist = self.tinderBackend.viewReceivedProposals()
        lblWelcome = Label(second_frame, text="Fan List", width=25, height=3, font=('Courier,16'), bg="pink", padx=15,
                           pady=5)
        lblWelcome.grid(row=0, column=0)

        lblname = Label(second_frame, text="Name", width=20, height=3, font=('Courier,16'), bg="pink", padx=15, pady=5)
        lblname.grid(row=0, column=1)

        lblgender = Label(second_frame, text="Gender", width=15, height=3, font=('Courier,16'), bg="pink", padx=15,
                          pady=5)
        lblgender.grid(row=0, column=2)

        lblcity = Label(second_frame, text="City", width=20, height=3, font=('Courier,16'), bg="pink", padx=35, pady=5)
        lblcity.grid(row=0, column=3)

        i = 1
        for user in userlist:
            lblId = Label(second_frame, text=user[3], width=2, height=1, font=('Arial', 15), bg="pink")
            lblId.grid(row=i, column=0, pady=10, padx=15)
            lblName = Label(second_frame, text=user[4], width=15, height=1, font=('Arial', 15), bg="pink")
            lblName.grid(row=i, column=1, pady=10, padx=15)
            lblGender = Label(second_frame, text=user[5], width=6, height=1, font=('Arial', 15), bg="pink")
            lblGender.grid(row=i, column=2, pady=10, padx=15)
            lblCity = Label(second_frame, text=user[6], width=15, height=1, font=('Arial', 15), bg="pink")
            lblCity.grid(row=i, column=3, pady=10, padx=15)
            if (self.tinderBackend.checkPropose(user[3])):
                btnPropose = Button(second_frame, text="Propose", width=8, height=1, font=('Arial', 15),
                                    bg="light blue",
                                    padx=15, pady=5,
                                    command=lambda k=i: self.sendProposal(userlist[k - 1][3]))
                btnPropose.grid(row=i, column=4, pady=10, padx=15)
            i = i + 1

    def viewMatches(self):
        child = Toplevel(self.root)
        child.title("Matches List")
        child.maxsize(1366, 768)
        child.minsize(1366, 768)

        child['bg'] = 'Pink'

        # Create a Main Frame
        main_frame = Frame(child)
        main_frame.pack(fill=BOTH, expand=1)
        # Create a Canvas
        my_canvas = Canvas(main_frame, background='Pink')
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
        # Add a scrollbar to the canvas
        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)
        # Configure the canvas
        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
        # Create Another Frame inside the canvas
        second_frame = Frame(my_canvas, background='Pink')
        # Add that new frame to a window in the canvas
        my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

        userlist = self.tinderBackend.viewMatches()
        lblWelcome = Label(second_frame, text="Match List", width=35, height=3, font=('Courier,16'), bg="pink")
        lblWelcome.grid(row=0, column=0)

        lblname = Label(second_frame, text="Name", width=35, height=3, font=('Courier,16'), bg="pink", padx=15, pady=5)
        lblname.grid(row=0, column=1)

        lblgender = Label(second_frame, text="Gender", width=35, height=3, font=('Courier,16'), bg="pink", padx=15,
                          pady=5)
        lblgender.grid(row=0, column=2)

        lblcity = Label(second_frame, text="City", width=35, height=3, font=('Courier,16'), bg="pink", padx=15, pady=5)
        lblcity.grid(row=0, column=3)

        i = 1
        for user in userlist:
            lblId = Label(second_frame, text=user[3], width=2, height=1, font=('Arial', 15), bg="pink")
            lblId.grid(row=i, column=0)
            lblName = Label(second_frame, text=user[4], width=15, height=1, font=('Arial', 15), bg="pink")
            lblName.grid(row=i, column=1)
            lblGender = Label(second_frame, text=user[5], width=6, height=1, font=('Arial', 15), bg="pink")
            lblGender.grid(row=i, column=2)
            lblCity = Label(second_frame, text=user[6], width=15, height=1, font=('Arial', 15), bg="pink")
            lblCity.grid(row=i, column=3)
            i = i + 1

    def logout(self, child):
        messagebox.showinfo("Thanks", "Thanks for playing around")
        self.tinderBackend.logout()
        child.destroy()


obj = TinderGUI()
