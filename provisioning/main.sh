#!/bin/bash

set -e # Stop script on error

sudo apt-get -y update
sudo apt-get -y upgrade

sudo apt-get -y install python-pip

sudo pip upgrade pip
sudo pip install virtualenv
virtualenv /home/vagrant/env-django-google-calendar -p python3

echo ". /home/vagrant/env-django-google-calendar/bin/activate" >> ~/.bashrc
echo "cd /home/vagrant/django-google-calendar" >> ~/.bashrc
