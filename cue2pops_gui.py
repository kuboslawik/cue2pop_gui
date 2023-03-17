# Requires at least Python 3.7 for capture_output parameter to work
from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk     as tk
import subprocess

REGIONS = ['SCUS','SLPS','SLPM','SLES','SLUS','LSP','SCES','SIPS','SCPS','SLED','PAPX','PTPX','PCPX','PEPX','PUPX','SCED','PL','PBPX','CPCS','SCEs','SCPM','SCAJ','ESPM','SCZS','PCPD','SLKA','PSRM','HPS']

def convert():
    button_convert.config(state='disable')
    message = Toplevel(master=window)
    message.resizable(False, False)
    message.title('Message')
    message.config(padx=20, pady=20)
    message_label = Label(master= message, text='Converting, please wait...')
    message_label.grid(column=0, row=0)
    window.update()
    script_directory = subprocess.run(['pwd'], shell=True, capture_output=True, text=True)
    subprocess.run(['cd', script_directory.stdout], shell=True)
    if var_radio.get() == 1:
        game_name_vcd = str(menu_value.get()) + '_' + str(game_id_3.get()) + '.' + str(game_id_2.get()) + '.' + str(game_name.get()) + '.VCD'
        cmd = ['./cue2pops \"' + source_file_path.get() +"\"  \"" + game_name_vcd + "\""]
    elif var_radio.get() == 2:
        cmd = ['./cue2pops \"' + source_file_path.get() +"\""]
    temp = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    print(temp)
    if temp.returncode == 0:
        message_label.config(text='Error:\n' + temp.stdout)
        message_button = Button(master=message, text='Back', command=lambda:[message.destroy(), button_convert.config(state='normal')])
        message_button.grid(column=0, row=1)
    elif temp.returncode == 1:
        message_label.config(text='File sucesfully converted!\n' + temp.stdout)
        message_button = Button(master=message, text='Back', command=lambda:[message.destroy(), button_convert.config(state='normal')])
        message_button.grid(column=0, row=1)
    else:
        message_label.config(text='Error:\n' + temp.stderr)
        message_button = Button(master=message, text='Back', command=lambda:[message.destroy(), button_convert.config(state='normal')])
        message_button.grid(column=0, row=1)
    


def file_picker():
    filename = fd.askopenfilename()
    source_file_path.set(filename)


def select_1():
    radio_2.deselect()
    menu_region.config(state='normal')
    label_underscore.config(state='normal')
    label_dot.config(state='normal')
    entry_game_id_3.config(state='normal')
    label_dot_2.config(state='normal')
    entry_game_id_2.config(state='normal')
    entry_game_name.config(state='normal')
    label_vcd.config(state='normal')


def select_2():
    radio_1.deselect()
    menu_region.config(state='disable')
    label_underscore.config(state='disable')
    label_dot.config(state='disable')
    entry_game_id_3.config(state='disable')
    label_dot_2.config(state='disable')
    entry_game_id_2.config(state='disable')
    entry_game_name.config(state='disable')
    label_vcd.config(state='disable')


window = Tk()
window.title('cue2pops_gui')
window.config(padx=20, pady=20)
window.resizable(False, False)

var_radio = IntVar()
var_radio.set(1)
radio_1 = Radiobutton(window, variable=var_radio, value=1, command=select_1)
radio_1.grid(column=0, row=2)
radio_1.select()

label_path = Label(master=window, text='CUE file path:')
label_path.grid(column=1, row=1)

source_file_path = StringVar(window, 'Path')
entry_path= Entry(master=window, width=70, textvariable=source_file_path)
entry_path.grid(column=2, row=1, columnspan=9)

button_pick_file = tk.Button(master=window, text='Pick file...', command=file_picker, width=12)
button_pick_file.grid(column=11, row=1)

#SLES_014.04.Grand Theft Auto 2.VCD

label_name = Label(master=window, text='Set title')
label_name.grid(column=1, row=2)

menu_value = StringVar(window)
menu_value.set(REGIONS)
menu_region = tk.OptionMenu(window, menu_value, *REGIONS)
menu_region.config()
menu_region.grid(column=2, row=2)

label_underscore = Label(master=window, text='_')
label_underscore.grid(column=3, row=2)

game_id_3 = StringVar(window, 'XXX')
entry_game_id_3 = Entry(master=window, width=4, textvariable=game_id_3, )
entry_game_id_3.config()
entry_game_id_3.grid(column=4, row=2)

label_dot = Label(master=window, text='.')
label_dot.grid(column=5, row=2)

game_id_2 = StringVar(window, 'XX')
entry_game_id_2 = Entry(master=window, width=3, textvariable=game_id_2)
entry_game_id_2.config()
entry_game_id_2.grid(column=6, row=2)

label_dot_2 = Label(master=window, text='.')
label_dot_2.grid(column=7, row=2)

game_name = StringVar(window, 'Title')
entry_game_name = Entry(master=window, width=10, textvariable=game_name)
entry_game_name.config(width=40)
entry_game_name.grid(column=8, row=2)

label_vcd = Label(master=window, text='.VCD')
label_vcd.grid(column=9,row=2)

label_none = Label(master=window, text='Keep file name')
label_none.grid(column=1,row=3)

button_convert = Button(master=window, text='Convert', command=convert, width=10)
button_convert.grid(column=11, row=4)

radio_2 = Radiobutton(window, variable=var_radio, value=2, command=select_2)
radio_2.grid(column=0, row=3)

window.mainloop()