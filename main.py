from Swarm import Swarm
from AntennaArray import AntennaArray
from args import parse
import sys, time

args = parse(sys.argv)

a = AntennaArray(args.antennae, 90)
swarm = Swarm(args.particles, a.generateRandomSolution, a.evaluate, args.inertia, args.cognitiveAttraction, args.socialAttraction)

start = time.time()
end = start + args.time
while time.time() < end:
    swarm.step()
    print(f'Time left: {int(end - time.time())}s        ', end='\r')
print(f'{swarm.gBest}\nPeak SLL: {swarm.gBestEvaluation}')