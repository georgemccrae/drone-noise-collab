# 1. Overview

- Order Generator is used to simulate the process of drone food delivery.

- Order Generator will automatically generate food delivery orders based on population density (PD) in fixed areas. Areas with high PD are more likely to generate food delivery orders, while areas with low PD are less likely to generate food delivery orders.

- According to OOP's principles, Order Generator will only generate orders. 

- TODO: These orders will be either accepted by drones or allocated by central processor.





# 2. Requirements

## a. Fixed Area

Orders will be generated in a fixed area. Coordinates will be represented by using longitude and latitude. Users will need to input four coordinates of the fixed area.


## b. Population Density

The program should be able to read population density data.


## c. Generate Orders

Orders can be generated before the program/simulation starts or generated gradually. 



## d. Orders & Population Density

Orders should be generated according to population density or randomly.





# 3. Data

## a. Map/Area

- Boundary
  - Top left (Coordinate)
  - Top right (Coordinate)
  - Bottom left (Coordinate)
  - Bottom right (Coordinate)
- `TODO`: Population density 



## c. Coordinate

- Longitude
- Latitude



## b. Order

- Time

- Location

- Start (Coordinate)

- End (Coordinate)