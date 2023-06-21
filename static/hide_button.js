const searchInput = document.getElementById('searchInput');
const clearButton = document.getElementById('clearButton');

searchInput.addEventListener('input', () => {
    if (searchInput.value.trim() !== '') {
        clearButton.style.display = 'inline-block';
    } else {
        clearButton.style.display = 'none';
    }
});

clearButton.addEventListener('click', () => {
    searchInput.value = '';
    clearButton.style.display = 'none';
});