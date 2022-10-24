import math as maths
from random import uniform 

DISTANCE_MINIMUM = 0.25

class PowerPeak:
    def __init__(this, elevation, power):
        this.elevation = float(elevation)
        this.power = float(power)

class AntennaArray:
    def __init__(this, antennaeCount, steeringAngle):
        this.antennaeCount = antennaeCount
        this.steeringAngle = steeringAngle
    
    def isValid(this, positions):
        positions.sort()
        return this.isValidAntennaeCount(positions) and this.isValidApertureSize(positions[-1]) and this.isValidPositions(positions) and this.isValidSpacing(positions)
    
    def isValidAntennaeCount(this, positions):
        return len(positions) == this.antennaeCount

    def isValidApertureSize(this, apertureSize):
        return apertureSize == this.antennaeCount/2

    def isValidPositions(this, positions):
        for p in positions:
            if (p < 0) or (p > this.antennaeCount/2):
                return False
        return True
    def isValidSpacing(this, positions):
        for i in range(1, this.antennaeCount-1):
            if (positions[i] - positions[i-1] < DISTANCE_MINIMUM) or (positions[i+1] - positions[i] < DISTANCE_MINIMUM):
                return False
        return True

    def getBoundsForNextAntenna(this, positionsSoFar):
        antennaeToGo = this.antennaeCount - len(positionsSoFar)
        if antennaeToGo <= 0: # already placed all antennae
            lowerBound = None
            upperBound = None
        elif antennaeToGo == 1: # placing last antenna
            lowerBound = this.antennaeCount / 2
            upperBound = this.antennaeCount / 2
        elif antennaeToGo == this.antennaeCount: # placing first antenna
            lowerBound = DISTANCE_MINIMUM
            upperBound = this.antennaeCount / 2 - DISTANCE_MINIMUM * antennaeToGo
        else: # placing mediate antenna
            lowerBound = positionsSoFar[-1] + DISTANCE_MINIMUM
            upperBound = this.antennaeCount / 2 - DISTANCE_MINIMUM * antennaeToGo 
        return lowerBound, upperBound
    
    def getArrayFactor(this, positions, elevation):
        total = 0.0
        for position in positions:
            total += maths.cos(2 * maths.pi * position * (maths.cos(maths.radians(elevation)) - maths.cos(maths.radians(this.steeringAngle))))
        return 20 * maths.log(abs(total))

    def evaluate(this, positions):
        if not this.isValid(positions):
            return float('inf')
        
        peaks = []
        prevPeak = PowerPeak(0, '-inf')
        currentPeak = PowerPeak(0, this.getArrayFactor(positions, 0.0))
        for el in range(1, 18001):
            elevation = el / 100
            nextPeak = PowerPeak(elevation, this.getArrayFactor(positions, elevation))
            if (prevPeak.power < currentPeak.power) and (currentPeak.power > nextPeak.power):
                peaks.append(currentPeak)
            prevPeak = currentPeak
            currentPeak = nextPeak
        peaks.append(PowerPeak(180, this.getArrayFactor(positions, 180)))

        peaks.sort(key= lambda p: p.power, reverse=True)
        if len(peaks) == 1:
            return float('-inf')
        distanceFromSteering = abs(peaks[0].elevation - this.steeringAngle)
        for i in range(1, len(peaks)):
            if abs(peaks[i].elevation - this.steeringAngle) < distanceFromSteering:
                return peaks[0].power
        return peaks[1].power

    def generateRandomSolution(this):
        '''
        generateRandomSolution Generates an array of random antenna positions, within the constraints of the AntennaArray.
        :return: an array of floats representing a random valid antenna array 
        '''
        antennae = []
        while this.getBoundsForNextAntenna(antennae) != (None, None):
            antennae.append(
                uniform(
                    *this.getBoundsForNextAntenna(
                        antennae
                    )
                )
            )
        return antennae