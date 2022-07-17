sudo apt -y install python-is-python3 python3-dev python3.10-venv apache2 apache2-dev sqlite3 moreutils

cd /home/ubuntu
mkdir blog
cd blog
python -m venv venv
. venv/bin/activate
pip install Flask mod_wsgi
deactivate
