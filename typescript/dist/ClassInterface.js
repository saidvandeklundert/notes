// tsc
// node .\dist\ClassInterface.js
var Human = /** @class */ (function () {
    function Human(firstName, lastName) {
        this.firstName = firstName;
        this.lastName = lastName;
    }
    Human.prototype.sayHello = function () {
        console.log("Hello");
    };
    Human.prototype.sayGoodbye = function () {
        console.log("Goodbye");
    };
    return Human;
}());
var marie = new Human("Marie", "van de Klundert");
marie.sayHello();
marie.sayGoodbye();
//# sourceMappingURL=ClassInterface.js.map