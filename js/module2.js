//1.Write a program that prompts the user for five numbers and prints them in the reverse order they were entered.
// Print the result to the console.
// Save the numbers to an array, then use for-loop to iterate in reverse order.
// Do not use array.reverse() function.
let numbers = [];

for (let i = 0; i < 5; i++) {
    let num = prompt(`Enter number ${i + 1}:`);
    numbers.push(num);
}

console.log("Numbers in reverse order:");
for (let i = 4; i >= 0; i--) {
    console.log(numbers[i]);
}
//2.Write a program that asks the user for the number of participants. After this, the program asks for the names of all participants. Finally,
// the program prints the names of the participants on the web page in an ordered list (<ol>) in alphabetical order.
function getParticipants() {
    const numParticipants = parseInt(prompt("Enter the number of participants:"), 10);
    const participants = [];

    for (let i = 0; i < numParticipants; i++) {
        const name = prompt(`Enter the name of participant ${i + 1}:`);
        participants.push(name);
    }

    participants.sort();

    console.log("Participants in alphabetical order:");
    participants.forEach(participant => {
        console.log(participant);
    });
}

getParticipants();
//3.Write a program that asks for the names of six dogs. The program prints dog names to unordered list <ul> in reverse alphabetical order. (
function getDogNames() {
    const dogs = [];

    for (let i = 0; i < 6; i++) {
        const name = prompt(`Enter the name of dog ${i + 1}:`);
        dogs.push(name);
    }

    dogs.sort().reverse();

    console.log("Dog names in reverse alphabetical order:");
    dogs.forEach(dog => {
        console.log(dog);
    });
}
getDogNames();
//4.Write a program that asks the user for numbers until he gives zero. The given numbers are printed in the console from the largest to the smallest
function collectNumbers() {
    const numbers = [];

    while (true) {
        const input = parseInt(prompt("Enter a number (0 to stop):"), 10);
        if (input === 0) {
            break; // Exit the loop if the input is zero
        }
        numbers.push(input); // Add the number to the array
    }
    numbers.sort((a, b) => b - a);


    console.log("Numbers from largest to smallest:");
    numbers.forEach(number => {
        console.log(number);
    });
}
collectNumbers();
//5.Write a program that prompts the user for numbers. When the user enters one of the numbers he previously entered, the program will announce that the number has already been given and stops its operation and then prints all the given numbers to the console in ascending order.
function collectNumbers() {
    const numbers = [];

    while (true) {
        const input = parseInt(prompt("Enter a number (or a duplicate to stop):"), 10);

        if (isNaN(input)) {
            console.log("Please enter a valid number.");
            continue;
        }
        if (numbers.includes(input)) {
            console.log(`The number ${input} has already been given.`);
            break; // Exit the loop if the number is a duplicate
        }

        numbers.push(input);
    }

    numbers.sort((a, b) => a - b);

    console.log("Given numbers in ascending order:");
    numbers.forEach(number => {
        console.log(number);
    });
}

collectNumbers();