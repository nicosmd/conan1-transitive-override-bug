from conan import ConanFile

class BasicConanfile(ConanFile):
    name = "libc"
    version = "0.1"
    description = "A basic recipe"

    def requirements(self):
        self.requires("liba/0.1")
        self.requires("libb/0.1")

    def generate(self):
        pass

    def build(self):
        pass

    def package(self):
        pass
