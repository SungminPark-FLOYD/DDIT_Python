function showDan(dan) {
	let res = "";
	for(let i = 1; i <= 9; i++) {
		res += dan + "*" + i + "=" + dan*i + "\n";
	}
	console.log(res);
}

showDan(5);