<script>
	import { API_ROOT } from "./api_root.js";
	import { writable } from "svelte/store";
	import { onMount } from "svelte";
	import { Link } from "svelte-navigator";
	import { toArticleDatetimeString } from "./datetime_utils.js";
	import TagPin from "./TagPin.svelte";
	import Comment from "./Comment.svelte";
	import NewCommentWidget from "./NewCommentWidget.svelte";

	export let article_url_name;
	let loading_url_name = "";
	let loaded_article = writable({});
	let comments = writable([]);
	let replying_to_index = -1;
	let something_loaded = false;

	function processComments(comment_data)
	{
		comment_data.sort((c0, c1) => c0.time_created - c1.time_created);
		var cc = comment_data.length;
		for (var i = 0; i < cc; i++)
		{
			comment_data[i].layer = 0;
			for (var j = 0; j < i; j++)
				if (comment_data[i].reply_to_id === comment_data[j].id)
				{
					comment_data[i].layer = comment_data[j].layer + 1;
					break;
				}
		}
		for (var i = 0; i < cc; i++)
			comment_data[i].last_activity = comment_data[i].time_created;
		for (var i = cc - 1; i >= 0; i--)
		{
			if (comment_data[i].layer === 0)
				continue;
			for (var j = 0; j < i; j++)
				if (comment_data[i].reply_to_id === comment_data[j].id && comment_data[j].last_activity < comment_data[i].last_activity)
					comment_data[j].last_activity = comment_data[i].last_activity;
		}
		comment_data.sort((c0, c1) => (c0.last_activity === c1.last_activity ? c0.layer - c1.layer : c1.last_activity - c0.last_activity));
		comments.set(comment_data);
	}

	function startArticleLoad(url_name)
	{
		if (loading_url_name === url_name)
		{
			setTimeout(() => MathJax.typeset(), 0);
			return;
		}
		loading_url_name = url_name;
		something_loaded = false;
		(async () => {
			fetch(API_ROOT + "get_article?url_name=" + url_name)
			.then(response => response.json())
			.then(data =>
			{
				if (data.url_name === article_url_name)
				{
					loaded_article.set(data);
					processComments(data.comments);
					something_loaded = true;
					setTimeout(() => MathJax.typeset(), 0);
				}
			});
		})();
	}
	$: startArticleLoad(article_url_name);

	onMount(() => startArticleLoad(article_url_name));

	function onCommentSubmit(e)
	{
		$comments.push(e.detail);
		processComments($comments);
		replying_to_index = -1;
	}

	function onCommentReply(index)
	{
		replying_to_index = index;
	}
</script>

{#if something_loaded}
	<h1>{$loaded_article.name}</h1>
	<p>created {toArticleDatetimeString($loaded_article.time_created)}</p>
	{#if $loaded_article.time_edited !== null}
		<p>last edited {toArticleDatetimeString($loaded_article.time_edited)}</p>
	{/if}
	{#each $loaded_article.tags as tag_data}
		<TagPin {tag_data} />
	{/each}
	<p class="content-description">
		{$loaded_article.description}
	</p>
	<div>
		{@html $loaded_article.content}
	</div>
	{#if replying_to_index === -1}
		<NewCommentWidget top_description="new comment" submit_button_text="create comment" article_id={$loaded_article.id} reply_to_id=null layer=0 cancellable=false on:submit={onCommentSubmit}/>
	{/if}
	{#each $comments as comment_data, i}
		<Comment {comment_data} on:reply={() => onCommentReply(i)} />
		{#if replying_to_index === i}
			<NewCommentWidget top_description="comment reply" submit_button_text="create reply" article_id={$loaded_article.id} reply_to_id={comment_data.id} layer={comment_data.layer + 1} cancelable=true on:submit={onCommentSubmit} on:cancel={(e) => replying_to_index = -1}/>
		{/if}
	{/each}
{/if}
