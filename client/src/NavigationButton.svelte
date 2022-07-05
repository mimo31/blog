<script>
	import { Link } from "svelte-navigator";
	export let link_to;
	export let text;
</script>

<tr><td><Link to={link_to}>{text}</Link></td></tr>
