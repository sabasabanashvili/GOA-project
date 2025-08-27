const prompt = require('Pompt')();

const numStr1 = prompt('Enter the first decimal number: ');
const numStr2 = prompt('Enter the second decimal number: ');

const sumInt = parseInt(numStr1) + parseInt(numStr2);

const sumFloat = parseFloat(numStr1) + parseFloat(numStr2);

const areEqual = sumInt === sumFloat;

console.log(`Sum with parseInt: ${sumInt}`);
console.log(`Sum with parseFloat: ${sumFloat}`);
console.log(`Are the sums equal (===)? ${areEqual}`);