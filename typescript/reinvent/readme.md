https://github.com/github/gitignore

https://docs.aws.amazon.com/CDK/latest/userguide
https://docs.aws.amazon.com/cdk/api/latest/docs/aws-construct-library.html
https://cdkworkshop.com/
https://catalog.workshops.aws/cicdonaws/
https://discord.gg/9zpd7TTRwq

cdkpatters.com
cdk8s.io
constructs.dev

gitter.im/awslabs/aws-cdk
aws/aws-cdk
aws/jsii

https://www.npmjs.com/package/cdk-dynamo-table-viewer

https://github.com/aws-samples/aws-cdk-examples


* `npm run build`   compile typescript to js
* `npm run watch`   watch for changes and compile
* `npm run test`    perform the jest unit tests
* `cdk deploy`      deploy this stack to your default AWS account/region
* `cdk diff`        compare deployed stack with current state
* `cdk synth`       emits the synthesized CloudFormation template


- lib/cdk-workshop-stack.ts is where your CDK application's main stack is defined. This is the file we'll be spending most of our time in.
- bin/cdk-workshop.ts is the entrypoint of the CDK application. It will load the stack defined in lib/cdk-workshop-stack.ts.
- package.json is your npm module manifest. It includes information like the name of your app, version, dependencies and build scripts like "watch" and "build" (package-lock.json is maintained by npm)
- cdk.json tells the toolkit how to run your app. In our case it will be "npx ts-node bin/cdk-workshop.ts"
- tsconfig.json your project's typescript configuration 
- .gitignore and .npmignore tell git and npm which files to include/exclude from source control and when publishing this module to the package manager.
- node_modules is maintained by npm and includes all your project's dependencies.



As you can see, the class constructors of both CdkWorkshopStack and lambda.Function (and many other classes in the CDK) have the signature (scope, id, props). This is because all of these classes are constructs. Constructs are the basic building block of CDK apps. They represent abstract "cloud components" which can be composed together into higher level abstractions via scopes. Scopes can include constructs, which in turn can include other constructs, etc.

Constructs are always created in the scope of another construct and must always have an identifier which must be unique within the scope it's created. Therefore, construct initializers (constructors) will always have the following signature:

    scope: the first argument is always the scope in which this construct is created. In almost all cases, you'll be defining constructs within the scope of current construct, which means you'll usually just want to pass this for the first argument. Make a habit out of it.
    id: the second argument is the local identity of the construct. It's an ID that has to be unique amongst construct within the same scope. The CDK uses this identity to calculate the CloudFormation Logical ID 

for each resource defined within this scope. To read more about IDs in the CDK, see the CDK user manual 
.
props: the last (sometimes optional) argument is always a set of initialization properties. Those are specific to each construct. For example, the lambda.Function construct accepts properties like runtime, code and handler. You can explore the various options using your IDE's auto-complete or in the online documentation 
.


