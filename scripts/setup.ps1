cd ..
$repo_url="https://github.com/Akul-AI/akulai-plugins"
$subdir="plugins"
git submodule add $repo_url
git submodule update --init --recursive
Move-Item -Path "akulai-plugins/$subdir" -Destination "akulai"
Remove-Item -Recurse -Force "akulai-plugins"
$vosk_url="https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip"
Invoke-WebRequest -Uri $vosk_url -OutFile "vosk-model-small-en-us-0.15.zip"
Expand-Archive -Path "vosk-model-small-en-us-0.15.zip" -DestinationPath "akulai"
Rename-Item -Path "akulai/vosk-model-small-en-us-0.15" -NewName "akulai/vosk_model"
Remove-Item "vosk-model-small-en-us-0.15.zip"
$node_url = "https://nodejs.org/dist/latest-version/node-x64.msi"
Invoke-WebRequest -Uri $node_url -OutFile "node-x64.msi"
Start-Process msiexec.exe -ArgumentList "/i node-x64.msi /quiet" -Wait
$strawberry_perl_url = "http://strawberryperl.com/download/5.32.0.1/strawberry-perl-5.32.0.1-64bit.msi"
Invoke-WebRequest -Uri $strawberry_perl_url -OutFile "strawberry-perl.msi"
Start-Process msiexec.exe -ArgumentList "/i strawberry-perl.msi /quiet" -Wait
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";C:\Perl64\bin", "Machine")
pip install -r requirements.txt
