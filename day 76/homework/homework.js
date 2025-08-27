function traverseArr(arr) {
    for (let i = 0; i < arr.length; i++) {
      console.log(arr[i]);
    }
  }
  
  // ფუნქციის გამოძახება განსხვავებული მასივებით
  traverseArr([1, 2, 3, 4, 5]);
  traverseArr(["ვაშლი", "ბანანი", "ატამი"]);

  function arr(n) {
    let result = [];
    for (let i = 0; i < n; i++) {
      result.push(i);
    }
    return result;
  }
