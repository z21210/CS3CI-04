import argparse
from math import log

parser = argparse.ArgumentParser(description='Finds a solution to an instance of the antenna array design problen via a particle swarm optimisation algorithm.')
parser.add_argument('--antennae', '-a', type=int, dest='antennae', help='The number of antennae on the antenna array', metavar='ANTENNAE', required=True)
parser.add_argument('--time', '-t', type=int, dest='time', help='The number of seconds to run the swarm for', metavar='TIME', required=True)
parser.add_argument('--particles', '-p', type=int, dest='particles', help='The number of particles in the swarm', metavar='PARTICLES')
parser.add_argument('--inertia', '-i', type=float, dest='inertia', help='The inertia coefficient of the particles', metavar='INERTIA', default=1/(2*log(2)))
parser.add_argument('--cognitive-attraction', '-c', type=float, dest='cognitiveAttraction', help='The cognitive attracion coefficient of the particles', metavar='COG_ATTR', default=log(2)+0.5)
parser.add_argument('--social-attraction', '-s', type=float, dest='socialAttraction', help='The social attracion coefficient of the particles', metavar='SOC_ATTR', default=log(2)+0.5)

def parse(argv):
    args = parser.parse_args(argv[1:])
    if args.particles == None:
        args.particles = args.antennae + 20
    return args