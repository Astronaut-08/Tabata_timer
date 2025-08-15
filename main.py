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
        # StringVars
        self.svar_work = tk.StringVar()
        self.svar_rest = tk.StringVar()
        self.svar_exercise = tk.StringVar()
        self.svar_round = tk.StringVar()
        self.svar_round_reset = tk.StringVar()
        # Main menu atr
        self.label_timer = tk.Label(self.window, font=('Times', 36), \
                                    text=self.sum_for_timer())
        self.combobox_preset = ttk.Combobox(self.window, state='readonly', \
                                            values=preset.select_all_id())
        self.label_work = tk.Label(self.window, text='Work:')
        self.label_rest = tk.Label(self.window, text='Rest:')
        self.label_exercise = tk.Label(self.window, text='Exercise:')
        self.label_round = tk.Label(self.window, text='Round:')
        self.label_round_reset = tk.Label(self.window, text='Round reset:')
        self.entry_work = tk.Entry(self.window, textvariable=self.svar_work)
        self.entry_rest = tk.Entry(self.window, textvariable=self.svar_rest)
        self.entry_exercise = tk.Entry(self.window, textvariable=self.svar_exercise)
        self.entry_round = tk.Entry(self.window, textvariable=self.svar_round)
        self.entry_round_reset = tk.Entry(self.window, textvariable=self.svar_round_reset)
        self.button_user_add = tk.Button(self.window, bg='blue',text='Add user', \
                                         font=('Times', 14), justify='center',\
                                         fg='white', command=self.add_user)
        self.button_user_del = tk.Button(self.window, bg='red', text='Del user', \
                                         font=('Times', 14), justify='center',\
                                         fg='white', command=self.del_user)
        self.button_start = tk.Button(self.window, bg='green')
        # Work menu atr
        self.label_wtimer = tk.Label()
        self.label_status = tk.Label()
        self.label_progres = tk.Label()
        self.button_stop = tk.Button()
        self.button_pause = tk.Button()
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
        # Events
        self.combobox_preset.bind('<<ComboboxSelected>>', self.on_select_preset)
        self.update()

    def update(self):
        '''Update the data with DB'''
        self.combobox_preset.config(values=preset.select_all_id())
        self.window.after(1000, self.update)

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
            print('Type error or Value error')
            return

    def del_user(self):
        '''Delete curent user'''
        sv = int(self.combobox_preset.get())
        preset.delete_records_by_name(sv)
        print('Succecful delete')

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

App(main)
main.mainloop()
