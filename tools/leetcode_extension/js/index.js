function hideItem(lockIcons) {
    lockIcons.each(function() {
        var p = $(this).parent().parent().parent().parent();
        if (p.is('tr')) {
            p.attr('style','display:none !important');
        }
    });
}

function listenList() {
    $('.question-list-table').bind('DOMNodeInserted', function(){
        var lockIcons = $('span[data-original-title="Subscribe to unlock"]');
        if(lockIcons.length) {
            $('.question-list-table').unbind('DOMNodeInserted');
            hideItem(lockIcons);
            listenList();
        }
    });
}

$('body').bind('DOMNodeInserted', function(){
    var lockIcons = $('span[data-original-title="Subscribe to unlock"]');
    if(lockIcons.length) {
        $('body').unbind('DOMNodeInserted');
        listenList();
    }
});
