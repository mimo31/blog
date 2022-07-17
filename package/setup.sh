cd /home/ubuntu/blog
ls | grep -xv "venv" | xargs rm -rf
cp ../package/server/*.py ../package/server/*.sql ../package/server/articles ../package/public ../package/start_server.sh ./ -r
chmod +x start_server.sh
sqlite3 database.db < create.sql
