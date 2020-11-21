def reward_function(params):

    # Parameters related to the agent
    all_wheels_on_track = params['all_wheels_on_track']    # flag to indicate if the agent is on the track
    x_coord = params['x']                                  # agent's x-coordinate in meters
    y_coord = params['y']                                  # agent's y-coordinate in meters
    distance_from_center = params['distance_from_center']  # distance in meters from the track center 
    is_crashed = params['is_crashed']                      # Boolean flag to indicate whether the agent has crashed.
    is_left = params ['is_left_of_center']                 # Flag to indicate if the agent is on the left side to the track center or not. 
    is_offtrack = params ['is_offtrack']                   # Boolean flag to indicate whether the agent has gone off track.
    is_reveresed = params['is_reversed']                   # flag to indicate if the agent is driving clockwise (True) or counter clockwise (False).
    heading= params['heading']                             # agent's yaw in degrees
    progress =params['progress']                           # percentage of track completed
    speed = params['speed']                                # agent's speed in meters per second (m/s)
    steering_angle = params['steering_angle']              # agent's steering angle in degrees
    steps = params['steps']                                # number steps completed
    
    # Parameters related to the track
    track_length = params['track_length']        # track length in meters.
    track_width = params['track_width']          # width of the track

    # Parameters related to object avoidance
    closest_objects = params['closest_objects']               # zero-based indices of the two closest objects to the agent's current position of (x, y).
    objects_distance = params ['objects_distance']            # list of the objects' distances in meters between 0 and track_length in relation to the starting line.
    objects_heading = params['objects_heading']               # list of the objects' headings in degrees between -180 and 180.
    objects_left_of_center = params['objects_left_of_center'] # list of Boolean flags indicating whether elements' objects are left of the center (True) or not (False).
    objects_location = params['objects_location']             # list of object locations [(x,y), ...].
    objects_speed = params['objects_speed']                   # list of the objects' speeds in meters per second.

    # Parameters related to waypoints
    waypoints = params['waypoints']                      # list of (x,y) as milestones along the track center
    closest_waypoints = params['closest_waypoints']      # indices of the two nearest waypoints.

    # Values for race conditions
    failure = 1e-3

    

    # Calculate 3 markers that are increasingly further away from the center line
    marker_1 = 0.1 * track_width    # One tenth width of track
    marker_2 = 0.25 * track_width   # Quater width of track
    marker_3 = 0.5 * track_width    # Half width of track

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        return float(failure)  # likely crashed/ close to off track

    return float(reward)
