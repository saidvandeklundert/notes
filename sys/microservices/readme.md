


### Monolith: 

Pattern in which an entire application is deployed as a single build.

Advantages:
- easy to access data and logic from different domains
- straightforward troubleshooting

Disadvatages:
- resourcewise, you can only scale the app as a whole, not individual parts of the app
- tight coupling often occurs in a monolith
- deployments become slower as the app grows
- testing pipeline becomes slower as the app grows
- sometimes a big change needs to be deployed that touches a lot of parts of the app at the same time

### Microservices:

Pattern in which components are designed as independently deployable services. Microservices are defined around business subdomains and talk to each other using lightweight protocols, such as HTTP.

Big companies, like AWS, originally dubbed this 'Service Oriented architecture'.

Advantages:
- indivdual services have a small codebase, leading to fast testing and rapid deployment
- flexible in terms of design. Every service can use it's own stack and language.
- easy to troubleshoot individual components

Disadvantages:



Microservices also come with some challenges:
- service deomposition: how to properly break down a system into micro-services and define their boundaries.
- integration tests
- handling service unavailability
- tshooting distributed transactions
- increased operational complexity and infra overhead



## Layers

Thinking about layers simplifies creation of microservices APIs. You could use the the following layers when thinking about them:

- `API layer`: adapter on top of the business layer that:
  - validates incoming requests  
  - communicates with the business layer
  - returns expected responses
- `Business layer`: implementation of the service capabilities and controls the interactions between the API layer and the data layer. For instance, it knows how to place an order or cancel one.
- `Data layer`: how to interface with the source data and make it persist

These layers can be applied in a hexagonal architecture:
- web api interface: the adapter that helps the core (business layer) communicate with web clients (we should be able to swap one front end to the other)
- business layer: the core of the app
- database: adapter to the data layer (we should be able to swap from one db to the other)

None of these layers should interfere with each other. We can achieve this by building `port` (or interfaces) between the core layer and the adapters. Leverage dependancy inversion to achieve this:
- depend on abstractions, not on low-level details
- abstractions should not depend on details, instead, details should depend on abstractions (e.g., the data layer depends on the interface and not the other way around)

## Microservices design

`service decomposition`: breaking a system down into microservices.

Three design principles can be of aid:
- `Database per service principle`: every microservice owns its data and access to it happens through the service's API.
- `Loose coupling principle`: must be able to update a service without affecting another one and each service must be able to complete requests without relying on other services
- `Single responsibility principle`: the microservice should be designed around a specific business capability or subdomain

You absolutely must get this right in order to prevent from building a distributed monolith.

### Database per service principle

Each microservice owns a specific set of the data. When other services need to access that data, they should use the service's API.

Services can use the same database, they should just be made to be the sole owner of part of the data.

The principle is important becase encapsulating data access behind a service allows us to design our data models for optimal access for the service. Additionally, we will also be able to make changes to the database without breaking other services.

When services own their own data, the coupling between them is automatically reduced.

### Loose coupling principle

Services should be designed with a clear separation of concenrs. Loosely coupled services don't rely on the implementation details of each other:
- services can operate independantly. If there is a service that cannot fulfill any request without calling another service, there is no clear separation of concerns and both services belong together.
- services can be updated without impact to other services

### Single responsibility principle

We should design components with few responsibilities, ideally with just one responsibility. Strive to design a microservice around a single business capability or subdomain.


## Service decomposition

`Decomposition by subdomains` is an approach that draws inspiration from the field of Domain-Diven Design (DDD). Decomposition by subdomains applies DDD to model processes and flows of the business through subdomains. Using this approach, we create a microservice for each subdomain. It oftentimes results ina  more robust technical design.

We can also use `decomposition by business capabilities`. Here, the structure of the business is analyzed and the microservices are mapped to teams/organizations. Can be less efficient and problematic later on in case or reorganizations.


Ideally, decomposition by subdomains AND by business capabilities is applied at the same time.


## REST

REST stands for Representational State Transfer. REST is an architectural style used to build loosely coupled and highly scalable APIs. REST APIs are structured around resources, which are entities that can be manipulated through the API.

There are two types of resources: 
- collections: list of entities (collections endpoint example: `/orders`)
- singletons: a single entity (singleton endpoint example: `/orders/{order_id}`)

The REST architecture implies the following constraints:
- Client-server architecture: the UI must be decoupled from the backend
- Statelessness: the server must not manage state between requests
- Cacheability: requests that always return the same respone must be cacheable
- Layered system: the API may be architected in layers, but such complexity must be hidden from the user
- Code on demand: the server can inject code into the user interface on demand
- Uniform interface: the API must provide a consistent interface for accessing and manipulating resources

