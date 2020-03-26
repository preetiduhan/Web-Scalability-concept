# Web-Scalability-concept

Front-end applications built with scale in mind are mostly stateless; they depend heavily on caching; and, most importantly, they allow horizontal scalability by simply adding more hardware.



The key difference between stateful and stateless services is that instances of a stateless service are fully interchangeable and clients can use any of the instances without seeing any difference in behavior. Stateful services, on the other hand, keep some “knowledge” between requests, which is not available to every instance of the service. Whenever clients want to use a stateful service, they need to stick to the selected instance to prevent any side effects.

THE ROLE OF A MESSAGE QUEUE IN A MICROSERVICE 
ARCHITECTURE:

In a microservice architecture, there typically are 
cross-dependencies that mean no single service can perform without getting help from 
other  services.  This  is  where  it  is  crucial  for  systems  to  have  a  mechanism  in  place,  
allowing services to keep in touch with each other with no blocked responses. Message 
queuing fulfils this purpose by providing a means for services to push messages to 
a  queue  asynchronously  and  ensure  they  are  delivered  to  the  correct  destination.  To  
implement message queuing, a message broker is required.

RabbitMQ is a message queuing software also known as a message broker or queue 
manager.

Message  queues  enable  asynchronous  
communication,  which  means  that  other  applications  (endpoints)  that  are  producing  
and  consuming  messages  interact  with  the  queue  instead  of  communicating  directly  
with each other. 

A message can include any information. It could, for example, contain information 
about a process or job that should start on another application, possibly even on another 
server, or it might be a simple text message.

-EXCHANGES

Messages are not published directly to a queue; instead, the producer sends a message 
to an exchange. The job of an exchange is to accept messages from the producer appli-cations  and  route  them  to  the  correct  message  queues.  It  does  this  with  the  help  of  
bindings  and  routing  keys.  A  binding  is  a  link  between  a  queue  and  an  exchange.
essages are not published directly to a queue. 
Instead, the producer sends messages to an exchange. Exchanges are message routing 
agents,  living  in  a  virtual  host  (vhost)  within  RabbitMQ.  Exchanges  accept  messages  
from  the  producer  application  and  route  them  to  message  queues  with  the  help  of  
header attributes, bindings, and routing keys. 

A  binding  is  a  “link”  configured  to  make  a  connection  between  a  queue  and  an 
exchange.  The  routing  key  is  a  message  attribute.  The  exchange  might  look  at  the  
routing key, depending on exchange type, when deciding on how to route the message 
to the correct queue.



