#!/bin/bash

cd ..
vosk_url="https://alphacephei.com/vosk/models/vosk-model-small-en-us-0.15.zip"
curl -o "vosk-model-small-en-us-0.15.zip" $vosk_url
unzip "vosk-model-small-en-us-0.15.zip" -d "akulai"
mv "akulai/model/vosk-model-small-en-us-0.15" "akulai/model/vosk_model"
rm "vosk-model-small-en-us-0.15.zip"
sudo apt-get update
sudo apt-get install -y nodejs
pip install -r requirements.txt
