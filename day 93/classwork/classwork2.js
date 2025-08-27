const prompt = require('prompt-sync')();

const expr = prompt('Enter a math expression (e.g., "12.5 + 7.3 * 2"): ');
const result = eval(expr);

console.log('Original expression:', expr);
console.log('Evaluated result:', result);
console.log('Integer conversion:', parseInt(result));
console.log('Float conversion:', parseFloat(result));
