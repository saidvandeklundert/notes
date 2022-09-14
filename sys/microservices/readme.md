


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



















Good links:
- https://www.thoughtworks.com/en-gb/insights/blog/rest-api-design-resource-modeling