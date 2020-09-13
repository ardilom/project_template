#!/bin/bash

function print_green(){
    echo -e "\033[32m$1\033[39m"
}


#!/bin/sh

print_green "Installing python 3.6"
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get -y install python3.6 python3.6-dev

print_green "Installing aptitude dependencies"
sudo apt-get -y install python-pip python-virtualenv build-essential

print_green "Installing image libraries"
sudo apt-get -y install libjpeg-dev zlib1g-dev zlib1g-dev

print_green "Installing translation libraries"
sudo apt-get -y install gettext

print_green "Installing postgres"
sudo apt-get -y install postgresql
sudo apt-get -y install libpq-dev

print_green "Installing pipenv"
sudo pip install pipenv

print_green "Installing python requirements with pipenv defined on Pipfile"
pipenv install

print_green "Installing yarn"
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt update
sudo apt install yarn nodejs
yarn –version

print_green "Installing vue-cli"
yarn global add @vue/cli

print_green "Installing yarn dependencies"
yarn install
