<script>
	import { Link } from "svelte-navigator";
	import TagPin from "./TagPin.svelte";
	import { toArticleDatetimeString } from "./datetime_utils.js";
	export let article_data;
</script>

<div id="article_box">
	<strong>{article_data.name}</strong><br />
	{toArticleDatetimeString(article_data.time_created)}<br />
	<Link to="/article/{article_data.url_name}">open</Link>
	{article_data.description}
	<br />
	{#each article_data.tags as tag_data}
		<TagPin {tag_data} />
	{/each}
</div>

<style>
	#article_box {
		margin: 15px;
	}
</style>
