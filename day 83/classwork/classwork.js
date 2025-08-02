const filterLongStrings = (arr) => {
    for (let i = 0; i < arr.length; i++) {
      if (arr[i].length <= 5) {
        continue;
      }
      console.log(arr[i]);
    }
  };
  
  // ცდისთვის
  const myList = ["apple", "banana", "cat", "elephant", "grape", "peach", "orange", "hi", "cherry", "kiwi"];
  
  filterLongStrings(myList);