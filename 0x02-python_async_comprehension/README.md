# Python - Async Comprehension

## Overview
This project focuses and explores a concept oulined in PEP 530 which is Asynchronous Comprehensions. By completing this project, one gains a good understanding of writing asynchronous generators, utilizing async comprehensions, and effectively type-annotating generators.

- `Asynchronous Generators` : are coroutines that produce a sequence of values asynchronously. They are defined using the async def syntax and employ the yield statement to produce values. By leveraging asynchronous generators, developers can efficiently generate sequences of data without blocking the event loop, thus enhancing concurrency and scalability.
- `Async Comprehensions` : provide a concise syntax for asynchronously generating collections of data. They enable developers to construct asynchronous generators in a compact and readable manner, similar to list comprehensions and generator expressions. By utilizing async comprehensions, developers can express complex asynchronous operations in a succinct and expressive manner, improving code readability and maintainability.
- `Type Annotation for Generators` : Python's type annotation system allows developers to specify the expected types of variables, parameters, and return values in their code. Type annotations for generators enable developers to provide additional type information for the values yielded by the generator. This helps improve code clarity, facilitate static type checking, and enhance overall code quality.

## Resources

- PEP 530 – Asynchronous Comprehensions (https://peps.python.org/pep-0530/)
- What’s New in Python: Asynchronous Comprehensions / Generators
- Type-hints for generators


## Tasks

### Task 0: Async Generator

File:

	- 0-async_generator.py, 0-main.py
Write a coroutine called async_generator that takes no arguments.
- The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the random module.



### Task 1: Async Comprehensions

Files

	- 1-async_comprehension.py, 1-main.py
Import async_generator from the previous task and then write a coroutine called async_comprehension that takes no arguments.
- The coroutine will collect 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers.



### Task 2: Run time for four parallel comprehensions

Files
	
	- 2-measure_runtime.py, 2-main.py
Import async_comprehension from the previous file and write a measure_runtime coroutine that will execute async_comprehension four times in parallel using asyncio.gather.
- measure_runtime should measure the total runtime and return it.

* Now, let's explain why the total runtime is roughly 10 seconds:

Each call to async_comprehension internally runs async_generator, which involves waiting for 1 second asynchronously per iteration. Since async_comprehension is called four times in parallel using asyncio.gather, the total time taken will be approximately 4 seconds (assuming there's no significant overhead).
The reason the total runtime is roughly 10 seconds (not exactly 4 seconds) is because there might be some overhead associated with starting and stopping coroutines, context switching, and other asyncio-related operations. Additionally, there could be slight variations in the execution time of each coroutine due to factors like system load, CPU performance, etc.
Therefore, even though the coroutines are executed in parallel, the total runtime is slightly longer than the sum of individual runtimes due to these factors.