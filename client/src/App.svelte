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
		<div id="top-title">
			<h1 id="top-title-headline">
				&#9830;&#9830;  mimo's blog  &#9830;&#9830;
			</h1>
		</div>
		<div id="flex-root-container">
			<div id="sidebar">
				<table>
					<NavigationButton link_to={"/"} text={"recent"} />
					{#each $categories as category}
						<NavigationButton link_to={"/category/" + category.url_name} text={category.name} />
					{/each}
					<NavigationButton link_to={"/tag_search"} text={"tag search"} />
					<NavigationButton link_to={"/about"} text={"about"} />
				</table>
			</div>
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
		</div>
	</main>
</Router>

<style>
	table {
		/* position: fixed; */
		/* float: left;
		vertical-align: middle; */
		margin: auto;
		margin-top: 10px;
		margin-bottom: 10px;
	}

	#content {
		flex: 8;
		padding: 10px;
	}

	#flex-root-container {
		display: flex;
	}

	#sidebar {
		flex: 1;
		background-color: #f0f0ff;
		min-height: 100vh;
	}

	#top-title {
		width: 100%;
	}

	#top-title-headline {
		/* position: fixed; */
	}

	main {
		width: 100%;
		height: 100%;
		text-align: center;
		display: table;
	}
</style>
