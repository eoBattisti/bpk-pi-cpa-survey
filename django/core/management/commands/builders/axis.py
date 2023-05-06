from axis.factories import AxleFactory

def create(command):
    command.print('Creating axis...')

    axis = list()

    for _ in range(command.size):
        axle = AxleFactory()
        axis.append(axle)

    command.cache['axis'] = axis
