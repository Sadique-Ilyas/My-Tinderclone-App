from tkinter import messagebox, Tk, Label, Button, Entry, Toplevel

from tinderBackend import *


class TinderGUI:
    def __init__(self):
        self.root = Tk()
        self.root.title("Tinder App")
        self.root.maxsize(1366, 768)
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
            child.maxsize(800, 600)
            child['bg'] = 'Pink'

            lblLogin = Label(child, text="   Email:", width=12, height=1, font=('Arial', 15), bg='pink')
            lblLogin.grid(row=0, column=0)
            entEmail = Entry(child, width=29, font=('Arial', 20))
            entEmail.grid(row=0, column=1)

            lblPassword = Label(child, text="   Password:", width=20, height=1, font=('Arial', 14), bg='pink')
            lblPassword.grid(row=1, column=0)
            entPassword = Entry(child, width=29, font=('Arial', 20))
            entPassword.grid(row=1, column=1)

            btnLogin = Button(child, text="Login", width=7, height=1, bg='light blue', font=('Arial', 15),
                              command=lambda: self.validate(child, entEmail.get(), entPassword.get()))
            btnLogin.grid(row=3, column=1)

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
        child.maxsize(800, 600)
        child['bg'] = 'Pink'

        lblName = Label(child, text="Name:", width=8, height=1, font=('Arial', 15))
        lblName.grid(row=0, column=0)
        entName = Entry(child, width=30, font=('Arial', 20))
        entName.grid(row=0, column=1)

        lblGender = Label(child, text="Gender:", width=8, height=1, font=('Arial', 15))
        lblGender.grid(row=1, column=0)
        entGender = Entry(child, width=30, font=('Arial', 20))
        entGender.grid(row=1, column=1)

        lblCity = Label(child, text="City:", width=8, height=1, font=('Arial', 15))
        lblCity.grid(row=2, column=0)
        entCity = Entry(child, width=30, font=('Arial', 20))
        entCity.grid(row=2, column=1)

        lblEmail = Label(child, text="Email:", width=8, height=1, font=('Arial', 15))
        lblEmail.grid(row=3, column=0)
        entEmail = Entry(child, width=30, font=('Arial', 20))
        entEmail.grid(row=3, column=1)

        lblPassword = Label(child, text="Password:", width=8, height=1, font=('Arial', 15))
        lblPassword.grid(row=4, column=0)
        entPassword = Entry(child, width=30, font=('Arial', 20))
        entPassword.grid(row=4, column=1)

        btnRegister = Button(child, width=8, height=2, text="Register", font=('Arial', 20),
                             command=lambda: self.addUser(child, entName.get(), entGender.get(), entCity.get(),
                                                          entEmail.get(), entPassword.get()))
        btnRegister.grid(row=5, column=1)

    def addUser(self, child, name, gender, city, email, password):
        self.tinderBackend.userRegister(name, gender, city, email, password)
        messagebox.showinfo('Success', 'Registration Successful !')
        child.destroy()

    def showUserMenu(self):
        child = Toplevel(self.root)
        child.title("User Window")
        child.maxsize(800, 600)
        child['bg'] = 'Pink'

        username = self.tinderBackend.fetchUserName()

        lblWelcome = Label(child, width=30, height=1, text=("Welcome %s !" % username[0][0]), bg='pink',
                           font=('Arial', 15))
        lblWelcome.grid(row=0, column=0, pady=10)

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
        child['bg'] = 'Pink'

        userlist = self.tinderBackend.viewAllUsers()

        lblWelcome = Label(child, text="User List", width=35, height=3, font=('Courier,16'), bg="pink", padx=15, pady=5)
        lblWelcome.grid(row=0, column=0)

        lblgender = Label(child, text="Gender", width=35, height=3, font=('Courier,16'), bg="pink", padx=15, pady=5)
        lblgender.grid(row=0, column=1)

        lblcity = Label(child, text="City", width=35, height=3, font=('Courier,16'), bg="pink", padx=15, pady=5)
        lblcity.grid(row=0, column=2)

        i = 1
        k = 0
        for user in userlist:
            if user[0] != self.tinderBackend.currentUserId:
                lblName = Label(child, text=user[1], width=15, height=1, font=('Arial', 15), padx=15, pady=5, bg="pink")
                lblName.grid(row=i, column=0)
                lblGender = Label(child, text=user[2], width=6, height=1, font=('Arial', 15), padx=15, pady=5,
                                  bg="pink")
                lblGender.grid(row=i, column=1)
                lblCity = Label(child, text=user[3], width=15, height=1, font=('Arial', 15), padx=15, pady=5, bg="pink")
                lblCity.grid(row=i, column=2)
                if (self.tinderBackend.checkPropose(user[0])):
                    btnPropose = Button(child, text="Propose", width=8, height=1, font=('Arial', 15), bg="light blue",
                                        padx=15, pady=5,
                                        command=lambda k=i: self.sendProposal(userlist[k - 1][0]))
                    btnPropose.grid(row=i, column=3)
            i = i + 1

    def sendProposal(self, userid):
        self.tinderBackend.propose(userid)
        messagebox.showinfo("Sent", " Proposal Sent ")

    def viewSent(self):
        child = Toplevel(self.root)
        child.title("Sent Proposals List")
        child.maxsize(1366, 768)
        child['bg'] = 'Pink'

        userlist = self.tinderBackend.viewSentProposals()
        lblWelcome = Label(child, text="Crush List", width=35, height=3, font=('Courier,16'), bg="pink")
        lblWelcome.grid(row=0, column=0)

        lblname = Label(child, text="Name", width=35, height=3, font=('Courier,16'), bg="pink", padx=15, pady=5)
        lblname.grid(row=0, column=1)

        lblgender = Label(child, text="Gender", width=35, height=3, font=('Courier,16'), bg="pink", padx=15, pady=5)
        lblgender.grid(row=0, column=2)

        lblcity = Label(child, text="City", width=35, height=3, font=('Courier,16'), bg="pink", padx=15, pady=5)
        lblcity.grid(row=0, column=3)

        i = 1
        for user in userlist:
            lblId = Label(child, text=user[3], width=2, height=1, font=('Arial', 15), bg="pink")
            lblId.grid(row=i, column=0)
            lblName = Label(child, text=user[4], width=15, height=1, font=('Arial', 15), bg="pink")
            lblName.grid(row=i, column=1)
            lblGender = Label(child, text=user[5], width=6, height=1, font=('Arial', 15), bg="pink")
            lblGender.grid(row=i, column=2)
            lblCity = Label(child, text=user[6], width=15, height=1, font=('Arial', 15), bg="pink")
            lblCity.grid(row=i, column=3)
            i = i + 1

    def viewReceived(self):
        child = Toplevel(self.root)
        child.title("Received List")
        child.maxsize(1366, 768)
        child['bg'] = 'Pink'

        userlist = self.tinderBackend.viewReceivedProposals()
        lblWelcome = Label(child, text="Fan List", width=35, height=3, font=('Courier,16'), bg="pink")
        lblWelcome.grid(row=0, column=0)

        lblname = Label(child, text="Name", width=35, height=3, font=('Courier,16'), bg="pink", padx=15, pady=5)
        lblname.grid(row=0, column=1)

        lblgender = Label(child, text="Gender", width=35, height=3, font=('Courier,16'), bg="pink", padx=15, pady=5)
        lblgender.grid(row=0, column=2)

        lblcity = Label(child, text="City", width=35, height=3, font=('Courier,16'), bg="pink", padx=15, pady=5)
        lblcity.grid(row=0, column=3)

        i = 1
        for user in userlist:
            lblId = Label(child, text=user[3], width=2, height=1, font=('Arial', 15), bg="pink")
            lblId.grid(row=i, column=0)
            lblName = Label(child, text=user[4], width=15, height=1, font=('Arial', 15), bg="pink")
            lblName.grid(row=i, column=1)
            lblGender = Label(child, text=user[5], width=6, height=1, font=('Arial', 15), bg="pink")
            lblGender.grid(row=i, column=2)
            lblCity = Label(child, text=user[6], width=15, height=1, font=('Arial', 15), bg="pink")
            lblCity.grid(row=i, column=3)
            i = i + 1

        lPropose = Label(child, text="Enter the ID",
                         width=25, height=2, font=('Arial', 12), bg="pink").grid(row=i, column=0, columnspan=2)
        entPropose = Entry(child, width=4, font=('Arial', 14))
        entPropose.grid(row=i, column=2)
        btnPropose = Button(child, text="Propose", width=10, height=2,
                            font=('Arial', 12), bg='light blue',
                            command=lambda: self.sendProposal(entPropose.get())).grid(row=i, column=3)

    def viewMatches(self):
        child = Toplevel(self.root)
        child.title("Matches List")
        child.maxsize(1366, 768)
        child['bg'] = 'Pink'

        userlist = self.tinderBackend.viewMatches()
        lblWelcome = Label(child, text="Match List", width=35, height=3, font=('Courier,16'), bg="pink")
        lblWelcome.grid(row=0, column=0)

        lblname = Label(child, text="Name", width=35, height=3, font=('Courier,16'), bg="pink", padx=15, pady=5)
        lblname.grid(row=0, column=1)

        lblgender = Label(child, text="Gender", width=35, height=3, font=('Courier,16'), bg="pink", padx=15, pady=5)
        lblgender.grid(row=0, column=2)

        lblcity = Label(child, text="City", width=35, height=3, font=('Courier,16'), bg="pink", padx=15, pady=5)
        lblcity.grid(row=0, column=3)

        i = 1
        for user in userlist:
            lblId = Label(child, text=user[3], width=2, height=1, font=('Arial', 15), bg="pink")
            lblId.grid(row=i, column=0)
            lblName = Label(child, text=user[4], width=15, height=1, font=('Arial', 15), bg="pink")
            lblName.grid(row=i, column=1)
            lblGender = Label(child, text=user[5], width=6, height=1, font=('Arial', 15), bg="pink")
            lblGender.grid(row=i, column=2)
            lblCity = Label(child, text=user[6], width=15, height=1, font=('Arial', 15), bg="pink")
            lblCity.grid(row=i, column=3)
            i = i + 1

    def logout(self, child):
        messagebox.showinfo("Thanks", "Thanks for playing around")
        self.tinderBackend.logout()
        child.destroy()


obj = TinderGUI()
