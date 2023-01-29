import os
import shutil
import zipfile
import requests
import platform

# Change directory to the parent directory of the script
os.chdir("..")

# Define the GitHub repository URL and subdirectory
repo_url = "https://github.com/Akul-AI/akulai-plugins"
subdir = "plugins"

# Use git submodules to fetch the plugins subdir in the akulai plugins repo
os.system("git submodule add {}".format(repo_url))
os.system("git submodule update --init --recursive")

# Move the files from the subdirectory to the local "akulai/plugins" folder
shutil.move("{}/".format(f"akulai-plugins/{subdir}"), "akulai/")

# Delete the files after copying them
shutil.rmtree("akulai-plugins")

# Use requests library to download vosk
vosk_url = "https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip"
response = requests.get(vosk_url)
with open("vosk-model-small-en-us-0.15.zip", "wb") as f:
    f.write(response.content)

# Extract the downloaded model
with zipfile.ZipFile("vosk-model-small-en-us-0.15.zip", "r") as zip_ref:
    zip_ref.extractall("akulai/model")

# Rename the extracted model to "vosk_model"
os.rename("akulai/model/vosk-model-small-en-us-0.15", "akulai/model/vosk_model")

# Clean up the downloaded archive
os.remove("vosk-model-small-en-us-0.15.zip")

# Check the current operating system
current_os = platform.system()

if current_os == "Windows":
    # Download and install Node.js
    node_url = "https://nodejs.org/dist/latest-version/node-x64.msi"
    response = requests.get(node_url)
    with open("node-x64.msi", "wb") as f:
        f.write(response.content)
    os.system("msiexec /i node-x64.msi /quiet")

    # Download Strawberry Perl for Windows
    strawberry_perl_url = "http://strawberryperl.com/download/5.32.0.1/strawberry-perl-5.32.0.1-64bit.msi"
    response = requests.get(strawberry_perl_url)
    with open("strawberry-perl.msi", "wb") as f:
        f.write(response.content)
    os.system("msiexec /i strawberry-perl.msi /quiet")

    # Add the Perl executable to the system path
    os.system('setx path "%path%;C:\Perl64\bin"')

elif current_os == "Linux":
    # Install Node.js
    os.system("sudo apt-get update")
    os.system("sudo apt-get install -y nodejs")
    # Download Strawberry Perl for Linux
    os.system("wget http://strawberryperl.com/download/5.32.0.1/strawberry-perl-5.32.0.1-64bit.tar.bz2")
    os.system("tar -xjf strawberry-perl-5.32.0.1-64bit.tar.bz2")
    os.system("./strawberry-perl-5.32.0.1-64bit/install.pl")
    os.system("sudo apt-get update")
    os.system("sudo apt-get install espeak-ng")
else:
    print("This script only supports Windows and Ubuntu. Exiting...")

# Install requirements
os.system('pip install -r requirements.txt')
exit()
