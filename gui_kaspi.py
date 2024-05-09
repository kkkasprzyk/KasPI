from config_kaspi import *
import threading
## Revision of code 27.04.2024 - Release 3 ##  -- > gui_kaspi.py module
import sys
import config_kaspi


print("""

██╗  ██╗ █████╗ ███████╗██████╗ ██╗                    ██████╗  ██████╗ ██████╗ ██╗  ██╗
██║ ██╔╝██╔══██╗██╔════╝██╔══██╗██║                    ╚════██╗██╔═████╗╚════██╗██║  ██║
█████╔╝ ███████║███████╗██████╔╝██║                     █████╔╝██║██╔██║ █████╔╝███████║
██╔═██╗ ██╔══██║╚════██║██╔═══╝ ██║                    ██╔═══╝ ████╔╝██║██╔═══╝ ╚════██║
██║  ██╗██║  ██║███████║██║     ██║                    ███████╗╚██████╔╝███████╗     ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝                    ╚══════╝ ╚═════╝ ╚══════╝     ╚═╝


                                                                                        """)


# def start_program(video_path):
#     global init_thread
#     init_thread = threading.Thread(target=select_and_initialize, args=(video_path,))
#     init_thread.start()

def select_and_initialize(video_path):
    initialize_yolo_model(select_line_points(video_path,int(1920/2),int(1080/2)),video_path,2,int(1920/2),int(1080/2))

def quit_program(root):
    print("########   ###      KONIEC   ###     ###############")
    sys.exit("Exiting the code with sys.exit()!")


def gui_kaspi(video_path):
    # Tworzenie głównego okna
    root = tk.Tk()
    root.title("KasPi 2024")

    # Ustawienie tła
    background_image = Image.open("8275340.jpg")
    background_photo = ImageTk.PhotoImage(background_image)
    background_label = tk.Label(root, image=background_photo)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    root.geometry("800x600")
    # Funkcja do obsługi przycisku Start
    def start_button_click():
        root.after(0,select_and_initialize,video_path)

    # Funkcja do obsługi przycisku Quit
    def quit_button_click():
        quit_program(root)

    button_style = {'font': ('Helvetica', 16, 'bold'), 'bg': '#4CAF50', 'fg': 'white'}

    # Tworzenie przycisku Start
    start_button = tk.Button(root, text="Start", command=start_button_click, **button_style)
    start_button.place(relx=0.5, rely=0.4, anchor="center")

    # Tworzenie przycisku Quit
    quit_button = tk.Button(root, text="Quit", command=quit_button_click, **button_style)
    quit_button.place(relx=0.5, rely=0.6, anchor="center")

    # Dodanie grafiki


    # Rozpoczęcie głównej pętli programu
    root.mainloop()


