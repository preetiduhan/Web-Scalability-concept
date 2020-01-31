# Web-Scalability-concept

Front-end applications built with scale in mind are mostly stateless; they depend heavily on caching; and, most importantly, they allow horizontal scalability by simply adding more hardware.



The key difference between stateful and stateless services is that instances of a stateless service are fully interchangeable and clients can use any of the instances without seeing any difference in behavior. Stateful services, on the other hand, keep some “knowledge” between requests, which is not available to every instance of the service. Whenever clients want to use a stateful service, they need to stick to the selected instance to prevent any side effects.

