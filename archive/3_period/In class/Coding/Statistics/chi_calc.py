from random import choice, shuffle
NUMBER_OF_FACES = 6
NUMBER_OF_TOTAL_MOVES = 60
EXPECTED_PROBABILITY = 1 / NUMBER_OF_FACES
EXPECTED_FREQUENCY = NUMBER_OF_TOTAL_MOVES / NUMBER_OF_FACES


faces = {face: 0 for face in range(1, NUMBER_OF_FACES + 1)}
def move():
    faces_list = [face for face in faces]
    counter = 0
    while counter < NUMBER_OF_TOTAL_MOVES:
        faces[choice(faces_list)] += 1
        counter += 1
    total_chi = 0
    for face in faces:
        chi = ((faces[face] - EXPECTED_FREQUENCY) ** 2) / EXPECTED_FREQUENCY
        total_chi += chi
        # print("Chi value for {} is {} with {} moves".format(face, chi, faces[face]))

    # print("Total Chi is {}".format(total_chi))
    return total_chi