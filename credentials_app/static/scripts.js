function toggleFormat(format) {
    var dictionaryFormat = document.getElementsByClassName('dictionary-format');
    var bulletsFormat = document.getElementsByClassName('bullets-format');
    for (var i = 0; i < dictionaryFormat.length; i++) {
        dictionaryFormat[i].style.display = format === 'dictionary' ? 'block' : 'none';
    }
    for (var i = 0; i < bulletsFormat.length; i++) {
        bulletsFormat[i].style.display = format === 'bullets' ? 'block' : 'none';
    }
}