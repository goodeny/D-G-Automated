from tkinter import *
from tkinter import filedialog
import threading
from website import Website

class Interface(Website):
    def __init__(self):
        self.window = Tk()
        self.center(831,554)
        self.window.title("D&G")
        self.window.config(bg=self.colors()['background'])
        self.window.overrideredirect(0)

        #files
        b_open = PhotoImage(file=self.paths()['b_open'])
        b_moment = PhotoImage(file=self.paths()['b_moment'])
        img_upload_image = PhotoImage(file=self.paths()['img_upload'])
        logo = PhotoImage(file=self.paths()['logo'])
        #print(self.load_img())

        #variables
        self.archive = 'Pedido-de-namoro-main/timeline.html'
        self.v_upload_img = False
        self.v_title = False
        self.v_description = False
        self.path_img = ""

        #components
        self.logo(logo)
        self.dg_image(img_upload_image)
        self.label_title()
        self.label_description()
        self.button_open_website(b_open)
        self.button_new_moment(b_moment)
        self.window.mainloop()

    def logo(self, image):
        logo = Label(self.window, bg=self.colors()['background'], image=image)
        logo.place(x=40,y=40)

    def button_open_website(self, image):
        #C:\Users\Goodeny\Desktop\flash\teste\site\components
        button = Button(self.window, 
                image=image, 
                activebackground=self.colors()['background'], 
                background=self.colors()['background'],
                bd=0,
                cursor='hand2',
                command=...
                )
        button.place(x=100, y=350)

    def button_new_moment(self, image):
        button = Button(self.window, 
                image=image, 
                activebackground=self.colors()['background'], 
                background=self.colors()['background'],
                bd=0,
                cursor='hand2',
                command=lambda: threading.Thread(target=self.commit_moment).start()
                )   
        button.place(x=100, y=420)

    def dg_image(self, image):
        label = Button(self.window, 
                bg=self.colors()['label'], 
                bd=0, 
                image=image,
                activebackground=self.colors()['background'],
                command=lambda: threading.Thread(target=self.load_img).start()
                )
        label.place(x=460, y=70)

    def label_title(self):
        self.label_title = Entry(self.window, 
                width=34, 
                font='Arial 13', 
                bg=self.colors()['label'],
                bd=0
                )
        self.label_title.place(x=460, y=260)
    
    def label_description(self):
        self.label_desc = Text(self.window, 
                width=44, 
                height=13, 
                font='Arial 10', 
                bg=self.colors()['label'], 
                bd=0
                )
        self.label_desc.place(x=460, y=290)

    def commit_moment(self):
        import shutil
        import os

        path = f"{os.getcwd()}\Pedido-de-namoro-main\img"
        #C:/Users/Goodeny/Pictures/Sem título.png
        path_img = self.path_img
        t = self.label_title.get()
        d = self.label_desc.get("1.0",END)
        n = None
        try:
            for num, l in enumerate(path_img):
                if l == "/":
                    #print(l, num)
                    n = num
            name_file = path_img[n+1:-1]+path_img[-1]
            shutil.copy(self.path_img, path)
        except:
            pass
        if path_img != "" and t != "" and d != "":
            self.insert(name_file,t,d)
    
    def load_img(self):
        self.filepath = filedialog.askopenfilename(title='Selecionar imagem', filetypes=(("PNG", "*.png"),("JPEG", "*.jpeg")))
        if self.filepath:
            self.path_img = self.filepath
         
    def center(self, w, h):
        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()
        x = (width - w)//2
        y = (height - h)//2
        return self.window.geometry(f"{w}x{h}+{x}+{y}")

    def colors(self):
        COLORS = {
            "background": "#D4C0FF",
            "label": "#D9E3FF"
        }
        return COLORS

    def paths(self):
        PATHS = {
                "b_open": "components/b_open_website.png",
                "b_moment": "components/b_new_moment.png",
                "img_upload": "components/bg_img.png",
                "logo": "components/Logo.png"
                }
        return PATHS