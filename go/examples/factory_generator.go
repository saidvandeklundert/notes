package main

import "fmt"

// the employee struct:
type employee struct {
	name, title string
	salary      int
}

func (f *employee) Create(name string) *employee {
	return &employee{name, f.title, f.salary}
}

// structural approach: returns pointer to created struct:
func EmployeeFactory(name, title string, salary int) *employee {
	return &employee{name, title, salary}
}

// functional approach: return function instead of object:
func EmployeeFactoryFunctional(title string, salary int) func(name string) *employee {
	return func(name string) *employee {
		return &employee{name, title, salary}
	}
}

func main() {
	Joe := EmployeeFactory("Joe", "developer", 60000)
	fmt.Printf(`
Joe value: 		            	%v
Joe pointer:           			%p
Joe Type:           			%T
`, Joe, &Joe, Joe)
	// Joe gets a bump:
	Joe.salary = 80000
	fmt.Printf(`
Joe value: 		            	%v
Joe pointer:           			%p
`, Joe, &Joe)
	// Joe is promoted:
	Joe.title = "senior developer"
	Joe.salary = 100000
	fmt.Printf(`
Joe value: 		            	%v
Joe pointer:           			%p
`, Joe, &Joe)
	// Create the factory using EmployeeFactoryFunctional:
	devFactory := EmployeeFactoryFunctional("developer", 80000)
	seniorDevFactory := EmployeeFactoryFunctional("senior developer", 100000)
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
	// We can still change the struct:
	Sally.salary = 100000
	fmt.Printf(`
Sally value: 		            	%v
Sally pointer:           			%p
`, Sally, &Sally)

}
