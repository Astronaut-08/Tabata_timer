'''This is main file for Tabata Timmer'''
import tkinter as tk
from tkinter import ttk
from back_tabata import Timer
import preset

main = tk.Tk()
class App:
    '''Our app'''
    def __init__(self, window):
        self.window = window
        self.window.geometry('620x400')
        self.window.resizable(False, False)
        # Frame
        self.main_menu = tk.Frame(self.window)
        self.work_menu = tk.Frame(self.window)
        # Timer
        self.mt = Timer()
        # StringVars
        self.svar_work = tk.StringVar()
        self.svar_rest = tk.StringVar()
        self.svar_exercise = tk.StringVar()
        self.svar_round = tk.StringVar()
        self.svar_round_reset = tk.StringVar()
        # Main menu atr
        self.label_timer = tk.Label(self.main_menu, font=('Times', 36), \
                                    text=self.sum_for_timer())
        self.combobox_preset = ttk.Combobox(self.main_menu, state='readonly', \
                                            values=preset.select_all_id())
        self.label_work = tk.Label(self.main_menu, text='Work:')
        self.label_rest = tk.Label(self.main_menu, text='Rest:')
        self.label_exercise = tk.Label(self.main_menu, text='Exercise:')
        self.label_round = tk.Label(self.main_menu, text='Round:')
        self.label_round_reset = tk.Label(self.main_menu, text='Round reset:')
        self.entry_work = tk.Entry(self.main_menu, textvariable=self.svar_work)
        self.entry_rest = tk.Entry(self.main_menu, textvariable=self.svar_rest)
        self.entry_exercise = tk.Entry(self.main_menu, textvariable=self.svar_exercise)
        self.entry_round = tk.Entry(self.main_menu, textvariable=self.svar_round)
        self.entry_round_reset = tk.Entry(self.main_menu, textvariable=self.svar_round_reset)
        self.button_user_add = tk.Button(self.main_menu, bg='blue',text='Add user', \
                                         font=('Times', 14), justify='center',\
                                         fg='white', command=self.add_user)
        self.button_user_del = tk.Button(self.main_menu, bg='red', text='Del user', \
                                         font=('Times', 14), justify='center',\
                                         fg='white', command=self.del_user)
        self.button_start = tk.Button(self.main_menu, bg='green', text='Start', \
                                         font=('Times', 36), justify='center',\
                                         fg='white', command=self.start_timer)
        # Work menu atr
        self.label_wtimer = tk.Label(self.work_menu, font=('Times', 36), justify='center',\
                                     fg='blue')
        self.label_status = tk.Label(self.work_menu, font=('Times', 36), justify='center',\
                                     text='Work', fg='blue')
        self.label_progres = tk.Label(self.work_menu, font=('Times', 36), justify='center')
        self.button_stop = tk.Button(self.work_menu, bg='red',text='STOP', \
                                    font=('Times', 24), justify='center',\
                                    fg='white', command=self.stop_timer)
        self.button_run_pause = tk.Button(self.work_menu)
        # Place at main menu
        self.label_timer.place(x=0, y=0, width=620, height=100)
        self.combobox_preset.place(x=10, y=110, width=600, height=30)
        self.label_work.place(x=0, y=150)
        self.label_rest.place(x=300, y=150)
        self.label_exercise.place(x=0, y=200)
        self.label_round.place(x=300, y=200)
        self.label_round_reset.place(x=0, y=250)
        self.entry_work.place(x=150, y=150)
        self.entry_rest.place(x=450, y=150)
        self.entry_exercise.place(x=150, y=200)
        self.entry_round.place(x=450, y=200)
        self.entry_round_reset.place(x=150, y=250)
        self.button_start.place(x=0, y=300, width=620, height=100)
        self.button_user_add.place(x=300, y=250, width=150, height=50)
        self.button_user_del.place(x=450, y=250, width=150, height=50)
        # Place at work menu
        self.label_wtimer.place(x=10, y=105, width=600, height=90)
        self.label_status.place(x=10, y=5, width=600, height=90)
        self.label_progres.place(x=10, y=205, width=600, height=90)
        self.button_stop.place(x=10, y=305, width=280, height=90)
        self.button_run_pause.place(x=310, y=305, width=280, height=90)
        # Events
        self.combobox_preset.bind('<<ComboboxSelected>>', self.on_select_preset)
        self.update()
        self.switch_frame(self.main_menu)

    def update(self):
        '''Update the data with DB'''
        self.combobox_preset.config(values=preset.select_all_id())
        self.main_menu.after(1000, self.update)

    def switch_frame(self, frame):
        '''Switched between frame'''
        for i in (self.main_menu, self.work_menu):
            i.pack_forget()
        frame.pack(fill='both', expand=True)

    def add_user(self):
        '''Added user'''
        second = [self.entry_work.get(), self.entry_rest.get(),\
                  self.entry_exercise.get(), self.entry_round.get(),\
                  self.entry_round_reset.get()]
        try:
            ws = list(map(int, second))
            preset.add_records(ws[0], ws[1], ws[2], ws[3], ws[4])
            print('Succesfull add')
        except (TypeError, ValueError):
            print('Nothing to add')
            return

    def del_user(self):
        '''Delete curent user'''
        try:
            sv = int(self.combobox_preset.get())
            preset.delete_records_by_name(sv)
            print('Succecful delete')
        except ValueError:
            print('Nothing write')

    def sum_for_timer(self):
        '''Return all time for timer'''
        try:
            sv = int(self.combobox_preset.get())
            r = preset.select_records_by_id(sv)
            result = ((r.work * r.exercises) + (r.rest * (r.exercises - 1)))\
            * r.rounds + (r.rounds_reset * (r.rounds - 1))
            return result
        except AttributeError:
            return 'TIMER'

    def on_select_preset(self, evt):
        '''Load presets'''
        sv = int(self.combobox_preset.get())
        result = preset.select_records_by_id(sv)
        self.svar_work.set(result.work)
        self.svar_rest.set(result.rest)
        self.svar_exercise.set(result.exercises)
        self.svar_round.set(result.rounds)
        self.svar_round_reset.set(result.rounds_reset)
        self.label_timer.config(text=self.sum_for_timer())
        # Timer
        self.mt = Timer(self.sum_for_timer(), self.dmt)

    def dmt(self, r):
        '''update label main timer'''
        self.label_progres.config(text=f'Time remaining: {r//60:02}:{r%60:02}')

    def start_timer(self):
        '''Start work'''
        if self.sum_for_timer():
            self.switch_frame(self.work_menu)
            sv = int(self.combobox_preset.get())
            result = preset.select_records_by_id(sv)
            self.mt.start()
            exer = result.exercises
            rou = result.rounds
        else:
            print('Select the user pls')

    def stop_timer(self):
        '''Stop and return to main nemu'''
        self.switch_frame(self.main_menu)

App(main)
main.mainloop()
