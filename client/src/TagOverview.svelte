<script>
	import { API_ROOT } from "./api_root.js";
	import ArticleBox from "./ArticleBox.svelte";
	import { writable } from "svelte/store";
	import { onMount } from "svelte";
	import { Link } from "svelte-navigator";

	export let tag_url_name;
	let loading_url_name = "";
	let loaded_tag = writable({});
	let something_loaded = false;

	function startTagLoad(url_name)
	{
		if (loading_url_name === url_name)
			return;
		loading_url_name = url_name;
		(async () => {
			fetch(API_ROOT + "get_tag?url_name=" + url_name)
			.then(response => response.json())
			.then(data =>
			{
				if (data.url_name === tag_url_name)
				{
					loaded_tag.set(data);
					something_loaded = true;
				}
			});
		})();
	}
	$: startTagLoad(tag_url_name);

	onMount(() => startTagLoad(tag_url_name));
</script>
{#if something_loaded}
	<h3>{$loaded_tag.description}</h3>
	{$loaded_tag.articles.length.toString() + " article" + ($loaded_tag.articles.length !== 1? "s" : "")}
	{#each $loaded_tag.articles as article}
		<ArticleBox article_data={article} />
	{/each}
{/if}

