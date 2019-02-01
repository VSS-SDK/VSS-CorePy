import subprocess
import os
import sys
import shutil

from setuptools import setup, find_packages
from distutils.spawn import find_executable

# Find the Protocol Compiler.
if 'PROTOC' in os.environ and os.path.exists(os.environ['PROTOC']):
    protoc = os.environ['PROTOC']
elif os.path.exists("../src/protoc"):
    protoc = "../src/protoc"
elif os.path.exists("../src/protoc.exe"):
    protoc = "../src/protoc.exe"
elif os.path.exists("../vsprojects/Debug/protoc.exe"):
    protoc = "../vsprojects/Debug/protoc.exe"
elif os.path.exists("../vsprojects/Release/protoc.exe"):
    protoc = "../vsprojects/Release/protoc.exe"
else:
    protoc = find_executable("protoc")


def generate_state():
    protoc_command = [ protoc, "-I/vsscorepy/protos", "-I.", "--python_out=.", "protos/state.proto" ]

    if subprocess.call(protoc_command) != 0:
        sys.exit(-1)

    shutil.move("protos/state_pb2.py", "vsscorepy/protos/state_pb2.py")


def generate_command():
    protoc_command = [ protoc, "-I/src/protos", "-I.", "--python_out=.", "protos/command.proto" ]
    
    if subprocess.call(protoc_command) != 0:
        sys.exit(-1)

    shutil.move("protos/command_pb2.py", "vsscorepy/protos/command_pb2.py")


def generate_debug():
    protoc_command = [ protoc, "-I/vsscorepy/protos", "-I.", "--python_out=.", "protos/debug.proto" ]
    
    if subprocess.call(protoc_command) != 0:
        sys.exit(-1)

    shutil.move("protos/debug_pb2.py", "vsscorepy/protos/debug_pb2.py")


def generate_control():
    protoc_command = [ protoc, "-I/vsscorepy/protos", "-I.", "--python_out=.", "protos/control.proto" ]
    
    if subprocess.call(protoc_command) != 0:
        sys.exit(-1)

    shutil.move("protos/control_pb2.py", "vsscorepy/protos/control_pb2.py")


if __name__ == '__main__':
    generate_state()
    generate_control()
    generate_command()
    generate_debug()

    setup(
        name='vsscorepy',
        version='0.1.1',
        packages=find_packages(),
        license='GPL3',
        url='https://vss-sdk.github.io/',
        author_email='johnathanfercher22@gmail.com',
        keywords=["IEEE", "VSS", "Robot Soccer", "VSS-SDK"],
        tests_require=["pytest",]
    )
