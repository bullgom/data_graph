# Data Graph

A data structure to manage a graph of data dependencies

## Requirements

- Auto forwarding of data
    when a data has been generated by a node, it should be forwarded to the
    connected nodes
- Edge management
  - create
  - delete
  - edit?
- Requirement checking
  - A node should be able to check if all the prerequisite datas are received
  - When it has received them all, generate new data and forward to next nodes
- Reset
    The prerequisites will be cached. Reset will, yes, reset all the cached data to None

- A node should keep its own generated data, children should use that

- A node should be able to generate multiple data? No!
- A receiver node should connect to one generator node at a time

## Terminologies

- DataNode composed of
  - RequirementChecker: Has a `callback(data_name)` which registers the generated
  data and when all the requirements are met, calls the `data_generator.generate(requirements)`
  - DataGenerator: Holds the logics for generating data
  - Port: Where the generated data resides

- RootDataNode: Instead of other node generting data, this node's data is
generated from external source
  - `put` method: A data is given by external mechanism
