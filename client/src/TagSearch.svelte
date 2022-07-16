<script>
	import { API_ROOT } from "./api_root.js";
	import TagBox from "./TagBox.svelte";
	import { onMount } from "svelte";
	import { writable } from "svelte/store";

	let tags = writable([]);

	onMount(async () => {
		fetch(API_ROOT + "list_tags")
		.then(response => response.json())
		.then(data =>
		{
			tags.set(data.tags);
		});
	});

	let search_text = "";
</script>

<p>You can search for tags here.</p>
<input type="text" bind:value={search_text}>
{#each $tags as tag_data}
	{#if tag_data.name.includes(search_text) }
		<TagBox {tag_data} />
	{/if}
{/each}
