In Go, a map is a collection of key/value pairs.



```go
// Map literal
Capitols := map[string]string{
	"Germany":     "Berlin",
	"Netherlands": "Amsterdam",
	"Switzerland": "Bern",
}
fmt.Println(Capitols["Netherlands"])        // Amsterdam
// Requested key doesn't exist so value type's zero value is returned:
fmt.Println(Capitols["France"])             // ""

// declare nil map (writing to a nil map causes panic!!):
var nilMap map[string]string 			// map[]

// declaring an empty map literal is not the same as a nil map, you can write to it:
emptyMap := map[string]string{}

// declare map with no values using make:
var dict = make(map[string]string) //map[]

// Add a key, value:
dict["a"] = "a" // map[a:a]

// Delete a key/value pair:
delete(dict, "a") // map[]
delete(dict, "b") // safe to try and remove non-existing keys, does not crash the program
fmt.Println(dict)

// Iterating over a map:
dict["a"] = "a"
dict["c"] = "c"
dict["b"] = "b"
for key, value := range dict {
	fmt.Println(key, value)
}
//a a
//c c
//b b

// Dicts do not have the order guaranteed.
// To guarantee the order, sort the dict first:
keyList := make([]string, 0)
for k, _ := range dict {
	keyList = append(keyList, k)
}
sort.Strings(keyList)
for _, k := range keyList {
	fmt.Println(k, dict[k])
}
//a a
//b b
//c c

// remove the pointer from the var (does not destroy the map!)
dict = nil
// destroy the map
for key := range dict {
	delete(dict, key)
}

// copy dict
var dict2 = make(map[string]string)
for key, value := range dict {
	dict2[key] = value
}

// Comma OK idiom:
if v, ok := dict["a"]; ok {
	fmt.Printf("The value is %v.\n", v)
} else {
fmt.Println("Value not found.")
}
// Or shorter:
v, ok := dict["a"]		// a, true 
v, ok := dict["z"]		// false 

// Merge map example for map[string]string:
func mergeMaps(m1, m2 map[string]string) map[string]string {
	for key := range m2 {
		if _, ok := m1[key]; !ok {
			m1[key] = m2[key]
		}
	}
	return m1
}

// Go does not provide sets, but you can (ab)use a map as one:
intSet := map[int]bool{}
intSet[10] = true
intSet[12] = true
// bc you cannot have duplicate keys, this is in effect a set.
// For union or other set operations, check non std lib packages.


```


