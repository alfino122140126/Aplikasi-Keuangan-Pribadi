from setuptools import setup

requires = [
    "pyramid",
    "sqlalchemy",
    "psycopg2-binary",
    "waitress",
    "PyJWT",
]

setup(
    name="keuangan_api",
    install_requires=requires,
    entry_points={
        "paste.app_factory": [
            "main = app:main",
        ],
    },
)
