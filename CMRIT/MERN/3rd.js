// Define a car object
const car = {
    make: 'Toyota',
    model: 'Camry',
    year: 2020,
    color: 'Red'
};

// Printing car object properties
console.log('Car Object Properties:');
for (let prop in car) {
    console.log(prop + ': ' + car[prop]);
}

// Deleting the second property
const properties = Object.keys(car);
if (properties.length >= 2) {
    delete car[properties[1]];
    console.log('\nAfter deleting the second property:');
    for (let prop in car) {
        console.log(prop + ': ' + car[prop]);
    }
} else {
    console.log('There are less than 2 properties in the car object.');
}

// Getting the length of the object
const length = Object.keys(car).length;
console.log('\nLength of the car object:', length);
