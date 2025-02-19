def reward_function(params):
    '''
    Example of penalize steering, which helps mitigate zig-zag behaviors
    '''
    def dist_2_points(x1, x2, y1, y2):
            return abs(abs(x1-x2)**2 + abs(y1-y2)**2)**0.5
    
    def closest_2_racing_points_index(racing_coords, car_coords):

            # Calculate all distances to racing points
            distances = []
            for i in range(len(racing_coords)):
                distance = dist_2_points(x1=racing_coords[i][0], x2=car_coords[0],
                                         y1=racing_coords[i][1], y2=car_coords[1])
                distances.append(distance)

            # Get index of the closest racing point
            closest_index = distances.index(min(distances))

            # Get index of the second closest racing point
            distances_no_closest = distances.copy()
            distances_no_closest[closest_index] = 999
            second_closest_index = distances_no_closest.index(
                min(distances_no_closest))

            return [closest_index, second_closest_index]
    
    def dist_to_racing_line(closest_coords, second_closest_coords, car_coords):
            
            # Calculate the distances between 2 closest racing points
            a = abs(dist_2_points(x1=closest_coords[0],
                                  x2=second_closest_coords[0],
                                  y1=closest_coords[1],
                                  y2=second_closest_coords[1]))

            # Distances between car and closest and second closest racing point
            b = abs(dist_2_points(x1=car_coords[0],
                                  x2=closest_coords[0],
                                  y1=car_coords[1],
                                  y2=closest_coords[1]))
            c = abs(dist_2_points(x1=car_coords[0],
                                  x2=second_closest_coords[0],
                                  y1=car_coords[1],
                                  y2=second_closest_coords[1]))

            # Calculate distance between car and racing line (goes through 2 closest racing points)
            # try-except in case a=0 (rare bug in DeepRacer)
            try:
                distance = abs(-(a**4) + 2*(a**2)*(b**2) + 2*(a**2)*(c**2) -
                               (b**4) + 2*(b**2)*(c**2) - (c**4))**0.5 / (2*a)
            except:
                distance = b

            return distance

    racing_line = [
                    [ 5.04608283e+00, 8.61460574e-01],
                    [ 5.03925822e+00, 1.16054809e+00],
                    [ 5.02821898e+00, 1.45790395e+00],
                    [ 5.01187937e+00, 1.75301202e+00],
                    [ 4.98907970e+00, 2.04528526e+00],
                    [ 4.95854952e+00, 2.33403774e+00],
                    [ 4.91880418e+00, 2.61841765e+00],
                    [ 4.86796774e+00, 2.89728438e+00],
                    [ 4.80398170e+00, 3.16925571e+00],
                    [ 4.72428100e+00, 3.43246118e+00],
                    [ 4.62575474e+00, 3.68437236e+00],
                    [ 4.50486544e+00, 3.92163167e+00],
                    [ 4.35631742e+00, 4.13844924e+00],
                    [ 4.17535546e+00, 4.32670210e+00],
                    [ 3.97021669e+00, 4.48961366e+00],
                    [ 3.74615139e+00, 4.62997975e+00],
                    [ 3.50733254e+00, 4.75082543e+00],
                    [ 3.25645607e+00, 4.85415157e+00],
                    [ 2.99573227e+00, 4.94170163e+00],
                    [ 2.72709102e+00, 5.01496661e+00],
                    [ 2.45218298e+00, 5.07482209e+00],
                    [ 2.17295879e+00, 5.12278464e+00],
                    [ 1.89099898e+00, 5.15979221e+00],
                    [ 1.60770194e+00, 5.18667666e+00],
                    [ 1.32424369e+00, 5.20409708e+00],
                    [ 1.04159084e+00, 5.21253034e+00],
                    [ 7.60524221e-01, 5.21234040e+00],
                    [ 4.81646432e-01, 5.20386454e+00],
                    [ 2.05383295e-01, 5.18747126e+00],
                    [-6.80005262e-02, 5.16356263e+00],
                    [-3.38322393e-01, 5.13244758e+00],
                    [-6.05585775e-01, 5.09465365e+00],
                    [-8.69624493e-01, 5.05021360e+00],
                    [-1.13016806e+00, 4.99890519e+00],
                    [-1.38693214e+00, 4.94045201e+00],
                    [-1.63928778e+00, 4.87393326e+00],
                    [-1.88651654e+00, 4.79830193e+00],
                    [-2.12738960e+00, 4.71168586e+00],
                    [-2.36049947e+00, 4.61209580e+00],
                    [-2.58436929e+00, 4.49783557e+00],
                    [-2.79725547e+00, 4.36759603e+00],
                    [-2.99827469e+00, 4.22204790e+00],
                    [-3.18604495e+00, 4.06150028e+00],
                    [-3.35720395e+00, 3.88473997e+00],
                    [-3.50534931e+00, 3.68963942e+00],
                    [-3.62245655e+00, 3.47609117e+00],
                    [-3.69603630e+00, 3.24672587e+00],
                    [-3.72342938e+00, 3.01094993e+00],
                    [-3.71703097e+00, 2.77574425e+00],
                    [-3.67419065e+00, 2.54505304e+00],
                    [-3.58820525e+00, 2.32515148e+00],
                    [-3.44911278e+00, 2.12871509e+00],
                    [-3.27356074e+00, 1.95610158e+00],
                    [-3.06869141e+00, 1.80746415e+00],
                    [-2.84042122e+00, 1.68154142e+00],
                    [-2.59432940e+00, 1.57541571e+00],
                    [-2.33426607e+00, 1.48659777e+00],
                    [-2.06393170e+00, 1.41169557e+00],
                    [-1.78644592e+00, 1.34717479e+00],
                    [-1.50486406e+00, 1.28889129e+00],
                    [-1.22385703e+00, 1.23392443e+00],
                    [-9.46500803e-01, 1.17412319e+00],
                    [-6.75021980e-01, 1.10659090e+00],
                    [-4.11523411e-01, 1.02876660e+00],
                    [-1.58229595e-01, 9.38285828e-01],
                    [ 8.20227841e-02, 8.32611744e-01],
                    [ 3.06013065e-01, 7.09559067e-01],
                    [ 5.08558649e-01, 5.66095619e-01],
                    [ 6.83849996e-01, 4.00445517e-01],
                    [ 8.23499955e-01, 2.11838045e-01],
                    [ 9.30908999e-01, 7.58095266e-03],
                    [ 1.00146778e+00, -2.09700319e-01],
                    [ 1.02584130e+00, -4.36158234e-01],
                    [ 9.88552959e-01, -6.60721079e-01],
                    [ 9.03330444e-01, -8.72392047e-01],
                    [ 7.79650289e-01, -1.06715285e+00],
                    [ 6.24954322e-01, -1.24399964e+00],
                    [ 4.40059419e-01, -1.39925398e+00],
                    [ 2.30347767e-01, -1.53315706e+00],
                    [-2.07611962e-04, -1.64624973e+00],
                    [-2.48305151e-01, -1.73933276e+00],
                    [-5.10512895e-01, -1.81419813e+00],
                    [-7.83979001e-01, -1.87271219e+00],
                    [-1.06627444e+00, -1.91682389e+00],
                    [-1.35523154e+00, -1.94875767e+00],
                    [-1.64922009e+00, -1.97040831e+00],
                    [-1.94715148e+00, -1.98297602e+00],
                    [-2.24060536e+00, -2.00570388e+00],
                    [-2.52833948e+00, -2.03983908e+00],
                    [-2.80896004e+00, -2.08691184e+00],
                    [-3.08084944e+00, -2.14850420e+00],
                    [-3.34208459e+00, -2.22625273e+00],
                    [-3.59074970e+00, -2.32131374e+00],
                    [-3.82318690e+00, -2.43637940e+00],
                    [-4.03498317e+00, -2.57360574e+00],
                    [-4.22057159e+00, -2.73447141e+00],
                    [-4.37103089e+00, -2.91999469e+00],
                    [-4.48781561e+00, -3.12290690e+00],
                    [-4.56900903e+00, -3.33881469e+00],
                    [-4.61280257e+00, -3.56299030e+00],
                    [-4.61538396e+00, -3.79007236e+00],
                    [-4.57905863e+00, -4.01409121e+00],
                    [-4.50628819e+00, -4.23034354e+00],
                    [-4.39636406e+00, -4.43359942e+00],
                    [-4.24630323e+00, -4.61603197e+00],
                    [-4.06179111e+00, -4.77392776e+00],
                    [-3.85048551e+00, -4.90799764e+00],
                    [-3.61717757e+00, -5.01896801e+00],
                    [-3.36590805e+00, -5.10816519e+00],
                    [-3.10011559e+00, -5.17725063e+00],
                    [-2.82303560e+00, -5.22858212e+00],
                    [-2.53763938e+00, -5.26517654e+00],
                    [-2.24621966e+00, -5.28984722e+00],
                    [-1.95040390e+00, -5.30484304e+00],
                    [-1.65167790e+00, -5.31273222e+00],
                    [-1.35116184e+00, -5.31581299e+00],
                    [-1.04970199e+00, -5.31613708e+00],
                    [-7.47950315e-01, -5.31556010e+00],
                    [-4.46316441e-01, -5.31467944e+00],
                    [-1.44971978e-01, -5.31304874e+00],
                    [ 1.55831599e-01, -5.31003940e+00],
                    [ 4.55820113e-01, -5.30499614e+00],
                    [ 7.54675156e-01, -5.29719222e+00],
                    [ 1.05205513e+00, -5.28589026e+00],
                    [ 1.34757828e+00, -5.27030958e+00],
                    [ 1.64080402e+00, -5.24959661e+00],
                    [ 1.93119310e+00, -5.22275606e+00],
                    [ 2.21811409e+00, -5.18869445e+00],
                    [ 2.50079659e+00, -5.14615962e+00],
                    [ 2.77844774e+00, -5.09399292e+00],
                    [ 3.04964122e+00, -5.03004650e+00],
                    [ 3.31244904e+00, -4.95167335e+00],
                    [ 3.56463355e+00, -4.85626341e+00],
                    [ 3.80323508e+00, -4.74080510e+00],
                    [ 4.02408303e+00, -4.60163796e+00],
                    [ 4.22075577e+00, -4.43406588e+00],
                    [ 4.38582089e+00, -4.23515325e+00],
                    [ 4.52583883e+00, -4.01499147e+00],
                    [ 4.64355372e+00, -3.77780912e+00],
                    [ 4.74130326e+00, -3.52670637e+00],
                    [ 4.82124391e+00, -3.26416234e+00],
                    [ 4.88541147e+00, -2.99223116e+00],
                    [ 4.93577262e+00, -2.71266584e+00],
                    [ 4.97421404e+00, -2.42697075e+00],
                    [ 5.00255600e+00, -2.13644630e+00],
                    [ 5.02252506e+00, -1.84220241e+00],
                    [ 5.03593389e+00, -1.54525019e+00],
                    [ 5.04434769e+00, -1.24637543e+00],
                    [ 5.04896814e+00, -9.46137295e-01],
                    [ 5.05101736e+00, -6.45034856e-01],
                    [ 5.05159712e+00, -3.43466744e-01],
                    [ 5.05157495e+00, -4.17148415e-02],
                    [ 5.05122514e+00, 2.59913350e-01],
                    [ 5.04971949e+00, 5.61101137e-01],
                    [ 5.04608283e+00, 8.61460574e-01]
                ]

    # Get closest indexes for racing line (and distances to all points on racing line)
    closest_index, second_closest_index = closest_2_racing_points_index(racing_line, [params["x"], params["y"]])

    # Get optimal [x, y] for closest and second closest index
    optimals = racing_line[closest_index]
    optimals_second = racing_line[second_closest_index]

    distance_to_racing_line = dist_to_racing_line(optimals[0:2], optimals_second[0:2], [params["x"], params["y"]])

    # Read input parameters
    # distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    abs_steering = abs(params['steering_angle']) # Only need the absolute steering angle
    # Calculate 3 marks that are farther and father away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width
    # Give higher reward if the car is closer to center line and vice versa
    if distance_to_racing_line <= marker_1:
        reward = 1.0
    elif distance_to_racing_line <= marker_2:
        reward = 0.5
    elif distance_to_racing_line <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3, # likely crashed/ close to off track
    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 15 
    # Penalize reward if the car is steering too much
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8
    return float(reward)