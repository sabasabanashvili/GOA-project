// Homework 1: Create and Access Fruits Array
let fruits = ["apple", "banana", "orange", "grape", "mango"];
console.log("First fruit:", fruits[0]);
console.log("Last fruit:", fruits[fruits.length - 1]);
console.log("Total number of fruits:", fruits.length);

// Homework 2: Modifying Arrays
let colors = ["red", "green", "blue"];
colors.push("yellow");         // Add to the end
colors.shift();                // Remove the first color
colors.unshift("purple");      // Add to the beginning
console.log("Final colors array:", colors);

// Homework 3: Loop Through an Array
let numbers = [2, 4, 6, 8, 10];
for (let i = 0; i < numbers.length; i++) {
  console.log("Doubled:", numbers[i] * 2);
}

// Function: Sum Array
function sumArray(arr) {
  let sum = 0;
  for (let i = 0; i < arr.length; i++) {
    sum += arr[i];
  }
  return sum;
}
console.log("Sum of [1, 2, 3]:", sumArray([1, 2, 3]));

// Homework 5: Find the Largest Number (no Math.max)
function findLargest(arr) {
  let largest = arr[0];
  for (let i = 1; i < arr.length; i++) {
    if (arr[i] > largest) {
      largest = arr[i];
    }
  }
  return largest;
}
console.log("Largest number is:", findLargest([3, 9, 1, 22, 7]));

// Homework 6: Array Includes Check
let favoriteMovies = ["Inception", "The Matrix", "Interstellar", "Avengers", "Titanic"];
let userMovie = prompt("Enter a movie name:");
if (favoriteMovies.includes(userMovie)) {
  alert("Yes, it's one of my favorites!");
} else {
  alert("No, I don't like that one much.");
}

// Homework 7: Join and Sort
let words = ["banana", "apple", "pear", "orange"];
words.sort(); // Sort alphabetically
let wordString = words.join(", ");
console.log("Sorted words:", wordString);

// Homework 1 (Extra): Random Number Generator
function getRandomNumber() {
  return Math.floor(Math.random() * 10) + 1;
}
console.log("Random number between 1 and 10:", getRandomNumber());

// Homework 2 (Extra): Rounding Numbers
let decimal = parseFloat(prompt("Enter a decimal number:"));
console.log("Rounded down:", Math.floor(decimal));
console.log("Rounded up:", Math.ceil(decimal));
console.log("Rounded to nearest:", Math.round(decimal));
