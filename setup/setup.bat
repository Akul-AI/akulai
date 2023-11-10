@echo off

cd ".."
cd "akulai"
SET vosk_url=https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip
curl "-o" "vosk-model-small-en-us-0.15.zip" "%vosk_url%"
unzip "vosk-model-small-en-us-0.15.zip" "-d" "akulai"
mv "akulai\models\vosk-model-small-en-us-0.15" "akulai\models\vosk_model"
DEL  "vosk-model-small-en-us-0.15.zip"
cd ".."
sudo "apt-get" "update"
sudo "apt-get" "install" "-y" "nodejs"
wget "http://strawberryperl.com/download/5.32.0.1/strawberry-perl-5.32.0.1-64bit.tar.bz2"
tar "-xjf" "strawberry-perl-5.32.0.1-64bit.tar.bz2"
./strawberry-perl-5.32.0.1-64bit/install.pl
pip install -r requirements.txt
