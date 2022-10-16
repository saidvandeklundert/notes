Lambda Layer
---

<!--BEGIN STABILITY BANNER-->
---

![Stability: Stable](https://img.shields.io/badge/stability-Stable-success.svg?style=for-the-badge)

> **This is a stable example. It should successfully build out of the box**
>
> This example is built on Construct Libraries marked "Stable" and does not have any infrastructure prerequisites to build.
---
<!--END STABILITY BANNER-->


## Overview

CDK example to create a Python Lambda that uses a Python [Lambda Layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html).
The example demonstrates use of Lambda Layer Python folder structure, and use of L2 Constructs for deploying and using Lambda Layer with a function in CDK.


```
$ python3 -m venv .env
$ source .env/bin/activate
% .env\Scripts\activate.bat
$ pip install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

### CDK Deploy

A Lambda layer is a .zip file archive that can contain additional code or data. When deployed, CDK creates a layer .zip
asset to be stored in a staging bucket managed by CDK. To enable this the AWS account being used needs to be
[bootstrapped](https://docs.aws.amazon.com/cdk/latest/guide/bootstrapping.html).

With default profile,
```
$ cdk bootstrap
```

With specific profile,
```
$ cdk bootstrap --profile test
```

With the bootstrap complete, we are ready to deploy the lambda function and lambda layer.

```
$ cdk deploy
```
