$( document ).ready(function() {
    // alert("heelo");

    /**
	 * This function searches for videos related to the keyword 'dogs'. The video IDs and titles
	 * of the search results are logged to Apps Script's log.
	 *
	 * Note that this sample limits the results to 25. To return more results, pass
	 * additional parameters as documented here:
	 *   https://developers.google.com/youtube/v3/docs/search/list
	 */
	// function searchByKeyword() {
	//   var results = YouTube.Search.list('id,snippet', {q: 'dogs', maxResults: 10 });
	//   for(var i in results.items) {
	//     var item = results.items[i];
	//     Logger.log('[%s] Title: %s', item.id.videoId, item.snippet.title);
	//   }
	// }

	function signin_p() {
	    console.log( "ready!" );
	}

	$(".signin-forum").hide();
	$("button.in").css("background-color", "#F7F7FF");
    $("button.in").css("color", "#232323");
    $("button.in").css("border", "1px solid #4B3FFC");



	$("button.in").click(function(){
	    $(".signup-forum").hide();
	    $(".signin-forum").show();

	    $("button.in").css("background-color", "rgba(0,0,0,0)");
	    $("button.in").css("color", "#F7F7FF");
	    $("button.in").css("border", "none");

	    $("button.up").css("background-color", "#F7F7FF");
	    $("button.up").css("color", "#232323");
	    $("button.up").css("border", "1px solid #4B3FFC");

	});

	$("button.up").click(function(){
	    $(".signin-forum").hide();
	    $(".signup-forum").show();

	    $("button.up").css("background-color", "rgba(0,0,0,0)");
	    $("button.up").css("color", "#F7F7FF");
	    $("button.up").css("border", "none");

	    $("button.in").css("background-color", "#F7F7FF");
	    $("button.in").css("color", "#232323");
	    $("button.in").css("border", "1px solid #4B3FFC");
	});
});