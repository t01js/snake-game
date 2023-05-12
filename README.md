# Snake Game

This is a simple implementation of the classic Snake Game using the Pygame library. The player controls a snake that moves around the screen, trying to eat food and grow longer while avoiding collisions with the walls and its own body.

## How to play

Use the arrow keys to control the movement of the snake. The objective is to eat the red food dots that appear randomly on the screen. Each time the snake eats a food dot, it grows longer. The game ends when the snake collides with the walls or its own body.

## Code Overview

### `Main` class

This class is responsible for the main game loop and overall management of the game. It initializes the game, updates the state of the snake and food objects, draws them on the screen, and handles events such as keyboard input.

### `Snake` class

This class represents the snake object in the game. It keeps track of the body segments, direction of movement, and methods for updating and drawing the snake. The `handle_key` method is used to change the direction of the snake based on the user input.

### `Food` class

This class represents the food object in the game. It is responsible for randomly generating new food positions on the screen and drawing them.

### Variable Names

- `self.screen`: represents the Pygame screen where the game is displayed.
- `self.clock`: represents the Pygame clock that manages the game's timing.
- `self.snake`: represents the `Snake` object that the player controls.
- `self.food`: represents the `Food` object that the snake tries to eat.
- `self.score`: keeps track of the player's score.
- `self.font`: represents the Pygame font used to display the score.

### Styling

Variable names have been written in **bold** to make them more visible and easy to read. 

## Dependencies

This code requires Pygame to be installed in order to run. You can install it using pip:

```
pip install pygame
```

## How to run

To run the game, simply execute the `main.py` file:

```
python main.py
```

## Acknowledgements

This code is based on a tutorial from [Tech With Tim](https://www.youtube.com/channel/UC4JX40jDee_tINbkjycV4Sg).
