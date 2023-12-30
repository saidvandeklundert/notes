The AWS CDK, Cloud Development Kit, is an open source framework that lets you define all your cloud applications and systems in code. You can use different languages (Typescript, Python, Java, C#, Go, Rust and more) to define and build your infrastructure.

Say you use Typescript as an example. You define your cloud resources, like Lambda, DynamoDB, SQS etc. all in Typescript. Using the CDK, then transpile this to cloudformation templates and use those templates to manage your infrastructures. All the while, you manage the Typescript you wrote like any other code you work with:
- version controlled
- peer reviewed
- automatically deployed after running through a pipeline


## CDK core concepts:

App: all the stacks you are deploying using the CDK.
Stack: a cloudformation stack, or a collection of related resources. For instance: a lambda, an API Gateway and a bucket.
Construct: a CDK representation of one or more cloud resources, for instance an S3 bucket.
- `Level 1 Construct`: depends on a cloudformation resource. Hardly any abstractions.
- `Level 2 Construct`: CDK developped and curated abstractions that you can use for more convenience.
  Example: a bucket class with methods that offer some developper ergonomics. Methods such as `bucket.addLifeCycleRule()` etc. that your IDE will point out to you exist and tell you what parameters you need to pass.
- `Level 3 Construct`: CDK developped and curated abstractions that lets you define entire applications. These patterns micht include an AWS Fargate container cluster employing an Application Load Balancer and a DynamoDB table. Note that L3 constructs can be a bit opinionated.

The applications, stacks, and constructs are written using common programming languages. For example, CDK written in Typescript will transpile to CloudFormation. 

The CDK also has CLI options to perform operations, such as synthesize CloudFormation templates from code, deploy the synthesized templates, do a diff with previously deployed templates etc.

The team that wrote the CDK leverages `jsii`:

'[jsii](https://github.com/aws/jsii) allows code in any language to naturally interact with JavaScript classes. It is the technology that enables the AWS Cloud Development Kit to deliver polyglot libraries from a single codebase!'

This technology generates binding with other languages allows people to use other languages to interact with the base Javascript classes that power the AWS CDK.




[cdk book examples](https://github.com/cdkbook/examples)


https://sage.amazon.dev/posts/832364