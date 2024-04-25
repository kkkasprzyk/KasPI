import tkinter as tk


## Revision of code 25.04.2024 - Release 1 ##  -- > gui_kaspi.py module



print("""

██╗  ██╗ █████╗ ███████╗██████╗ ██╗                    ██████╗  ██████╗ ██████╗ ██╗  ██╗
██║ ██╔╝██╔══██╗██╔════╝██╔══██╗██║                    ╚════██╗██╔═████╗╚════██╗██║  ██║
█████╔╝ ███████║███████╗██████╔╝██║                     █████╔╝██║██╔██║ █████╔╝███████║
██╔═██╗ ██╔══██║╚════██║██╔═══╝ ██║                    ██╔═══╝ ████╔╝██║██╔═══╝ ╚════██║
██║  ██╗██║  ██║███████║██║     ██║                    ███████╗╚██████╔╝███████╗     ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝                    ╚══════╝ ╚═════╝ ╚══════╝     ╚═╝


                                                                                        """)
def gui_kaspi():
    # Tworzenie głównego okna
    root = tk.Tk()
    root.title("Moje pierwsze GUI")


    # Funkcja do obsługi przycisku
    def button_click():
        label.config(text="Wciśnięto przycisk!")


    # Tworzenie przycisku
    button = tk.Button(root, text="Kliknij mnie!", command=button_click)
    button.pack()

    # Tworzenie etykiety
    label = tk.Label(root, text="Witaj w moim GUI")
    label.pack()

    # Rozpoczęcie głównej pętli programu
    root.mainloop()