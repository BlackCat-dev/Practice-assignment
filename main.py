from tkinter import *
from tkinter import messagebox as mb
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
from csv import DictReader
import _thread
import send_mail_f
import login
import pandas as pd
import numpy as np
import re
from re import findall
from bs4 import BeautifulSoup
import requests

try:
    f = open('logs.csv','r')
    d = f.read(1024)
    f.close()
    if d != '':
        pass
    else:
        login.login()
except:
    login.login()



def main_loop():
    
    f = open('logs.csv','r')
    r = DictReader(f)
    global username
    global password
    global mail_list
    mail_list = []
    for i in r:
        username = i['username']
        password = i['password']
    f.close()
        



    def logout_func():
        f = open('logs.csv','w')
        f.write('')
        win.destroy()




    def vald_email():
        to = to_e.get()
        subject = subject_e.get()
        message = mail_text.get(1.0,END)
        if '@' in to:
            try:
                send_mail_f.send_mail(username,password,to,subject,message)
                mb.showinfo('Отправлено',f'Электронное письмо успешно отправлено на {to}')
            except:
                mb.showerror('Ошибка подключения','Не удается подключиться к Интернету. Пожалуйста, проверьте свое подключение к Интернету.')
        else:
            mb.showerror('Ошибка','Неверный адрес электронной почты')



    def send_mul_mail_loop():
        to = to_e.get()
        subject = subject_e.get()
        message = mail_text.get(1.0,END)

        ##----------------------------------------------------------------
        ## Блок для тестирования
        ##----------------------------------------------------------------
        try:
            emails_test = 'eamdestiny@gmail.com, Egor.Gologuzov@urfu.me'
            emails_test = str(emails_test)
            emails_test = emails_test.split(", ")
            mail_list_test = []
            mail_list_test.append(emails_test)
        ##----------------------------------------------------------------
        ## Блок для тестирования
        ##----------------------------------------------------------------
            for mail in mail_list_test:
                send_mail_f.send_mail(username,password,mail,subject,message)
            mb.showinfo('Отправлено',f'Электронное письмо успешно отправлено {len(emails_test)} пользователям')
        except:
            mb.showerror('Ошибка подключения','Не удается подключиться к Интернету. Пожалуйста, проверьте свое подключение к Интернету.')



    def send_mul_mail():
        try:        
            _thread.start_new_thread(send_mul_mail_loop,())
        except:
            mb.showerror('Ошибка','Пожалуйста, прикрепите файл с таблицей, содержащий ссылки. Для получения дополнительной помощи обратитесь к кнопке "О приложении".')





    def exs_func():
        try:
            filename = askopenfilename()
            try:
                df = pd.read_excel(filename)
                link1 = df['Ссылки'].tolist()
                link2 = df['ССЫЛКА1'].tolist()
                link3 = df['ССЫЛКА2'].tolist()
                link = link1 + link2 + link3
                links = str(link)
                links = links.replace("'", " '")
                urls = re.findall(r'(https?://[^\s]+)', links)
                email =r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
                for url in urls:
                    r = requests.get(url, allow_redirects=False)
                    soup = BeautifulSoup(r.text, 'html.parser')
                    emails = soup.find_all(text=re.compile(email))
                    for mail in emails:
                        mail_list.append(mail)
                mb.showinfo('Информация',f'Найденные адреса электронной почты: {mail_list} ')
            except:
                mb.showerror('Ошибка','Ошибка при чтении файла с таблицей. Пожалуйста, обратитесь за помощью к кнопке "Информация".')
        except:
            pass





    def about_func():
        mb.showinfo('About', 'С помощью этого приложения можно отправлять письма на другие почтовые адреса.'
        '[Кнопка - Написать письмо]'
        'А также, обрабатывать таблицы - извлекать необходимые данные и отправлять письмо.'
        '[Кнопка - отправить с использованием таблицы]')




    def mul_mail_func():
        ## Log Bg
        log_bg.place(x=1000)
        log_img.place(x=1000)
        log_in_as.place(x=1000)
        name.place(x=1000)

        ## Menu Options
        menu_bg.place(x=1000)
        mail_b.place(x=1000)
        mul_mail_b.place(x=1000)
        about_b.place(x=1000)
        cl_l.place(x=1000)
        logout_b.place(x=1000)

        ## Plus Button
        plus_button.place(x=1000)

        ## Compose Email
        header_l.place(x=20,y=50)
        to_l.place(x=40,y=120)

        ## To
        to_e.place(x=1000)

        ## Exs
        exs_b.place(x=90,y=120)
        exs_ab.place(x=310,y=110)

        
        subject_l.place(x=40,y=170)
        subject_e.place(x=90,y=170)
        mail_text.place(x=40,y=220)
        send_b.place(x=280,y=440)
        cancel_b.place(x=360,y=440)

        send_b['command'] = send_mul_mail





    def home_func():
        ## Log Bg
        log_bg.place(x=0,y=30)
        log_img.place(x=50,y=60)
        log_in_as.place(x=180,y=60)
        name.place(x=180,y=100)

        ## Menu Options
        menu_bg.place(x=0,y=32)
        mail_b.place(x=10,y=200)
        mul_mail_b.place(x=10,y=270)
        about_b.place(x=10,y=340)
        cl_l.place(x=173,y=385)
        logout_b.place(x=10,y=410)

        ## Plus Button
        plus_button.place(x=370,y=420)

        ## Compose Email
        header_l.place(x=1000)
        to_l.place(x=1000)
        to_e.place(x=1000)
        subject_l.place(x=1000)
        subject_e.place(x=1000)
        mail_text.place(x=1000)
        send_b.place(x=1000)
        cancel_b.place(x=1000)

        ##Mul_mail
        exs_ab.place(x=1000)
        exs_b.place(x=1000)

        

    def email_func():
        ## Log Bg
        log_bg.place(x=1000)
        log_img.place(x=1000)
        log_in_as.place(x=1000)
        name.place(x=1000)

        ## Menu Options
        menu_bg.place(x=1000)
        mail_b.place(x=1000)
        mul_mail_b.place(x=1000)
        about_b.place(x=1000)
        cl_l.place(x=1000)
        logout_b.place(x=1000)

        ## Plus Button
        plus_button.place(x=1000)

        ## Compose Email
        header_l.place(x=20,y=50)
        to_l.place(x=40,y=120)
        to_e.place(x=90,y=120)
        subject_l.place(x=40,y=170)
        subject_e.place(x=90,y=170)
        mail_text.place(x=40,y=220)
        send_b.place(x=280,y=440)
        cancel_b.place(x=360,y=440)
        send_b['command'] = vald_email
        exs_ab.place(x=1000)


    bg = 'royal blue'

    win = Tk()
    win.geometry('450x487')
    win.resizable(0,0)
    win.title('Почта')

    Label(win, text='',bg=bg,width=450,font=('arial black',15,'bold'),relief='groove').pack()
    Label(win, text='Почта',bg=bg,fg='white',font=('arial black',12,'bold')).place(x=350,y=3)

    home_img = PhotoImage(file='resources/home.png')
    Button(win, image=home_img,bg=bg,bd=0,command=home_func).place(x=8,y=3)


    plus_img = PhotoImage(file='resources/plus2.png') 
    plus_button = Button(win, image=plus_img,bd=0,command=email_func)




    ## Меню

    menu_bg = Label(win, text='',bg=bg,width=15,font=('arial black',15,'bold'),relief='groove',height=25)
    log_bg = Label(win,bg=bg,width=50,height=9,relief='groove')
    login_img =PhotoImage(file='resources/login.png')
    log_img = Label(win,image=login_img,bg=bg)
    log_in_as = Label(win, text='Вы вошли в систему как : ',bg=bg,font=('',16),fg='white')
    name = Label(win, text=username,bg=bg,font=('',15,'bold'),fg='white')
    if len(username) > 25:
        name['font'] = ('',14,'bold')
    mail_img = PhotoImage(file='resources/mail.png')
    mail_b = Button(win, image=mail_img, bg=bg,bd=0,text='\n     Написать письмо    \n',compound='left',fg='black',font=('arial black',10,'bold'),command=email_func)
    mul_mail_img = PhotoImage(file='resources/ms-excel.png')
    mul_mail_b = Button(win, image=mul_mail_img, bg=bg,bd=0,text=' Отправить\n   с использованием    \n таблицы',compound='left',fg='black',font=('arial black',10,'bold'),command=mul_mail_func)
    about_img = PhotoImage(file='resources/about.png')
    about_b = Button(win, image=about_img, bg=bg,bd=0,text='\n       О приложении      \n',compound='left',fg='black',font=('arial black',10,'bold'),command=about_func)
    logout_img = PhotoImage(file='resources/logout-24.png')
    logout_b = Button(win, image=logout_img, bg=bg,bd=0,text='\n               Выйти              \n',compound='left',fg='black',font=('arial black',10,'bold'),command=logout_func)

    cl_l = Label(win, text='Нажмите кнопку\n + \nчтобы отправить\n электронное письмо.',fg='#c8c8c8',font=('arial black',15,'bold'))




    ## Написать электронное письмо
    
    header_l = Label(win, text='Написать электронное письмо',font=('Cambria',20))
    to_l = Label(win, text='Кому : ',font=('Cambria',15))
    to_e = Entry(win, font=('Cambria',15),width=30)
    subject_l = Label(win, text='Тема : ',font=('Cambria',15))
    subject_e = Entry(win, font=('Cambria',15),width=30)
    mail_text = Text(win,wrap=WORD, font=('Cambria',13),height=10,width=43,bg='ghost white')
    send_b = Button(win, text='Отправить',bg='white',fg='black',bd=0, font=('Cambria',13),command=vald_email)
    cancel_b = Button(win, text='Назад',bg='white',fg='black',bd=0, font=('Cambria',13),command=home_func)
    exs_b = Button(win,  text='Прикрепите файл с таблицей',bd=2, font=('Cambria',13),command=exs_func)
    about2_img = PhotoImage(file='resources/about (2).png')
    exs_ab = Button(win, image=about2_img,bd=0,command=lambda : mb.showinfo('Информация', f'Выберите файл с таблицей, где присутствуют столбцы с ссылками на сайты. На этих страницах будут найдены необходимые почтовые адреса.'))





    home_func()

    win.mainloop()


main_loop()

