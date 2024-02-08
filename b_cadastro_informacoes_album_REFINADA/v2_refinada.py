from tkinter import *
from tkinter import ttk

user_attempts = 0
user_search = 0
saved_albums = 0
current_height = 10

current_album_reference = []
current_all_albums_reference = []

def main_features():
    global main_window, current_height
    main_window = Tk()
    main_window.title("v1 - Cadastro de Álbuns")
    main_window.geometry("750x800")
    main_window.resizable(False, False)

    main_font = ("Arial", 14)
    main_window.option_add("*Font", main_font)

    main_title_label = Label(main_window, text="Cadastre informações sobre álbuns de artistas", font=("Arial", 20))
    main_title_label.place(x=95, y=current_height)
    
def generic_label(generic_text, more_height = 0, exact_height = 0, exact_widht = 35):
    global current_height
    generic_label = Label(main_window, text = generic_text)
    if more_height != 0:
        current_height += more_height
    elif exact_height != 0:
        current_height = exact_height
    else:
        current_height += 35
    generic_label.place(x = exact_widht, y = current_height)

def status_saving_album_label(generic_text, exact_height, color = "black"):
    global current_height, user_attempts, message_saving_album_label
    current_height = exact_height
    if user_attempts == 0:
        message_saving_album_label = Label(main_window, text = generic_text, fg = color, anchor='center')
        message_saving_album_label.place(x = 35, y = current_height)
    else:
        message_saving_album_label.config(text = generic_text, fg = color)
    user_attempts += 1
    
def generic_text_box():
    global current_height
    generic_text_box = Entry(main_window, bd = 3, width = 30)
    current_height += 25
    generic_text_box.place(x = 35, y = current_height)
    current_album_reference.append(generic_text_box)
    
def generic_radio_button_two_options(generic_text, generic_text_2):
    global current_height
    current_height += 30
    generic_radio_button = IntVar()
    generic_radio_button.set(1)

    generic_radio_button_option_1 = Radiobutton(main_window, text=generic_text, variable=generic_radio_button, value=1)
    generic_radio_button_option_2 = Radiobutton(main_window, text=generic_text_2, variable=generic_radio_button, value=2)

    generic_radio_button_option_1.place(x=35, y=current_height)
    current_height += 30
    generic_radio_button_option_2.place(x=35, y=current_height)
    current_album_reference.append(generic_radio_button)

def saving_the_album_button():
    global current_height
    saving_album_button = Button(main_window, text="Adicionar álbum")
    saving_album_button.config(command=saving_the_album)
    current_height += 35
    saving_album_button.place(x = 35, y = current_height)

def saving_the_album():
    global current_album_reference, current_album
    current_album = [current_album_reference[0].get(), current_album_reference[1].get(), current_album_reference[2].get(), current_album_reference[3].get()]
    for x, y in enumerate(current_album):
        current_album[x] = str(y).strip()
    
    while True:
        with open('registered_albums.txt', 'r', encoding='UTF-8') as archive_txt:
            list_from_archive_txt = archive_txt.readlines()
            print(list_from_archive_txt)
            if '' in current_album:
                status_saving_album_label("Você ainda não preencheu todos os campos necessários. Tente novamente.", 360, "red")
                break
            
            try:
                current_album[1] = int(current_album[1])
            except Exception:
                status_saving_album_label("Você inseriu um ano inválido. Tente novamente.", 360, "red")
                break
            
            if list_from_archive_txt:
                for line_archive_txt in list_from_archive_txt:
                    if line_archive_txt.split(",")[0] == current_album[0]:
                        status_saving_album_label("Você inseriu um álbum já existente no programa. Tente novamente.", 360, "red")
                        break
                if line_archive_txt.split(",")[0] == current_album[0]:
                    break
            
            with open('registered_albums.txt', 'a', encoding='UTF-8') as archive_txt:
                for x in current_album:
                    if x != current_album[3]:
                        archive_txt.write(f'{x},')
                    else:
                        archive_txt.write(f'{x}\n')
                    status_saving_album_label(f'O álbum inserido ({current_album[0]}) foi salvo!', current_height + 40, "green")
            
            current_saved_albums_tree()
            break

