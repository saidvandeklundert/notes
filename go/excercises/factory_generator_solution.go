package main

import "fmt"

// Create an employee struct:
type employee struct {
	name, title string
	salary      int
}

// Define a function that can create an instance of an Employee
func (f *employee) Create(name string) *employee {
	return &employee{name, f.title, f.salary}
}

// Define a factory function that returns pointer to a struct of the type employee.
// Name the func EmployeeFactory and allow the specification of all the structfields:
func EmployeeFactory(name, title string, salary int) *employee {
	return &employee{name, title, salary}
}

// Define a factory function that returns  function which will return pointer to a struct of the type employee.
// Name the func EmployeeFactoryFunctional. The higher order function should allow the specification of all the structfields.
// The lower order function should allow the specification of the name field only.
// Goal of the function is to be able to instantiate a factory for a certain role/salary level.
// We need to be able to use the function like so: EmployeeFactoryFunctional("developer", 80000)
func EmployeeFactoryFunctional(title string, salary int) func(name string) *employee {
	return func(name string) *employee {
		return &employee{name, title, salary}
	}
}

func main() {
	// Use the EmployeeFactory function to create Joe the developer with a salary of 60000:
	Joe := EmployeeFactory("Joe", "developer", 60000)
	// Print the values that make up Joe:
	fmt.Printf(`
Joe value: 		            	%v
Joe pointer:           			%p
Joe Type:           			%T
`, Joe, &Joe, Joe)
	// Increase Joe's salary to 80 kand verify it increased:
	Joe.salary = 80000
	fmt.Printf(`
Joe value: 		            	%v
Joe pointer:           			%p
`, Joe, &Joe)
	// Increase Joe's salary to 100k and change his function to 'senior developer':
	Joe.title = "senior developer"
	Joe.salary = 100000
	fmt.Printf(`
Joe value: 		            	%v
Joe pointer:           			%p
`, Joe, &Joe)
	// Create a developer factory that can make developers earning 80k and senior developers making 100k:
	devFactory := EmployeeFactoryFunctional("developer", 80000)
	seniorDevFactory := EmployeeFactoryFunctional("senior developer", 100000)
	// Instantiate Sally the dev and Marie the senior dev:
	Sally := devFactory("Sally")
	Marie := seniorDevFactory("Marie")
	fmt.Printf(`
Sally value: 		            	%v
Sally pointer:           			%p
`, Sally, &Sally)
	fmt.Printf(`
Marie value: 		            	%v
Marie pointer:           			%p
`, Marie, &Marie)
	// Give Sally and Marie a raise and verify that they are now making 20k more:
	Sally.salary = 100000
	Marie.salary = 120000
	fmt.Printf(`
Sally salary: 		            	%v
Marie salary:           			%v
`, Sally, Marie)

}