There are API design patterns that can be of help:
- API Gateway pattern:


URI: Uniform Resource Identifier: used to identify individual resources. The URI must be unique and should always return the same resource. For isntance, URI `/orders/121` should always return the same order. When it is deleted, the order should not be re-used.

### HATEOAS

Hyoermedia as the Engine of Application State, or HATEOAS. This is a paradigm in the design of REST APIs that emphasizes the concept of descoverability.

Example, when a client requests a resource from the server, the response must contain a list of related links to the resource. So when someone requests details for an order, the response should include links to cancel and to pay for the order.

```json
{
    "status": "active",
    "created": "2023-09-01",
    "order": [
        {
            "product": "cappuccino",
            "size": "small",
            "quantity": 1
        },
    ],
    "links": [
        {
            "href": "/orders/8/cancel",
            "description": "Cancels the order",
            "type": "POST"
 
        },
    ]
}
```
HATEOAS is not always used because:
- doc already has this info, OpenAPI for instance already provides better and more documentation
- there are too many related endpoints so the info is not very useful
- it is not always clear what is related

### Richardson Maturity Model:

- level 0: web APIs a la RPC: all requesrts to the server are done on the same endpoint
- level 1: introducing the concept of resource: instead of 1 endpoint, the server exposes URLs that represent resources
- level 2: using HTTP methods and status codes: HTTP verbs and status codes are introduced.
- level 3: API discoverability (HATEOAS for instance)

### Structured resource URLs with HTTP methods:

HTTP requests indicate the type of action we want to perform in the server. The most relevant HTTP methods in REST APIs are:
- GET: returns information about the requested resource
- POST: creates a new resource
- PUT: performs a full update by replacing a resource
- PATCH: update specific properties of a resource
- DELETE: deletes a resource

Put versus patch: full replace vs incremental update.

Together, the above facilitate CRUD: Create, Update, Read and Delete.


### HTTP status codes:
- 1xx group: signals that an operation is in progress.
- 2xx group: signals that a request was successfully processed.
- 3xx group: signals that a resource has been moved to a new location.
- 4xx group: signals that something was wrong with the request.
- 5xx group: signals that there was an error while processing the request.




## OpenApI specifications

The OpenAPI specification is a standard that describes how you can document RESTful APIs. With the specification, you can describe every element of an API. This includes the endpoints, the formats of the requests and responses, the payloads and the security.

A OpenAPI specfication that describes an API can be used to generate:
- an HTML page that serves as documentation (e.g. ReDoc)
- a swagger page that serves as documentation as well as some testing
- a CLI
- client libraries in all sorts of languages

An OpenAPI is structured around 5 sections:
1: openapi: the version of OpenAPI used to produce the specifications
2: info: general information (title, version, etc)
3: servers: list of URLs where the API is available. Can contain multiple URLs (for staging, prod etc.).
4: paths: describe the endpoints exposed by the API, including the epected payloads, the allowed parameters and the format of the responses.
5: components: defines reusable elements that are referenced across the specification, such as schemas, parameters, security schemes, request bodies and responses. 


`Schema`: a definition of the expected attributes and types in your request and response objects. OpenAPI schemas are defined using JSON Schema syntax. It can be written in JSON or YAML:

```json
{
    "order": {
        "product": "coffee",
        "size": "big",
        "quantity": 1
    }
}
```

Or in YAML:

```yaml
order:
  product: coffee
  size: big
  quantity: 1
```
When things get overly nested, use JSON pointers:


```json
{
    "OrderItemSchema": {
        "type": "object",
        "properties": {
            "product": {
                "type": "string"
            },
            "size": {
                "type": "string"
            }
        }
    },
    "Order": {
        "status": {
            "type": "string"
        },
        "order": {
            "type": "array",
            "items": {
                "$ref": '#/OrderItemSchema'
            }
        }
    }
}
```







## API authorization and authentication

Authentication: verify the identity of a user

Authorization: determine what resources a user is allowed to access.

### Authentication

2 important options:
- OAuth (Open Authorization): standard protocol for access delegation
- OpenID Connect (OIDC)



#### OAuth

OAuth allows a user to grant 3rd party apps access to protected resources they own in another website without sharing credentials.

Typically the access is granted by issuing a token wich the third party application uses to access the user's information.

#### OpenID Connect (OIDC)


OIDC is an identity verification protocol that allows users to bring their identity from one website (the identity provider) to another. OIDC is built on top of OAuth and we can use the same flows defined by OAuth to authenticate users.

