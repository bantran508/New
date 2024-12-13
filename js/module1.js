//1Write a program that logs to the console this text: I'm printing to console!
console.log("I'm printing to console!");

//2Write a program that prompts for user's name and then greets the user. Print the result to the HTML document:
var name = prompt("What is your name?");

console.log("Hello, " + name + "!");
//3Write a program that prompts for three integers. The program prints the sum,
// product and average of the numbers to the HTML document.

var num1 = parseInt(prompt("Enter the first integer:"));
var num2 = parseInt(prompt("Enter the second integer:"));
var num3 = parseInt(prompt("Enter the third integer:"));

var sum = num1 + num2 + num3;
var product = num1 * num2 * num3;
var average = sum / 3;

console.log("Sum: " + sum);
console.log("Product: " + product);
console.log("Average: " + average.toFixed(2));
//4In the Harry Potter children's books, the sorting hat assigns a new student
// at Hogwarts School of Witchcraft and Wizardry to one of the four classes,
// which are Gryffindor, Slytherin,Hufflepuff, and Ravenclaw. Write an electronic sorting hat
// that asks for a student's name and draws a room for him.
// If you enter Anna as the name, for example, the program prints to the HTML document "Anna, you are Ravenclaw."
var houses = ["Gryffindor", "Slytherin", "Hufflepuff", "Ravenclaw"];

var name = prompt("What is your name?");

var randomIndex = Math.floor(Math.random() * houses.length);
var assignedHouse = houses[randomIndex];

console.log(name + ", you are " + assignedHouse + "!");
//5Write a program that asks the user to enter a year and notifies the user whether the input year is a leap year.
// A year is a leap year if it is divisible by four. However, years divisible by 100 are leap years only
// if they are also divisible by 400. Print the result on the HTML document.
var year = parseInt(prompt("Enter a year:"));

var isLeapYear;
if ((year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0)) {
    isLeapYear = true;
} else {
    isLeapYear = false;
}

if (isLeapYear) {
    console.log(year + " is a leap year.");
} else {
    console.log(year + " is not a leap year.");
}