def current_saved_albums_tree():
    global current_album, saved_albums, current_saved_album_tree
    if saved_albums != 0:
        current_saved_album_tree.insert('', 'end', values=(current_album[0],))
    else:
        current_saved_album_column = ('current_saved_album_name_column')
        current_saved_album_tree = ttk.Treeview(main_window, columns = current_saved_album_column, show = 'headings')
        current_saved_album_tree.heading('current_saved_album_name_column', text='Nome do Álbum')
        current_saved_album_tree.insert('', 'end', values = (current_album[0],))
        current_saved_album_tree.grid(row = 0, column = 0, sticky = 'snew')
        generic_label("Álbuns cadastrados agora:", 0, 50, 450)
        current_saved_album_tree.place(x = 400, y = 80, width = 315, height = 270)
    saved_albums += 1

def filters_all_albums_radio_buttons():
    current_height = 400
    try:
        filters_all_albums_ratio_button
    except Exception:
        text_all_albums_label = Label(main_window, text = "Navegue por todos os álbuns já salvos utilizando estes filtros!")
        text_all_albums_label.place(x = 100, y = current_height)
        
        text_all_albums_label_2 = Label(main_window, text = "Insira Ano/Nome:")
        text_all_albums_label_2.place(x = 35, y = current_height+200)
    
    filters_all_albums_ratio_button = IntVar()
    filters_all_albums_ratio_button.set(1)

    filters_all_albums_ratio_button_option_1 = Radiobutton(main_window, text = "Todos", variable = filters_all_albums_ratio_button, value = 1)
    filters_all_albums_ratio_button_option_2 = Radiobutton(main_window, text = "Nome do Álbum", variable = filters_all_albums_ratio_button, value = 2)
    filters_all_albums_ratio_button_option_3 = Radiobutton(main_window, text = "Anterior à", variable = filters_all_albums_ratio_button, value = 3)
    filters_all_albums_ratio_button_option_4 = Radiobutton(main_window, text = "Posterior à", variable = filters_all_albums_ratio_button, value = 4)
    filters_all_albums_ratio_button_option_5 = Radiobutton(main_window, text = "Igual à", variable = filters_all_albums_ratio_button, value = 5)
    
    filters_all_albums_ratio_button_option_1.place(x=35, y=current_height+30)
    filters_all_albums_ratio_button_option_2.place(x=35, y=current_height+60)
    filters_all_albums_ratio_button_option_3.place(x=35, y=current_height+90)
    filters_all_albums_ratio_button_option_4.place(x=35, y=current_height+120)
    filters_all_albums_ratio_button_option_5.place(x=35, y= current_height+150)
    current_all_albums_reference.append(filters_all_albums_ratio_button)

def year_from_all_albums_filter_text_box():
    current_height = 400
    year_display_input_text_box = Entry(main_window, bd = 3)
    year_display_input_text_box.place(x = 35, y = current_height+230, width=150)
    current_all_albums_reference.append(year_display_input_text_box)
    
def search_year_from_all_albums_button():
    current_height = 400
    search_the_year_album_button = Button(main_window, text="Buscar")
    search_the_year_album_button.config(command=searching_all_albums)
    search_the_year_album_button.place(x = 35, y = current_height+270)

def status_from_search_all_albums_label(generic_text, exact_height, color = "black"):
    global current_height, user_search, message_status_from_search_all_albums_label
    current_height = exact_height
    if user_search == 0:
        message_status_from_search_all_albums_label = Label(main_window, text = generic_text, fg = color, anchor='center')
        message_status_from_search_all_albums_label.place(x = 35, y = 750)
    else:
        message_status_from_search_all_albums_label.config(text = generic_text, fg = color)
    user_search += 1
    
def search_all_albums_tree():
    global current_album_tree
    columns_search = ('Nome do Álbum', 'Ano', 'Nome(s)', 'Lançamento')

    current_album_tree = ttk.Treeview(main_window, columns=columns_search, show='headings')

    current_album_tree.heading('Nome do Álbum', text='Nome do Álbum')
    current_album_tree.heading('Ano', text='Ano')
    current_album_tree.heading('Nome(s)', text='Nome(s)')
    current_album_tree.heading('Lançamento', text='Lançamento')

    current_album_tree.grid(row=0, column=0, sticky='nsew')
    current_album_tree.place(x=200, y=450, width=510, height=290)

    current_album_tree.column('Nome do Álbum', width=180)
    current_album_tree.column('Ano', width=70)
    current_album_tree.column('Nome(s)', width=150)
    current_album_tree.column('Lançamento', width=70)
    
