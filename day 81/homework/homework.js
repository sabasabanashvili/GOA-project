// 1. Print numbers from 1 to 5
let i = 1;
do {
  console.log(i);
  i++;
} while (i <= 5);

// 2. Print even numbers from 2 to 10
let j = 2;
do {
  if (j % 2 === 0) console.log(j);
  j++;
} while (j <= 10);

// 3. Print numbers from 10 down to 1
let k = 10;
do {
  console.log(k);
  k--;
} while (k >= 1);

// 4. Ask user to enter a number until it's greater than 100
let num;
do {
  num = parseFloat(prompt("Enter a number greater than 100:"));
} while (isNaN(num) || num <= 100);

// 5. Sum numbers from 1 to 10 and print total
let sum = 0;
let m = 1;
do {
  sum += m;
  m++;
} while (m <= 10);
console.log("Total sum from 1 to 10:", sum);
