const type = arguments[0];
var Search_bar = document.getElementsByClassName('layer__content')[0];

// Get the select element inside the 9th select-container
var selectElement = Search_bar.getElementsByClassName('select-container')[9].querySelector('select');

if (selectElement) {
    // Loop through the options to find the right one
    var options = selectElement.options;
    for (var i = 0; i < options.length; i++) {
        if (options[i].text.trim() === type) {
            selectElement.selectedIndex = i;
            break;
        }
    }

    // Fire a change event to make sure the website notices the change
    var event = new Event('change', { bubbles: true });
    selectElement.dispatchEvent(event);
}