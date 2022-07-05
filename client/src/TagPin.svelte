<script>
	export let tag_data;
	import { Link } from "svelte-navigator";
</script>

<div id="tag_pin">
	<Link to="/tag/{tag_data.url_name}">{tag_data.name}</Link>
</div>

<style>
	#tag_pin {
		margin: 2px;
		background-color: #f0f0f0;
	}
</style>
