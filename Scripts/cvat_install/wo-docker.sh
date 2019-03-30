#! /bin /bash
sudo apt-get remove docker docker-engine docker.io containerd runc
sudo apt-get update

sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common
curl -fsSl https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo apt-key fingerprint 0EBFCD88

sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
#if you are not using ubuntu, change "$(lsb_release -cs)" into your parent Ubuntu distro
#also amd64 can be changed accordingly, into either one of these: armhf arm64 ppc64le or s390x

sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
sudo docker run hello-world
