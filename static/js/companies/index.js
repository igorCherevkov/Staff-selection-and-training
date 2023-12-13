'use strict';

let dropDown = document.querySelector('.dropDown');
let picture = document.querySelector('.profile-pic');

picture.addEventListener('click', function() {
    dropDown.classList.toggle('dropDown-hidden');
});