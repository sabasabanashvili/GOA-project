function printEvenNumbers(a, b, c, d, e, f, g, h, i, j) {
    let numbers = [a, b, c, d, e, f, g, h, i, j];
  
    for (let num of numbers) {
      if (num % 2 === 0) {
        console.log(num);
      }
    }
  }
  
  printEvenNumbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
  