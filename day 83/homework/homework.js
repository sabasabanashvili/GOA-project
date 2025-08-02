// 4) Print numbers from 1 to 5 using a do...while loop
let i = 1;
do {
  console.log(i);
  i++;
} while (i <= 5);

// 5) Print even numbers from 2 to 10 using a do...while loop
let j = 2;
do {
  console.log(j);
  j += 2;
} while (j <= 10);

// 6) Print numbers from 10 down to 1 using a do...while loop
let k = 10;
do {
  console.log(k);
  k--;
} while (k >= 1);

// 7) Ask the user to enter a number until they enter a number greater than 100
let num;
do {
  num = parseFloat(prompt("Enter a number greater than 100:"));
} while (num <= 100);

// 8) Sum numbers from 1 to 10 using a do...while loop
let sum = 0;
let x = 1;
do {
  sum += x;
  x++;
} while (x <= 10);
console.log("Sum from 1 to 10:", sum);

// 9) Use a for...of loop to print each element of an array of numbers
let numbers = [1, 2, 3, 4, 5];
for (let n of numbers) {
  console.log(n);
}

// 10) Use a for...of loop to print each character of a string
let word = "hello";
for (let char of word) {
  console.log(char);
}

// 11) Use a for...of loop to sum all numbers in an array and print the total
let nums = [10, 20, 30];
let total = 0;
for (let n of nums) {
  total += n;
}
console.log("Total:", total);

// 12) Use a for...of loop to print only the even numbers from an array of numbers
let arr = [1, 2, 3, 4, 5, 6];
for (let n of arr) {
  if (n % 2 === 0) {
    console.log("Even:", n);
  }
}

// 13) Use a for...of loop to print all names from an array of names
let names = ["Anna", "Luka", "Nino"];
for (let name of names) {
  console.log(name);
}

// 14) Use a for...in loop to print all property names (keys) of an object
let person = { name: "John", age: 25, city: "Tbilisi" };
for (let key in person) {
  console.log("Key:", key);
}

// 15) Use a for...in loop to print all property values of an object
for (let key in person) {
  console.log("Value:", person[key]);
}

// 16) Use a for...in loop to count the number of properties in an object
let count = 0;
for (let key in person) {
  count++;
}
console.log("Property count:", count);

// 17) Use a for...in loop to check if a specific key exists in an object
if ("age" in person) {
  console.log("Key 'age' exists!");
}

// 18) Use a for...in loop to create a string listing all keys from an object
let keyString = "";
for (let key in person) {
  keyString += key + " ";
}
console.log("All keys:", keyString.trim());
