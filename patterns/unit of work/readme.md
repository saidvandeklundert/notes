## Unit of work pattern

Unit of work is a design pattern that guarantees the atomicity of our business transations, ensuring that all transations are committed at once, or rolled back if any of them fails.

The notion comes from the world of databases, where database transactions are implemented as units of work which ensure that every transaction is:
- atomic: everything succeeds or everything fails
- consistent: it conforms to the constraints of the database
- isolated: does not interfere with other transactions
- durable: written to persistent storage