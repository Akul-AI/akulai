# Define the GitHub repository URL and subdirectory
$repo_url = "https://github.com/Akul-AI/akulai-plugins"
$subdir = "default_plugins"

# Create the "akulai/plugins" folder if it doesn't exist
if (!(Test-Path "akulai/plugins")) {
New-Item -ItemType Directory -Path "akulai/plugins"
}

# Change directory to the parent directory of the script
Set-Location ..

# Use git submodules to fetch the default_plugins subdir in the akulai plugins repo
git submodule add $repo_url
git submodule update --init --recursive

# Move the files from the subdirectory to the local "akulai/plugins" folder
Move-Item "$subdir*" "akulai/plugins"

# Use a hardcoded version of vosk which gets downloaded from their website
Invoke-WebRequest -Uri "https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip" -OutFile "vosk-model-small-en-us-0.15.zip"

Extract the downloaded model
Expand-Archive "vosk-model-small-en-us-0.15.zip" -DestinationPath "akulai"

Rename the extracted model to "vosk_model"
Rename-Item -Path "vosk-model-small-en-us-0.15" -NewName "vosk_model"

Clean up the downloaded archive and extracted subdirectory
Remove-Item "$subdir" -Recurse
Remove-Item "$subdir.zip"
Remove-Item "vosk-model-small-en-us-0.15.zip"

Ask the user if they are using Windows
$choice = Read-Host "Are you using Windows? (y/n) "

if ($choice -eq "y") {
    # Download and install the latest version of Node.js
    Invoke-WebRequest -Uri "https://nodejs.org/dist/latest-version/node-x64.msi" -OutFile "node-x64.msi"
    Start-Process "msiexec" -ArgumentList "/i node-x64.msi /quiet" -Wait
    # Download and install the latest version of espeak-ng
    $espeak_ng_url = (Invoke-WebRequest -Uri "https://sourceforge.net/projects/espeak/files/espeak-ng/" | Select-String -Pattern "href=".*espeak-ng.*msi"").line
    $espeak_ng_url = $espeak_ng_url -replace "href=","" -replace """,""
    Invoke-WebRequest -Uri "https://sourceforge.net$espeak_ng_url" -OutFile "espeak-ng.msi"
    Start-Process "msiexec" -ArgumentList "/i espeak-ng.msi /quiet" -Wait

    # Download and install the latest version of ActivePerl
    $activeperl_url = (Invoke -WebRequest -Uri "https://downloads.activestate.com/ActivePerl/releases" | Select-String -Pattern "href=".*ActivePerl.*msi"").line
    $activeperl_url = $activeperl_url -replace "href=","" -replace """,""
    Invoke-WebRequest -Uri $activeperl_url -OutFile "ActivePerl.msi"
    Start-Process "msiexec" -ArgumentList "/i ActivePerl.msi /quiet" -Wait
} 
else {
    Write-Host "This script is only compatible with Windows. Check for other scripts that support your system. Exiting..."
    Exit
}
