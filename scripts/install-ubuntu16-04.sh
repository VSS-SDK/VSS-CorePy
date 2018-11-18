#!/usr/bin/env bash

INSTALL_UBUNTU_16_04 () {
    apt-get -y install pkg-config
    apt-get -y install g++ cmake libzmqpp3 libzmqpp-dev protobuf-compiler libprotobuf-dev libboost-all-dev
    apt-get -y install python3 python3-pip
    INSTALLED=1
}