# PYHVR Project

## Business Requirements

- An MVP of a REST API client library for use with interacting with Fivetran's HVR software
- The client should cover all documented rest api versions
- The client should provide a function for each endpoint available in each version
- The client should be importable and should take at least a base url, a username and a password for initialization
- The client should serialize and deserialize json to python objects
- The client should raise exceptions with helpful error messages in case of errors

## Technical Details

- Implemented in Python 3.12
- ALWAYS Use uv for package management
- The client should have asyncio support
- The client should be in a subdirectory named src
- No persistence
- Use popular libraries
- As simple as possible
- The client should be usable within a context manager


## Strategy

1. Research the HVR Rest APIS located here, https://fivetran.com/docs/hvr6/rest-api/rest-api-reference
2. Write plan with success criteria for each phase to be checked off. Include project scaffolding, including .gitignore, and rigorous unit testing.
3. Execute the plan ensuring all critiera are met
4. Carry out extensive integration testing with Playwright or similar, fixing defects
5. Only complete when the MVP is finished and tested, with the server running and ready for the user

## Coding standards

1. Use latest versions of libraries and idiomatic approaches as of today
2. Keep it simple - NEVER over-engineer, ALWAYS simplify, NO unnecessary defensive programming. No extra features - focus on simplicity.
3. Be concise. Keep README minimal. IMPORTANT: no emojis ever
4. Follow 12 factor app best practices
5. Use internal functions where it makes sense
6. ALWAYS test using pytest
7. ALWAYS format and lint code using ruff

