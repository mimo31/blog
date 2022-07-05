from flask import Flask, jsonify, request, send_file
import sqlite3

app = Flask(__name__,
        static_url_path='',
        static_folder='public')

def get_db_connection():
    c = sqlite3.connect('database.db')
    return c

def send_index():
    resp = send_file("public/index.html")
    print(resp)
    return resp

@app.route("/")
def index_route0():
    return send_index()

@app.route("/article/<trail_url>")
def index_route1(trail_url):
    return send_index()

@app.route("/category/<trail_url>")
def index_route2(trail_url):
    return send_index()

@app.route("/tag_search")
def index_route3():
    return send_index()

@app.route("/about")
def index_route4():
    return send_index()

def addheader(data_object):
    response = jsonify(data_object)
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:8080')
    return response

@app.route('/api/list_categories', methods=['GET'])
def list_categories():
    conn = get_db_connection()
    entries = conn.cursor().execute("SELECT id,name,url_name FROM category").fetchall()
    conn.close()
    print(entries)
    return addheader({ "categories": list(map(lambda cat: { "id": cat[0], "name": cat[1], "url_name": cat[2] }, entries)) })

def parse_article_array(article_entries):
    return list(map(lambda art:
        {
            "id": art[0],
            "name": art[1],
            "url_name": art[2],
            "time_created": art[3],
            "description": art[4]
        }, article_entries))

@app.route('/api/get_category', methods=['GET'])
def get_category():
    conn = get_db_connection()
    cat_url_name = request.args.get('url_name')
    entry = conn.cursor().execute("SELECT id,name FROM category WHERE url_name=?", (cat_url_name,)).fetchall()
    if len(entry) == 0:
        conn.close()
        return "category " + cat_url_name + " does not exist", 404
    else:
        cat_id = entry[0][0]
        cat_name = entry[0][1]
        article_entries = conn.cursor().execute("SELECT id,name,url_name,time_created,description FROM article WHERE category_id=?", (cat_id,)).fetchall()
        return addheader({
            "id": cat_id,
            "name": cat_name,
            "url_name": cat_url_name,
            "articles": parse_article_array(article_entries)
        })

@app.route('/api/get_article', methods=['GET'])
def get_article():
    conn = get_db_connection()
    art_url_name = request.args.get('url_name')
    entry = conn.cursor().execute("SELECT id,name,time_created,time_edited,filename,description,category_id FROM article WHERE url_name=?", (art_url_name,)).fetchall()
    if len(entry) == 0:
        conn.close()
        return "article " + art_url_name + " does not exist", 404
    else:
        uentry = entry[0]
        filehandle = open("articles/" + uentry[4], 'r');
        article_content = filehandle.read();
        filehandle.close()
        return addheader({
            "id": uentry[0],
            "name": uentry[1],
            "url_name": art_url_name,
            "time_created": uentry[2],
            "time_edited": uentry[3],
            "content": article_content,
            "description": uentry[5],
            "category_id": uentry[6]
            })

@app.route('/api/list_articles', methods=['GET'])
def list_articles():
    conn = get_db_connection()
    article_entries = conn.cursor().execute("SELECT id,name,url_name,time_created,description FROM article").fetchall()
    return addheader({
        "articles": parse_article_array(article_entries)
        })
