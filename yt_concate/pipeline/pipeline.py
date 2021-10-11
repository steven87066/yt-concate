from yt_concate.pipeline.steps.steps import StepException

class PipeLine:
    def __init__(self,steps):
        self.steps = steps

    def run(self, inputs):
        for step in self.steps:
            try:
                step.process(inputs)
            except StepException as e:
                print('Exception Happened:', e)
                break

