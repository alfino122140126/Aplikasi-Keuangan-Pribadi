from setuptools import setup, find_packages

setup(
    name='keuangan_api',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pyramid',
        'sqlalchemy',
        'psycopg2-binary',
    ],
    entry_points={
        'console_scripts': [
            'initialize_keuangan_pribadi_db = keuangan_api.scripts.initializedb:main',
        ],
    },
)