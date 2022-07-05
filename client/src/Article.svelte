<script>
	import { API_ROOT } from "./api_root.js";
	import { writable } from "svelte/store";
	import { onMount } from "svelte";
	import { Link } from "svelte-navigator";
	import { toArticleDatetimeString } from "./datetime_utils.js";
	import TagPin from "./TagPin.svelte";

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
	<p>created {toArticleDatetimeString($loaded_article.time_created)}</p>
	{#if $loaded_article.time_edited !== null}
		<p>last edited {toArticleDatetimeString($loaded_article.time_edited)}</p>
	{/if}
	{#each $loaded_article.tags as tag_data}
		<TagPin {tag_data} />
	{/each}
	<p id="article_description">
		{$loaded_article.description}
	</p>
	{@html $loaded_article.content}
{/if}

<style>
	#article_description {
		font-weight: lighter;
	}
</style>
