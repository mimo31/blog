<script>
	import { API_ROOT } from "./api_root.js";
	import { writable } from "svelte/store";
	import { onMount } from "svelte";
	import { Link } from "svelte-navigator";

	export let article_url_name;
	let loading_url_name = "";
	let loaded_article = writable({});
	let something_loaded = false;

	function startArticleLoad(url_name)
	{
		if (loading_url_name === url_name)
			return;
		loading_url_name = url_name;
		something_loaded = false;
		(async () => {
			fetch(API_ROOT + "get_article?url_name=" + url_name)
			.then(response => response.json())
			.then(data =>
			{
				if (data.url_name === article_url_name)
				{
					loaded_article.set(data);
					something_loaded = true;
				}
			});
		})();
	}
	$: startArticleLoad(article_url_name);

	onMount(() => startArticleLoad(article_url_name));
</script>

{#if something_loaded}
	<h2>{$loaded_article.name}</h2>
	{@html $loaded_article.content}
{/if}
