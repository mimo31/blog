<script>
	import { Link } from "svelte-navigator";

	export let tag_data;
</script>

<div id="tag_box">
	<Link to="/tag/{tag_data.url_name}">{tag_data.name}</Link><br />
	{tag_data.article_count.toString() + " article" + (tag_data.article_count !== 1 ? "s" : "")}<br />
	{tag_data.description}
</div>

<style>
	#tag_box {
		border: 2px blue;
		margin: 15px;
	}
</style>