def searching_all_albums():
    global current_album_tree, saved_albums
    current_height = 770
    current_album_from_all_albums_searching_list = [current_all_albums_reference[0].get(), current_all_albums_reference[1].get()]
    status_from_search_all_albums_label("", current_height)
    if saved_albums == 0:
        status_from_search_all_albums_label("Crie pelo menos 1 álbum antes de visualizar outros.", current_height, "red")
    else:
        while True:
            with open('registered_albums.txt', 'r', encoding='UTF-8') as archive_txt:
                list_from_archive_txt = archive_txt.readlines()
        
                if current_album_from_all_albums_searching_list[0] == 1:
                    current_album_tree.delete(*current_album_tree.get_children())
                    for line_archive_txt in list_from_archive_txt:
                        line_archive_txt = line_archive_txt.split(",")
                        current_album_tree.insert('', 'end', values=(line_archive_txt[0], line_archive_txt[1], line_archive_txt[2], "Não" if line_archive_txt[3] == "1\n" else "Sim"))
                    break
                
                if '' in current_album_from_all_albums_searching_list:
                    status_from_search_all_albums_label("Você ainda não preencheu todos os campos necessários. Tente novamente.", current_height, "red")
                    
                elif current_album_from_all_albums_searching_list[0] == 2:
                    current_album_tree.delete(*current_album_tree.get_children())
                    add_for_name = 0
                    for line_archive_txt in list_from_archive_txt:
                        line_archive_txt = line_archive_txt.split(",")
                        if current_album_from_all_albums_searching_list[1] in line_archive_txt[0]:
                            add_for_name += 1
                            current_album_tree.insert('', 'end', values=(line_archive_txt[0], line_archive_txt[1], line_archive_txt[2], "Não" if line_archive_txt[3] == "1\n" else "Sim"))
                    if add_for_name == 0:
                        status_from_search_all_albums_label("Não foi encontrado nenhum álbum com o trecho inserido.", current_height, "red")
                            
                else:
                    try:
                        current_album_from_all_albums_searching_list[1] = int(current_album_from_all_albums_searching_list[1])
                    except Exception:
                        status_from_search_all_albums_label("Você inseriu um ano inválido. Tente novamente.", current_height, "red")
                        break
                
                    current_album_tree.delete(*current_album_tree.get_children())
                    add_for_name = 0
                    
                    if current_album_from_all_albums_searching_list[0] == 3:
                        for line_archive_txt in list_from_archive_txt:
                            line_archive_txt = line_archive_txt.split(",")
                            if int(line_archive_txt[1]) < current_album_from_all_albums_searching_list[1]:
                                add_for_name += 1
                                current_album_tree.insert('', 'end', values=(line_archive_txt[0], line_archive_txt[1], line_archive_txt[2], "Não" if line_archive_txt[3] == "1\n" else "Sim"))
                        if add_for_name == 0:
                            status_from_search_all_albums_label("Não foi encontrado nenhum álbum com o limite inserido..", current_height, "red")
                    
                    elif current_album_from_all_albums_searching_list[0] == 4:
                        for line_archive_txt in list_from_archive_txt:
                            line_archive_txt = line_archive_txt.split(",")
                            if int(line_archive_txt[1]) > current_album_from_all_albums_searching_list[1]:
                                add_for_name += 1
                                current_album_tree.insert('', 'end', values=(line_archive_txt[0], line_archive_txt[1], line_archive_txt[2], "Não" if line_archive_txt[3] == "1\n" else "Sim"))
                        if add_for_name == 0:
                            status_from_search_all_albums_label("Não foi encontrado nenhum álbum com o limite inserido..", current_height, "red")
                    
                    else:
                        for line_archive_txt in list_from_archive_txt:
                            line_archive_txt = line_archive_txt.split(",")
                            if int(line_archive_txt[1]) == current_album_from_all_albums_searching_list[1]:
                                add_for_name += 1
                                current_album_tree.insert('', 'end', values=(line_archive_txt[0], line_archive_txt[1], line_archive_txt[2], "Não" if line_archive_txt[3] == "1\n" else "Sim"))
                        if add_for_name == 0:
                            status_from_search_all_albums_label("Não foi encontrado nenhum álbum com o limite inserido.", current_height, "red")
                    
                break

def main():
    main_features()
    generic_label("Nome do Álbum:")
    generic_text_box()
    generic_label("Ano de Lançamento do Álbum:")
    generic_text_box()
    generic_label("Nome da Banda ou Artista:")
    generic_text_box()
    generic_label("É lançamento do artista?")
    generic_radio_button_two_options("Não", "Sim")
    saving_the_album_button()
    filters_all_albums_radio_buttons()
    year_from_all_albums_filter_text_box()
    search_all_albums_tree()
    search_year_from_all_albums_button()
    main_window.mainloop()

if __name__ == "__main__":
    main()
