import matplotlib.pyplot as plt #allows us to use matplotlib which prints out the image later
#Helps read the file Input from the CSV
with open("Planet_size_and_locations.csv", 'r') as data_file: 
    Data = data_file.readlines() #Now, we are able to read each line

#These are the constants that are used for each different calculation
G = 6.67408e-11 #Gravitational constant
Time_step = 10000
Number_of_steps = 6000 
MassSun = 2e+30

#Allows us to create a class assigning each variable that is on the csv
class Planet: #
    def __init__ (self, Planet, Mass, Diameter, Xlocation, Ylocation, Xvelocity, Yvelocity): #The use of __init__ in this case aids in initalizing the object's state to the data members
        self.name = Planet
        self.mass = float(Mass)
        self.diameter = float(Diameter)
        self.xlocation = float(Xlocation) #Use of float as there is a great use of decimals 
        self.ylocation = float(Ylocation) 
        self.xvelocity = float(Xvelocity)
        self.yvelocity = float(Yvelocity)
        self.x_values = []
        self.y_values = []      #Creating 3 empty lists, which will store the x, y and z values which are then plotted on the 3D graph
        self.z_values = []   

    def xacceleration(self, Xloc, Yloc): #Helps with calculating the acceleration for X
        Calc1 = G * MassSun
        Calc2 = (Xloc**2) + (Yloc**2)
        Calc3 = Calc2**(3/2)
        Calc4 = Calc1/Calc3
        xacceleration = Calc4 * (0-Xloc)
        return xacceleration #by returning the value, it gives the value back to the caller for when needed

    def yacceleration(self, Xloc, Yloc): #Helps calculate the acceleration for Y
        Calc1 = G * MassSun
        Calc2 = (Xloc**2) + (Yloc**2)
        Calc3 = Calc2**(3/2)
        Calc4 = Calc1/Calc3
        yacceleration = Calc4 * (0-Yloc)
        return yacceleration

    def velocity(self, xacceleration, yacceleration, xvelocity, yvelocity):#This function allows us to calculate the new velocity, which is then used in the location calculation
        self.xvelocity = xvelocity + (xacceleration * Time_step)
        self.yvelocity = yvelocity + (yacceleration * Time_step)
        return self.xvelocity, self.yvelocity

    def location(self, Xlocation, Ylocation, xvelocity_new, yvelocity_new): #This function is the calculation for the respective locations
        self.xlocation = Xlocation + (xvelocity_new * Time_step)
        self.ylocation = Ylocation + (yvelocity_new * Time_step)
        return Xlocation, Ylocation

planets = [] #a list that is created to store the values for each individual planets
#for loop that helps me order the planets and their corresponding data
for line in Data[1:]:
    planet,Mass,Diameter,Xlocation,Ylocation,Xvelocity,Yvelocity = line.strip().split(',') #The use of '.strip()', helps in removing all of the leading and trailing spaces from a string, cleaning up the data that is presented
    planet_data = Planet(planet, Mass, Diameter, Xlocation, Ylocation, Xvelocity, Yvelocity)
    planets.append(planet_data) #The planet data has been appended onto one empty list, where this data will be distributed later 

#This for loop collects the data from the previous for loop and allow us to append the x and y values for each planet
for i in range(6000):
    for a in range(1,5):
        mercuryxacceleration = planets[a].xacceleration(planets[a].xlocation, planets[a].ylocation)
        mercury_Y_acceleration = planets[a].yacceleration(planets[a].xlocation, planets[a].ylocation)
        planets[a].velocity(mercuryxacceleration , mercury_Y_acceleration , planets[a].xvelocity, planets[a].yvelocity)
        planets[a].x_values.append(planets[a].xlocation) #appending the x-value
        planets[a].y_values.append(planets[a].ylocation) #appending the y-value 
        planets[a].z_values.append(0)
        planets[a].location(planets[a].xlocation, planets[a].ylocation, planets[a].xvelocity, planets[a].yvelocity)

#This helps plot the axis for the 3d graph
plt.style.use('dark_background') #generates a dark background
fig = plt.figure() #this is used to create the figure object
fig.canvas.set_window_title('3D Planet Orbit Projection') #helps plot the title of the window.
ax = fig.add_subplot(1,1,1, projection='3d') #Helps plot the 3D axis that 

#Helps me make a full black background
ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 0.0)) 
ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 0.0))
ax.grid(True) #inputs the grid within the 3d axis 
ax.set_zlim(-0.5,0.5)

#Helps plot each respective planet, with the inital location and the new location which is plotted as a circle
plt.plot(0,0,0, "o", color = 'yellow', label = 'sun') #This is a plot for the sun which goes in is exactly in the middle.

plt.plot(0,5.7E+10, "o", color = 'orange' )#Plot for the initial location of Mercury
plt.plot(planets[1].x_values, planets[1].y_values, planets[1].z_values, label = 'Mercury', color='orange') #Plot for the Orbit of Mercury where a circle is generated

plt.plot(0,1.1E+11, "o", color = 'green')#Plot for the initial location of Venus
plt.plot(planets[2].x_values, planets[2].y_values, planets[2].z_values, label = 'Venus', color='green') #Plot for Venus' orbit

plt.plot(0,1.5E+11, "o", color = 'blue')#Plot for the initial location of earth
plt.plot(planets[3].x_values, planets[3].y_values, planets[3].z_values, label = 'Earth', color='blue') #Plot for Earth's Orbit

plt.plot(0,2.2E+11, "o", color = 'red')#Plot for the inital location of Mars
plt.plot(planets[4].x_values, planets[4].y_values, planets[4].z_values, label = 'Mars', color='red') #Plot for Mars' Orbit

plt.title('Planet 3D Orbits, to scale') #This helps us name the title and the labels
plt.xlabel('X location') #Helps label the X axis, which is the location of the planets along the x-axis
plt.ylabel('Y location') #Helps label the Y-axis, which is the location of the planets along the y-axis

plt.legend()#This helps create a legend where there is a key generated as a result, used as there are more than one planet
plt.show()#Helps show the axis.
