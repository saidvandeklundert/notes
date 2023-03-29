// tsc
// node .\dist\GenericsBasics.js

function returnKeys<T extends object>(obj: T): T{
    console.log(Object.keys(obj));
    return obj;
}

const a = returnKeys({ a: 1, b: 2, c: 3 });
const b = returnKeys({ 1: "a", 2: "b", 3: "c" });

interface GenericPerson<T> {
    name: string;
    age: number;
    item: T;
}

const janneman: GenericPerson<string> = {
    name: "Jan",
    age: 30,
    item: "cheese"
}
console.log(janneman);

class GenericNumber<NumType> {
    zeroValue: NumType;
    add: (x: NumType, y: NumType) => NumType;
  }
   
class MyClass<T> {
    field: T
    constructor(field: T) {
        this.field = field
    }
}
  
const example = new MyClass("Hello World");
const another_example = new MyClass(123);
console.log(example, another_example);