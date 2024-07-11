from tkinter import *
from mydb import Database
from tkinter import messagebox
from myapi import API
class NLPApp:
    def __init__(self):
        #create a db object
        self.dbo = Database()
        self.apio = API()
        #login  ka gui load karna
        self.root = Tk()
        self.root.title('NLPApp')
        self.root.geometry('350x600')
        self.root.configure(bg='#34495E')
        self.login_gui()
        self.root.mainloop()
    def clear(self):
        for _ in self.root.pack_slaves():
            _.destroy()
    
    
    def login_gui(self):
        self.clear()
        heading = Label(self.root,text='NLPApp',bg='#34495E',
              fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        label1 = Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root,text='Enter Password')
        label2.pack(pady=(10,10))

        self.password_input = Entry(self.root,width=50,show='*')
        self.password_input.pack(pady=(5,10),ipady=4)

        login_btn = Button(self.root,text='Login',width=30,height=2,command = self.perform_login)
        login_btn.pack(pady=(10,10))

        label3 = Label(self.root,text="Not a member?")
        label3.pack(pady=(20,10))

        redirect_btn = Button(self.root,text="Register Now",command = self.register_gui)
        redirect_btn.pack(pady=(10,10))
    
    def register_gui(self):
        self.clear()
        heading = Label(self.root,text='NLPApp',bg='#34495E',
              fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        label0 = Label(self.root,text='Enter Name')
        label0.pack(pady=(10,10))

        self.name_input = Entry(self.root,width=50)
        self.name_input.pack(pady=(5,10),ipady=4)

        label1 = Label(self.root,text='Enter Email')
        label1.pack(pady=(10,10))

        self.email_input = Entry(self.root,width=50)
        self.email_input.pack(pady=(5,10),ipady=4)

        label2 = Label(self.root,text='Enter Password')
        label2.pack(pady=(10,10))

        self.password_input = Entry(self.root,width=50,show='*')
        self.password_input.pack(pady=(5,10),ipady=4)

        register_btn = Button(self.root,text='Register',width=30,height=2,command = self.perform_registration)
        register_btn.pack(pady=(10,10))

        label3 = Label(self.root,text="Already a member?")
        label3.pack(pady=(20,10))

        redirect_btn = Button(self.root,text="Login Now",command = self.login_gui)
        redirect_btn.pack(pady=(10,10))

    def perform_registration(self):
        name = self.name_input.get()
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.add_data(name,email,password)

        if response:
           messagebox.showinfo('success','Registration Succesful')

        else:
            messagebox.showerror("error",'Email already exists')


    def perform_login(self):
        email = self.email_input.get()
        password = self.password_input.get()

        response = self.dbo.search(email,password)

        if response:
            messagebox.showinfo('Success','Login Successful')
            self.home_gui()
        else:
            messagebox.showerror('Error','Incorrect email/password')

    
    def home_gui(self):
        self.clear()

        heading = Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        sentiment_btn = Button(self.root,text='Sentiment Analysis',
                               width=30,height=4,command=self.sentiment_gui)
        sentiment_btn.pack(pady=(10,10))

        abuse_btn = Button(self.root,text='Abuse Prediction',
                               width=30,height=4,command=self.abuse_gui)
        abuse_btn.pack(pady=(10,10))

        taxonomy_btn = Button(self.root,text='Taxonomy',
                               width=30,height=4,command=self.taxonomy_gui)
        taxonomy_btn.pack(pady=(10,10))

        logout_btn = Button(self.root,text='Logout',
                               width=30,height=4,command=self.login_gui)
        logout_btn.pack(pady=(10,10))

    def sentiment_gui(self):
        self.clear()

        heading = Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        heading = Label(self.root,text='Sentiment Analysis',bg='#34495E',fg='white')
        heading.pack(pady=(10,20))
        heading.configure(font=('verdana',24))

        label1 = Label(self.root,text='Enter the text')
        label1.pack(pady=(10,10))

        self.sentiment_input = Entry(self.root,width=50)
        self.sentiment_input.pack(pady=(5,10),ipady=4)
       
        sentiment_btn = Button(self.root,text='Analyse Sentiment',
                               command=self.do_sentiment_analysis)
        sentiment_btn.pack(pady=(10,10))

        self.sentiment_result = Label(self.root, text='',bg='#34495E',fg='white')
        self.sentiment_result.pack(pady=(10, 10))
        self.sentiment_result.configure(font=('verdana', 16))


        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10, 10))  

    def do_sentiment_analysis(self):

        text = self.sentiment_input.get()
        result = self.apio.sentiment_analysis(text)

        nested_dict = result['sentiment']
        ans = max(nested_dict,key=nested_dict.get)

        self.sentiment_result['text'] = ans+' mostly'

    def taxonomy_gui(self):
        self.clear()

        heading = Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        heading = Label(self.root,text='Taxonomy',bg='#34495E',fg='white')
        heading.pack(pady=(10,20))
        heading.configure(font=('verdana',24))

        label1 = Label(self.root,text='Enter the text')
        label1.pack(pady=(10,10))

        self.taxonomy_input = Entry(self.root,width=50)
        self.taxonomy_input.pack(pady=(5,10),ipady=4)
       
        taxonomy_btn = Button(self.root,text='Do Taxonomy',
                               command=self.do_taxonomy_analysis)
        taxonomy_btn.pack(pady=(10,10))

        self.taxonomy_result = Label(self.root, text='',bg='#34495E',fg='white')
        self.taxonomy_result.pack(pady=(10, 10))
        self.taxonomy_result.configure(font=('verdana', 16))


        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10, 10))  

    def do_taxonomy_analysis(self):

        text = self.taxonomy_input.get()
        result = self.apio.do_taxonomy(text)

        # Extract the list of entities
        entities = result['taxonomy']

        # Collect the name values
        names = [entity['tag'] for entity in entities]  

        #convert names list to string 

        ans = '\n'.join(names)
        
        
        self.taxonomy_result['text'] = ans


    def abuse_gui(self):
        self.clear()

        heading = Label(self.root,text='NLPApp',bg='#34495E',fg='white')
        heading.pack(pady=(30,30))
        heading.configure(font=('verdana',24,'bold'))

        heading = Label(self.root,text='Abuse Detection',bg='#34495E',fg='white')
        heading.pack(pady=(10,20))
        heading.configure(font=('verdana',24))

        label1 = Label(self.root,text='Enter the text')
        label1.pack(pady=(10,10))

        self.abuse_input = Entry(self.root,width=50)
        self.abuse_input.pack(pady=(5,10),ipady=4)
       
        abuse_btn = Button(self.root,text='Detect Abuse',
                               command=self.do_abuse_analysis)
        abuse_btn.pack(pady=(10,10))

        self.abuse_result = Label(self.root, text='',bg='#34495E',fg='white')
        self.abuse_result.pack(pady=(10, 10))
        self.abuse_result.configure(font=('verdana', 16))


        goback_btn = Button(self.root, text='Go Back', command=self.home_gui)
        goback_btn.pack(pady=(10, 10))  

    def do_abuse_analysis(self):

        text = self.abuse_input.get()
        result = self.apio.abuse_detection(text)

        ans = max(result,key=result.get)

        self.abuse_result['text'] = 'it is '+ans
    


        




nlp = NLPApp()     