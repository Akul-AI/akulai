# Define the GitHub repository URL and subdirectory
$repo_url = "https://github.com/Akul-AI/akulai-plugins"
$subdir = "default_plugins"

# Create the "akulai/plugins" folder if it doesn't exist
if (!(Test-Path "akulai/plugins")) {
    New-Item -ItemType Directory -Path "akulai/plugins"
}

# Change directory to the parent directory of the script
Set-Location ..

# Download the subdirectory from the GitHub repository
Invoke-WebRequest -Uri "$repo_url/tree/master/$subdir" -OutFile "$subdir.zip"

# Extract the files from the downloaded archive
Expand-Archive "$subdir.zip"

# Move the files from the subdirectory to the local "akulai/plugins" folder
Move-Item "$subdir\*" "akulai/plugins"

# Get the latest version of the vosk model
$vosk_version = (Invoke-WebRequest -Uri "https://api.github.com/repos/alphacep/vosk-api/releases/latest" | ConvertFrom-Json).tag_name

# Download the latest English vosk model
Invoke-WebRequest -Uri "https://github.com/alphacep/vosk-api/releases/download/$vosk_version/vosk-model-en-$vosk_version.zip" -OutFile "vosk-model-en-$vosk_version.zip"

# Extract the downloaded model
Expand-Archive "vosk-model-en-$vosk_version.zip" -DestinationPath "akulai"

# Rename the extracted model to "vosk_model"
Rename-Item -Path "vosk-model-en-$vosk_version" -NewName "vosk_model"

# Clean up the downloaded archive and extracted subdirectory
Remove-Item "$subdir" -Recurse
Remove-Item "$subdir.zip"
Remove-Item "vosk-model-en-$vosk_version.zip"

# Ask the user if they are using Windows
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
    $activeperl_url = (Invoke-WebRequest -Uri "https://downloads.activestate.com/ActivePerl/releases" | Select-String -Pattern "href=".*ActivePerl.*msi"").line
    $activeperl_url = $activeperl_url -replace "href=","" -replace """,""
    Invoke-WebRequest -Uri $activeperl_url -OutFile "ActivePerl.msi"
    Start-Process "msiexec" -ArgumentList "/i ActivePerl.msi /quiet" -Wait
    
}
else {
    Write-Host "This script is only compatible with Windows. Check for other scripts that support your system. Exiting..."
    Exit
}
