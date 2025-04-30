var Search_bar = document.getElementsByClassName('layer__content')[0]
var buttons = Search_bar.querySelectorAll('button')
for (i = 0; i <= buttons.length; i++) {
    if (buttons[i].innerText.trim() === 'Seek') {
        buttons[i].querySelectorAll('span')[1].click();
        break;
    }
}