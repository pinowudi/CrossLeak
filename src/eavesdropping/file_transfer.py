#!/usr/bin/env python
import os
import yaml

with open("setup.yaml","r") as f:
    setup = yaml.load(f, Loader=yaml.FullLoader)

RV_FOLDER = setup["raw_video_folder"]
V_FOLDER = setup["dated_video_folder"]
W_FOLDER = setup["wifi_data_folder"]
A_FOLDER = setup["audio_folder"]
AI_SERVER = setup["AI_SERVER"]
AI_USER = setup["AI_USER"]

os.system("scp "+V_FOLDER + "*.h264 " + AI_USER + "@" + AI_SERVER +":~/video/ > /dev/null 2>&1")
os.system("scp " + W_FOLDER + "* " + AI_USER + "@" + AI_SERVER +":~/wifi_data/ > /dev/null 2>&1")
os.system("scp " + A_FOLDER + "*.wav " + AI_USER + "@" + AI_SERVER +":~/audio/ > /dev/null 2>&1")

os.system("rm -rf "+RV_FOLDER+"*")
os.system("rm -rf "+V_FOLDER+"*")
os.system("rm -rf "+W_FOLDER+"*")
os.system("rm -rf "+A_FOLDER+"*")


