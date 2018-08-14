import random
from time import sleep

import logging
log = logging.getLogger('')
log.addHandler(logging.NullHandler())

from pymeasure.experiment import Procedure, IntegerParameter, Parameter, FloatParameter, Measurable

class TestProcedure(Procedure):
    
    iterations = IntegerParameter('Loop Iterations', default=100)
    delay = FloatParameter('Delay Time', units='s', default=0.2)
    seed = Parameter('Random Seed', default='12345')
    iteration = Measurable('Iteration', default = 0)
    random_number = Measurable('Random Number', random.random)
    offset = Measurable('Random Number + 1', default = 0)

    def startup(self):
        log.info("Setting up random number generator")
        random.seed(self.seed)
        
    def measure(self):
        data = self.get_datapoint()
        data['Random Number + 1'] = data['Random Number'] + 1
        log.debug("Produced numbers: %s" % data)
        self.emit('results', data)
        self.emit('progress', 100.*self.iteration.value/self.iterations)

    def execute(self):
        log.info("Starting to generate numbers")
        for self.iteration.value in range(self.iterations):
            self.measure()
            sleep(self.delay)
            if self.should_stop():
                log.warning("Catch stop command in procedure")
                break

    def shutdown(self):
        log.info("Finished")