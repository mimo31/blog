INSERT INTO category (name, url_name, description)
	VALUES
		("test math", "test_math", "a category with articles about the queen of sciences"),
		("test physics", "test_physics", "a category with articles studying nature in a systematic way");

INSERT INTO article (name, url_name, time_created, time_edited, description, category_id)
	VALUES
		("test Euler's identity", "test_eulers_identity", 1656841113.0, NULL, "This article reveals a secret about a famous formula.", 1),
		("test Fibonacci numbers", "test_fibonacci", 1657055830.0, 1657055980.0, "This article has been suggested by a friend from debating club.", 1);

INSERT INTO tag (name, url_name, description)
	VALUES
		("test complex numbers", "test_complex_numbers", "anything related to the set of complex numbers (the algebraic closure of the real numbers)"),
		("test c++", "test_cpp", "anything related to the programming language C++");

INSERT INTO article_tags (article_id, tag_id)
	VALUES
		(1, 1);

INSERT INTO comment (content, author, time_created, reply_to_id, article_id)
	VALUES
		("I agree that the Euler's identity is doof.", "test smart user", 1656841213.0, NULL, 2),
		("u stupid", "test rude user", 1656841313.0, 1, 2);
