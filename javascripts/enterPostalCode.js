const postcode = arguments[0];
const enterevent = new KeyboardEvent('keydown', {
    key: 'Enter',
    keyCode: 13,
    code: 'Enter',
    which: 13,
    bubbles: true,
    cancelable: true
});

const spaceevent = new KeyboardEvent('keydown', {
    key: ' ',
    keyCode: 32,
    code: 'Space',
    which: 32,
    bubbles: true,
    cancelable: true
});


var Search_bar = document.getElementsByClassName('layer__content')[0];
var inputField = Search_bar.querySelectorAll('input')[1];
inputField.value = postcode;
await new Promise(resolve => setTimeout(resolve, 2000));
inputField.click();
await new Promise(resolve => setTimeout(resolve, 2000));
inputField.dispatchEvent(spaceevent);
await new Promise(resolve => setTimeout(resolve, 2000));
inputField.dispatchEvent(enterevent);