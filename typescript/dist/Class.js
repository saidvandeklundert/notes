var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (Object.prototype.hasOwnProperty.call(b, p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        if (typeof b !== "function" && b !== null)
            throw new TypeError("Class extends value " + String(b) + " is not a constructor or null");
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
// tsc
// node .\dist\Class.js 
var Server = /** @class */ (function () {
    function Server(port, address) {
        this.port = port;
        this.address = address;
    }
    Server.prototype.startServer = function () {
        console.log("Server started on ".concat(this.address, ":").concat(this.port));
    };
    return Server;
}());
var DBServer = /** @class */ (function (_super) {
    __extends(DBServer, _super);
    function DBServer(port, address) {
        return _super.call(this, port, address) || this;
    }
    DBServer.prototype.startServer = function () {
        console.log("DBServer started on ".concat(this.address, ":").concat(this.port));
    };
    DBServer.prototype.stopServer = function () {
        console.log("DBServer stopped on ".concat(this.address, ":").concat(this.port));
    };
    return DBServer;
}(Server));
var server = new DBServer(8080, "localhost");
server.startServer();
console.log("Access private field ".concat(server.address));
//# sourceMappingURL=Class.js.map