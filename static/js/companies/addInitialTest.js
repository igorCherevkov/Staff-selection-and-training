'use strict';

let addButton1 = document.querySelector('#form-labels__add');
let template1 = document.querySelector('#form-labels__withnew');
let newTemplate1 = document.querySelector('#form-vacancy');

addButton1.addEventListener('click', function() {
    let newNode = newTemplate1.content.cloneNode(true);
    template1.append(newNode);
});