from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk as tk

regions = ['SLPS','SLPM','SLES','SLUS','LSP','SCUS','SCES','SIPS','SCPS','SLED','PAPX','PTPX','PCPX','PEPX','PUPX','SCED','PL','PBPX','CPCS','SCEs','SCPM','SCAJ','ESPM','SCZS','PCPD','SLKA','PSRM','HPS']


def print_StringVar():
    game_name_vcd = str(menu_value.get()) + '_' + str(game_id_3.get()) + '.' + str(game_id_2.get()) + '.' + str(game_name.get()) + '.VCD'
    print(game_name_vcd)

def convert():
    if var_radio.get() == 1:
        print(1)
    elif var_radio.get() == 2:
        print(2)
    else:
        print('else')

def file_picker():
    filename = fd.askopenfilename()
    print(filename)
    source_file_path.set(filename)

def select_1():
    radio_2.deselect()
    label_none.config(fg='grey')
    label_name.config(fg='black')
    #menu_region.config()
    label_underscore.config(fg='black')
    label_dot.config(fg='black')
    entry_game_id_3.config(fg='black')
    label_dot_2.config(fg='black')
    entry_game_id_2.config(fg='black')
    entry_game_name.config(fg='black')
    label_vcd.config(fg='black')

def select_2():
    radio_1.deselect()
    label_none.config(fg='black')
    label_name.config(fg='grey')
    #menu_region.config()
    label_underscore.config(fg='grey')
    label_dot.config(fg='grey')
    entry_game_id_3.config(fg='grey')
    label_dot_2.config(fg='grey')
    entry_game_id_2.config(fg='grey')
    entry_game_name.config(fg='grey')
    label_vcd.config(fg='grey')

window = Tk()
window.title('cue2pops_gui')
window.config(padx=20, pady=20)

var_radio = IntVar()
var_radio.set(1)
radio_1 = Radiobutton(window, variable=var_radio, value=1, command=select_1)
radio_1.grid(column=0, row=2)
radio_1.select()

label_path = Label(text='CUE file path:')
label_path.grid(column=1, row=1)

source_file_path = StringVar(window, 'Path')
entry_path= Entry(width=50, textvariable=source_file_path)
entry_path.grid(column=2, row=1, columnspan=8)

button_pick_file = tk.Button(text='Pick file...', command=file_picker)
button_pick_file.grid(column=10, row=1)

#SLES_014.04.Grand Theft Auto 2.VCD

label_name = Label(text='Set title')
label_name.grid(column=1, row=2)

menu_value = StringVar(window, regions[5])
menu_region = tk.OptionMenu(window, menu_value, *regions)
menu_region.config()
menu_region.grid(column=2, row=2)

label_underscore = Label(text='_')
label_underscore.grid(column=3, row=2)

game_id_3 = StringVar(window, 'XXX')
entry_game_id_3 = Entry(width=4, textvariable=game_id_3, )
entry_game_id_3.config()
entry_game_id_3.grid(column=4, row=2)

label_dot = Label(text='.')
label_dot.grid(column=5, row=2)

game_id_2 = StringVar(window, 'XX')
entry_game_id_2 = Entry(width=3, textvariable=game_id_2)
entry_game_id_2.config()
entry_game_id_2.grid(column=6, row=2)

label_dot_2 = Label(text='.')
label_dot_2.grid(column=7, row=2)

game_name = StringVar(window, 'Title')
entry_game_name = Entry(width=10, textvariable=game_name)
entry_game_name.grid(column=8, row=2)

label_vcd = Label(text='.VCD')
label_vcd.grid(column=9,row=2)

label_none = Label(text='Keep file name', fg='grey')
label_none.grid(column=1,row=3)

button_convert = Button(text='Convert', command=convert)
button_convert.grid(column=11, row=4)

radio_2 = Radiobutton(window, variable=var_radio, value=2, command=select_2)
radio_2.grid(column=0, row=3)


window.mainloop()
