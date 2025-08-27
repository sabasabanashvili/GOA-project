let i = 1;
do {
  console.log(i);
  i++;
} while (i <= 5);

let j = 2;
do {
  if (j % 2 === 0) console.log(j);
  j++;
} while (j <= 10);

let k = 10;
do {
  console.log(k);
  k--;
} while (k >= 1);

let num;
do {
  num = parseFloat(prompt("Enter a number greater than 100:"));
} while (num <= 100 || isNaN(num));

let sum = 0, a = 1;
do {
  sum += a;
  a++;
} while (a <= 10);
console.log("Sum:", sum);

let fruits = ["apple", "banana", "cherry", "grape", "kiwi"];
for (let fruit of fruits) {
  console.log(fruit);
}

for (let n = 1; n <= 20; n++) {
  if (n === 13) break;
  console.log(n);
}

let colors = ["red", "green", "yellow", "blue", "purple"];
for (let color of colors) {
  if (color === "blue") break;
  console.log(color);
}

for (let c = 1; c <= 50; c++) {
  if (c % 4 === 0 && c % 5 === 0) break;
  console.log(c);
}

let word = "developer";
for (let letter of word) {
  if (letter === "a") break;
  console.log(letter);
}

let total = 0, x = 1;
while (true) {
  total += x;
  if (total >= 100) break;
  x++;
}
console.log("Total:", total);
