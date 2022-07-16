<script>
	export let tag_data;
	import { Link } from "svelte-navigator";
</script>

<div id="tag_pin">
	<Link to="/tag/{tag_data.url_name}">{tag_data.name}</Link>
</div>

<style>
	#tag_pin {
		margin: 3px;
		background-color: #f0f0f0;
		display: inline-block;
		padding: 4px;
	}
</style>
