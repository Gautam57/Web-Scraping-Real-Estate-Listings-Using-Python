var success = false;
var pagination = document.getElementsByClassName('Pagination_pagination__s5mQ8')[0];
if (pagination) {
    var allbuttons = pagination.querySelectorAll('button');
    if (allbuttons){
        numberOfPages = allbuttons[allbuttons.length - 2].innerText
        success = true;
    }
}

if (success) {
    return numberOfPages;
}
else {
    return 1;
}