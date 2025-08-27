console.getElementById("main")
function printName(){
    console.log("საბა საბანასლი")
}

let interval= setInterval(printName,10)

function stopInterval() {
    clearInterval(intervalId);
    console.log("ინტერვალი გაუქმდა");
  }