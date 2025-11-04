## OOPS RELATED PROBLEMS

### 1. Bank Account System
    - Build a BankAccount class where users can:
    - Deposit and withdraw money
    - Check balance through a getter (no direct variable access)
    - Prevent overdrawing (encapsulation)

    ! Focus: Private attributes (__balance), getters/setters, input validation.

### 2. Student Gradebook
    - Create a Student class that stores marks in different subjects and calculates:
    - Total marks, Average, Grade (A/B/C/D)

    ! Focus: Constructor, instance methods, encapsulation.

### 3. Shopping Cart
    - Create a Product and Cart class.
    - Add/remove items to the cart.
    - Calculate total price.
    - Handle edge cases (like removing an item not in cart).

    ! Focus: Class interactions (composition).

### 4. Shape Hierarchy
    - Create an abstract base class Shape with an abstract method area().
    - Then implement:
        - Circle
        - Rectangle
        - Triangle
    - Each should override area() appropriately.

    ! Focus: abc module, abstraction, inheritance, polymorphism.

### 5. Vehicle Inheritance Model
    - Build: A Vehicle base class with start_engine() and stop_engine().
    - Subclasses like Car, Bike, and Truck that override start_engine()   differently.
    - Add attributes like fuel_type, max_speed, and capacity.

    ! Focus: Inheritance and method overriding.

### 6. Employee Management System
    - Create:
    - Base class: Employee
    - Subclasses: Manager, Developer, Intern
    - Each should have a calculate_salary() method that computes salary differently.

    ! Focus: Inheritance, polymorphism, class vs instance attributes.

### 7. Notification System
    - Create a base class Notification with a method send().
    - Implement child classes:
        - EmailNotification
        - SMSNotification
        - PushNotification
    - Each should implement send() differently.
    - Then write a function that sends notifications without knowing the object type (duck typing).

    ! Focus: Polymorphism, method overriding.

### ---------------------------------- DONE -----------------------------------------

### 8. Library Management System
    - Classes: Book
    - Member: Librarian
    - Library (that holds collections and handles lending/returning)
    - Apply encapsulation for availability status, and use inheritance if needed for roles.

    ! Focus: Object relationships, real-world modeling, encapsulation, abstraction.

### 9. Payment Gateway (Abstraction + Polymorphism)
    - Abstract class: PaymentProcessor
    - Implement:
        - CreditCardProcessor
        - PayPalProcessor
        - CryptoProcessor
    - Each with a different process_payment() implementation.

    ! Focus: abc module, polymorphism, dependency injection.

### 10. Restaurant Order System

    - Classes: MenuItem, Order, Customer, Restaurant.
    - The restaurant can take multiple orders, each containing menu items.
    - Calculate total, apply discounts (maybe through a DiscountMixin class).

    ! Focus: Composition, inheritance, mixins.

### 11. Online Course Platform (Like Udemy)

    - Course class (title, instructor, price).
    - User class (can enroll in courses).
    - Instructor and Student inherit from User.
    - Platform class manages users and courses.

    ! Focus: Class hierarchy, polymorphism, data modeling.

### 12. E-commerce Backend Mock
    - Classes:
        - Product, 
        - Customer, 
        - Order, 
        - Cart, 
        - Payment.
    - Order uses PaymentProcessor abstraction (like real backend).
    - Add apply_coupon() using a Mixin for reusable logic.

    ! Focus: Full OOP system, abstraction, encapsulation, composition, and mixins.

### 13. Model-View-Controller Simulation
    - Build a mini version of MVC in Python:
    - Model class handles data (like a User model).
    - View class displays it (simple text output).
    - Controller handles interactions between them.

    ! Focus: Abstraction and layering — OOP in Flask architecture.

### 14. Custom Exception Hierarchy
    - Define custom exception classes for backend errors like:
        - DatabaseConnectionError
        - InvalidInputError
        - AuthenticationError

    ! Focus: Inheritance and error handling design.

### 15. Repository Pattern for Flask Models
    - Create a UserRepository class that encapsulates CRUD logic for a User model.
    - You can later plug it into a Flask route.

    ! Focus: Encapsulation, abstraction, separation of concerns.
