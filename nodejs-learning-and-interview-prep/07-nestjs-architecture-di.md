# Chapter 7: NestJS Architecture & Dependency Injection

To design enterprise-grade, maintainable Node.js backends, senior candidates are expected to know NestJS. NestJS brings architectural discipline, combining TypeScript support, Object-Oriented Programming (OOP) principles, and Functional Reactive Programming (FRP).

---

## 🏗️ The Core Architecture: Modules, Controllers, & Providers

NestJS structures applications into three core building blocks:

```text
       +-------------------------------------------------+
       |                  AppModule (Root)               |
       +-------------------------------------------------+
          /                                            \
+----------------------+                      +----------------------+
|     UsersModule      |                      |     AuthModule       |
+----------------------+                      +----------------------+
  /                 \                           /                 \
[UsersController] [UsersService]        [AuthController] [AuthService]
 (HTTP Endpoints)  (Business Logic)     (HTTP Endpoints)  (Business Logic)
```

### 1. Controllers
*   **Role:** Handle incoming HTTP requests, routing, and returning responses to the client.
*   **Best Practice:** Keep controllers thin. They should only validate requests and delegate business logic to services.

### 2. Providers (Services, Repositories, Helpers)
*   **Role:** Encapsulate business logic, database queries, and external API integrations.
*   **Key Behavior:** Can be injected as a dependency into controllers or other providers.

### 3. Modules
*   **Role:** Organizers that group related controllers and providers together.
*   **Imports:** Modules needed by this module.
*   **Controllers:** API routes handled by this module.
*   **Providers:** Injectable services instantiated by Nest.
*   **Exports:** Providers that this module makes visible and usable to *other* modules.

---

## 💉 Dependency Injection (DI) & Inversion of Control (IoC)

One of NestJS's core features is its **Inversion of Control (IoC)** container, which automates dependency management via **Dependency Injection (DI)**.

### Why DI Matters:
*   Without DI, class `UsersController` must manually instantiate `new UsersService()`. This tight coupling makes testing and swapping dependencies (like using a mock database repository) difficult.
*   With DI, the controller simply states what it needs in its constructor, and the IoC container instantiates and manages the lifecycle of the dependency.

### How NestJS DI Works Under the Hood:
1.  **Metadata Reflection:** TypeScript compiles metadata using `reflect-metadata`. Nest reads the constructor parameters of your classes.
2.  **The Registry:** The IoC container registers providers marked with the `@Injectable()` decorator.
3.  **Instantiation:** When `UsersController` is created, Nest looks at the constructor:
    ```typescript
    constructor(private readonly usersService: UsersService) {}
    ```
    Nest checks if an instance of `UsersService` exists in the container. If not, it instantiates `UsersService` first (recursively resolving any of `UsersService`'s dependencies) and passes it to the controller.

---

## 🔄 The NestJS Request Lifecycle

When a request hits a NestJS application, it goes through a highly structured pipeline. Understanding this lifecycle is critical for senior interviews:

```text
Request 
  │
  ├── 1. Global Middleware / Module Middleware
  │
  ├── 2. Guards (CanActivate - Auth / Roles check)
  │
  ├── 3. Interceptors (Pre-handler logic / caching)
  │
  ├── 4. Pipes (Validation / Transformation - ValidationPipe)
  │
  ├── 5. Route Handler (Controller method logic)
  │
  ├── 6. Interceptors (Post-handler logic / payload modification)
  │
  └── Exception Filters (Runs ONLY if an error is thrown in steps 2-5)
        │
        v
    Response
```

### 1. Guards
*   **Purpose:** Determine whether a request should be handled by the route handler based on conditions (permissions, authentication status).
*   **Execution:** Runs after middleware, but *before* interceptors or pipes.
*   **Example:** JwtAuthGuard.

### 2. Interceptors
*   **Purpose:** Bind extra logic before/after execution, transform the returned payload, extend basic behavior (e.g., logging, caching, timeouts).
*   **Execution:** Runs both before and after the route handler.

### 3. Pipes
*   **Purpose:** Transform input data (e.g., parsing a string to integer) or validate request body properties (using `class-validator` and `ValidationPipe`).
*   **Execution:** Runs right before the route handler.

### 4. Exception Filters
*   **Purpose:** Catch unhandled exceptions throughout the request lifecycle, formatting a clean, unified JSON error response for the client.

---

## 🧪 Testing NestJS: Unit & Integration Tests

Nest provides a `@nestjs/testing` package to mock the IoC container during testing:

```typescript
import { Test, TestingModule } from '@nestjs/testing';
import { UsersController } from './users.controller';
import { UsersService } from './users.service';

describe('UsersController', () => {
  let controller: UsersController;
  let service: UsersService;

  beforeEach(async () => {
    // Compile a mock IoC module
    const module: TestingModule = await Test.createTestingModule({
      controllers: [UsersController],
      providers: [
        {
          provide: UsersService,
          useValue: {
            findAll: jest.fn().mockResolvedValue([{ id: 1, name: 'John' }]),
          },
        },
      ],
    }).compile();

    controller = module.get<UsersController>(UsersController);
    service = module.get<UsersService>(UsersService);
  });

  it('should return mock users', async () => {
    expect(await controller.findAll()).toEqual([{ id: 1, name: 'John' }]);
  });
});
```
