
var operation = prompt('Enter Operation');
// give option of

var number1 = prompt('Put first number');

var number2 = prompt('Put in second number');

	
if (operation === '+') {

	var number = parseInt(number1) + parseInt(number2);

alert("Sum is" + " " + number)

} else if(operation === '-') {

var number = parseInt(number1) - parseInt(number2);

alert("Sum is" + " " + number) 

} else if(operation === '/'){

var number = parseInt(number1) - parseInt(number2);

alert("Sum is" + " " + number)

} else if (operation === '*'){

var number = parseInt(number1) * parseInt(number2);

alert("Sum is" + " " + number)

} else {( alert('Invalid Operation'))
};

