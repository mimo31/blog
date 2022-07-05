sudo apt -y install python-is-python3 python3-dev python3.10-venv apache2 apache2-dev sqlite3

cd /home/ubuntu
mkdir blog
cd blog
cp ../setup_files/server/*.py ../setup_files/server/*.sql ../setup_files/server/articles ../setup_files/public ../setup_files/start_server.sh ./ -r
chmod +x start_server.sh
python -m venv venv
. venv/bin/activate
pip install Flask mod_wsgi
deactivate
sqlite3 database.db < create.sql
