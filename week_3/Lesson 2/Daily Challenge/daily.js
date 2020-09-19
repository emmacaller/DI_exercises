var str = "I am not that bad at singing"

var find = str.indexOf("not")

var find2 = str.indexOf("bad")

if (find2>find){

var substr= str.substring(find,find2 +3) // extracts the words in the perameters, start position
	console.log(str.replace(substr,"good"))

	
}else (console.log(str))