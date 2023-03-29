// tsc
// node .\dist\Class.js 
abstract class Server {
    // private is inaccessible outside the class, even subclasses
    // protected is accessible only in the class and its subclasses
    protected port: number;
    protected address: string;

    constructor(port: number, address: string) {
        this.port = port;
        this.address = address;
    }

    startServer(): void {
        console.log(`Server started on ${this.address}:${this.port}`);
    }

    abstract stopServer(): void;
}

class DBServer extends Server {
    constructor(port: number, address: string) {
        super(port, address); // call the base class constructor
    }

    startServer(): void {
        console.log(`DBServer started on ${this.address}:${this.port}`);
    }

    stopServer(): void {
        console.log(`DBServer stopped on ${this.address}:${this.port}`);
    }

}

const server = new DBServer(8080, "localhost");
server.startServer();

console.log(`Access private field ${(server as any).address}`)