chrome.extension.onMessage.addListener(
    function(request, sender, sendResponse) {
    if (request.message === "activate_icon") {
        chrome.tabs.query({active:true,windowType:"normal", currentWindow: true}, function(d){
            chrome.pageAction.show(d[0].id);
        })
    }
    if(request.comments) {
        $.ajax({
            type : 'POST',
            contentType: 'application/json',
            headers: {"Access-Control-Allow-Origin":"*"},
            url : "http://127.0.0.1:5000/predict/",
            data : JSON.stringify({'comments': request.comments})
        });
    }
});