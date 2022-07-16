INSERT INTO category (name, url_name, description)
	VALUES
		("Calculus of Variations", "calculus_of_variations", "articles about the calculus of variations");

INSERT INTO article (name, url_name, time_created, time_edited, description, category_id)
	VALUES
		("Calculus of Variations Basics", "standard_calculus_of_variations", "1657335849.0", "1658005102.0", "introducing the calculus of variations by showing two standard examples", "1");

INSERT INTO tag (name, url_name, description)
	VALUES
		("calculus of variations", "calculus_of_variations", "tag relating to the calculus of variations"),
		("mathematical optimization", "math_optimization", "tag relating to problems about optimizing some mathematical metric (a function, in the simplest case) often with a computer's help");

INSERT INTO article_tags (article_id, tag_id)
	VALUES
		(1, 1),
		(1, 2);

INSERT INTO comment (content, author, time_created, reply_to_id, article_id)
	VALUES
		("hi, this is me, the author", "mimo31", 1658005595.0, NULL, 1);
