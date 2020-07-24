// sends message to background.js to activate popup
chrome.runtime.sendMessage({"message": "activate_icon"});

var comments = []

// searches for all comment text
$("#content-text.style-scope.ytd-comment-renderer").each(function(index) {
    comments.push($(this).text())
})
console.log(comments)

// sends comments to background.js as array
chrome.runtime.sendMessage({"comments": comments})
