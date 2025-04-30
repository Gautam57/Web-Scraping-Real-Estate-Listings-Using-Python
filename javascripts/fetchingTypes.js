var Search_bar = document.getElementsByClassName('layer__content')[0];
var selectElement = Search_bar.getElementsByClassName('select-container')[9].querySelector('select');

allOptions = selectElement.querySelectorAll('option');
alltypes = "";

for (i = 0; i < allOptions.length; i++) {
    type = allOptions[i].innerText
    alltypes += type + ";"
}
return alltypes;