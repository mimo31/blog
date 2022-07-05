<script>
	import { Link } from "svelte-navigator";
	export let article_data;
</script>

<p>
	<strong>{article_data.name}</strong><br />
	<Link to="/article/{article_data.url_name}">open</Link>
	{article_data.description}
</p>
