<script>
	import { toArticleDatetimeString } from "./datetime_utils.js";
	import { createEventDispatcher } from "svelte";

	const dispatch = createEventDispatcher();

	export let comment_data;

</script>

<div id="comment" style="margin-left: {comment_data.layer * 20}px;">
	<p>{comment_data.author}</p>
	<p>{toArticleDatetimeString(comment_data.time_created)}</p>
	<p>{comment_data.content}</p>
	<button type="button" on:click={() => dispatch("reply")}>reply</button>
</div>

<style>
	#comment {
		background-color: #dfdfff
	}
</style>
