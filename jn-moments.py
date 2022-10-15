error = True
#code will run until user input allows it to calculate a moment
while error == True:
    length_of_beam = float(input("What is the length of the beam? (in metres) "))
    position_of_pivot = float(input("What is the position of the pivot? (in metres from the start of the beam) "))
    mass_of_beam = float(input("What is the mass of the beam? (in kg) "))
    position_of_force = float(input("What is the position of the force? (also in metres from the start of the beam) "))
    magnitude_of_force = float(input("What is the magnitude of the force? (in Newtons) "))
    is_positive = input("Is the force acting upwards? ")
    position_of_centre_of_mass = 0.5*length_of_beam
    #assuming the beam is uniform
    moment_of_weight = (position_of_centre_of_mass-position_of_pivot)*mass_of_beam*9.81
    #taking 9.81 as the value of gravitational field strength
    #measuring clockwise as positive and anti-clockwise as negative
    moment_of_force = (position_of_force-position_of_pivot)*magnitude_of_force
    if is_positive == "yes":
        total_moment = moment_of_weight-moment_of_force
        error = False
    elif is_positive == "no":
        total_moment = moment_of_weight+moment_of_force
        error = False
    else:
        print("Error. Please try again.")

if total_moment>0:
    print("There is a total moment of",total_moment,"N clockwise.")
elif total_moment<0:
    print("There is a total moment of",total_moment*-1,"N anti-clockwise.")
else:
    print("The beam is in equilibrium.")

