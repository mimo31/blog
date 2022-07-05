<script>
	import { API_ROOT } from "./api_root.js";
	import { Router, Route, Link } from "svelte-navigator";	
	import { onMount } from "svelte";
	import { writable } from "svelte/store";
	import Category from "./Category.svelte";
	import Article from "./Article.svelte";
	import NavigationButton from "./NavigationButton.svelte";
	import RecentArticles from "./RecentArticles.svelte";

	let categories = writable([]);

	onMount(async () => {
		fetch(API_ROOT + "list_categories")
		.then(response => response.json())
		.then(data =>
		{
			categories.set(data.categories);
			//console.log(data.categories);
		});
	});
	
	/*
	let category_url_name = "";
	let category_ready = false;
	let category_name = "";
	let category_articles = writable([]);
	
	function gotoCategory(name, url_name)
	{
		console.log("going to " + url_name);
		category_url_name = url_name;
		category_name = name;
		category_ready = false;
		category_articles.set([]);
		(async () => {
			fetch(API_ROOT + "get_category?url_name=" + url_name)
			.then(response => response.json())
			.then(data =>
			{
				if (data.url_name === category_url_name)
				{
					category_articles.set(data.articles);
					category_ready = true;
					console.log(data.articles);
				}
			});
		})();
	}
	
	let article_name = "";
	let article_url_name = "";
	let article_ready = false;
	let article_data = {};

	function gotoArticle(name, url_name)
	{
		article_url_name = url_name;
		article_name = name;
		article_ready = false;
		article_data.set({});
		(async () => {
			fetch(API_ROOT + "get_article?url_name=" + url_name)
			.then(response => response.json())
			.then(data =>
			{
				console.log("checking validity");
				if (data.url_name === article_url_name)
				{
					article_data = data;
					//article_data.set(data);
					console.log("setting data to...");
					console.log(data);
					console.log("data is...");
					console.log(data.content);
					console.log("content is...");
					console.log(article_data.content);
					article_ready = true;
				}
			});
		})();
	}
	*/
</script>

<Router>
	<main>
		<table>
			<NavigationButton link_to={"/"} text={"recent"} />
			{#each $categories as category}
				<NavigationButton link_to={"/category/" + category.url_name} text={category.name} />
			{/each}
			<NavigationButton link_to={"/tag_search"} text={"tag search"} />
			<NavigationButton link_to={"/about"} text={"about"} />
		</table>
		<Route path="/">
			<RecentArticles />
		</Route>
		<Route path="/category/*">
			<Route path=":url_name" let:params>
				<Category category_url_name={params.url_name} />
				<!--
				{#each $category_articles as article}
				<p>
					<strong>{article.name}</strong><br />
					<Link to="/article/{article.url_name}" on:click="{gotoArticle(article.name, article.url_name)}">open</Link>
					{article.description}
				</p>
				{/each}
				category with URL {params.name}
				-->
			</Route>
		</Route>
		<Route path="/article/*">
			<Route path=":url_name" let:params>
				<Article article_url_name={params.url_name} />
			</Route>
		</Route>
		<Route path="/tag_search">
			You'll be able to search articles by tags here.
		</Route>
		<Route path="/about">
			This will be the <i>about</i> page.
		</Route>
	</main>
</Router>

<style>
	main {
		text-align: center;
		padding: 1em;
		max-width: 240px;
		margin: 0 auto;
	}

	h1 {
		color: #ff3e00;
		text-transform: uppercase;
		font-size: 4em;
		font-weight: 100;
	}

	@media (min-width: 640px) {
		main {
			max-width: none;
		}
	}
</style>
