from tkinter import *
from tkinter import filedialog as fd
from tkinter import ttk as tk
import subprocess

regions = ['SLPS','SLPM','SLES','SLUS','LSP','SCUS','SCES','SIPS','SCPS','SLED','PAPX','PTPX','PCPX','PEPX','PUPX','SCED','PL','PBPX','CPCS','SCEs','SCPM','SCAJ','ESPM','SCZS','PCPD','SLKA','PSRM','HPS']


def convert():
    if var_radio.get() == 1:
            game_name_vcd = str(menu_value.get()) + '_' + str(game_id_3.get()) + '.' + str(game_id_2.get()) + '.' + str(game_name.get()) + '.VCD'
    elif var_radio.get() == 2:
        print(2)
    #cmd = 'cd /home/kuba/Dokumenty && ls'    #'./cue2pops .' + source_file_path.get() + ' ' + game_name_vcd
    cmd = ['ls']
    #print(cmd)
    try:
        temp = subprocess.Popen(cmd, shell=True,  stdout=subprocess.PIPE, check=True
    )
    except FileNotFoundError as exc:
        print(f"Process failed because the executable could not be found.\n{exc}")
    except subprocess.CalledProcessError as exc:
        print(
            f"Process failed because did not return a successful return code. "
            f"Returned {exc.returncode}\n{exc}"
        )
    except subprocess.TimeoutExpired as exc:
        print(f"Process timed out.\n{exc}") 
    #temp = subprocess.run(cmd, capture_output=True, encoding='utf-8')
    # get the output as a string
    #output = str(temp.communicate()) 
    print(str(temp.stdout))


def file_picker():
    filename = fd.askopenfilename()
    source_file_path.set(filename)


def select_1():
    radio_2.deselect()
    label_none.config(state='disable')
    label_name.config(state='normal')
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
    label_none.config(state='normal')
    label_name.config(state='disable')
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

var_radio = IntVar()
var_radio.set(1)
radio_1 = Radiobutton(window, variable=var_radio, value=1, command=select_1)
radio_1.grid(column=0, row=2)
radio_1.select()

label_path = Label(text='CUE file path:')
label_path.grid(column=1, row=1)

source_file_path = StringVar(window, 'Path')
entry_path= Entry(width=70, textvariable=source_file_path)
entry_path.grid(column=2, row=1, columnspan=9)

button_pick_file = tk.Button(text='Pick file...', command=file_picker)
button_pick_file.grid(column=11, row=1)

#SLES_014.04.Grand Theft Auto 2.VCD

label_name = Label(text='Set title')
label_name.grid(column=1, row=2)

menu_value = StringVar(window)
menu_value.set(regions[5])
print(regions[5])
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
entry_game_name.config(width=40)
entry_game_name.grid(column=8, row=2)

label_vcd = Label(text='.VCD')
label_vcd.grid(column=9,row=2)

label_none = Label(text='Keep file name', state='disable')
label_none.grid(column=1,row=3)

button_convert = Button(text='Convert', command=convert)
button_convert.grid(column=11, row=4)

radio_2 = Radiobutton(window, variable=var_radio, value=2, command=select_2)
radio_2.grid(column=0, row=3)

window.mainloop()
