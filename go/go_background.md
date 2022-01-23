Developped at Google by Robert Griesemer (Hotspot JVM, UTF-9), Rob Pike (plan 9, UTF-8), and Ken Thompson ( C, Unix).

Created with concurrency and parallelism in mind. It was first released 2012 with three goals in mind:
- efficient compilation
- efficient execution
- ease of programming

The 'why' for Go is described [here](https://golang.org/doc/faq#creating_a_new_language) and the purpose is described [here](https://golang.org/doc/faq#What_is_the_purpose_of_the_project).

Go is good for:
- web services at scale
- networking (HTTP, TCP, UDP)
- concurrency/parallelism
- systems
- automation/command line tools


Guiding principles of the Go design:
- expressive, comprehensible, sophisticated
- clean, clear, easy to read





From Rob Pike:
```
Go programming language was conceived as an answer to some of the problems we were seeing developing software infrastructure at Google. The computing landscape today is almost unrelated to the environment in which languages being used, mostly C++, Java and Python, had been created.

The problems introduced by multicore processors, networked systems, massive computation clusters and the web programming model were being worked around rather than addressed head-on.

Moreover, the scale has changed: today's server programscomprise tens of millions of lines of code, are worked on by hundreds or even thousands of programmers, and are updated literaly every day. To make matters worse, build time has stretched to many minutes, even hours, on large compilation clusters.
```


From Brian Kernighan:
```
Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it.
```


From Edsger W. Dijkstra:
```
Simplicity is a great virtue but it requires hard work to achieve it and education to appreciate it. And to make matters worse: complexity sells better.
```