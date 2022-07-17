cd /home/ubuntu/blog
. venv/bin/activate
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8000
mod_wsgi-express start-server wsgi.py --processes 1 --port 8000
