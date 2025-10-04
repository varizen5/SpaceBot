import tkinter as tk
import subprocess
import sys

def get_version():
    try:
        with open("version.txt") as f:
            return f.read().strip()
    except:
        return "Versione sconosciuta"

def check_updates():
    # Esegue updater.py
    subprocess.Popen([sys.executable, "updater.py"])
    sys.exit()  # Chiude main.py, verrà riavviato da updater.py se serve

def main():
    version = get_version()

    root = tk.Tk()
    root.title("SpaceBot")

    # Dimensioni finestra
    root.geometry("300x150")

    # Messaggio
    label = tk.Label(root, text=f"Benvenuto in SpaceBot!\nVersione: {version}", font=("Arial", 12), pady=20)
    label.pack()

    btn_check = tk.Button(root, text="Controlla aggiornamenti", command=check_updates)
    btn_check.pack(pady=5)

    # Bottone di uscita
    button = tk.Button(root, text="Chiudi", command=root.destroy)
    button.pack()

    root.mainloop()

main()