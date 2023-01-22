#!/bin/bash

# Define the GitHub repository URL and subdirectory
repo_url="https://github.com/Akul-AI/akulai-plugins"
subdir="default_plugins"

# Create the "akulai/plugins" folder if it doesn't exist
if [ ! -d "akulai/plugins" ]; then
    mkdir -p akulai/plugins
fi

# Change directory to the parent directory of the script
cd ..

# Download the subdirectory from the GitHub repository
curl -LJO $repo_url/tree/master/$subdir

# Extract the files from the downloaded archive
tar xvf $subdir.tar

# Move the files from the subdirectory to the local "akulai/plugins" folder
mv $subdir/* akulai/plugins/

# Clean up the downloaded archive and extracted subdirectory
rm -rf $subdir $subdir.tar

# Get the latest version of the vosk model
vosk_version=$(curl -s https://api.github.com/repos/alphacep/vosk-api/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")')

# Download the latest English vosk model
curl -LJO https://github.com/alphacep/vosk-api/releases/download/${vosk_version}/vosk-model-en-${vosk_version}.zip

# Unzip the downloaded model
unzip vosk-model-en-${vosk_version}.zip

# Rename the extracted model to "vosk_model"
mv vosk-model-en-${vosk_version} akulai/vosk_model

# Clean up the downloaded archive and extracted subdirectory
rm -rf $subdir $subdir.tar vosk-model-en-${vosk_version}.zip

# Ask the user if they are using Ubuntu
read -p "Are you using Ubuntu? (y/n) " choice

if [ "$choice" = "y" ]; then
    # Download and install the latest version of Node.js
    curl -sL https://deb.nodesource.com/setup_current.x | sudo -E bash -
    sudo apt-get install -y nodejs

    # Download the latest version of espeakng
    sudo apt-get install espeak-ng
    
    # Download and install the Perl interpreter
    sudo apt-get install -y perl

    # Download and install cpanm
    curl -L https://cpanmin.us | perl - App::cpanminus

else
    echo "This script is only compatible with Ubuntu. Check for other scripts that support your system. Exiting..."
    exit 1
fi
