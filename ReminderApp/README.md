A minimal reminder app I built while teaching OOPs.

Uses `outputformat` library to prettify output, the `main.py` acts as frontend, `timer.py` acts as backend.

- `main.py` runs on main thread.
- `timer.py` can either run on a background thread alongside `main.py` or as a standalone script on main thread (better approach).
- `REFRESH_INTERVAL` can be updated in utils.py

It's not so complex so y'all can just figure the installation on your own.
- Install requirements.
- Depending upon how you wanna run it, check out `main.py` and uncomment the threading lines if you want to run timer on a separate thread.
- Run `main.py` (and `timer.py` if you're not going with threaded approach).

LICENSE: Do What The F*ck You Want To
I really don't give a crap 👍
