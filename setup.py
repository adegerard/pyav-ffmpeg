import setuptools
import sys

if sys.platform == "win32":
    include_dirs = ["C:\\cibw\\pyav\\include"]
    library_dirs = ["C:\\cibw\\pyav\\lib"]
else:
    include_dirs = ["/tmp/pyav/include"]
    library_dirs = ["/tmp/pyav/lib"]

setuptools.setup(
    name="dummy",
    package_dir={"": "src"},
    packages=["dummy"],
    ext_modules=[
        setuptools.Extension(
            "dummy.binding",
            include_dirs=include_dirs,
            library_dirs=library_dirs,
            libraries=[
                "avformat",
                "avcodec",
                "avdevice",
                "avutil",
                "avfilter",
                "swscale",
                "swresample",
            ],
            sources=["src/dummy/binding.c"],
        ),
    ],
)
