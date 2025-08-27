const person = {
    name: "Saba",
    surname: "Kavtaradze",
    academy: "Academy",
    city: "Tbilisi",
    role: "Student",
    favColor: "Blue",
    printFullName: function() {
      console.log(this.name + " " + this.surname);
    },
    printFavColor: function() {
      console.log(this.favColor);
    }
  };
  
  console.log(person);
  console.log(person.city);
  person.printFullName();
  person.favColor = "Red";
  console.log(person.favColor);
  