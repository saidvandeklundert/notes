

Cloudformation is a template that captures the stack you wish to deploy to AWS.

CDK is a development kit you can use to express your cloud infrastructure in code. For instance, you can use typescript and define the stacks you wish to deploy to AWS as multiple classes. You can then use the CDK to generate the Cloudformation template for you.

When you use `cdk deploy` after having written your stack in Typescript:
- the Typescript will transpile to Javascript
- the Javascript will run and generate the Cloudformation template
- the Cloudformation template will be deployed to AWS


![CF and CDK](/img/cdk_cloudformation.png "CF and CDK")

### Lazy

```
!check what the CDK would build:
cdk list

! generate the Cloudformation template to cdk.out:
cdk synth

cdk deploy MyStack

cdk deploy --hotswap MyStack
```