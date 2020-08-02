chrome.extension.onMessage.addListener(
    function(request, sender, sendResponse) {
    if (request.message === "activate_icon") {
        chrome.tabs.query({active:true,windowType:"normal", currentWindow: true}, function(d){
            chrome.pageAction.show(d[0].id);
        })
    }
    if(request.comments) {
        $.ajax({
            type: 'POST',
            contentType: 'application/json',
            headers: {"Access-Control-Allow-Origin":"*"},
            url: "https://video-vantage.herokuapp.com/predict/",
            data: JSON.stringify({'comments': request.comments}),
            success: function(resp) {
                chrome.tabs.query({active: true, currentWindow: true}, function(tabs){
                    chrome.tabs.sendMessage(tabs[0].id, {rating: resp.rating}, function(response) {});  
                });
            }
        });
    }
});