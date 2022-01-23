A struct is a composite aggregation type.


```go
// Define struct of the custom type Human:
type Human struct {
	FirstName string
	LastName  string
	Age       int
}

// Declare, initialize and assign a value to the struct:
Marie := Human{
	FirstName: "Marie",
	LastName:  "van de Klundert",
	Age:       2,
}

// Struct fields populated according to the order in which they are defined:
Jan := Human{"Jan", "van de Klundert", 5}
fmt.Printf("%v", Marie) // {Marie van de Klundert 2}
fmt.Printf("%v", Jan)   // {Jan van de Klundert 5}
fmt.Printf("%T", Jan)   // main.Human
// Create and print a struct with it's 0-values:
Zero := Human{}
fmt.Printf("%+v", Zero) // main.Human{FirstName: LastName: Age:0}
Zero.FirstName = "Sub"
Zero.LastName = "Zero"
Zero.Age = 201
fmt.Printf("%+v", Zero) // {FirstName:Sub LastName:Zero Age:201}

```

```go
// Structs can hold all types and have structs embedded within them:
type Person struct {
	Name        string
	Age         int
	Children    []string
	Favorites   map[string]string
	ContactInfo Contact
}
type Contact struct {
	Email string
	Phone string
}

Joe := Person{
	Name:     "Joe",
	Age:      35,
	Children: []string{"Jo", "Anne"},
	Favorites: map[string]string{
		"Color": "blue",
		"Food":  "pizza",
	},
	ContactInfo: Contact{
		Email: "jan@yolo.com",
		Phone: "06121345678",
	},
}	

// Create and use a struct receiver function:
func (p Person) PrintName() {
	fmt.Println(p.Name)
}
Joe.PrintName()								// Joe

// Pass the struct as a value to a func and change the name:
func (p Person) UpdateName(s string) {
	p.Name = s
	fmt.Println("Name in the function", p.Name)
}
Joe.UpdateName("Jimmy")						// Name in the function Jimmy
Joe.PrintName()								// Joe

// Pass the Person pointer or have the func transform the value into a pointer:
func (p *Person) UpdateNameByReference(s string) {
	(*p).Name = s
	fmt.Println("Name in the function", p.Name)
}
JoePointer := &Joe
JoePointer.UpdateNameByReference("Jimmy")	// Name in the function Jimmy
Joe.PrintName()								// Jimmy

// Working with the value directly (Go converts it to a pointer for us):
Joe.UpdateNameByReference("Carl")			// Name in the function Carl 
Joe.PrintName()								// Carl
```

```go
// Define struct / blueprint
type NetworkDevice struct {
	Name            string
	OperationSystem string
	OsVersion       string
}
// Declare a variable of the type NetworkDevice and set to 0 value:
var R1 NetworkDevice
// Define instance of a struct literal:
R1 := NetworkDevice{
	Name:            "R1",
	OperationSystem: "junos",
	OsVersion:       "16.R4",
}
// print Go-syntax representation of instance to screen
fmt.Printf("struct: %#v\n", R1)

// print individual struct values:
fmt.Println(R1.Name)			// R1
fmt.Println(R1.OperationSystem)	// junos
fmt.Println(R1.OsVersion)		// 16.R4

// Change or assign an individual struct value:
R1.Name = "Router1"
fmt.Println(R1.Name)			// Router1
```



```go
// Embedded struct, where Face is embedded in Human:
type Face struct {
	EyeColor string
	Eyes     int
}

type Human struct {
	name string
	Face		// Notice it is not Face Face
}
// We create Joe's Face:
joesFace := Face{EyeColor: "brown", Eyes: 2}
// After this, we create Joe:
joe := Human{name: "Joe", Face: joesFace}

// We can now access Joe's face properties directly:
joe.name			// Joe
joe.EyeColor		// brown
// Accessing the Face struct is also allowed:
joe.Face.EyeColor	// brown

// The anonymous struct can be constructed inside the main struct as well:
marie := Human{
	name: "marie",
	Face: Face{EyeColor: "blue", Eyes: 2},
}
marie.EyeColor		// blue
```