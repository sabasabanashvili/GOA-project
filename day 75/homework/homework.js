// 2) Log numbers 1 to 5 every second, then stop
let i = 1;
let interval = setInterval(() => {
  console.log(i);
  if (i === 5) clearInterval(interval);
  i++;
}, 1000);

// 3) Show a message every 2 seconds, stop after 10 seconds
let msg = setInterval(() => {
  console.log("Message");
}, 2000);

setTimeout(() => {
  clearInterval(msg);
}, 10000);

// 4) Change background color every 3 seconds, stop after 5 changes
let change = 0;
let bg = setInterval(() => {
  document.body.style.backgroundColor =
    "#" + Math.floor(Math.random() * 16777215).toString(16);
  change++;
  if (change === 5) clearInterval(bg);
}, 3000);

// 5) Show current time every second, stop after 15 seconds
let timeCount = 0;
let time = setInterval(() => {
  console.log(new Date().toLocaleTimeString());
  timeCount++;
  if (timeCount === 15) clearInterval(time);
}, 1000);

// 6) Simple timer that counts up to 10 seconds
let timer = 0;
let t = setInterval(() => {
  timer++;
  console.log(timer);
  if (timer === 10) clearInterval(t);
}, 1000);

// 7) Log second element from array of 4 numbers
let nums = [5, 10, 15, 20];
console.log(nums[1]);

// 8) Change first element to 100 and log the array
nums[0] = 100;
console.log(nums);

// 9) Log each of 3 strings using direct indexing
let strings = ["one", "two", "three"];
console.log(strings[0]);
console.log(strings[1]);
console.log(strings[2]);

// 10) Find sum of first and last elements in array of 5 numbers
let arr = [1, 2, 3, 4, 5];
let sum = arr[0] + arr[arr.length - 1];
console.log(sum);
