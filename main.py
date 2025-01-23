# importing libraries for graph
import matplotlib.pyplot as plt
import numpy as np


# func that calculates density of material sensor interacts with 
def density(mass, volume):
  return mass/ volume 
  
#func to see if oil detected  
def if_oil(density):
  is_oil= False
  # density of oil ranges between 750-900
  # density of water is 1000 (kg/m3)
  # taking a sample from the ocean using the sensor calculate the density

  if  density>= 750 and density <= 900:
    is_oil = True
    
  return is_oil

# function for outmost point on x axis
def edges (x_cord):
  low = None
  high= None
  for each in x_cord:
    if high==None or each> high:
      high = each

    if low== None or each< low:
      low= each

  return low, high


#main file
if __name__ == "__main__":
  
  '''
  num_molecules = int(input("Number of Molecules to Analyze:\n> "))
  x_cord= [] 
  y_cord= [] 


  # getting all x and y cordinates 
  for i in range(1, num_molecules+1):

    #calculating density 
    print(f"\nMolecule {i}.")
    density1 = density(float(input("> Mass: ")), float(input("> Volume: ")))

    #checking if not oil molecule 
    if if_oil(density1):     
      
      #if it is an oil moelcules
      print("Position:")
      x, y= float(input("> X cordinate = ")), float(input("> Y cordinate = "))
  
      # adding the cordinates 
      x_cord.append(x)
      y_cord.append(y)
      
  '''
  
  # eg. of graph the sensor can create 
  plt.figure(figsize=(10,6))
  x_cord = np.random.normal(0,10,1000)
  y_cord = np.random.normal(0,10,1000)

  
  # getting outermost edge points of graph of molecules
  # when we plot all the point from the complete data set, given by the sensor -> we should be able o identify the edges of the scatter plot to see where the skimmers would be thrown to collect the oil molecules
  x_low, x_high = edges(x_cord)
  y_low, y_high = edges(y_cord)
  print(f"The edge points for skimmer to be thrown:\n- North= {round(y_high, 3)} m\n- East= {round(x_high, 3)} m\n- South= {round(y_low, 3)} m\n- West= {round(x_low, 3)} m")


  # drawing the graph
  plt.scatter(x_cord, y_cord)
  plt.xlabel('$ Longitude$ $(x) $' , fontsize = 12)
  plt.ylabel('$ Latitude$ $(y) $' , fontsize = 12)
  plt.title ('Oil Molecules Detection ')
  plt.show()

  
  











  
  