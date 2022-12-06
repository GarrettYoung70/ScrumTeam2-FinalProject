'''
Function to generate cost matrix for flights
Input: none
Output: Returns a 12 x 4 matrix of prices
'''
import os

def get_cost_matrix():
    cost_matrix = [[100, 75, 50, 100] for row in range(12)]
    return cost_matrix
    #[100, 75, 50, 100]
    #[100, 75, 50, 100]
    #[100, 75, 50, 100]
    #[100, 75, 50, 100]
    #[100, 75, 50, 100]
    #[100, 75, 50, 100]
    #[100, 75, 50, 100]
    #[100, 75, 50, 100]
    #[100, 75, 50, 100]
    #[100, 75, 50, 100]
    #[100, 75, 50, 100]
    #[100, 75, 50, 100]

def calculate_cost_matrix():
    matrix = get_cost_matrix()
    return(matrix)

def getSeatingChart():
    #Create the seating chart with all default values
    seatingChart = [['0' for col in range(4)] for row in range(12)]
    #Initialize array to store taken seats for checking later
    takenSeats = []
    reservation = []
    #Open reservations.txt
    with open("reservations.txt") as f:
        #Iterate through each line in the txt file
        cost_matrix = get_cost_matrix()
        for x in f:
            #Split the lines up by ,
            reservation = x.split(",")
            #Change the default value in the seating chart to X for each taken seat
            seatingChart[int(reservation[1])][int(reservation[2])] = "X"
            takenSeats.append([int(reservation[1]), int(reservation[2])])
        f.close()
    return seatingChart

def getTotalCost():
    totalCost = 0
    cost_matrix = get_cost_matrix()
    seatingChart = getSeatingChart()
    rows = 12
    columns = 4
    for i in range(rows):
        for j in range(columns):
            if seatingChart[i][j] == "X":
                totalCost = cost_matrix[i][j] + totalCost
            else:
                continue
    return totalCost