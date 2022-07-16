<script>
	import { API_ROOT } from "./api_root.js";
	import ArticleBox from "./ArticleBox.svelte";
	import { writable } from "svelte/store";
	import { onMount } from "svelte";
	import { Link } from "svelte-navigator";

	export let category_url_name;
	let loading_url_name = "";
	let loaded_category = writable({});
	let something_loaded = false;

	function startCategoryLoad(url_name)
	{
		if (loading_url_name === url_name)
			return;
		loading_url_name = url_name;
		(async () => {
			fetch(API_ROOT + "get_category?url_name=" + url_name)
			.then(response => response.json())
			.then(data =>
			{
				if (data.url_name === category_url_name)
				{
					loaded_category.set(data);
					something_loaded = true;
				}
			});
		})();
	}
	$: startCategoryLoad(category_url_name);

	onMount(() => startCategoryLoad(category_url_name));
</script>
{#if something_loaded}
	<h2>{$loaded_category.name}</h2>
	<p class="content-description">
		{$loaded_category.description}
	</p>
	{$loaded_category.articles.length.toString() + " article" + ($loaded_category.articles.length !== 1? "s" : "")}
	{#each $loaded_category.articles as article}
		<ArticleBox article_data={article} />
	{/each}
{/if}
