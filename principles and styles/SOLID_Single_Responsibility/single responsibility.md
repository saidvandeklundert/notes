## SRP: Single Responsibility Principle.

A software component (class, function) should have only one reason to change.  This is the case when a component is in charge of doing a single concrete thing.

When a component has only one reason to change, there is a high-cohesion. SRP helps us build more cohesive abstractions—objects that do one thing well, following the Unix philosophy. 

What we want to avoid at all costs is creating a 'god' object. A god object is an object that knows too much and has too many responsibilities.

When we are thinking about the SRP, we should ask ourselves if the class or function is responsible for things that demonstrate some sort of cohesion. Consider removing the functionalities that seem out of place and put them in their own class/function. 


Detecting SRP violations:
- if you describe a class and you oftentimes say 'and', 'and', 'and', then chances are the class is doing too much.
- if we keep having to update a class for reasons stemming from different domains, the class is doing too much
- if we find methods that are mutually exclusive and do not relate to each other, they are the different responsibilities that have to be broken down into smaller classes.


Example:

```python
class SystemMonitor:
    def load_activity(self):
        """Get the events from a source, to be processed."""
    def identify_events(self):
        """Parse the source raw data into events (domain objects)."""
    def stream_events(self):
        """Send the parsed events to an external agent."""
```

To:

```python
class ActivityWatcher:
    def load_activity(self):
        """Get the events from a source, to be processed."""
class  SystemMonitor:        
    def identify_events(self):
        """Parse the source raw data into events (domain objects)."""
class EventService:        
    def stream_events(self):
        """Send the parsed events to an external agent."""  

class AlterSystem:
    # get the classes above and use them 
    # in the run method.
    def run()->None:
         
```