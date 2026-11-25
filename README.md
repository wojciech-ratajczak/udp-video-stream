# udp-video-stream

stream wideo po UDP między dwoma urządzeniami, nadawca i odbiorca.

## co jest póki co

- hello.py, nadawca-udp.py, odbiorca-udp.py - pierwsze testy UDP w Pythonie, wysyłanie gołych pakietów (localhost, lan)
- pipelines.txt - komendy gstreamera, nadawca i odbiorca, kamera -> H.264 -> RTP -> UDP -> okno
- nadawca-gstreamer.py - nadawca w pythonie skleja pipeline z pipelines

## co działa

- localhost na windowsie i na linuxie
- laptop -> PC po LAN, obraz dochodzi bez problemu
- nadawca-gstreamer.py: kamera laptopa -> PC po LAN, start i stop z programu

## jak odpalić

### wersja z terminala (pipelines.txt)

1. na urządzeniu odbierającym odpalić odbiorcę z pipelines.txt
2. na urządzeniu wysyłającym w nadawcy podmienić `host=` na IP odbiorcy i ewentualnie `device=` na swoją kamerę
3. u odbiorcy otworzyć port w firewallu, np. `sudo ufw allow from <sieć> to any port 5006 proto udp`
   (nadawca nic nie musi, ruch wychodzący jest domyślnie przepuszczany)

windows: zamiast `v4l2src ... ! jpegdec` jest `mfvideosrc`



## kamera uwaga!

moja kamera daje 1280x720@30 tylko jako MJPG, surowy YUYV w 720p ma tylko 10 fps.
dlatego na linuxie najpierw zamawiam `image/jpeg` i rozpakowuję `jpegdec`, potem dopiero `videoconvert`.
na windowsie robi to za mnie Media Foundation. formaty kamery: `v4l2-ctl -d /dev/video0 --list-formats-ext`

## co dalej

- wielokrotny start/stop zamiast entera i konczenia programu
- poprawienie stabilnosci?

## wymagania

Python 3, GStreamer 1.x z pluginami base/good/bad/ugly + libav (x264enc, avdec_h264, jpegdec), `gst-launch-1.0` w PATH, PyGObject (na później)