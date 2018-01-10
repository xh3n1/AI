import random


class Environment(object):
    def __init__(self):
        # instantiate locations and conditions
        # 0 denotes Clean and 1 denotes Dirty
        self.locationCondition = {'A': '0', 'B': '0'}

        # randomize conditions in locations A and B
        self.locationCondition['A'] = random.randint(0, 1)
        self.locationCondition['B'] = random.randint(0, 1)


class SimpleReflexVacuumAgent(Environment):
    def __init__(self, Environment):
        print Environment.locationCondition
        # Instantiate performance measurement
        Score = 0
        # place vacuum at random location
        vacuumLocation = random.randint(0, 1)
        # if vacuum at A
        if vacuumLocation == 0:
            print "Vacuum randomly placed at A"
            # and A is Dirty
            if Environment.locationCondition['A'] == 1:
                print "A is Dirty"
                # suck and mark clean
                Environment.locationCondition['A'] = 0;
                Score += 1
                print "A has been Cleaned"

                # if B is Dirty
                if Environment.locationCondition['B'] == 1:
                    print "B is Dirty"
                    # move to B
                    print "Moving to B"
                    Score -= 1
                    # suck and mark clean
                    Environment.locationCondition['B'] = 0;
                    Score += 1
                    print "B has been Cleaned"
            else:

                # if B is Dirty
                if Environment.locationCondition['B'] == 1:
                    print "B is Dirty"
                    # move to B
                    Score -= 1
                    print "Moving to B"
                    # suck and mark clean
                    Environment.locationCondition['B'] = 0;
                    Score += 1
                    print "B has been Cleaned"

        elif vacuumLocation == 1:
            print "Vacuum randomly placed at B"
            # and B is Dirty
            if Environment.locationCondition['B'] == 1:
                print "B is Dirty"
                # suck and mark clean
                Environment.locationCondition['B'] = 0;
                Score += 1
                print "B has been Cleaned"

                # if A is Dirty
                if Environment.locationCondition['A'] == 1:
                    print "A is Dirty"
                    # move to A
                    Score -= 1
                    print "Moving to A"
                    # suck and mark clean
                    Environment.locationCondition['A'] = 0;
                    Score += 1
                    print "A has been Cleaned"
            else:

                # if A is Dirty
                if Environment.locationCondition['A'] == 1:
                    print "A is Dirty"
                    # move to A
                    print "Moving to A"
                    Score -= 1
                    # suck and mark clean
                    Environment.locationCondition['A'] = 0;
                    Score += 1
                    print "A has been Cleaned"
        # done cleaning
        print Environment.locationCondition
        print "Performance Measurement: " + str(Score)


theEnvironment = Environment()
theVacuum = SimpleReflexVacuumAgent(theEnvironment)