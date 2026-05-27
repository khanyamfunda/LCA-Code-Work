// Create an empty array called colors
const colors = [];

// Add three colors to the array using push()
colors.push("red");
colors.push("blue");
colors.push("green");

// Create another array called numbers with five numbers
const numbers = [10, 20, 30, 40, 50];

// Remove the second color from the colors array
colors.splice(0, 1);

// Add a new color to the beginning of the colors array
colors.unshift("yellow");

// Print the length of both arrays
console.log("Colors array:", colors);
console.log("Length of colors array:", colors.length);

console.log("Numbers array:", numbers);
console.log("Length of numbers array:", numbers.length);