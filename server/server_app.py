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
    return addheader({ "categories": list(map(lambda cat: { "id": cat[0], "name": cat[1], "url_name": cat[2] }, entries)) })

def parse_article_array(article_entries):
    return list(map(lambda art:
        {
            "id": art[0],
            "name": art[1],
            "url_name": art[2],
            "time_created": art[3],
            "description": art[4],
            "tags": article_tag_array(art[0])
        }, article_entries))

@app.route('/api/get_category', methods=['GET'])
def get_category():
    conn = get_db_connection()
    cat_url_name = request.args.get('url_name')
    entry = conn.cursor().execute("SELECT id,name,description FROM category WHERE url_name=?", (cat_url_name,)).fetchall()
    if len(entry) == 0:
        conn.close()
        return "category " + cat_url_name + " does not exist", 404
    else:
        cat_id = entry[0][0]
        article_entries = conn.cursor().execute("SELECT id,name,url_name,time_created,description FROM article WHERE category_id=?", (cat_id,)).fetchall()
        return addheader({
            "id": cat_id,
            "name": entry[0][1],
            "url_name": cat_url_name,
            "description": entry[0][2],
            "articles": parse_article_array(article_entries)
        })

@app.route('/api/get_tag', methods=['GET'])
def get_tag():
    conn = get_db_connection()
    tag_url_name = request.args.get('url_name')
    entry = conn.cursor().execute("SELECT id,name,description FROM tag WHERE url_name=?", (tag_url_name,)).fetchall()
    if len(entry) == 0:
        conn.close()
        return "tag " + tag_url_name + " does not exist", 404
    else:
        tag_id = entry[0][0]
        article_entries = conn.cursor().execute("SELECT article.id,article.name,article.url_name,article.time_created,article.description FROM article INNER JOIN article_tags ON article.id=article_tags.article_id WHERE article_tags.tag_id=?", (tag_id,)).fetchall()
        return addheader({
            "id": tag_id,
            "name": entry[0][1],
            "url_name": tag_url_name,
            "description": entry[0][2],
            "articles": parse_article_array(article_entries)
        })

def article_tag_array(article_id):
    conn = get_db_connection()
    entries = conn.cursor().execute("SELECT article_tags.tag_id,tag.name,tag.url_name FROM article_tags INNER JOIN tag ON article_tags.tag_id = tag.id WHERE article_tags.article_id=?", (article_id,)).fetchall()
    return list(map(lambda tag:
        {
            "id": tag[0],
            "name": tag[1],
            "url_name": tag[2]
        }, entries));

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
            "category_id": uentry[6],
            "tags": article_tag_array(uentry[0])
            })

@app.route('/api/list_articles', methods=['GET'])
def list_articles():
    conn = get_db_connection()
    article_entries = conn.cursor().execute("SELECT id,name,url_name,time_created,description FROM article").fetchall()
    return addheader({
        "articles": parse_article_array(article_entries)
        })

@app.route('/api/list_tags', methods=['GET'])
def list_tags():
    conn = get_db_connection()
    tag_entries = conn.cursor().execute("SELECT id,name,url_name,description FROM tag").fetchall()
    return addheader({ "tags":
        list(map(lambda tag:
            {
                "id": tag[0],
                "name": tag[1],
                "url_name": tag[2],
                "description": tag[3],
                "article_count": conn.cursor().execute("SELECT COUNT(*) FROM article_tags WHERE tag_id=?", (tag[0],)).fetchall()[0][0]
            }, tag_entries)) });
