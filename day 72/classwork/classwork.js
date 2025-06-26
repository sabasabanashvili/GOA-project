// 1. Shortest Word (7 kyu)
function findShort(s) {
    return Math.min(...s.split(" ").map(word => word.length));
  }
  
  // 2. Remove String Spaces (8 kyu)
  function noSpace(x) {
    return x.replace(/\s/g, "");
  }
  
  // 3. Mumbling (7 kyu)
  function accum(s) {
    return s.split('')
            .map((char, i) => char.toUpperCase() + char.toLowerCase().repeat(i))
            .join('-');
  }
  
  // 4. Sum of Positive (8 kyu)
  function positiveSum(arr) {
    return arr.filter(n => n > 0).reduce((sum, n) => sum + n, 0);
  }
  
  // 5. Multiply (8 kyu)
  function multiply(a, b) {
    return a * b;
  }
  
  // 6. Sum of Two Numbers (8 kyu)
  function sum(a, b) {
    return a + b;
  }
  
  // 7. Even or Odd (8 kyu)
  function evenOrOdd(number) {
    return number % 2 === 0 ? "Even" : "Odd";
  }
  
  // 8. Hello World (8 kyu)
  function greet() {
    return "hello world!";
  }
  
  // 9. Binary Addition (8 kyu)
  function addBinary(a, b) {
    return (a + b).toString(2);
  }
  
  // 10. Validate PIN code (7 kyu)
  function validatePIN(pin) {
    return /^(\d{4}|\d{6})$/.test(pin);
  }
  
  // 11. Is Triangle? (7 kyu)
  function isTriangle(a, b, c) {
    return a + b > c && a + c > b && b + c > a;
  }
  
  // 12. Two to One (7 kyu)
  function longest(s1, s2) {
    return [...new Set(s1 + s2)].sort().join('');
  }
  
  // 13. Compound Array - Array.plusArray (7 kyu)
  function arrayPlusArray(arr1, arr2) {
    return [...arr1, ...arr2].reduce((sum, n) => sum + n, 0);
  }
  
  // 14. Third Angle of a Triangle (8 kyu)
  function otherAngle(a, b) {
    return 180 - a - b;
  }
  
  // 15. Number of People in the Bus (7 kyu)
  function number(busStops) {
    return busStops.reduce((acc, [on, off]) => acc + on - off, 0);
  }
  