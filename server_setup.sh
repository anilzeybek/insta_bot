cd ~
sudo apt update
sudo apt install -y git build-essential npm postgresql postgresql-contrib python3-pip python3-dev libpq-dev nginx firefox
sudo npm install -g n
sudo n 15.11.0
git clone https://github.com/anilzeybek/insta_bot
cd insta_bot/bot
pip3 install -r requirements.txt
cd ../server
sudo npm i
cd ..
sudo -u postgres createdb instabot
sudo -u postgres psql instabot < instabot.sql
chmod +x geckodriver