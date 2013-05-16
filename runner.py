import inject
import nose

import selenium.webdriver

from core.environment import Environment, test_scope
from core.nose_plugin import EnvironmentRunnerPlugin

import inject.scopes


class FirefoxEnvironment(Environment):
    def configure(self):
        def get_webdriver():
            return selenium.webdriver.Firefox()

        @inject.param('webdriver', 'webdriver')
        def driver_quit(webdriver):
            webdriver.quit()

        self.injector.bind('webdriver', to=get_webdriver, scope=test_scope)
        #self.after_test_hook(driver_quit)
        self.after_suite_hook(driver_quit)


env = FirefoxEnvironment()

if __name__ == '__main__':
    nose.main(argv=['-c setup.cfg'], addplugins=[EnvironmentRunnerPlugin(env)])
