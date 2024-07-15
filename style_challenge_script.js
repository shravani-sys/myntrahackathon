const outfitForm = document.getElementById('outfit-form');
const outfitList = document.getElementById('outfit-list');

outfitForm.addEventListener('submit', function(event) {
    event.preventDefault();

    const outfitName = document.getElementById('outfit-name').value;
    const outfitDescription = document.getElementById('outfit-description').value;

    const outfitElement = document.createElement('div');
    outfitElement.classList.add('outfit', 'mt-3');
    outfitElement.innerHTML = `
        <h4>${outfitName}</h4>
        <p>${outfitDescription}</p>
        <img src="https://via.placeholder.com/150" alt="${outfitName}">
    `;

    outfitList.appendChild(outfitElement);

    outfitForm.reset();
});
