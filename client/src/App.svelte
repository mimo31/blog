<script>
	import { API_ROOT } from "./api_root.js";
	import { Router, Route, Link } from "svelte-navigator";	
	import { onMount } from "svelte";
	import { writable } from "svelte/store";
	import Category from "./Category.svelte";
	import Article from "./Article.svelte";
	import NavigationButton from "./NavigationButton.svelte";
	import RecentArticles from "./RecentArticles.svelte";
	import TagSearch from "./TagSearch.svelte";
	import TagOverview from "./TagOverview.svelte";

	let categories = writable([]);

	onMount(async () => {
		fetch(API_ROOT + "list_categories")
		.then(response => response.json())
		.then(data =>
		{
			categories.set(data.categories);
		});
	});
</script>

<Router>
	<main>
		<h1>
			mimo's blog
		</h1>
		<table>
			<NavigationButton link_to={"/"} text={"recent"} />
			{#each $categories as category}
				<NavigationButton link_to={"/category/" + category.url_name} text={category.name} />
			{/each}
			<NavigationButton link_to={"/tag_search"} text={"tag search"} />
			<NavigationButton link_to={"/about"} text={"about"} />
		</table>
		<div id="content">
			<Route path="/">
				<RecentArticles />
			</Route>
			<Route path="/category/*">
				<Route path=":url_name" let:params>
					<Category category_url_name={params.url_name} />
				</Route>
			</Route>
			<Route path="/article/*">
				<Route path=":url_name" let:params>
					<Article article_url_name={params.url_name} />
				</Route>
			</Route>
			<Route path="/tag_search">
				<TagSearch />
			</Route>
			<Route path="/tag/*">
				<Route path=":url_name" let:params>
					<TagOverview tag_url_name={params.url_name} />
				</Route>
			</Route>
			<Route path="/about">
				This will be the <i>about</i> page.
			</Route>
		</div>
	</main>
</Router>

<style>
	table {
		float: left;
		vertical-align: middle;
	}

	#content {
		float: left;
	}

	main {
		width: 100%;
		height: 100%;
		text-align: center;
		display: table;
	}
</style>
