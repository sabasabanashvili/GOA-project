//1
function printUntilZero(...args) {
    for (let arg of args) {
      if (arg === 0) break;
      console.log(arg);
    }
  }
  
  //2
  function printNumbersOnly(...args) {
    for (let arg of args) {
      if (typeof arg === "string") continue;
      console.log(arg);
    }
  }
  
  //3
  const multiply = function(a, b) {
    return a * b;
  };
  
  //4
  setInterval(function() {
    console.log("This message logs every 2 seconds");
  }, 2000);
  
  //5
  const btn = document.getElementById("myButton");
  btn.addEventListener("click", function() {
    alert("Button clicked!");
  });
  
  //6
  (function() {
    console.log("Hello, world!");
  })();
  
  //7
  (function(num) {
    console.log(num * num);
  })(5); // Example with 5
  
  //8
  (function(numbers) {
    let sum = 0;
    for (let n of numbers) {
      sum += n;
    }
    console.log(sum);
  })([1, 2, 3, 4, 5]);
  
  //9
  function localScopeExample() {
    let localVar = "I'm local";
  }
  localScopeExample();

  //10
  function outerFunc() {
    let outerVar = 1;
    function innerFunc() {
      outerVar = 2;
    }
    console.log("Before innerFunc:", outerVar);
    innerFunc();
    console.log("After innerFunc:", outerVar);
  }
  outerFunc();
  
  //11

  {
    var x = 1;
    let y = 2;
    const z = 3;
  }
  console.log(x); 
  // 1
  function testScope() {
    if (true) {
      var a = 10;
      let b = 20;
      const c = 30;
    }
    console.log(a); // 10

  }
  testScope();
  