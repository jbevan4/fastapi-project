# [SQLModel_over_DAO]

- Status: Accepted <!-- optional -->
- Deciders: JLB <!-- optional -->
- Date: 2023-07-20 <!-- optional -->

Technical Story: [description | ticket/issue URL] <!-- optional -->

## Context and Problem Statement

I found myself needing to iteratively prototype and generate database tables efficiently without writing raw sql. The challenge was to find a solution that balances the speed of development without duplicating models into Data Access Objects (DOAs)

## Decision Drivers <!-- optional -->

- I'm lazy
- I dislike raw sql
- I have no idea what I'm doing

## Considered Options

- [SQLModel](https://sqlmodel.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/) in conjuction with [Alembic](https://alembic.sqlalchemy.org/en/latest/)

## Decision Outcome

SQLModel, because it was fast af to integrate

### Positive Consequences <!-- optional -->

- Able to generate tables with a single line of code

### Negative Consequences <!-- optional -->

- Feels like i've tied myself to SQLModel, which is super gross in terms of clean architecture
- I think I'm probably going to maybe strip this out at some point

## Pros and Cons of the Options <!-- optional -->

### SQLModel

- Good, because it's a single line of code to set up my db
- Good, because I didn't have to duplicate my models
- Bad, because I've sold my soul to SQLModel

### SQLAlchemy & Alembic

- Good, because its the most used tool for python database interactions
- Good, because its got a huge userbase and has solved most database problems
- Bad, because its a hefty setup

## Links <!-- optional -->

- [SQLModel](https://sqlmodel.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Alembic](https://alembic.sqlalchemy.org/)
