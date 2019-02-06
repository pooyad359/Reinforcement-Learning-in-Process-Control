
EPISODES = 2000
MEAN_EPISODE=10
MAX_TIME = 100
SAVE_ANN_MODEL=False
LOAD_ANN_MODEL = False
TRAIN_MODEL=True

# Model parameters Tank 1
TANK_PARAMS = {
    'height':10,
    'width':3,
    'pipe_radius':0.5,
    'max_level':0.9,
    'min_level':0.1
}

TANK_DIST = {
    'add':True,
    'nom_flow':0.5,
    'var_flow':0.0,
    'max_flow':1,
    'min_flow':0,
}
# Model parameters Tank 1

INIT_LEVEL=0.5 # initial water level for each episode

# Choke parameters
TBCC = 1 # Time before choke change

# Agent parameters
MEMORY_LENGTH=3000
SS_POSITION = 0.5 # steady state set position
VALVE_START_POSITION=0
OBSERVATIONS = 2 # Number of time steos observed
VALVE_POSITIONS= 30 # Number of valve positions 
GAMMA = 0.98    # discount rate
EPSILON = 1.0  # exploration rate

EPSILON_MIN = 0.0001
EPSILON_DECAY = 0.95
LEARNING_RATE = 0.001
NUMBER_OF_HIDDEN_LAYERS = [10]
BATCH_SIZE=30


# Render parameters
RENDER=True
LIVE_REWARD_PLOT= False
