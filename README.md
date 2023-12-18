# Real Estate CLI

## Overview

The Real Estate CLI is a command-line interface designed for searching vacant houses based on location, number of bedrooms, and price range. The project consists of two main scripts:

1. `realestate_db_setup.py`: This script sets up the SQLite database, creating a table named "houses" to store information about available houses. It also inserts sample data for demonstration purposes.

2. `realestate_cli.py`: This script provides the command-line interface for users to search for vacant houses. It connects to the SQLite database, constructs SQL queries based on the provided criteria, and displays the results.

## Getting Started

### Prerequisites

- Python 3.x
- SQLite

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/shaddybett/real-estate-cli.git
   ```
