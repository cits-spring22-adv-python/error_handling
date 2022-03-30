# Error Handling

## Instructions
The following project is a fully built program that can utilize command line arguments
to create gradient tiled image. It's origin occurs in the top-left corner of the image,
and then proceeds left to right, top to bottom. The

### Running the Program
The program can be run in two ways:

1. With Command Line Arguments
   1. When running with Command Line Arguments, they are as follows:
      1. starting_color    | The RGB hex code for the starting color, with no #.
      2. ending_color      | The RGB hex code for the ending color, with no #.
      3. blocks_per_vector | The number of blocks in a given row or column.

Example Using Command Line Arguments

`python main.py ed5f55 6e98cc 4`

There are no other variations that you need to implement.

2. Without Command Line Arguments
   1. Without command line arguments, the program should choose two random colors for
      starting and ending color, as well as random number of blocks per vector.
      This number should be divisible by 2.
