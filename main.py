from tkinter import *
from tkinter import messagebox
from datetime import datetime, timedelta

def clicked():
    res1 = " {}".format(txt1.get())
    res2 = " {}".format(txt2.get())
    res3 = " {}".format(txt3.get())
    res4 = " {}".format(txt4.get())

    today = datetime.now().strftime("%d.%m.%Y")
    now = datetime.strptime(today, "%d.%m.%Y")
    birthday = datetime.strptime(res4, " %d.%m.%Y")
    age = now - birthday
    second = age.total_seconds()
    age_second = int(second)
    age_in_years = (age_second / 86400) // 365
    rounded_age = round(age_in_years)
    age_str = str(rounded_age)

    if (rounded_age == 20) or (rounded_age == 45):
        messagebox.showinfo('Замена паспорта', "Здравствуйте," + res1 + res2 + res3 + "." + " На данный момент Вам " + age_str + " лет." + " Если Вы до сих пор не поменяли паспорт, сделайте это в ближайшем МФЦ. Не забудьте оплатить штраф (если просрочено 90 дней).")
    elif (rounded_age < 20):
        age_20 = birthday + timedelta(days=7300)
        date_age_20 = age_20 - now
        second_age_20 = date_age_20.total_seconds()
        age_second_20 = int(second_age_20)
        last_age_20 = (age_second_20 / 86400)
        rounded_age_20 = round(last_age_20)
        age_str_20 = str(rounded_age_20)
        messagebox.showinfo('Замена паспорта', "Здравствуйте," + res1 + res2 + res3 + "." + " На данный момент Вам " + age_str + " лет." + " Через " + age_str_20 + " день Вам необходимо будет обратиться в ближайший МФЦ для замены паспорта. Если вы не поменяете паспорт в течение 90 дней, на Вас будет наложен штраф.")
    elif (rounded_age > 20) and (rounded_age < 45):
        age_45 = birthday + timedelta(days=16425)
        date_age_45 = age_45 - now
        second_age_45 = date_age_45.total_seconds()
        age_second_45 = int(second_age_45)
        last_age_45 = (age_second_45 / 86400)
        rounded_age_45 = round(last_age_45)
        age_str_45 = str(rounded_age_45)
        messagebox.showinfo('Замена паспорта', "Здравствуйте," + res1 + res2 + res3 + "." + " На данный момент Вам " + age_str + " лет." + " Через " + age_str_45 + " день Вам необходимо будет обратиться в ближайший МФЦ для замены паспорта. Если вы не поменяете паспорт в течение 90 дней, на Вас будет наложен штраф.")
    elif (rounded_age > 45):
        messagebox.showinfo('Замена паспорта', "Здравствуйте," + res1 + res2 + res3 + "." + " На данный момент Вам " + age_str + " лет." + " Замена паспорта не требуется.")

window = Tk()
window.title("Замена паспорта")
window.geometry('600x300')

lbl = Label(window, text="")
lbl.grid(column=0, row=0)
lbl = Label(window, text="     Для получении информации о дате получения паспорта Вам необходимо ввести следующие данные.")
lbl.grid(column=0, row=1)
lbl = Label(window, text="")
lbl.grid(column=0, row=2)

lbl1 = Label(window, text="Фамилия")
lbl1.grid(column=0, row=3)
txt1 = Entry(window,width=20)
txt1.grid(column=0, row=4)

lbl2 = Label(window, text="Имя")
lbl2.grid(column=0, row=5)
txt2 = Entry(window,width=20)
txt2.grid(column=0, row=6)

lbl3 = Label(window, text="Отчество")
lbl3.grid(column=0, row=7)
txt3 = Entry(window,width=20)
txt3.grid(column=0, row=8)

lbl4 = Label(window, text="Дата рождения (дд.мм.гггг)")
lbl4.grid(column=0, row=9)
txt4 = Entry(window,width=20)
txt4.grid(column=0, row=10)

lbl = Label(window, text="")
lbl.grid(column=0, row=11)

btn = Button(window, text='Далее', command=clicked)
btn.grid(column=0, row=12)

window.mainloop()