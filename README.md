# udp-video-stream

stream wideo po UDP między dwoma urządzeniami, nadawca i odbiorca.

## co jest poki co

- hello.py, nadawca-udp.py, odbiorca-udp.py - pierwsze testy UDP w Pythonie, wysyłanie gołych pakietów (localhost, lan)
- pipelines.txt - komendy gstreamera, nadawca i odbiorca. kamera -> H.264 -> RTP -> UDP -> okno
- nadawca-gstreamer.py - na razie pusty, ma odpalać i zatrzymywać stream z Pythona

## co dziala

- localhost na windowsie i na linuxie
- laptop -> PC po LAN, obraz dochodzi bez problemu

## jak odpalic

1. na urządzeniu odbierającym odpalić odbiorcę z pipelines.txt
2. na urządzeniu wysyłającym w nadawcy podmienić `host=` na IP odbiorcy i ewentualnie `device=` na swoją kamerę
3. u odbiorcy otworzyć port w firewallu, np. `sudo ufw allow from <sieć> to any port 5006 proto udp`
   (nadawca nic nie musi, ruch wychodzący jest domyślnie przepuszczany)

windows: zamiast `v4l2src ... ! jpegdec` jest `mfvideosrc`

## kamera uwaga!

moja kamera daje 1280x720@30 tylko jako MJPG, surowy YUYV w 720p ma tylko 10 fps.
dlatego na linuxie najpierw zamawiam `image/jpeg` i rozpakowuje `jpegdec`, potem dopiero `videoconvert`.
na windowsie robi to za mnie Media Foundation. formaty kamery: `v4l2-ctl -d /dev/video0 --list-formats-ext`

## do zrobienia

- start/stop streamu komendą po UDP bez wyłączania programu (python)
- test na innym środowisku, przez WireGuarda, z inną kamerą

## wymagania

Python 3, GStreamer 1.x z pluginami base/good/bad/ugly + libav (x264enc, avdec_h264, jpegdec), PyGObject (na później)