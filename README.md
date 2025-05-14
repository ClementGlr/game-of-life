# Game of life

Create a python version of game of life

#### How to use it

First you need to have python3

Then install pygame with the following :
`pip install pygame`

Finally just launch the game with
`python src/front.py`

#### How to play

For now the size of the grid is what you see (the grid does not continue after the screen)
When you launch the game you can click on the square to place/remove living cell. Then press 'space' to launch the simulation. At every moment you can press 'space' again to pause the game and add/remove living cell.

#### Rule of game of life

Each dark cell is a living cell. Each white on is a dead one. Between each step the living and dead cell are updated following those rules :

1.  Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
2.  Any live cell with more than three live neighbours dies, as if by overcrowding.
3.  Any live cell with two or three live neighbours lives on to the next generation.
4.  Any dead cell with exactly three live neighbours becomes a live cell.
