# Pendulum Collision Simulation

## Overview

This project is a simple pendulum collision simulation built using the Python `PyGame` library. The simulation features two pendulums, each attached to the same fixed point, and the user can adjust the mass of each pendulum before starting the simulation. During the simulation, the pendulums swing back and forth under the influence of gravity, and when they collide, their angular velocities are exchanged based on their masses.

## Features

- **Interactive Menu**: Adjust the mass of each pendulum using the keyboard before starting the simulation.
- **Realistic Physics**: The pendulums' movement is based on real physics calculations, including angular acceleration, gravity, and mass.
- **Collision Detection**: When the pendulums collide, their velocities change according to their masses, simulating a physical collision.
- **Return to Menu**: The user can press `ESC` at any time during the simulation to return to the main menu.

## Instructions

### Prerequisites

Make sure you have Python installed along with the `pygame` library. You can install `pygame` using pip:

```bash
pip install pygame
```

### How to Run the Program

1. Clone or download the project files.
2. Run the `pendulum_simulation.py` script:
   
   ```bash
   python pendulum_simulation.py
   ```

3. You'll start on the **Main Menu** screen, where you can adjust the mass of the pendulums:
   - Use the `LEFT` and `RIGHT` arrow keys to decrease or increase the mass of **Pendulum 1**.
   - Use the `UP` and `DOWN` arrow keys to decrease or increase the mass of **Pendulum 2**.
   - Once you're satisfied with the mass values, press `SPACE` to start the simulation.

4. In the simulation, the pendulums will swing, and you'll see them interact and collide.
   - You can press `ESC` at any time to return to the main menu.

### Controls Summary

- `LEFT/RIGHT ARROW KEYS`: Adjust the mass of Pendulum 1.
- `UP/DOWN ARROW KEYS`: Adjust the mass of Pendulum 2.
- `SPACE`: Start the simulation.
- `ESC`: Return to the main menu.

## Simulation Details

- The pendulums are connected to the same origin, and they swing due to the influence of gravity.
- The angle of each pendulum is updated based on the current angular velocity and the gravitational force.
- The mass of each pendulum affects the outcome of collisions. Heavier pendulums transfer less of their velocity upon impact.
- The simulation runs at 60 frames per second, and the motion is recalculated every frame for smooth animation.

## Future Improvements

Here are a few possible extensions that could be implemented in the future:
- **Energy Loss**: Add friction or air resistance to simulate energy loss over time.
- **Visual Enhancements**: Improve the graphics with textures, animations, or trails that show the path of the pendulums.
- **Additional Features**: Include more pendulums or allow the user to change the length of the strings.

## License

This project is open-source and licensed under the MIT License. You are free to modify and distribute the code as long as proper credit is given.

---

### Author

Prof. Pimpão – Educational project on physics simulation using Python and PyGame.
