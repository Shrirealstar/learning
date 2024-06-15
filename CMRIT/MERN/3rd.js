const car = {
	make : "Toyota",
	model : "Inova",
	year : 2000,
	color : "Black"
};

console.log("Original properties of car : ");
for(let key in car){
	console.log(key + ':' + car[key]);
};

delete car.model;

console.log("After deletion :");
for(let key in car){
	console.log(key + ':' + car[key]);
};


const length = Object.keys(car).length;
console.log("Length of the object : ", length);