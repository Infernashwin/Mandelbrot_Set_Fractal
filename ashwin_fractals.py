'''
Program Name: ashwin_fractal.py 
Programmer Name: Ashwin Mayurathan
Date: 5-09-2022
Description: This code generates an image  mandelbrot set fractal, and adds 
             coloured sections to represent how fast certain points become diverge

Imports from Tkinter and Complex_Numbers
'''
from ComplexNum import *
import tkinter as tk

#Creates the Window and Cavas
window = tk.Tk()
window.geometry ("800x800")
window.title ("Mandelbrot Set Window")
canvas = tk.Canvas(window, height = 800, width = 800)

#Creates a constant which stores a number and a colour.
#Uses the colour to represent the how fast a point diverges.
DIVERGE_COLOURS = [[13, "#33F9FF"], [14, "#33FFA5"], [16, "#F3FF33"], [20, "#FFB233"], [35, "#FF3633"]]

#Main Function
def main():
    #For how many points along the x plane of the canvas
    for i in range(800):
        #For how many points along the y plane of the canvas
        for x in range(800):
            #Adjusts the given co-ordinates on the plane to a new value
            #x values become a number from -2 to 1
            #y values become a number from -1 to 1
            new_points = adjust(i,x)

            #Creates a variables to store the adjusted points as a complex number
            #The x value is the real portion
            #The y values is the imaginary portion
            starting_num = ComplexNum()
            starting_num.assign_val(new_points[0], new_points[1])

            #Sends the adjusted point aswell as the orignial points to the function plot_point
            plot_point(starting_num,i,x)

    #Draws everything into the canvas
    canvas.pack ()
    canvas.update ()

    #Keeps the tkinter GUI running
    window.mainloop ()

#Adjust Function: This functions changes the coordinates to be in the range for 
#                 the points to be used in the recursive sequence.
def adjust(x, y):
    #Adjusts the x co-ordinate
    x = 3*x/800 - 2
    #Adjusts the y co-ordinate
    y = 3*y/800 - 1.5
    #returns the adjusted values
    return(x,y)

#Plot Point Function: This function plots the points on to the canvas based on their 
#                     coordinates.
def plot_point(constant, canvas_x, canvas_y):
    #Initializes Variables count and run
    count = 0 #How many times the sequence has been run
    run = True #If the sequence should be run

    #Creates a complex number to store the current number of the sequence
    current_num = ComplexNum()

    #Until 100 itterations have been run or the code gets into an error
    while ((count <= 100) and (run)): 
        #Increment count
        count += 1

        #Try to run the sequence
        try:
            current_num.run_sequence(constant)

        #If an error occues then stop the sequence
        except:
            run = False

    #Auto sets the colour to be black
    colour = "#000000"

    #Uses count to see how long it taken to diverge, and sets the colour according 
    #to the list DIVERGE_COLOURS
    for elem in DIVERGE_COLOURS:
        if (count >= elem[0]):
            colour = elem[1]

    #If the sequence did not diverge
    if (-1 <= current_num.get_imaginary_val() <= 1 and -2 <= current_num.get_num_val() <= 1):
        colour = "#FFFFFF"

    #Draw the dot on the canvas
    line = canvas.create_line(canvas_x, canvas_y, canvas_x + 1, canvas_y + 1, fill = colour)

#Call the main function to start the code
main()