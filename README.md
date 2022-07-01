# Random Diagram Generator for Shan House Clash of Centipedes Game 2022

Use case:
- Each generated diagram is each assigned to a player in our Clash of Centipedes Game, as a unique identifier :)

What this script does:
- Generates n number of diagrams
- Each diagram is a big triangle, made of 9 small triangles
- Each of the 9 small triangles are color coded
- Each diagram generated is associated with a code that describes its color coded state

Planning:
- Find a python module that can convert canvas drawing into jpg files
- Use a script to generate a string-encoded shape, detailing the color coding of the shape
- Use tkInter Canvas to draw the required shapes
- Convert the shapes into jpg files