When we authenticate using the OIDC protocol, we distinguish two types of tokens:
- `ID tokens`: identify the user, and they contain information such as the user’s name, their email, and other personal details. You must use ID tokens only to verify the user identity, and never to determine whether a user has access to an API. 
- `Access tokens`: validates API access. Typically does not contain user information and instead contain a set of claims about the access rights of the user.

In short: 
- an `id token`:
  - carries an identity
  - the audience of the ID token is the autorization server
- an `access token`:
  -  carries claims about user's right to access the API
  - the audience is the API you build

## Jason Web Tokens (JWT)

In OAuth and OpenID Connect, user access is verified by means of a token known as JSON Web Token or JWT.

A JWT is a token that represents a JSON document. The JSON document contains claims, such as who issued the token, what the audience of the token is or when the token expires. The JSON document is typically encoded as a Base64 string. JWTs are normally signed with a private secret or a cryptographic key.

Example of a JWT:
```
eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpc3MiOiJodHRwczovL2F1dGguY29mZmVlbWVzaC5pby8iLCJzdWIiOiJlYzdiYmNjZi1jYTg5LTRhZjMtODJhYy1iNDFlNDgzMWE5NjIiLCJhdWQiOiJodHRwOi8vMTI3LjAuMC4xOjgwMDAvb3JkZXJzIiwiaWF0IjoxNjM4MjI4NDg2LjE1OTg4MSwiZXhwIjoxNjM4MzE0ODg2LjE1OTg4MSwic2NvcGUiOiJvcGVuaWQifQ.oblJ5wV9GqrhIDzNSzcClrpEQTMK8hZGzn1S707tDtQE__OCDsP9J2Wa70aBua6X81-zrvWBfzrcX--nSyT-A9uQxL5j3RHHycToqSVi87I9H6jgP4FEKH6ClwZfabVwzNIy52Zs7zRdcSI4WRz1OpHoCM-2hNtZ67dMJQgBVIlrXcwKAeKQWP8SxSDgFbwnyRTZJt6zijRnCJQqV4KrK_M4pv2UQYqf9tQpj2uflTsVcZq6XsrFLAgqvAg-YsIarYw9d63rs4H_I2aB3_T_1dGPY6ic2R8WDT1_AXzi-crjoWq9A51SN-kMaTLhE_v2MSBB3A0zrjbdC4ZvuszAqQ
```

If you look closely at the above example, you’ll see the string contains two periods. The periods act as delimiters which separate each component of the JSON Web Token. A JSON Web Token document has three sections:
- `Header`: identifies the type of token, as well as the algorithm and the key that were used sign the token. We use this information to apply the right algorithm to verify the token’s signature.
- `Payload`: contains the document’s set of claims. The JWT specification includes a list of reserved claims which identify the issuer of the token (the authorization server), the token’s audience or intended recipient (our API server), and its expiry date, among other details. In addition to JWT’s standard claims, a payload can also include custom claims. We use this information to determine whether the user has access to the API.
- `Signature`: a string representing the token’s signature.


### JWT header:

JSON Web Tokens contain a header which describes the type of token, as well as the algorithm and the key that that were used to sign the token. 

Example of a header:
```json
{
  "alg": "RS256",
  "typ": "JWT",
  "kid": "ZweIFRR4l1dJlVPHOoZqf"
}
```
What does this mean?
- alg: tells us that the token was signed using the RS256 algorithm.
- typ: tells us that this is a JWT token.
- kid: tell us that the key used to sign the token has the ID ZweIFRR4l1dJlVPHOoZqf.

### JWT payload

Example:
```json
{
  "iss": "https://auth.coffeemesh.io/",
  "sub": "ec7bbccf-ca89-4af3-82ac-b41e4831a962",
  "aud": "http://127.0.0.1:8000/orders",
  "iat": 1667155816,
  "exp": 1667238616,
  "azp": "7c2773a4-3943-4711-8997-70570d9b099c",
  "scope": "openid"
}
```

- `iss` tells us that the token has been issued by the https://auth.coffeemesh.io server identity service.
- `sub` tell us that the user has the identifier ec7bbccf-ca89-4af3-82ac-b41e4831a962. The value of this identifier is owned by the identity service. Our APIs can use this value to control access to the resources owned by this user in an opaque way. We say this ID is opaque because it doesn’t disclose any personal information about the user.
- `aud` tells us that this token has been issued to grant access to the orders API. If the value of this field is a different URL, the orders will reject the request.
- `iat` tells us that the token was issued on the 30th of October of 2022 at 6:50pm.
- `exp` tells us that the token expires on the 31st of October of 2022 at 5:50pm.
- `azp` tells us that the token has been requested by an application with identifier 7c2773a4-3943-4711-8997-70570d9b099c. This is typically a frontend application. This claim is common in tokens that have been issued using the OpenID Connect protocol.
- The `scope` field tells us that this token was issued using the OpenID Connect protocol.

