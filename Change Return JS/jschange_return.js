'use strict';

// Some supermarkets have automatic change dispensers.  Let's write a program that will do the same thing.

function transform(input) {
    if(input) {
        clearError();
        // this is the logic for the program
        var change = input
        
        // checks to see if anything divided by 25 then counts how many times.  Then leaving the remainder.
        var quarters = Math.floor(change/25);
        var change = change - (quarters*25);
        
         // checks to see if anything divided by 10 then counts how many times.  Then leaving the remainder.
        var dimes = Math.floor(change/10);
        var change = change - (dimes*10);
        
         // checks to see if anything divided by 5 then counts how many times.  Then leaving the remainder.
        var nickels = Math.floor(change/5);
        var change = change - (nickels*5);
        
         // checks to see if anything divided by 1 then counts how many times.  
        var pennies = Math.floor(change/1);
        var change = change - (pennies*1);
        
        // shows results in console
        console.log(quarters, dimes, nickels, pennies);
        
        // prints results
        var result = (quarters+" Quarters, "+dimes+" Dimes, "+nickels+" Nickels, "+pennies+" Pennies.")
        
        printResult(result)
    }
    
    // bring up an error if nothing entered
    else {
        printError("Enter a value");
        focusInput();
    }
}

// this part of the program was alread written for the class as part of the template.
document.addEventListener('DOMContentLoaded', function (evt) {

  setup(transform);
  focusInput();
});


function focusInput() {
  document.querySelector('[name="input"]').focus();
}

function printResult(str) {
  document.getElementById('result').innerHTML = str;
}

function printError(str) {
  var err = document.getElementById('error');
  err.classList.add('error');
  err.innerHTML = str;
}

function clearError() {
  var err = document.getElementById('error');
  err.innerHTML = '';
  err.classList.remove('error');
}

function setup(callback) {
  document.querySelector('form')
    .addEventListener('submit', function (evt) {
    evt.preventDefault();
    var value = document.querySelector('input').value;
    callback(value);
  });
}

