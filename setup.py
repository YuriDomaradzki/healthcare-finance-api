from setuptools import setup, find_packages

VERSION = '0.1.0' 
DESCRIPTION = 'Implementation of a private REST API for the financial sector of a healthcare company'
LONG_DESCRIPTION = "This package contains the implementation of a private REST API for the financial "\
                   "sector of a healthcare company. The API provides secure access to information "\
                   "on purchases made by the company's patients/customers, covering data on patients," \
                   " pharmacies and transactions."

with open('requirements.txt', 'r') as reqs:
    requires = [req.replace('\n', '') for req in reqs.readlines()]

packages = find_packages()

setup(
        name="healthcare_finance_api", 
        version=VERSION,
        author="Yuri Domaradzki",
        author_email="yuridomaradzki@gmail.com",
        url="https://github.com/YuriDomaradzki/healthcare-finance-api.git",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        license='MIT',
        keywords='healthcare finance REST API',
        packages=packages,
        include_package_data=True,
        install_requires=requires,
        classifiers= [
            "Development Status :: 1 - Planning",
            'Programming Language :: Python :: 3 :: Only',
            "Operating System :: OS Independent",
            "Topic :: Software Development :: Libraries :: Python Modules"
        ]
)