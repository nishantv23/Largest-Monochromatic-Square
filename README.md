# Largest-Monochromatic-Square

The input is a (rectangular) grayscale image. Assuming a 8-bit representation, each pixel
is classified based on its value as Dark (0-63), Light (192-255), or Gray (64-191). Identifying a largest Light square and a largest Dark square inside it, and to mark the boundaries of the squares on the image itself by a contrasting shade.
You can suitably modify the algorithm used for the theory assignment (reproduced below)
and use a suitable image processing library for conversion between the image file and the
pixel matrix.
The input is represented as a m × n matrix of 0s and 1s, with 0 standing for Black and 1
for White. An example is shown below with the largest monochromatic squares all being
of dimension two.
