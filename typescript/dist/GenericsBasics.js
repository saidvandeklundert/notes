// tsc
// node .\dist\GenericsBasics.js
function returnKeys(obj) {
    console.log(Object.keys(obj));
    return obj;
}
var a = returnKeys({ a: 1, b: 2, c: 3 });
var b = returnKeys({ 1: "a", 2: "b", 3: "c" });
var janneman = {
    name: "Jan",
    age: 30,
    item: "cheese"
};
console.log(janneman);
var GenericNumber = /** @class */ (function () {
    function GenericNumber() {
    }
    return GenericNumber;
}());
var MyClass = /** @class */ (function () {
    function MyClass(field) {
        this.field = field;
    }
    return MyClass;
}());
var example = new MyClass("Hello World");
var another_example = new MyClass(123);
console.log(example, another_example);
//# sourceMappingURL=GenericsBasics.js.map