'use strict';

//var change = input

//var quarters = Math.floor(change / 25);
//var change = change - (quarters * 25);

//var dimes = Math.floor(change / 10);
//var change = change - (dimes * 10);

//var nickles = Math.floor(change / 5);
//var change = change - (nickles * 5);

//var pennies = Math.floor(change / 1);
//var change = change - (pennies * 1);

//console.log(quarters, dimes, nickles, pennies);



/* ************************* */
/* your javascript goes here */

// inside the function below is where you will
// do your work
// the transform function takes a string as an input
// and print out the result using the `printResult`
// function
// you can add more functions above to keep your
// code clean and readable
function transform(input) {
  if (input) {
    clearError();
    // do some transform of the user's input
    // vvvvvv HERE vvvvvv

    // your stuff HERE
   
    var change = input

    var quarters = Math.floor(change / 25);
    var change = change - (quarters * 25);

    var dimes = Math.floor(change / 10);
    var change = change - (dimes * 10);

    var nickles = Math.floor(change / 5);
    var change = change - (nickles * 5);

    var pennies = Math.floor(change / 1);
    var change = change - (pennies * 1);

    console.log(quarters, dimes, nickles, pennies);
      
    var result = (quarters + " quaters, " + dimes + " dimes. " + nickles + " nickles, and " + pennies + " pennies.")

    printResult(result);
  }
  else {
    printError('Enter a value');
    focusInput();
  }
}

document.addEventListener('DOMContentLoaded', function (evt) {
  // you can rename the `transform` function
  // above, but if you do, you need to change
  // the name here, too
  setup(transform);
  focusInput();
});

/* ************************************** */
/* do not change anything below this line */

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
