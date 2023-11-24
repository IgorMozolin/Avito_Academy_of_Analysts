# Final project
In this project you can find my implementation of the interface for ordering pizza.

## Pizza CLI

Pizza CLI is a simple command-line interface (CLI) for ordering pizzas 
and tracking delivery times. It provides a set of commands to 
order different types of pizzas and optionally include delivery.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/IgorMozolin/Avito_Academy_of_Analysts
   cd Final_project
  
2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt

##Usage

###Order a Pizza

To order a pizza, use the order command. You can specify the pizza type, 
size, and choose whether to include delivery.

    python cli.py order --delivery --size XL Hawaiian
    
###Display the Menu

To see the available pizzas and their ingredients, use the menu command.

    python cli.py menu
    
###Testing

The project includes a set of tests to ensure the functionality of the Pizza CLI. 
Run the tests using the following command:

    pytest tests.py