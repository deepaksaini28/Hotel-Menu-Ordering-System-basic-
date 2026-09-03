# Hotel Menu

A simple Python command-line restaurant ordering program. Users can select up to two items from the menu and see the total order amount.

## Features

- Displays the restaurant menu
- Accepts item names without worrying about uppercase or lowercase letters
- Ignores extra spaces around item names
- Supports ordering a second item
- Calculates and displays the total amount

## Menu

| Item | Price |
| --- | ---: |
| Pizza | 100 |
| Pasta | 90 |
| Coffee | 80 |
| Chai | 40 |

## Requirements

- Python 3.x

## How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/your-repository-name.git
   ```

2. Open the project folder:

   ```bash
   cd your-repository-name
   ```

3. Run the program:

   ```bash
   python hotel_Menu.py
   ```

   On some systems, use:

   ```bash
   python3 hotel_Menu.py
   ```

## Example

```text
Welcome Deepak Restarant
Pizza : 100
Pasta : 90
Coffee : 80
Chai : 40
Enter the name of the item you want to order: Pizza
Your item pizza has been added to your order
Do you want to order another item? (yes/no): yes
enter the name of second item = Coffee
Your item coffee has been added to your order
Your total order amount is : 180
```

## Project Structure

```text
.
|-- hotel_Menu.py
|-- README.md
```

## Future Improvements

- Add quantities for each item
- Allow more than two items in one order
- Add a payment or checkout option
- Store menu items in a database

## Author

Deepak