### Producing a JWT

To form the final JSON Web Token, we encode the header, the payload, and the signature using base64url encoding. The header, payload, and signature are then concatenated using periods as separators. Libraries like PyJWT take care of the heavy lifting of producing a JSON Web Token.



To produce a signed token with this payload, we use PyJWT’s encode() function, passing in the token, the key to sign the token, and the algorithm we want to use to sign the token:


```python
>>> import jwt
>>> jwt.encode(payload=payload, key='secret', algorithm=’HS256')
'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2F1dGguY29mZmVlbWVzaC5pby8iLCJzdWIiOiJlYzdiYmNjZi1jYTg5LTRhZjMtODJhYy1iNDFlNDgzMWE5NjIiLCJhdWQiOiJodHRwOi8vMTI3LjAuMC4xOjgwMDAvb3JkZXJzIiwiaWF0IjoxNjY3MTU1ODE2LCJleHAiOjE2NjcyMzg2MTYsImF6cCI6IjdjMjc3M2E0LTM5NDMtNDcxMS04OTk3LTcwNTcwZDliMDk5YyIsInNjb3BlIjoib3BlbmlkIn0.sZEXZVitCv0iVrbxGN54GJr8QecZfHA_pdvfEMzT1dI'
```

For a more secure encryption, we use a private/public key pair to sign the token with the RS256 algorithm. To sign JWTs, we typically use keys that follow the X.509 standard, which allows us to bind an identity to a public key. To generate a private/public key pair, run the following command from your terminal:
```
$ openssl req -x509 -nodes -newkey rsa:2048 -keyout private_key.pem -out public_key.pem -subj "/CN=coffeemesh"
```
The minimum input for a X.509 certificate is the subject’s common name (CN), which in this case we set coffeemesh. If you omit the -subj flag, you’ll be prompted with a series of questions about the identity you want to bind the certificate to. This command produces a private key under a file named private_key.pem, and the corresponding public key under a file named public_key.pem. 


Example:
```python
# file: jwt_generator.py
from datetime import datetime, timedelta
from pathlib import Path
import jwt
from cryptography.hazmat.primitives import serialization
def generate_jwt():
    now = datetime.utcnow()
    payload = {
        "iss": "https://auth.coffeemesh.io/",
        "sub": "ec7bbccf-ca89-4af3-82ac-b41e4831a962",
        "aud": "http://127.0.0.1:8000/orders",
        "iat": now.timestamp(),
        "exp": (now + timedelta(hours=24)).timestamp(),
        "scope": "openid",
    }
    private_key_text = Path("private_key.pem").read_text()
    private_key = serialization.load_pem_private_key(
        private_key_text.encode(),
        password=None,
    )
    return jwt.encode(payload=payload, key=private_key, algorithm="RS256")
print(generate_jwt())
```


You can use https://jwt.io to inspect a JWT. ALternaticely, use the following Python:
```python
>>> import base64
>>> base64.decodebytes('eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9'.encode())
b'{"alg":"RS256","typ":"JWT",}'
```

### Validating a JWT


You must:
- validate the JWT's signature
- validate that it's claims are correct

Users must send a JWT in each request and the API server must validate the token on each request. JWTs are designed for stateless communication between client and server and must be validated properly. Though, sometimes you'll see caching being used.

Tokens can be signed with a secret key or with a private/public key pair. 

To validate a token in code, we first load the public key:
```python
>>> from cryptography.x509 import load_pem_x509_certificate
>>> from pathlib import Path
>>> public_key_text = Path('public_key.pem').read_text()
>>> public_key = load_pem_x509_certificate(public_key_text.encode('utf-8')).public_key()
```

Now that we have the public key, we use it to validate a token:
```python
>>> import jwt
>>> access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ..."
>>> jwt.decode(token, key=public_key, algorithms=['RS256'], audience=["http://127.0.0.1:8000/orders"])
{'iss': 'https://auth.coffeemesh.io/', 'sub': 'ec7bbccf-ca89-4af3-82ac-b41e4831a962', 'aud': 'http://127.0.0.1:8000/orders', 'iat': 1638114196.49375, 'exp': 1638200596.49375, 'scope': 'openid'}
```

### Adding authorization

There are 2 major strategies for handling authorization:
1. handling validation in an API Gateway
2. handling validation in each service

This describes the second strategy.



Good links:
- https://www.thoughtworks.com/en-gb/insights/blog/rest-api-design-resource-modeling