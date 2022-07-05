export function toArticleDatetimeString(timestamp)
{
	var date = new Date(timestamp * 1000);
	return new Intl.DateTimeFormat('default', { dateStyle: 'medium', timeStyle: 'short' }).format(date);
}
