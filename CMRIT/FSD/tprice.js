// Prompt for input
var price = parseFloat(prompt("Enter the product price:"));
var product_name = prompt("Enter the product name:");
var tax = parseFloat(prompt("Enter the tax:"));

// Calculate total
var total = price + tax;

// Output the result
console.log("The total cost of " + product_name + " is: $" + total.toFixed(2));
