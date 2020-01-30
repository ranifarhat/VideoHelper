$( document ).ready(function() {
    function openInNewTab(url) {
	  // var win = window.open(url, '_blank');
	  var importantStuff = window.open(url, '_blank');
	  importantStuff.document.write('Loading preview...');
	  importantStuff.focus();
	}

	openInNewTab($("div.redir_me").html());
	window.location.href="/";
});