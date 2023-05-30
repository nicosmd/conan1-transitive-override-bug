from conan import ConanFile

class BasicConanfile(ConanFile):
    name = "libd"
    version = "0.1"
    description = "A basic recipe"

    def requirements(self):
        self.requires("liba/1.0", override=True)
        self.requires("libc/0.1")

    def generate(self):
        pass

    def build(self):
        pass

    def package(self):
        pass
