import os
import sys
import subprocess
import urllib3
import zipfile
current_version = 1.1

print("Roblox Executors | BootStrapper")
subprocess.call([sys.executable, '-m', 'pip', 'install', 'requests', 'rarfile'])
local_appdata = os.getenv('LOCALAPPDATA')
if local_appdata:
    folder = os.path.join(local_appdata, 'RobloxBootStrapper')
    print("Directory to be used", folder)
    os.makedirs(folder, exist_ok=True)
    print("Directory created Success!")
else:
    print("Environment variable 'LOCALAPPDATA' not found.")
import requests
import rarfile
# define URL and path
version_url = "https://raw.githubusercontent.com/rhuda21/BootStrapper/main/resources/version.txt"
update_url = "https://raw.githubusercontent.com/rhuda21/BootStrapper/main/main.py"
version_file_path = os.path.join(folder, "version.txt")
update_file_path = os.path.join(folder, "main.py")

response = requests.get(version_url)
latest_version = response.text.strip()
print("The Latest Version is", latest_version)

def download_file(url, folder, file_name):
    response = requests.get(url)
    file_path = os.path.join(folder, file_name)
    with open(file_path, 'wb') as file:
        file.write(response.content)
        print(f"File downloaded and saved to: {file_path}")
# Compare with the current version
if float(latest_version) > current_version:
    print("Update is being Downloaded")
    response = requests.get(update_url)
    with open(update_file_path, 'wb') as file:
        file.write(response.content)
    subprocess.call([sys.executable, update_file_path])
    sys.exit(0)
# functions
def unzip_file(zip_path, dest_folder):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(dest_folder)
    print(f"Unzipped {zip_path} to {dest_folder}")
    def unrar_file(rar_path, dest_folder):
        with rarfile.RarFile(rar_path, 'r') as rar_ref:
            rar_ref.extractall(dest_folder)
            print(f"Unzipped {rar_path} to {dest_folder}")
def download_atlantis():
    print("Downloading Atlantis...")
    atlantis_link = "https://getatlantis.xyz/Build.rar"
    download_file(atlantis_link, folder, "Atlantis.rar")
    rar_path = os.path.join(folder, "Atlantis.rar")
    dest_folder = os.path.join(folder, "Atlantis")
    unrar_file(rar_path, dest_folder)
    exe_path = os.path.join(dest_folder, "Atlantis.exe")
    os.system(f'"{exe_path}"')
def download_ronix():
    print("Downloading Ronix...")
    ronix_link = "https://file4.gofile.io/download/web/88060654-0335-4deb-8baa-1bfef59b02d7/RonixBuild.rar"
def download_jjsploit():
    print("Downloading JJSploit...")
    jjsploit_link = "https://raw.githubusercontent.com/rhuda21/BootStrapper/refs/heads/main/software/JJSploit.zip"
    download_file(jjsploit_link, folder, "JJSploit.zip")
    zip_path = os.path.join(folder, "JJSploit.zip")
    dest_folder = os.path.join(folder, "JJSploit")
    os.makedirs(dest_folder, exist_ok=True)
    unzip_file(zip_path, dest_folder)
    exe_path = os.path.join(dest_folder, "JJSploit.exe")
    os.system(f'"{exe_path}"')
def download_xeno():
    print("Downloading Xeno...")

def download_swift():
    print("Downloading Swift...")

def download_luna():
    print("Downloading Luna...")
exec_dict = {
    "Atlantis": download_atlantis,
    "Ronix": download_ronix,
    "Jj": download_jjsploit,
    "Xeno": download_xeno,
    "Swift": download_swift,
    "Luna": download_luna
}

print("Supported Executors:", *exec_dict.keys())
WhichExec = input("What executor would you like to use?").title()
if WhichExec in exec_dict:
    exec_dict[WhichExec]()  # Call the corresponding function
else:
    print(f"{WhichExec} is not a supported executor.")