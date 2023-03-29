function generateEmail(input) {
    return "Hello ".concat(input.firstName, ", ....");
}
var jan = {
    firstName: "Jan",
    lastName: "van de Klundert",
    job: "developer",
};
console.log(generateEmail(jan));
// guard function:
function isPerson(potentialPerson) {
    if ('firstName' in potentialPerson && 'lastName' in potentialPerson && 'job' in potentialPerson) {
        return true;
    }
    else {
        return false;
    }
}
function printEMailIfPerson(potentialPerson) {
    if (isPerson(potentialPerson)) {
        console.log(generateEmail(potentialPerson));
    }
}
printEMailIfPerson(jan);
printEMailIfPerson({ name: "Marie", lastName: "van de Klundert", job: "manager" });
//# sourceMappingURL=Interface.js.map