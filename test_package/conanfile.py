from conans import ConanFile, tools
import os

class NicegrafShadercTestConan(ConanFile):
    settings = "os_build", "arch_build"

    def imports(self):
        self.copy("nicegraf_shaderc*", dst="bin", src="bin")

    def test(self):
        if not tools.cross_building(self.settings):
            os.chdir("bin")
            self.run("nicegraf_shaderc")
