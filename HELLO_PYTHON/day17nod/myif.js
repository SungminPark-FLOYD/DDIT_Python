/**
 * 
 */
let jumsu = 80;
let res = "";
if(jumsu >= 90) {
	res = "수"
}else if(jumsu >= 80) {
	res = "우"
}else if(jumsu >= 70) {
	res = "미"
}else if(jumsu >= 60) {
	res = "양"
}else {
	res = "가"
}
console.log(res);