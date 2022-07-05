rm -r venv
python3 -m venv venv
. venv/bin/activate
pip3 install Flask mod_wsgi
deactivate
