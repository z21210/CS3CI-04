from Particle import Particle
from math import log

class Swarm:
    def __init__(this, swarmSize, initialiser, evaluator, \
            inertia=1/(2*log(2)), cognitiveAttraction=log(2)+0.5, socialAttraction=log(2)+0.5):
        particles = []
        for i in range(swarmSize):
            particles.append(Particle(initialiser, evaluator, inertia, cognitiveAttraction, socialAttraction))
        this.particles = particles
        this.gBest, this.gBestEvaluation = None, float('inf')
        this.stepGBest()

    def stepGBest(this):
        gBest, gBestEvaluation = this.gBest, this.gBestEvaluation
        for particle in this.particles:
            if particle.pBestEvaluation < gBestEvaluation:
                gBest, gBestEvaluation = particle.pBest, particle.pBestEvaluation
        this.gBest, this.gBestEvaluation = gBest, gBestEvaluation
    
    def stepParticles(this):
        for particle in this.particles:
            particle.step(this.gBest, this.gBestEvaluation)
    
    def step(this):
        this.stepParticles()
        this.stepGBest()