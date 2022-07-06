<script>
	import { API_ROOT } from "./api_root.js";
	import { createEventDispatcher } from "svelte";

	export let top_description;
	export let submit_button_text;
	export let article_id;
	export let reply_to_id;
	export let layer;
	export let cancelable;

	let author_input = "";
	let content_input = "";

	const dispatch = createEventDispatcher();

	function submit()
	{
		(async () => {
			fetch(API_ROOT + "post_comment", {
				method: 'POST',
				headers: { "Content-Type": "text/plain" },
				body: JSON.stringify({
					"article_id": article_id,
					"content": content_input,
					"author": author_input,
					"time_created": Date.now() / 1000,
					"reply_to_id": reply_to_id
				})
			}).then(response => response.json())
				.then(data =>
					{
						dispatch('submit', data);
						author_input = "";
						content_input = "";
					});
		})();
	}
</script>

<div style="margin-left: {layer * 20}px;">
	<p>
		{top_description}
	</p>
	Author (you): <input type="text" bind:value={author_input}> <br />
	Your comment: <input type="text" bind:value={content_input}> <br />
	<button type="button" on:click={submit}>{submit_button_text}</button>
	{#if cancelable}
		<button type="button" on:click={() => dispatch("cancel")}>cancel</button>
	{/if}
</div>
