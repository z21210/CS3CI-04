import numpy as np
from random import uniform

class Particle:
    def __init__(this, initialiser, evaluator, inertia, cognitiveAttraction, socialAttraction):
        this.position = np.array(initialiser())
        this.velocity = np.zeros(this.position.ndim)
        this.inertia = inertia
        this.cognitiveAttraction = cognitiveAttraction
        this.socialAttraction = socialAttraction
        this.evaluator = evaluator
        this.pBest = this.position
        this.pBestEvaluation = this.evaluate()

    def evaluate(this):
        return this.evaluator(this.position)

    def stepPosition(this):
        this.position = this.position + this.velocity
    
    def stepVelocity(this, gBest):
        this.velocity \
            = this.inertia * this.velocity \
            + this.cognitiveAttraction * np.random.rand(this.position.ndim) * (this.pBest - this.position) \
            + this.socialAttraction    * np.random.rand(this.position.ndim) * (gBest      - this.position)

    def stepPBest(this):
        evaluation = this.evaluate()
        if evaluation < this.pBestEvaluation:
            this.pBest = this.position
            this.pBestEvaluation = evaluation
        
    def stepGBest(this, gBest, gBestEvaluation):
        evaluation = this.evaluate()
        if evaluation < gBestEvaluation:
            return this.position, evaluation
        else:
            return gBest, gBestEvaluation
        
    def step(this, gBest, gBestEvaluation):
        this.stepVelocity(gBest)
        this.stepPosition()
        this.stepPBest()
        this.stepGBest(gBest, gBestEvaluation)