#!/bin/bash

# Update the package list and install Python3 and pip if they are not already installed
sudo apt update
sudo apt install -y python3 python3-pip

# Install the required Python packages
pip3 install opencv-python pyzbar dbr qreader

# Verify the installations
echo "Installed packages:"
pip3 show opencv-python pyzbar dbr qreader
