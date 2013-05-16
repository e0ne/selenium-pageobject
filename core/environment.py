import inject
from inject.scopes import Application

# TODO (e0ne): move scope type to setting of injector
test_scope = Application()


class Environment(object):
    """
    Abstract class for defining the environment.
    Inherit it and define you dependency injection configuration
    in configure method.
    """

    def __init__(self):
        self.injector = inject.Injector()

        self.before_suite_hooks = []
        self.after_suite_hooks = []

        self.before_test_hooks = []
        self.after_test_hooks = []

        self.configure()

    def before_suite(self):

        inject.register(self.injector)

        for hook in self.before_suite_hooks:
            hook()

    def after_suite(self):
        for hook in self.after_suite_hooks:
            hook()
        self.unregister_test_scope()
        inject.unregister(self.injector)

    def before_test(self):
        for hook in self.before_test_hooks:
            hook()

    def register_test_scope(self):
        #test_scope.register()
        pass

    def after_test(self):
        for hook in self.after_test_hooks:
            hook()
        #self.unregister_test_scope()

    def unregister_test_scope(self):
        #test_scope.unregister()
        pass

    def before_suite_hook(self, hook):
        self.before_suite_hooks.append(hook)

    def after_suite_hook(self, hook):
        self.after_suite_hooks.append(hook)

    def before_test_hook(self, hook):
        self.before_suite_hooks.append(hook)

    def after_test_hook(self, hook):
        self.after_test_hooks.append(hook)

    def configure(self):
        pass
