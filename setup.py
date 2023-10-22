from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0.0',
    author='Danil Kazakov',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder=clean_folder.clean:start']}
)
#PS C:\Users\ka3ak\OneDrive\Рабочий стол\clean_folder> $env:PATH +=";C:\Users\ka3ak\AppData\Local\Packages\PythonSoftwareFoundation.Python.3.11_qbz5n2kfra8p0\LocalCache\local-packages\Python311\Scripts"
#PS C:\Users\ka3ak\OneDrive\Рабочий стол\clean_folder> clean-folder .\garbage\