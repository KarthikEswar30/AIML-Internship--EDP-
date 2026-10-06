# AI-Powered Personal Finance Assistant for Expense Categorization and Spending Insights

The goal of this project is to build a personal finance assistant that helps users manage transactions, automatically categorize expenses, analyze spending, track budgets, and generate personalized financial insights.

## Week 9 - Finalize Capstone Direction

Week 9 focuses on finalizing the scope, features, data requirements, architecture, and technology stack for the capstone project.

### Problem Statement

Managing personal finances manually can make it difficult to organize transactions, understand spending patterns, and monitor budgets. The proposed system aims to provide a simple application that automatically categorizes transactions and presents useful financial information and insights to the user.

### Proposed Solution

The Personal Finance Assistant will allow users to manually enter financial transactions. A machine-learning classification model will automatically predict the category of expense descriptions. The stored transactions will then be used for spending analysis, budget tracking, and personalized financial insights.

### Core Features

- Manual transaction entry
- Automatic ML-based expense categorization
- Income and expense tracking
- Spending analysis
- Budget tracking
- Personalized financial insights

### User Input

The prototype will allow the user to enter:

- Transaction description
- Amount
- Date
- Transaction type (Income or Expense)

A CSV dataset will be used for training the machine-learning model. CSV upload will not be the primary user input for the application.

### Expense Categories

The initial expense categories are:

- Food
- Transport
- Shopping
- Bills
- Entertainment
- Healthcare
- Education
- Other

### Proposed System Flow

User Transaction
    ->
Data Processing
    ->
ML Expense Categorization
    ->
Transaction Storage
    ->
Spending and Budget Analysis
    ->
Personalized Insights
    ->
User Dashboard

### Planned Technology Stack

#### Machine Learning and Data Processing

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib

#### Database

- SQLite

#### Backend

- Python
- FastAPI

#### Frontend

- React
- Vite
- Tailwind CSS

#### Development and Version Control

- VS Code
- Jupyter Notebook
- Git
- GitHub

### ML Approach

A machine-learning classification model will be trained using a financial transaction dataset to automatically categorize expense descriptions. The exact classification algorithm will be selected after examining and preprocessing the training dataset in Week 10.

### Database Approach

SQLite will be used to store user transactions during the prototype stage. It is a lightweight file-based database that can be used directly with the Python application.

### Scope

The capstone will focus on transaction categorization, financial tracking, spending analysis, budget monitoring, and personalized insights through a web-based application.

The following advanced features are intentionally outside the current scope and will be kept on hold:

- Expense or spending prediction
- Anomaly detection
- LLM-based chatbot
- Bank account/API integration

### Week 10-12 Plan

- Week 10: Build the core capstone features and produce a working prototype.
- Week 11: Deploy the application and obtain a live link.
- Week 12: Final polish, GitHub README update, and prepare the 5-minute demo pitch.

### Expected Outcome

A working personal finance assistant that accepts manual transactions, automatically categorizes expenses using machine learning, stores financial records, analyzes spending, tracks budgets, and provides personalized financial insights.