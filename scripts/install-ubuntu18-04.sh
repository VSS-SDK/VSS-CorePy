#!/usr/bin/env bash

INSTALL_UBUNTU_18_04 () {
    apt-get -y install pkg-config
    apt-get -y install g++ cmake libzmq5 libzmq3-dev protobuf-compiler libprotobuf-dev libboost-all-dev
    apt-get -y install python3 pip3
    INSTALLED=1
}