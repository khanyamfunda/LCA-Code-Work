let person1 =  "white";

if(person1 == 'red'){
  console.log("your favourite color is red");
}
else if(person1 == 'black'){
  console.log("your favourite color is black")
}
else if(person1 == undefined){
  console.log("Mfondini awuna favorite color wena")
}
else{
  console.log("Uli zambane le sofa kwedini")
}

switch (person1){//key
  case "red":
    console.log("your favourite color is red")
    break;
  case "black":
    console.log("your favorite color is black")
    break;
  case undefined:
    console.log("Mfondini awuna favorite color wena")
    default:
      console.log("Your color is "+ person1)
}
let person2= "white"
console.log(
  person2 == "red"?"Their favorite color is red":"no favorite color"
)
//loops
 let vegetables = ["lettuce", "tomato", "avocado", "carrot"]
 for (let n=0; n<vegetables.length; n++){
  console.log(n + 1 + "." +vegetables[n]);
 }
if(vegetables = "carrot"){
  console.log("This is a " +vegetables+" is the list")
}
if(vegetables = "avocado"){
  console.log("This is a "+vegetables + " is in the list")
}