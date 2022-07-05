<script>
	import { API_ROOT } from "./api_root.js";
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
	{#each $loaded_category.articles as article}
		<p>
			<strong>{article.name}</strong><br />
			<Link to="/article/{article.url_name}">open</Link>
			{article.description}
		</p>
	{/each}
{/if}
