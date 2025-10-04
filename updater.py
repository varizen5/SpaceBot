import requests, os, zipfile, shutil

# 🔧 Configura qui il tuo repo
GITHUB_USER = "varizen5"
REPO_NAME = "SpaceBot"
RAW_BASE = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/main/"
ZIP_URL = f"https://github.com/{GITHUB_USER}/{REPO_NAME}/archive/refs/heads/main.zip"

def get_remote_version():
    url = RAW_BASE + "version.txt"
    r = requests.get(url)
    if r.status_code == 200:
        return r.text.strip()
    else:
        print("Errore nel recupero della versione remota.")
        return None

def get_local_version():
    try:
        with open("version.txt") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "0.0.0"

def update_files():
    print("Scarico aggiornamento...")
    r = requests.get(ZIP_URL)
    if r.status_code != 200:
        print("Errore nel download del file ZIP.")
        return

    with open("update.zip", "wb") as f:
        f.write(r.content)

    try:
        with zipfile.ZipFile("update.zip", 'r') as zip_ref:
            zip_ref.extractall("update_temp")
    except zipfile.BadZipFile:
        print("Il file scaricato non è un ZIP valido.")
        return

    src_folder = f"update_temp/{REPO_NAME}-main"
    for filename in os.listdir(src_folder):
        src_path = os.path.join(src_folder, filename)
        dst_path = os.path.join(".", filename)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)

    os.remove("update.zip")
    shutil.rmtree("update_temp")
    print("Aggiornamento completato.")

def main():
    remote_version = get_remote_version()
    local_version = get_local_version()

    if remote_version and remote_version != local_version:
        print(f"Aggiornamento disponibile: {local_version} → {remote_version}")
        update_files()
    else:
        print("Nessun aggiornamento disponibile.")

    os.system("python main.py")

main()
