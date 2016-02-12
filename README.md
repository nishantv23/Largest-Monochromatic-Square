# Largest-Monochromatic-Square

The input is a (rectangular) grayscale image. Assuming a 8-bit representation, each pixel
is classified based on its value as Dark (0-63), Light (192-255), or Gray (64-191). The program identifies a largest Light square and a largest Dark square inside it, and marks the boundaries of the squares on the image itself by a contrasting shade.

The input is represented as a m × n matrix of 0s and 1s, with 0 standing for Black and 1 for White. Program is based on the opencv library of python.
To install opencv follow the given link => http://milq.github.io/install-opencv-ubuntu-debian/
