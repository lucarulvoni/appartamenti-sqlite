from tkinter import *
from tkinter import messagebox
from database import Database

db = Database('store.db')


def populate_list():
    parts_list.delete(0, END)
    for row in db.fetch():
        parts_list.insert(END, row)


def add_item():
    if nome_text.get() == '' or cognome_text.get() == '' or cellulare_text.get() == '' or appartamento_text.get() == '' or prezzo_text.get() == '':
        messagebox.showerror(
            'Campi richiesti', 'Si prega di compilare tutti i campi')
        return
    db.insert(nome_text.get(), cognome_text.get(),
              cellulare_text.get(), appartamento_text.get(), prezzo_text.get())
    parts_list.delete(0, END)
    parts_list.insert(END, (nome_text.get(), cognome_text.get(),
                            cellulare_text.get(), appartamento_text.get(), prezzo_text.get()))
    clear_text()
    populate_list()


def select_item(event):
    try:
        global selected_item
        index = parts_list.curselection()[0]
        selected_item = parts_list.get(index)

        nome_entry.delete(0, END)
        nome_entry.insert(END, selected_item[1])
        cognome_entry.delete(0, END)
        cognome_entry.insert(END, selected_item[2])
        cellulare_entry.delete(0, END)
        cellulare_entry.insert(END, selected_item[3])
        appartamento_entry.delete(0, END)
        appartamento_entry.insert(END, selected_item[4])
        prezzo_entry.delete(0, END)
        prezzo_entry.insert(END, selected_item[5])
    except IndexError:
        pass


def remove_item():
    db.remove(selected_item[0])
    clear_text()
    populate_list()


def update_item():
    db.update(selected_item[0], nome_text.get(), cognome_text.get(),
              cellulare_text.get(), appartamento_text.get(), prezzo_text.get())
    populate_list()


def clear_text():
    nome_entry.delete(0, END)
    cognome_entry.delete(0, END)
    cellulare_entry.delete(0, END)
    appartamento_entry.delete(0, END)
    prezzo_entry.delete(0, END)


# def chiudiMaschera_text():
#     app.destroy()

def ExitApplication():
    MsgBox = messagebox.askquestion(
        'Chiudi applicazione', 'Sei sicuro di voler chiudere applicazione', icon='warning')
    if MsgBox == 'yes':
        app.destroy()
    else:
        messagebox.showinfo(
            'Ritorno', 'Stai per tornare alla schermata dell\'applicazione')


# Create window object
app = Tk()

# Nome
nome_text = StringVar()
nome_label = Label(app, text='Nome', font=('bold', 14), pady=20)
nome_label.grid(row=0, column=0, sticky=W)
nome_entry = Entry(app, textvariable=nome_text)
nome_entry.grid(row=0, column=1)
# Cognome
cognome_text = StringVar()
cognome_label = Label(app, text='Cognome', font=('bold', 14))
cognome_label.grid(row=0, column=2, sticky=W)
cognome_entry = Entry(app, textvariable=cognome_text)
cognome_entry.grid(row=0, column=3)
# Cellulare
cellulare_text = StringVar()
cellulare_label = Label(app, text='Cellulare', font=('bold', 14))
cellulare_label.grid(row=1, column=0, sticky=W)
cellulare_entry = Entry(app, textvariable=cellulare_text)
cellulare_entry.grid(row=1, column=1)
# Appartamento
appartamento_text = StringVar()
appartamento_label = Label(app, text='Appartamento', font=('bold', 14))
appartamento_label.grid(row=1, column=2, sticky=W)
appartamento_entry = Entry(app, textvariable=appartamento_text)
appartamento_entry.grid(row=1, column=3)
# Prezzo
prezzo_text = StringVar()
prezzo_label = Label(app, text='Prezzo €', font=(
    'bold', 14), activebackground='blue')
prezzo_label.grid(row=1, column=4, sticky=W)
prezzo_entry = Entry(app, textvariable=prezzo_text)
prezzo_entry.grid(row=1, column=5)
# Parts List (Listbox)
parts_list = Listbox(app, height=8, width=50, border=0)
parts_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
# Create scrollbar
scrollbar = Scrollbar(app)
scrollbar.grid(row=3, column=3)
# Set scroll to listbox
parts_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=parts_list.yview)
# Bind select
parts_list.bind('<<ListboxSelect>>', select_item)

# Buttons
add_btn = Button(app, text='Aggiungi', width=12, height=3,
                 background='green', foreground='white', command=add_item)
add_btn.grid(row=2, column=0, pady=20)

remove_btn = Button(app, text='Rimuovi', bd=2, width=12, height=3,
                    background='red', foreground='white', command=remove_item)
remove_btn.grid(row=2, column=1)

update_btn = Button(app, text='Aggiorna', width=12,
                    height=3, command=update_item)
update_btn.grid(row=2, column=2)

clear_btn = Button(app, text='Cancella Campi', width=12, height=3,
                   background='lightblue', foreground='white', command=clear_text)
clear_btn.grid(row=2, column=3)

chiudi_btn = Button(app, text='Chiudi', width=12, height=3,
                    background='magenta', foreground='white', command=ExitApplication)
chiudi_btn.grid(row=2, column=4)

app.title('Gestione Appartamenti Via Trieste')
app.geometry('700x400')

# Populate data
populate_list()

# Start program
app.mainloop()


# To create an executable, install pyinstaller and run
# '''
# pyinstaller --onefile --add-binary='/System/Library/Frameworks/Tk.framework/Tk':'tk' --add-binary='/System/Library/Frameworks/Tcl.framework/Tcl':'tcl' part_manager.py
# '''
