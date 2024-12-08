from tkinter import *
from pymsgbox import confirm
from pymsgbox import alert
from sqlite_code import *
from re import fullmatch
from main import CheckPattern
class SchoolSystem:
    def __init__(self,root,db,dbt,dbs,dbr):
        self.root = root
        self.db = db
        self.dbt = dbt
        self.dbs = dbs
        self.dbr = dbr
        self.root.title('صفحه خدمات')
        self.root.geometry('1350x760')

        self.lable = Label(master=self.root,text='صفحه خدمات',font=('IranSans',37),bd=12,bg='#047478',fg='white',relief=RIDGE,height=2)
        self.lable.pack(fill='x')
        self.lable_stu = Label(master=self.root,text='خدمات فرهنگیان/دانش آموزان',font=('IranSans',20),
                               bd=12,bg='#047478',fg='white',relief=RIDGE,width=40,height=2)
        self.lable_stu.place(x=5,y=150)
        self.lable_mas = Label(master=self.root,text='خدمات مدیران',font=('IranSans',20),
                               bd=12,bg='#047478',fg='white',relief=RIDGE,width=40,height=2)
        self.lable_mas.place(x=680,y=150)

        self.but_lable_teach = Button(master=root,text='ورود فرهنگیان',font=('IranSans',15),
                                      bg='#047478',fg='white',width=30,pady=15,command=self.TeachPage)
        self.but_lable_teach.place(x=155,y=300)
        self.but_lable_stu = Button(master=root,text='ورود دانش آموزان',font=('IranSans',15),
                                    bg='#047478',fg='white',width=30,pady=15,command=self.StudentPage)
        self.but_lable_stu.place(x=155,y=400)
        self.but_lable_mas = Button(master=self.root, text='ورود مدیران', font=('IranSans', 15),
                                    bg='#047478',fg='white',width=30,pady=15,command=self.MasterPage)
        self.but_lable_mas.place(x=840,y=300)
        self.but_exit = Button(master=root,text='خروج',font=('IranSans',15),
                               bg='#047478',fg='white',width=20,pady=10,command=lambda:self.exit(root))
        self.but_exit.place(x=5,y=650)
    def MasterPage(self):
        self.rot = Tk()
        self.rot.title('صفحه ثبت نام')
        self.rot.geometry('1350x760')

        self.lable_master = Label(master=self.rot,text='صفحه ثبت نام',font=('IranSans',37),bd=12,bg='#047478',fg='white',relief=RIDGE,height=2)
        self.lable_master.pack(fill='x')
        self.label_name = Label(master=self.rot,text=':لطفا نام و نام خانوادگی خود را وارد کنید',
                                font=('IranSans',20),bd=12,bg='#047478',fg='white')
        self.label_name.place(x=480,y=170)
        self.label_num_mas = Label(master=self.rot,text=':لطفا کد پرسنلی خود را وارد کنید',
                                  font=('IranSans',20),bd=12,bg='#047478',fg='white')
        self.label_num_mas.place(x=550,y=330)

        self.entry_name = Entry(master=self.rot,width=22,font=('IranSans',25),justify='right')
        self.entry_name.place(x=480,y=250)
        self.entry_num_mas = Entry(master=self.rot,width=22,font=('IranSans',25))
        self.entry_num_mas.place(x=480,y=410)

        self.but_register = Button(master=self.rot,text='ثبت نام',font=('IranSans',15),bg='#047478',fg='white',width=20,
                               pady=10,command=self.register_master)
        self.but_register.place(x=570,y=500)
        self.but_come = Button(master=self.rot,text='ورود',font=('IranSans',15),bg='#047478',fg='white',width=20,
                               pady=10,command=self.login_master)
        self.but_come.place(x=1110,y=650)
        self.but_exit = Button(master=self.rot,text='خروج',font=('IranSans',15),bg='#047478',fg='white',width=20,
                               pady=10,command=lambda:self.exit(self.rot))
        self.but_exit.place(x=5,y=650)
    def register_master(self):
        name = self.entry_name.get()
        num_mas = self.entry_num_mas.get()
        if name == '' or num_mas == '':
            alert('اطلاعات کافی نیست','ناموفق')
        elif self.check_num(num_mas) is False:
            alert('اطلاعات نادرست است','ناموفق')
        else:
            result = self.db.select_db(num_master=num_mas)
            if result is not None:
                if result[0] == name:
                    alert('شما قبلا ثبت نام کرده اید','موفقیت')
                else:
                    alert('اطلاعات نادرست است','ناموفق')
            else:
                self.db.insert_db(name=name,num_master=num_mas)
                alert('ثبت نام با موفقیت انجام شد','موفقیت')
    def login_master(self):
        name = self.entry_name.get()
        num_mas = self.entry_num_mas.get()
        master = self.db.select_db(num_master=num_mas)
        if name == '' or num_mas == '':
            alert('اطلاعات کافی نیست','ناموفق')
        elif self.check_num(num_mas) is False:
            alert('اطلاعات نادرست است','ناموفق')
        else:
            if master is not None:
                if master[0] == name:
                    alert(f'{name} خوش آمدید','موفقیت')
                    self.regis_teach_stu()
                else:
                    alert('کاربری یافت نشد','ناموفق')
            else:
                alert('کاربری یافت نشد','ناموفق')
        self.rot.mainloop()
    def regis_teach_stu(self):
        self.ot = Tk()
        self.ot.title('صفحه ورود')
        self.ot.geometry('1350x760')

        self.lable = Label(master=self.ot,text='صفحه ورود',font=('IranSans',37),bd=12,bg='#047478',fg='white',relief=RIDGE,height=2)
        self.lable.pack(fill='x')
        self.lable_stu = Label(master=self.ot,text='ثبت نام دانش آموزان',font=('IranSans',20),
                               bd=12,bg='#047478',fg='white',relief=RIDGE,width=40,height=2)
        self.lable_stu.place(x=5,y=150)
        self.lable_teacher = Label(master=self.ot,text='ثبت نام فرهنگیان',font=('IranSans',20),
                               bd=12,bg='#047478',fg='white',relief=RIDGE,width=40,height=2)
        self.lable_teacher.place(x=680,y=150)
        self.label_name_stud = Label(master=self.ot,text=':لطفا نام و نام خانوادگی دانش آموز را وارد کنید',font=('IranSans',20),
                                    bd=12,bg='#047478',fg='white')
        self.label_name_stud.place(x=130,y=280)
        self.label_numstud = Label(master=self.ot,text=':لطفا شماره دانش آموزی دانش آموز را وارد کنید',font=('IranSans',20),
                                  bd=12,bg='#047478',fg='white')
        self.label_numstud.place(x=120,y=400)
        self.label_nameteach = Label(master=self.ot,text=':لطفا نام و نام خانوادگی دبیر را وارد کنید',
                                font=('IranSans',20),bd=12,bg='#047478',fg='white')
        self.label_nameteach.place(x=830,y=280)
        self.label_numteach = Label(master=self.ot,text=':لطفا شماره پرسنلی دبیر را وارد کنید',
                                    font=('IranSans',20),bd=12,bg='#047478',fg='white')
        self.label_numteach.place(x=870,y=400)

        self.entry_name_stud = Entry(master=self.ot,width=22, font=('IranSans',25),justify='right')
        self.entry_name_stud.place(x=180,y=350)
        self.entry_numstud = Entry(master=self.ot,width=22, font=('IranSans',25))
        self.entry_numstud.place(x=180,y=470)
        self.entry_nameteach = Entry(master=self.ot,width=22,font=('IranSans',25),justify='right')
        self.entry_nameteach.place(x=830,y=350)
        self.entry_numteach = Entry(master=self.ot,width=22,font=('IranSans',25))
        self.entry_numteach.place(x=835,y=470)
        
        self.but_rgiteach = Button(master=self.ot,text='ثبت نام',font=('IranSans',15),bg='#047478',fg='white',width=15,
                                   pady=10,command=self.regis_teach)
        self.but_rgiteach.place(x=850,y=550)
        self.but_rgistu = Button(master=self.ot,text='ثبت نام',font=('IranSans',15),bg='#047478',fg='white',width=15,
                               pady=10,command=self.regis_stu)
        self.but_rgistu.place(x=200,y=550)
        self.but_exit = Button(master=self.ot,text='خروج',font=('IranSans',15),bg='#047478',fg='white',width=13,
                               pady=10,command=lambda:self.exit(self.ot))
        self.but_exit.place(x=5,y=650)
    def regis_teach(self):
        name_t = self.entry_nameteach.get()
        num_t = self.entry_numteach.get()
        if name_t == '' or num_t == '':
            alert('اطلاعات کافی نیست','ناموفق')
        elif self.check_num(num_t) is False:
            alert('اطلاعات نادرست است','ناموفق')
        else:
            res = self.dbt.select_dbt(num_teach=num_t)
            if res is not None:
                if res[0] == name_t:
                    alert('شما قبلا ثبت نام کرده اید','موفقیت')
                else:
                    alert('اطلاعات نادرست است','ناموفق')
            else:
                self.dbt.insert_dbt(name_teach=name_t,num_teach=num_t)
                alert('ثبت نام با موفقیت انجام شد','موفقیت')
    def regis_stu(self):
        name_s = self.entry_name_stud.get()
        num_s = self.entry_numstud.get()
        if name_s == '' or num_s == '':
            alert('اطلاعات کافی نیست','ناموفق')
        elif self.check_num_stu(num_s) is False:
            alert('اطلاعات نادرست است','ناموفق')
        else:
            res = self.dbs.select_dbs(num_stu=num_s)
            if res is not None:
                if res[0] == name_s:
                    alert('شما قبلا ثبت نام کرده اید','موفقیت')
                else:
                    alert('اطلاعات نادرست است','ناموفق')
            else:
                self.dbs.insert_dbs(name_stu=name_s,num_stu=num_s)
                alert('ثبت نام با موفقیت انجام شد','موفقیت')
        self.ot.mainloop()
    def TeachPage(self):
        self.rt = Tk()
        self.rt.title('صفحه ثبت نام')
        self.rt.geometry('1350x760')

        self.lable_teach = Label(master=self.rt,text='صفحه ثبت نام',font=('IranSans',37),bd=12,bg='#047478',fg='white',relief=RIDGE,height=2)
        self.lable_teach.pack(fill='x')
        self.label_name_teach = Label(master=self.rt,text=':لطفا نام و نام خانوادگی خود را وارد کنید',
                                font=('IranSans',20),bd=12,bg='#047478',fg='white')
        self.label_name_teach.place(x=480,y=170)
        self.label_num_teach = Label(master=self.rt,text=':لطفا شماره پرسنلی خود را وارد کنید',
                                    font=('IranSans',20),bd=12,bg='#047478',fg='white')
        self.label_num_teach.place(x=520,y=330)

        self.entry_name_teach = Entry(master=self.rt,width=22,font=('IranSans',25))
        self.entry_name_teach.place(x=480,y=250)
        self.entry_num_teach = Entry(master=self.rt,width=22,font=('IranSans',25))
        self.entry_num_teach.place(x=480,y=410)

        self.but_come_teach = Button(master=self.rt,text='ورود',font=('IranSans',15),bg='#047478',fg='white',width=20,
                               pady=10,command=self.log_teach)
        self.but_come_teach.place(x=1110,y=650)
        self.but_exit_teach = Button(master=self.rt,text='خروج',font=('IranSans',15),bg='#047478',fg='white',width=20,
                               pady=10,command=lambda:self.exit(self.rt))
        self.but_exit_teach.place(x=5,y=650)
    def log_teach(self):
        name = self.entry_name_teach.get()
        number = self.entry_num_teach.get()
        teach = self.dbt.select_dbt(num_teach=number)
        if name == '' or number == '':
            alert('اطلاعات کافی نیست','ناموفق')
        elif self.check_num(number) is False:
            alert('اطلاعات نادرست است','ناموفق')
        else:
            if teach is not None:
                if teach[0] == name:
                    alert(f'{name} خوش آمدید','موفقیت')
                    self.regis_report()
                else:
                    alert('کاربری یافت نشد','ناموفق')
            else:
                alert('کاربری یافت نشد','ناموفق')
        self.rt.mainloop()
    def regis_report(self):
        self.report = Tk()
        self.report.title('صفحه ثبت کارنامه')
        self.report.geometry('1350x760')

        self.lable = Label(master=self.report,text='نام و نام خانوادگی دانش آموز',font=('IranSans',20),bd=12,bg='#047478',fg='White')
        self.lable.place(x=1000,y=50)
        self.lable_num = Label(master=self.report,text='شماره دانش آموزی دانش آموز',font=('IranSans',20),bd=12,bg='#047478',fg='white')
        self.lable_num.place(x=350,y=50)
        self.lable_m = Label(master=self.report,text='ریاضی',font=('IranSans',20),bd=12,bg='#047478',fg='white')
        self.lable_m.place(x=1200,y=250)
        self.lable_p = Label(master=self.report,text='فارسی',font=('IranSans',20),bd=12,bg='#047478',fg='white')
        self.lable_p.place(x=1210,y=350)
        self.lable_s = Label(master=self.report,text='علوم',font=('IranSans',20),bd=12,bg='#047478',fg='white')
        self.lable_s.place(x=1220,y=450)
        self.lable_q = Label(master=self.report,text='قرآن',font=('IranSans',20),bd=12,bg='#047478',fg='white')
        self.lable_q.place(x=1230,y=550)

        self.entry = Entry(master=self.report,width=13,font=('IranSans',30))
        self.entry.place(x=680,y=50)
        self.entry_num = Entry(master=self.report,width=13,font=('IranSans',30))
        self.entry_num.place(x=20,y=50)
        self.entry_m = Entry(master=self.report,width=10,font=('IranSans',30))
        self.entry_m.place(x=930,y=250)
        self.entry_p = Entry(master=self.report,width=10,font=('IranSans',30))
        self.entry_p.place(x=930,y=350)
        self.entry_s = Entry(master=self.report,width=10,font=('IranSans',30))
        self.entry_s.place(x=930,y=450)
        self.entry_q = Entry(master=self.report,width=10,font=('IranSans',30))
        self.entry_q.place(x=930,y=550)

        self.button = Button(master=self.report,text='ثبت نام',font=('IranSans',15),bg='#047478',fg='white',width=20,
                                     pady=10,command=self.login_report)
        self.button.place(x=1110,y=650)
        self.but_exit = Button(master=self.report,text='خروج',font=('IranSans',15),bg='#047478',fg='white',width=20,
                                     pady=10,command=lambda:self.exit(self.report))
        self.but_exit.place(x=5,y=650)
    def login_report(self):
        stu = self.entry.get()
        code = self.entry_num.get()
        math = self.entry_m.get()
        pers = self.entry_p.get()
        scin = self.entry_s.get()
        qur = self.entry_q.get()
        stud = self.dbs.select_dbs(num_stu=code)
        rpo = self.dbr.select_dbr(nation_code=code)
        if stu == '' or code == '' or math == '' or pers == '' or scin == '' or qur == '':
            alert('اطلاعات کافی نیست','ناموفق')
        elif self.check_num_stu(code) is False:
            alert('اطلاعات نادرست است','ناموفق')
        elif rpo is not None:
            if rpo[0] == stu:
                alert('کارنامه ی این دانش آموز قبلا ثبت شده است','ناموفق')
            else:
                alert('اطلاعات نادرست است','ناموفق')
        else:
            if self.check_number(math) and self.check_number(pers) and self.check_number(scin) and self.check_number(qur) is True:
                if stud is not None:
                    if stud[0] == stu:
                        rep = self.dbr.insert_dbr(name=stu,nation_code=code,math=math,persian=pers,science=scin,quran=qur)
                        alert(f'کارنامه ی {stu} با موفقیت ثبت شد','موفقیت')
                    else:
                        alert('کاربری یافت نشد','ناموفق')
                else:
                    alert('کاربری یافت نشد','ناموفق')
            else:
                alert('اطلاعات نادرست است', 'ناموفق')
        self.report.mainloop()
    def StudentPage(self):
        self.ro = Tk()
        self.ro.title('صفحه ثبت نام')
        self.ro.geometry('1350x760')

        self.lable_student = Label(master=self.ro,text='صفحه ثبت نام',font=('IranSans',37),bd=12,bg='#047478',fg='white',relief=RIDGE,height=2)
        self.lable_student.pack(fill='x')
        self.label_name_stu = Label(master=self.ro,text=':لطفا نام و نام خانوادگی خود را وارد کنید',font=('IranSans',20),
                                    bd=12,bg='#047478',fg='white')
        self.label_name_stu.place(x=480,y=170)
        self.label_numstu = Label(master=self.ro,text=':لطفا شماره دانش آموزی خود را وارد کنید',font=('IranSans',20),
                                  bd=12,bg='#047478',fg='white')
        self.label_numstu.place(x=470,y=330)
        self.lable_class = Label(master=self.ro,text=':لطفا پایه تحصیلی خود را وارد کنید',font=('IranSans',20),bd=12,bg='#047478',fg='white')
        self.lable_class.place(x=530,y=490)

        self.entry_name_stu = Entry(master=self.ro,width=22,font=('IranSans',25))
        self.entry_name_stu.place(x=480,y=250)
        self.entry_numstu = Entry(master=self.ro,width=22,font=('IranSans',25))
        self.entry_numstu.place(x=480,y=410)
        self.entry_class = Entry(master=self.ro,width=22,font=('IranSans',25))
        self.entry_class.place(x=480,y=570)

        self.but_come_stu = Button(master=self.ro,text='ورود',font=('IranSans',15),
                                   bg='#047478',fg='white',width=20,pady=10,command=self.log_stud)
        self.but_come_stu.place(x=1110,y=650)
        self.but_exit_stu = Button(master=self.ro,text='خروج',font=('IranSans',15),bg='#047478',fg='white',width=20,
                                     pady=10,command=lambda:self.exit(self.ro))
        self.but_exit_stu.place(x=5,y=650)
    def log_stud(self):
        name = self.entry_name_stu.get()
        number = self.entry_numstu.get()
        stud = self.dbr.select_dbr(nation_code=number)
        if name == '' or number == '':
            alert('اطلاعات کافی نیست', 'ناموفق')
        elif self.check_num_stu(number) is False:
            alert('اطلاعات نادرست است', 'ناموفق')
        else:
            if stud is not None:
                if stud[0] == name:
                    alert(f'{name} خوش آمدید', 'موفقیت')
                    self.show_report()
                else:
                    alert('کاربری یافت نشد', 'ناموفق')
            else:
                alert('کاربری یافت نشد', 'ناموفق')
        self.ro.mainloop()
    def show_report(self):
        self.shrep = Tk()
        self.shrep.title('مشاهده کارنامه')
        self.shrep.geometry('1350x760')

        self.lable = Label(master=self.shrep,text='کارنامه تحصیلی',font=('IranSans',30),bd=12,bg='#047478',
                                   fg='white',relief=RIDGE,height=2)
        self.lable.pack(fill='x')
        nation = self.entry_numstu.get()
        report = self.dbr.select_for_report(nation_code=nation)
        if report is not None:
            for user in report:
                self.lable_name = Label(master=self.shrep,text=f'  نام و نام خانوادگی {user[1]}',font=('IranSans',20),bd=12,bg='#047478',fg='white')
                self.lable_name.place(x=900,y=150)
                self.lable_number = Label(master=self.shrep,text=f'  شماره دانش آموزی {user[2]}',font=('IranSans',20),bd=12,bg='#047478',fg='white')
                self.lable_number.place(x=200,y=150)
                self.lable_m = Label(master=self.shrep,text=f'  نمره ی ریاضی {user[3]}',font=('IranSans',20),bd=12,bg='#047478',fg='white')
                self.lable_m.place(x=930,y=250)
                self.lable_p = Label(master=self.shrep,text=f'  نمره ی فارسی {user[4]}',font=('IranSans',20),bd=12,bg='#047478',fg='white')
                self.lable_p.place(x=930,y=350)
                self.lable_s = Label(master=self.shrep,text=f'  نمره ی علوم {user[5]}',font=('IranSans',20),bd=12,bg='#047478',fg='white')
                self.lable_s.place(x=930,y=450)
                self.lable_q = Label(master=self.shrep,text=f'  نمره ی قرآن {user[6]}',font=('IranSans',20),bd=12,bg='#047478',fg='white')
                self.lable_q.place(x=930,y=550)
                self.lable_avrage = Label(master=self.shrep,text=f' معدل {(user[3]+user[4]+user[5]+user[6]) / 4}',font=('IranSans',20),bd=12,bg='#047478',fg='white')
                self.lable_avrage.place(x=930,y=650)
            else:
                pass
        else:
            pass
        self.but_exit_stu = Button(master=self.shrep,text='خروج',font=('IranSans',15),bg='#047478',fg='white',width=20,
                                     pady=10,command=lambda:self.exit(self.shrep))
        self.but_exit_stu.place(x=5,y=650)
        self.shrep.mainloop()
    def check_number(self,value):
        res = CheckPattern(value)
        if res.check_is_number():
            return True
        else:
            return False

    def check_num_stu(self,value):
        res = CheckPattern(value)
        if res.check_iranian_nation_code():
            return True
        else:
            return False

    def check_num(self,num):
        if fullmatch(r'[0-9]{8,8}',num):
            return True
        else:
            return False

    def exit(self,root):
        self.root = root
        mg = confirm(text='شوید؟ خارج میخواهید که مطمئنید آیا',title='خروج',buttons=('بله','خیر'))
        if mg == 'بله':
            self.root.destroy()

if __name__ == '__main__':
    db = Masterdb('./masterdatabase.db')
    dbt = Teacherdb('./teacherdatabase.db')
    dbs = Studentdb('./studentdatabase.db')
    dbr = reportdb('./reportdatabase.db')
    root = Tk()
    app = SchoolSystem(root,db,dbt,dbs,dbr)
    root.mainloop()
    db.close()
    dbt.close()
    dbs.close()
    dbr.close()