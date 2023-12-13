'use strict';

let addButton1 = document.querySelector('#form-labels__add1');
let template1 = document.querySelector('#form-labels__withnew1');
let newTemplate1 = document.querySelector('#form-vacancy');
let addButton2 = document.querySelector('#form-labels__add2');
let template2 = document.querySelector('#form-labels__withnew2');
let newTemplate2 = document.querySelector('#form-files');
let addButton3 = document.querySelector('#form-labels__add3');
let template3 = document.querySelector('.main-company-info-none');

addButton1.addEventListener('click', function() {
    let newNode = newTemplate1.content.cloneNode(true);
    template1.append(newNode);
});

addButton2.addEventListener('click', function() {
    let newNode = newTemplate2.content.cloneNode(true);
    template2.append(newNode);
});

addButton3.addEventListener('click', function() {
    template3.classList.toggle('main-company-info__inf');
});