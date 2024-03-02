Over the last few months, I dove into the AWS CDK. I really love working with it and I have used it to deploy a few simple applications. This article is written like an introduction and contains some notes on things I do not want to forget.

### AWS CDK introduction: what is it?


The AWS CDK, Cloud Development Kit, is an open source framework that lets you define all your cloud applications and systems in code. You can use different languages (Typescript, Python, Java, C#, Go, Rust and more) to define and build your infrastructure.

Say you use Typescript as an example. You define your cloud resources, like Lambda, DynamoDB, SQS and more in Typescript. Using the CDK, the Typescript will get transpiled to cloudformation templates and those templates are then used to manage your infrastructures. By managing this infrastructure through a programming language, you can easily have the infrastructure:
- version controlled
- peer reviewed
- automatically deployed after running through a pipeline of tests


Addit

## CDK core concepts:

`App`: all the stacks you are deploying using the CDK.
`Stack`: a cloudformation stack, or a collection of related resources. For instance: a lambda, an API Gateway and a bucket.
`Construct``: a CDK representation of one or more cloud resources, for instance an S3 bucket. A concstruct is an abstraction over cloudformation resources and it always represents 1 or more resources. Constructs can be categorized into multiple levels:
- `Level 1 Construct`: depends on a cloudformation resource. Hardly any abstractions.
- `Level 2 Construct`: CDK developped and curated abstractions that you can use for more convenience.
  Example: a bucket class with methods that offer some developper ergonomics. Methods such as `bucket.addLifeCycleRule()` etc. that your IDE will point out to you exist and tell you what parameters you need to pass.
- `Level 3 Construct`: CDK developped and curated abstractions that lets you define entire applications. These patterns might include an AWS Fargate container cluster employing an Application Load Balancer and a DynamoDB table. Note that L3 constructs can be a bit opinionated.

The applications, stacks, and constructs are written using common programming languages. For example, CDK written in Typescript will transpile to CloudFormation. 

The CDK also has CLI options to perform operations, such as synthesize CloudFormation templates from code, deploy the synthesized templates, do a diff with previously deployed templates etc.

The team that wrote the CDK leverages `jsii`:

'[jsii](https://github.com/aws/jsii) allows code in any language to naturally interact with JavaScript classes. It is the technology that enables the AWS Cloud Development Kit to deliver polyglot libraries from a single codebase!'

This technology generates binding with other languages allows people to use other languages to interact with the base Javascript classes that power the AWS CDK.


## Constructs

From the CDK book:

'The essence of abstraction is preserving information
that is relevant in a given context, and forgetting
information that is irrelevant in that context.'
-John V. Guttag, Introduction to Computation and Programming Using
Python (January 18 2013)

The top construct is the `App`. The `App` can contain 1 or more `Stacks`. These `Stacks` represent a collection of related resources. A `Stack` can contain 1 or more `Constructs`.  Essentially, you build your cloud app by:
- instantiating the App by passing in 1 or more Stacks
- instantiating the Stacks by passing in 1 or more Constructs

Level 1: The most basic construct that offers very little abstractions over the cloud formation resources. They always start with `Cfn` and lack any default settings etc.

Level 2: CDK developped and curated abstractions that you can use for more convenience. Some abstractions are provided that make it easier to wire different resources together. Helper methods are offered for common tasks (adding a table to DynamoDB for instance). Additionally, work was put in to provide some sensible defaults.

Level 3: The level 3 constructs contain multiple constructs from a lower level and combined, constitute an entire application or functionality. The CDK team also developped and curated Level 3 construct abstractions that lets you define entire applications. These patterns might include an AWS Fargate container cluster employing an Application Load Balancer and a DynamoDB table. Note that L3 constructs can be a bit opinionated. Most oftentimes, you will be writing your own Layer 3 constructs when you are creating your cloud resources. 

Constructs are grouped together in `Stacks`. The `Stacks` need to be added to the `App` and this is how the constructs can be deployed. For some inspiration on constructs in a variety of languages, check the [constructs](https://constructs.dev/) website.

## 

## Recommendation and best practices

A collection of tips and best practices that I have come across:
- put every application, stack and construct in its own file for increased readability
- put CDK code in it's own repo, with a readme that contains some description as well as a diagram of what is deployed
- write tests

## Links:

- [constructs](https://constructs.dev/) website.
- [cdk book examples](https://github.com/cdkbook/examples)
- [CDK on Github](https://github.com/aws/aws-cdk)
- [Typescript docs](https://www.typescriptlang.org/docs/)
- [Typescript handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
https://sage.amazon.dev/posts/832364