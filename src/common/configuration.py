# Switches
# Print delivery info to the terminal
PRINT_TERMINAL = True
# Plot the simulation
PLOT_SIMULATION = True
# Use DensityMatrix to track matrix: tracking noise in matrix
USE_DENSITY_MATRIX = True
# Use local order data: True - load predefined orders; False - generate new orders
USE_LOCAL_ORDER = True
# TODO: load and use population density for harm calculation and path-finding
USE_POPULATION_DENSITY = True

# Prioritize low average noise cells
# Use the first or second cost function: 'first' - K; 'second' - P
COST_FUNCTION = 'second'
PRIORITIZE_K = 5
PRIORITIZE_P = 0

# Coordinates of Tesco warehouses in London
# LONDON_WAREHOUSES = [
#     [51.5394, -0.2251],  # Tilling Road, Cricklewood
#     [51.5254, -0.0194],  # Hancock Road, Mile End
#     [51.6503, -0.1738],  # Station Road, Wealdstone
#     [51.4912, -0.0791],  # Dunton Road, Southwark
#     [51.6132, -0.1318],  # Coppetts Centre, North Finchley
# ]

# Tesco warehouses in London outskirts - distribution centres
# LONDON_WAREHOUSES = [
#     [51.4912, -0.2476],  # Tesco Distribution Centre, Greenford
#     [51.5141, 0.2012],  # Tesco Distribution Centre, Dagenham
# ]
   # [51.6734, -0.0481],  # Tesco Fulfillment Centre, Enfield
    #[51.2887, -0.1747],  # Tesco Distribution Centre, Croydon
LONDON_WAREHOUSES = [
    [51.4303, -0.1276],  # Streatham
    [51.4613, -0.3037],  # Richmond
    [51.5380, -0.1022],  # Islington
    [51.4875, -0.0595]    # Bermondsey
]


#20 Tesco warehouses in London - evenely distribtued
# LONDON_WAREHOUSES = [
#     [51.5136, 0.0681],  # Tesco Extra Beckton (East)
#     [51.5275, -0.0154],  # Tesco Extra Bromley-by-Bow (East)
#     [51.5083, 0.0441],  # Tesco Express Barking (East)
#     [51.5471, 0.0552],  # Tesco Express East Ham (East)
#     [51.5141, 0.0318],  # Tesco Extra Gallions Reach (East)
#     [51.5013, -0.3714],  # Tesco Extra Southall Bulls Bridge (West)
#     [51.5535, -0.2857],  # Tesco Extra Wembley (West)
#     [51.4909, -0.2534],  # Tesco Express Ealing Broadway (West)
#     [51.5104, -0.2925],  # Tesco Express Hounslow (West)
#     [51.4948, -0.2235],  # Tesco Express Shepherd's Bush (West)
#     [51.6136, -0.0426],  # Tesco Extra Edmonton (North)
#     [51.6151, -0.0455],  # Tesco Extra Enfield (North)
#     [51.6481, -0.1784],  # Tesco Extra Harrow Wealdstone (North)
#     [51.5908, -0.1042],  # Tesco Express Finchley Central (North)
#     [51.6501, -0.1948],  # Tesco Express Mill Hill (North)
#     [51.4042, -0.2286],  # Tesco Extra Raynes Park (South)
#     [51.3385, -0.1119],  # Tesco Extra Purley (South)
#     [51.4511, -0.0194],  # Tesco Express Greenwich (South)
#     [51.4615, -0.1643],  # Tesco Express Tooting (South)
#     [51.4738, -0.1229],  # Tesco Express Clapham Road (South)
# ]



# LONDON_WAREHOUSES = [
#     [51.500773, 0.160277],
#     [51.389926, 0.110440],
#     [51.361253, -0.119953],
#     [51.375578, -0.124525],
#     [51.372757, -0.121484],
#     [51.556886, -0.264871],
#     [51.556944, -0.262778],
#     [51.653594, -0.024036],
#     [51.524925, 0.111827],
#     [51.520417, -0.006570],
#     [51.504271, -0.447186],
#     [51.520837, -0.006301],
#     [51.521963, -0.080489],
#     [51.502286, -0.073931]
# ]



# Total number of orders (5000 predefined orders)
ORDERS = 1000
# Total number of drones
DRONES = 200
# Noise matrix cell size (in meter)
NOISE_CELL_LENGTH = 2000
NOISE_CELL_WIDTH = 2000
# Harm threshold (in dB)
HARM_AVG_LEVEL = 45
HARM_MAX_LEVEL = 85

# Center iteration running step (doesn't work if the program is running very slowly)
# e.g. CENTER_PER_SLICE_TIME = 1s, the program will run each iteration for 0.5 second (if possible)
# when it's the iteration to writing data to local, the program will slow down a little bit,
# but it will run faster in the next a few iterations to compensate for the slow-down
CENTER_PER_SLICE_TIME = 0.5

# Paths
# Base path for saving/loading orders to/from the local
ORDER_BASE_PATH = 'recourses/data/order/orders_v2.csv'
NEW_ORDER_BASE_PATH = 'recourses/data/order/drone_delivery_orders_volod.csv'
# Base path for saving/loading matrix tracking data
NOISE_BASE_PATH = 'recourses/results/matrix/trajectory'
# Base path for saving heatmap/density map
HEATMAP_BASE_PATH = 'recourses/results/matrix/heatmaps'
# Base path for saving overlay images of folium map and density matrix
OVERLAY_BASE_PATH = 'recourses/results/matrix/heatmaps/overlay'
# Geographical data
GEO_PATH = 'recourses/data/geo/london_lsoa_simple.geojson'
# Old population density data
OLD_POPULATION_DENSITY_PATH = 'recourses/data/population/newing_propensity_shop_online.csv'
# New population density data
NEW_POPULATION_DENSITY_PATH = 'recourses/data/population/London_msoa_2021_with_population_density.geojson'
# Simulation plotter background image
BACKGROUND_IMAGE_PATH = 'recourses/images/map.jpeg'
# Base path for saving matrix density matrix
MATRIX_BASE_PATH = 'recourses/results/matrix/matrix'
# Base path for saving matrix histogram
HISTOGRAM_BASE_PATH = 'recourses/results/matrix/histogram'
# Base path for experiment results
RESULT_BASE_PATH = 'recourses/results/experiments'



# Map
CRS = 'epsg:3857'
# Map boundary
MAP_LEFT   = -0.3489999
MAP_RIGHT  = 0.166
MAP_TOP    = 51.624
MAP_BOTTOM = 51.415

# offset range 0-200m (latitude) to a random generated coordinate
# Notice this is calculated at around 37 latitude
RANDOM_LA_COORD_OFFSET = 0.001802
# Notice this is calculated at around 37 latitude
# offset range 0-200m (longitude) to a random generated coordinate
RANDOM_LO_COORD_OFFSET = 0.002278

# geo popup layer style and highlight functions
style_function = lambda x: {'fillColor': '#ffffff',
                            'color': '#000000',
                            'fillOpacity': 0.1,
                            'weight': 0.1}
highlight_function = lambda x: {'fillColor': '#000000',
                                'color': '#000000',
                                'fillOpacity': 0.50,
                                'weight': 0.1}
