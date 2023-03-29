// tsc
// node .\dist\ClassInterface.js

interface Ihuman {
    sayHello(): void;
    sayGoodbye(): void;
}

class Human implements Ihuman {

    firstName: string;
    lastName: string;

    constructor( firstName: string, lastName: string) {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    sayHello(): void {
        console.log("Hello");
    }
    sayGoodbye(): void {
        console.log("Goodbye");
    }
}


const marie = new Human("Marie", "van de Klundert");
marie.sayHello();
marie.sayGoodbye();