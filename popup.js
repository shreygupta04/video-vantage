// executes content.js when called

chrome.tabs.executeScript({
    file: 'content.js'
}); 

chrome.extension.onMessage.addListener(
    function(request, sender, sendResponse) {
    if (request.rating) {
        console.log(request.rating)
        $(".stars").html(request.rating.toString());

        $.fn.stars = function() {
            return $(this).each(function() {
                // Get the value
                var val = request.rating
                // Make sure that the value is in 0 - 5 range, multiply to get width
                var size = Math.max(0, (Math.min(5, val))) * 16;
                // Create stars holder
                var $span = $('<span />').width(size);
                // Replace the numerical value with stars
                $(this).html($span);
            });
        }
        $(function() {
            $('span.stars').stars();
        });
    }
});