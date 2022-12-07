# Script to setup pycaret on AWS Cloud9 IDE

sudo apt-get update;
sudo apt-get install -y python3.8;
sudo apt-get install -y python3.8-distutils;
sudo add-apt-repository ppa:deadsnakes/ppa;
sudo unlink /usr/bin/python3 && sudo ln -s /usr/bin/python3.8 /usr/bin/python3;
sudo unlink /usr/bin/python && sudo ln -s /usr/bin/python3 /usr/bin/python;
sudo pip3 install --upgrade setuptools;
sudo pip3 install --upgrade pip;
sudo pip3 install --upgrade distlib;
# --pre and [full] were used when pycaret3 wasnt the latest.
# ignore pexpect was added due to an error when pip couldnt uninstall pexpect
sudo pip3 install --pre pycaret --ignore-installed pexpect;
