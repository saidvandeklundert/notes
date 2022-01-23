package main

// Create an employee struct:

// Define a function that can create an instance of an Employee

// Define a factory function that returns pointer to a struct of the type employee.
// Name the func EmployeeFactory and allow the specification of all the structfields:

// Define a factory function that returns  function which will return pointer to a struct of the type employee.
// Name the func EmployeeFactoryFunctional. The higher order function should allow the specification of all the structfields.
// The lower order function should allow the specification of the name field only.
// Goal of the function is to be able to instantiate a factory for a certain role/salary level.
// We need to be able to use the function like so: EmployeeFactoryFunctional("developer", 80000)

func main() {
	// Use the EmployeeFactory function to create Joe the developer with a salary of 60000:

	// Print the values that make up Joe:

	// Increase Joe's salary to 80 kand verify it increased:

	// Increase Joe's salary to 100k and change his function to 'senior developer':

	// Create a developer factory that can make developers earning 80k and senior developers making 100k:

	// Instantiate Sally the dev and Marie the senior dev:

	// Give Sally and Marie a raise and verify that they are now making 20k more:

}
