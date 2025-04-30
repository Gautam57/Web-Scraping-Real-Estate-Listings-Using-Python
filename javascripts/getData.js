var cardContainer = document.getElementsByClassName('cardContainer');
var cards = cardContainer[0].getElementsByClassName('listing-card');
var nextcardvalues = "";

for (let i = 0; i < cards.length; i++) {
    let cardsvalues = cards[i].querySelectorAll('dl');
    if (cardsvalues.length > 0) {
        let price = cardsvalues[0].innerText.trim();
        let area = cardsvalues[1].innerText.trim();
        nextcardvalues += price + ";" + area + "|";
    }
}
return nextcardvalues;