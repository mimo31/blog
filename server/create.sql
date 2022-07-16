CREATE TABLE category (
	id				INTEGER PRIMARY KEY,
	name			CHAR(255) NOT NULL,
	url_name		CHAR(255) NOT NULL UNIQUE,
	description		TEXT NOT NULL
);

CREATE TABLE article (
	id 				INTEGER PRIMARY KEY,
	name 			CHAR(255) NOT NULL,
	url_name 		CHAR(255) NOT NULL UNIQUE,
	time_created	REAL NOT NULL,
	time_edited		REAL,
	/* filename		CHAR(255) NOT NULL, */
	description		TEXT NOT NULL,
	category_id		INTEGER NOT NULL,

	FOREIGN KEY(category_id) REFERENCES category(id)
);

CREATE TABLE tag (
	id				INTEGER PRIMARY KEY,
	name			CHAR(255) NOT NULL,
	url_name		CHAR(255) NOT NULL UNIQUE,
	description		TEXT NOT NULL
);

CREATE TABLE article_tags (
	id				INTEGER PRIMARY KEY,
	article_id		INTEGER NOT NULL,
	tag_id			INTEGER NOT NULL,
	FOREIGN KEY(article_id) REFERENCES article(id),
	FOREIGN KEY(tag_id) REFERENCES tag(id)
);

CREATE TABLE comment (
	id				INTEGER PRIMARY KEY,
	content			TEXT NOT NULL,
	author			CHAR(255) NOT NULL,
	time_created 	REAL NOT NULL,
	reply_to_id		INTEGER,
	article_id		INTEGER NOT NULL,

	FOREIGN KEY(reply_to_id) REFERENCES comment(id),
	FOREIGN KEY(article_id) REFERENCES article(id)
);
