'use strict';

let addButton = document.querySelector('.form-labels__add');
let template = document.querySelector('.form-labels__withnew');
let newTemplate = document.querySelector('.form-labels__container');

addButton.addEventListener('click', function() {
    let newNode = newTemplate.cloneNode(true);
    template.append(newNode);
});