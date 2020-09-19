# HookRunner
## Status:
Project in developement phase.

## What and Why?:
The idea to this project was born from the necissity to tight control over user scripts, for example RPM in-between install scripts(post<Something>(.sh)? or pre<Something>(.sh)? ... ).
Because this script are most of the times, bash based, it basiclly allows all the users free editing on the script and a varied options to impelement their logic ( And I saw crazy things, like entire backup logics of 100+ code lines poping up on a single script file).
This is very annoying If you need to supply distribution services which is constanly updated by a large number of teams and pepole.
  
## Description:
Hook Runner is a more strict tight framework, emphasizing DSL and C libraries to create a balance between capability and saftey, written in python. 

## Flaw Chart:
[Flow Chart Here](https://github.com/eladch156/HookRunner/blob/master/HookRunner.png?raw=true)

  
## Tutorial / Instructions 
<To Be Added>
  
## Pro && Cons ( I can think of ... )
### Pros
- Safer then using bash user scripts.
- Due to using C based library interaction - The inner core logic is faster, safer and stronger.
- Easy to montior compared to bash - In case of errors. Very easy to find code owner to speed up problem fixing.
- Not designed to be a console, so can work as a Service for example.
- Very dynamic TCP Socket communication - Making multiple sources easier.
- Libraries can be easily updated - Even after deployment.
- Decoupling between script logic to IS logic.
### Cons
- Commands require pre-compilation
- Python is not the fastest in the world, so some functionallity might be slower compared to bash.
- DSL to initiate command running might be limited.
- Monetization still required - This is just a framework to make it better. 

# License, Credits
- Antlr4
- Typescript, Babel, Webpack, Node, VueJS, Flask, Flask-RESTFUL - For Web Client IS.
