// Interfaces do not exist during the runtime.
interface Person {
    firstName: string,
    lastName: string,
    job: job,
    optional?: string
}
type job = "developer" | "manager" | "tester"

function generateEmail(input: Person):string {
    return `Hello ${input.firstName}, ....`
    
}

const jan: Person = {
    firstName: "Jan",
    lastName: "van de Klundert",
    job: "developer",
}


    
console.log(generateEmail(jan))

// guard function:
function isPerson(potentialPerson: any): boolean {
    if ('firstName' in potentialPerson && 'lastName' in potentialPerson && 'job' in potentialPerson){
        return true;
    } else {
        return false;
    }
}

function printEMailIfPerson(potentialPerson: any): void {
    if (isPerson(potentialPerson)) {
        console.log(generateEmail(potentialPerson));
    }
}

printEMailIfPerson(jan);
printEMailIfPerson({name: "Marie", lastName: "van de Klundert", job: "manager"});