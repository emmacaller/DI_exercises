
// EX1---

// var userinput = prompt("Put in word")

// for (i=0; i<userinput.length; i++)
// {
// 	switch(userinput.charAt(i))
// 	{
// 		case 'a':
// 		userinput=userinput.replace('a','b')
// 		break;
// 		case 'e' :
// 		userinput=userinput.replace('e','c')
// 		break;
// 		case "i":
// 		userinput=userinput.replace('i', 'd')
// 		break;
// 		case 'o':
// 		userinput=userinput.replace('o','f')
// 		break
// 		case "u":
// 		userinput=userinput.replace('u', 'g')

// 	}

// } console.log(userinput)


// var userword =prompt("Put in word");

// EX 2 SWITCH

// var user = prompt('What language do you speak?')

// switch(user){
// case 'English':
// console.log("Hello");
// break;
// case 'Hebrew':
// console.log("Shalom")
// break;
// case "French":
// console.log("Bonjour")
// break;
// default:
// alert(":)")
// }

// EX3-----

// var userinput = prompt("What is your grade?")


// if(userinput>90) {
// 	console.log('A')
// } else if (userinput<=90&&userinput>80){
// 	console.log('B')
// } else if (userinput<=80&&userinput>70){
// 	console.log('C')
// }else if(userinput<=70){
// 	console.log('D')
// }

// EX 4----

// var zip = prompt("Whats your zip code")

// var check = true

// if (zip.length<=5){
// 	check=false





//Ascii code of 0 is 48, 1 is 49 and 9 is 57
// for(i=0;i<zipcode.length;i++) // to check the whole string
// {
// if(zipcode.charAt(i)===' ') // check for spaces
// check=false
// if(zipcode.charCodeAt(i)<48 || zipcode.charCodeAt(i)>57)
// check=false; //check for only digets allowed
// }
// if(check==true)
// {
// console.log("good");
// }
// else
// {
// console.log("error");
// }

// //other way to do it 

// var zipcode="1235";
// var check=true;
// var regexp=/\s/g // checks for spaces 
// var regexp1=/\D/g // checks for non didjit characters

// if(regexp.test(zipcode)===true) // if it has a space then the answer is false
// {
// {
// check=false
// }
// else if(regexp1.test(zipcode)===true) // if it has a non diget then the answer is false
// {
// check=false
// }
// else if(zipcode.length>5)
// {
// check=false;
// }


// if(check==true)
// {
// console.log("good");
// }
// else
// {
// console.log("error");
// }