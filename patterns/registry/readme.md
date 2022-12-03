## Registry

The idea behind the registry is that an application can accept new functionality by having it injected.

For instance, in an object based approach, an app would accept factories that can return a task. Users of the app can extend the app by injecting their own factory and task into the app and then using their own extension inside the existing app.

This can be usefull in case there is a framework to manage network devices and nodes. Since every network is different, allowing users to provide their own modules to the app in this way make the app more applicable and usable to a wider audience. A use case in this example would be where a user extends the app with a factory/task that can perform backups for  certain specific device type that is in use in the network.