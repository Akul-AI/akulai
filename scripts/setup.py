import os
import shutil
import zipfile
import requests
import platform

# Change directory to the parent directory of the script
os.chdir("..")

# Define the GitHub repository URL and subdirectory
repo_url = "https://github.com/Akul-AI/akulai-plugins"
subdir = "default_plugins"

# Create the "akulai/plugins" folder if it doesn't exist
if not os.path.exists("akulai/plugins"):
    os.makedirs("akulai/plugins")

# Use git submodules to fetch the default_plugins subdir in the akulai plugins repo
os.system("git submodule add {}".format(repo_url))
os.system("git submodule update --init --recursive")

# Move the files from the subdirectory to the local "akulai/plugins" folder
shutil.move("{}/".format(f"akulai-plugins/{subdir}"), "akulai/plugins/")

# Delete the files after copyiong them
shutil.rmtree("akulai-plugins")

# Use requests library to download vosk
vosk_url = "https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip"
response = requests.get(vosk_url)
with open("vosk-model-small-en-us-0.15.zip", "wb") as f:
    f.write(response.content)

# Extract the downloaded model
with zipfile.ZipFile("vosk-model-small-en-us-0.15.zip", "r") as zip_ref:
    zip_ref.extractall("akulai")

# Rename the extracted model to "vosk_model"
os.rename("akulai/vosk-model-small-en-us-0.15", "akulai/vosk_model")

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

    # Download and install ActivePerl
    activeperl_url = "https://downloads.activestate.com/ActivePerl/releases/5.32.0.320/ActivePerl-5.32.0-320-x86_64-mswin64-64int.msi"
    response = requests.get(activeperl_url)
    with open("ActivePerl.msi", "wb") as f:
        f.write(response.content)
        os.system("msiexec /i ActivePerl.msi /quiet")
        
        # Add the Perl executable to the system path
        os.system('setx path "%path%;C:\Perl64\bin"')

elif current_os == "Linux":
    # Install Node.js
    os.system("sudo apt-get update")
    os.system("sudo apt-get install -y nodejs")
    # Install the latest version of ActivePerl
    os.system("sudo apt-get install -y libperl-dev")
    os.system("wget -O - https://www.cpan.org/src/5.0/perl-5.32.0.tar.gz | tar xz")
    os.chdir("perl-5.32.0")
    os.system("./Configure -des -Dprefix=$HOME/perl")
    os.system("make")
    os.system("make test")
    os.system("make install")
    os.system("echo 'export PATH=$HOME/perl/bin:$PATH' >> ~/.bashrc")
    os.system("source ~/.bashrc")
else:
    print("This script only supports Windows and Ubuntu. Exiting...")

# Install requirements
os.system('pip install -r requirements.txt')
exit()
