# Unittests and Integration Tests

## Overview
This project aims to implement unit tests and integration tests for a back-end application. Unit testing focuses on testing individual components in isolation, while integration testing ensures that different parts of the system work together as expected. 

## Testing Approach
### Unit Tests
Unit tests are designed to verify the correctness of individual functions by testing standard inputs and corner cases. These tests should only focus on the logic encapsulated within the function being tested, with external dependencies such as network or database calls being mocked. The primary goal of unit testing is to ensure that a function behaves as expected under various scenarios.

### Integration Tests
Integration tests evaluate the interactions between different components of the application, ensuring that the code paths work seamlessly from end to end. Unlike unit tests, integration tests may involve real external calls such as HTTP requests, file I/O, or database operations. The purpose of integration testing is to validate the integration and collaboration between various parts of the system.

Other concepts handled include:
### Memoization
Memoization is actually an optimization technique that is used to speed up the execution time of functions by caching the results of expensive function calls and returning the catched result when the same input occurs again. This technique is very useful and comes in handy when dealing with recursive algorithms where the same inputs are computed repeatedly.

## Objectives
- Explain the difference between unit and integration tests.
- Apply common testing patterns such as mocking, parametrization, and fixtures.

## Execution
`$ python -m unittest path/to/test_file.py`

## Required files
`utils.py`
`client.py`
`fixtures.py`
