<script>
	import { API_ROOT } from "./api_root.js";
	import ArticleBox from "./ArticleBox.svelte";
	import { writable } from "svelte/store";
	import { onMount } from "svelte";

	let loaded = false;
	let articles = writable([]);

	onMount(async () => {
		fetch(API_ROOT + "list_articles")
			.then(response => response.json())
			.then(data =>
			{
				articles.set(data.articles);
			});
	});
</script>

{#each $articles as article}
	<ArticleBox article_data={article} />
{/each}
