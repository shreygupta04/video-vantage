chrome.extension.onMessage.addListener(
    function(request, sender, sendResponse) {
    if (request.message === "activate_icon") {
        chrome.tabs.query({active:true,windowType:"normal", currentWindow: true}, function(d){
            chrome.pageAction.show(d[0].id);
        })
    }
    if(request.comments) {
        console.log(request.comments)
    }
});