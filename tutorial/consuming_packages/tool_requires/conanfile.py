from conan import ConanFile

class SimpleCmakeProject(ConanFile):
    name = 'simple_cmake_project'
    requires = ["zlib/1.3.1"]
    settings = ["build_type"]
    generators = ["CMakeDeps", "CMakeToolchain"]
    tool_requires = ["cmake/3.31.3"]
