# Checklist

## introduction

This folder host autonomous python project that you can use in order to validate your installation

## Project

### LED Matrice

set you virtual env in `checklist/neopixel`

```bash
python -m venv ${project}/checklist/neopixel
./bin/pip3 install -r requirements.txt
sudo ./bin/python3 main.py
```

### Camera

to take image manually

```bash
rpicam-still -o tmp-$(date +%y%m%d%H%M%S).png \
   --height 480 --width 640 --shutter 100000 \
   --gain 1 --immediate --nopreview \
   --awbgains 1,1
```

set you virtual env in `checklist/camera`

```bash
sudo apt update && sudo apt install python3-picamzero -y
python -m venv --system-site-packages ${project}/checklist/camera
./bin/pip3 install -r requirements.txt
sudo ./bin/python3 main.py
```

### Screen

this will display grid on your screen
set you virtual env in `checklist/screen`

```bash
python -m venv ${project}/checklist/screen
./bin/pip3 install -r requirements.txt
./bin/python3 main.py
```