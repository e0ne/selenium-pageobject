from nose.plugins import Plugin


class EnvironmentRunnerPlugin(Plugin):
    def __init__(self, environment):
        super(EnvironmentRunnerPlugin, self).__init__()
        self.environment = environment

    def options(self, parser, env):
        self.enabled = True

    def configure(self, options, conf):
        pass

    def begin(self):
        self.environment.before_suite()

    def finalize(self, result):
        self.environment.after_suite()

    def beforeTest(self, test):
        self.environment.before_test()

    def afterTest(self, test):
        self.environment.after_test()
