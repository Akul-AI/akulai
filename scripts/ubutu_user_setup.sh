#!/bin/bash

# Define the GitHub repository URL and subdirectory
repo_url="https://github.com/Akul-AI/akulai-plugins"
subdir="default_plugins"

# Create the "akulai/plugins" folder if it doesn't exist
if [ ! -d "akulai/plugins" ]; then
  mkdir -p "akulai/plugins"
fi

# Change directory to the parent directory of the script
cd ..

# Use git submodules to fetch the default_plugins subdir in the akulai plugins repo
git submodule add $repo_url
git submodule update --init --recursive

# Move the files from the subdirectory to the local "akulai/plugins" folder
mv "$subdir"/* "akulai/plugins"

# Use wget to download vosk
wget "https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip"

# Extract the downloaded model
unzip "vosk-model-small-en-us-0.15.zip" -d "akulai"

# Rename the extracted model to "vosk_model"
mv "akulai/vosk-model-small-en-us-0.15" "akulai/vosk_model"

# Clean up the downloaded archive and extracted subdirectory
rm -r "$subdir"
rm "$subdir.zip"
rm "vosk-model-small-en-us-0.15.zip"

# Ask the user if they are using Windows
read -p "Are you using Ubuntu? (y/n) " choice

if [ "$choice" = "y" ]; then
    # Install Node.js and espeak-ng
    sudo apt-get update
    sudo apt-get install -y nodejs espeak-ng
    # Install the latest version of ActivePerl
    sudo apt-get install -y libperl-dev
    wget -O - "https://www.cpan.org/src/5.0/perl-5.32.0.tar.gz" | tar xz
    cd perl-5.32.0
    ./Configure -des -Dprefix=$HOME/perl
    make
    make test
    make install
    echo 'export PATH=$HOME/perl/bin:$PATH' >> ~/.bashrc
    source ~/.bashrc
else
    echo "This script is only compatible with Ubuntu. Check for other scripts that support Windows. Exiting..."
    exit
fi
