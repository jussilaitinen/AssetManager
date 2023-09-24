# Portfolio Management App

Application Architecture:
The Portfolio Management App's foundational structure has been established using Python's Flask framework. This serves as the backbone to ensure smooth user interactions and reliable performance across various functionalities.

Key Achievements:
Database Configuration: The app is integrated with a PostgreSQL database named "assetmanager". This ensures robust data management for user and asset information.

User Authentication: A functioning user authentication system is in place. Users can:

Log into the system using their credentials.
Register for a new account (Sign-up functionality).
Receive feedback if login credentials are incorrect or if a username already exists during registration.
Login & Sign-up Pages: Corresponding templates (login.html and signup.html) have been integrated, facilitating user interactivity.

User Dashboard: Upon successful login, users are redirected to a placeholder "second page" that can be further developed to showcase portfolio details and other functionalities.

More work is needed to get more relevant data and show it in an informative way to the customers

## Description

Portfolio Management App is a web-based application designed to help individuals manage and track their investment portfolios across multiple asset classes, including stocks, bonds, real estate, and more. It provides features for tracking asset performance, risk assessment, and investment diversification.

## Key Features

### All Users
- **User Authentication:** Sign up, login, and logout
- **Dashboard:** Overview of all assets in the portfolio with latest value and performance metrics
- **Asset Allocation:** View and modify the percentage allocation of different assets
- **Performance Metrics:** View key metrics like total return, annualized return, volatility, etc.
- **Asset Addition:** Add new assets to the portfolio manually or by searching available stocks, bonds, etc.
- **Asset Removal:** Remove assets from the portfolio
- **Risk Assessment:** Analyze the portfolio’s risk profile based on historical data and correlations between assets

### Admin
- **User Management:** Ability to manage users (optional)
- **Asset Classes:** Add or remove available asset classes (Stocks, Bonds, Real Estate, etc.)

## Technologies

 -**Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript 
- **Database:** PostgreSQL 
