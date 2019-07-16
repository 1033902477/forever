from Experiment.DataProcess.OperationData import OperationBaseData


class StartTest(OperationBaseData):

    def start_test(self):
        self.operation_data()

if __name__ == '__main__':
    StartTest().start_test()