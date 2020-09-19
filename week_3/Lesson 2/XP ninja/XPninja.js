// EX 1 --

var younger=2016

var elder=2010
var d=new Date();
var youngerage=d.getFullYear()-younger
console.log(youngerage)
var elderage=d.getFullYear()-elder
console.log(elderage)
while(youngerage!==(elderage/2))
{

youngerage++;
elderage++;

}
if(youngerage===(elderage/2))
{
console.log("Age of younger son:"+youngerage)
console.log("Age of younger son:"+elderage)
console.log("The year would be:"+(younger+youngerage))


}



// EX 2 --


// var input =prompt("Put a string")
// console.log(input.lastIndexOf("ing")  ) //search for ing in the last position
//  if(input.length<3){
// 	console.log(input)
// } else if(input.search("ing")!== -1 && input.lastIndexOf("ing")===input.length-3){ // means ing is present 
//   console.log(input + "ly")
// }
// else if(input.length>=3){
// 	console.log(input + "ing")
// } 
