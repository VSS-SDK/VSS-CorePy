#!/usr/bin/env bash

INSTALL_BASE() {
    apt-get update && apt-get upgrade
    apt-get -y install lsb-release git

    DISTRO=`lsb_release -si`
    RELEASE=`lsb_release -sr`
    RELEASE_DEBIAN=`lsb_release -sr | cut -c1-1`
    ARCHITECTURE=`uname -m`
}

INSTALL_PYTHON_DEPENDENCIES() {
    pip3 install pytest
    pip3 install zmq
    pip3 install git+https://github.com/VSS-SDK/VSS-CorePy 
}