import tkinter as tk

def get_version():
    try:
        with open("version.txt") as f:
            return f.read().strip()
    except:
        return "Versione sconosciuta"

def main():
    version = get_version()

    root = tk.Tk()
    root.title("SpaceBot")

    # Dimensioni finestra
    root.geometry("300x150")

    # Messaggio
    label = tk.Label(root, text=f"Benvenuto in SpaceBot!\nVersione: {version}", font=("Arial", 12), pady=20)
    label.pack()

    # Bottone di uscita
    button = tk.Button(root, text="Chiudi", command=root.destroy)
    button.pack()

    root.mainloop()

main()
