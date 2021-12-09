#!/bin/sh
curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
sudo apt-get install -y nodejs
npm install
cd api
python -m venv venv
source venv/bin/activate
pip install flask python-dotenv