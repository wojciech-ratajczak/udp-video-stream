# udp-video-stream

docelowo: stream wideo z łazika do centrali po UDP.

## Co jest póki co :

- hello.py, nadawca-udp.py, odbiorca-udp.py - pierwsze testy UDP w Pythonie, wysyłanie gołych pakietów (localhost, lan)
- pipelines.txt - komendy gstreamera, nadawca i odbiorca. kaamera -> H.264 -> RTP -> UDP -> okno. Działa na localhost
- nadawca-gstreamer.py - na razie pusty, ma odpalac i zatrzymywac stream z Pythona

## Do zrobienia

- stream między dwoma komputerami
- start/stop streamu komendą po UDP
- odpalenie na Linux (v4l2src zamiast mfvideosrc)

## Wymagania

Python 3, GStreamer 1.x (x264enc, avdec_h264)
