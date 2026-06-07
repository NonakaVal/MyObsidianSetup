
<%*
let yt_url = await navigator.clipboard.readText();
let url = "https://www.youtube.com/oembed?format=json&url="+yt_url;
let resp = await tp.obsidian.request({url});
let video = JSON.parse(resp);
%>[<%video["author_name"]%>, ▶ *<%video["title"]%>*](<%yt_url%>)
