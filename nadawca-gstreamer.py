##to do: on i off pipeline nadawcy z pyjtona, subprocess.Popen


import subprocess

HOST = "127.0.0.1"  #127 loopback
PORT = 5006


#zrodlo testowe dla PC:
ZRODLO = " videotestsrc ! videoconvert"

#zrodlo dla laptopa omarchy:
#ZRODLO = " v4l2src device=/dev/video0 ! image/jpeg,width=1280,height=720,framerate=30/1 ! jpegdec ! videoconvert"

argumentgstreamer = "video/x-raw,format=NV12,width=1280,height=720,framerate=30/1 ! x264enc tune=zerolatency bitrate=2000 speed-preset=ultrafast key-int-max=30 bframes=0 sliced-threads=true ! rtph264pay config-interval=1 pt=96 mtu=1200 ! udpsink host=" + HOST + " port=" +str(PORT) +" sync=false"

POTOK =("gst-launch-1.0" + ZRODLO + " ! " + argumentgstreamer)

proces = subprocess.Popen(POTOK.split())
input("stream dziala, Enter = stop\n")


proces.terminate()
proces.wait()

print("zatrzymano")