from setuptools import setup, find_packages

setup(
    name='mc3_dashboard',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "dash",
        "dash-bootstrap-components",
        "pandas",
        "geopandas",
        "plotly",
        "shapely"
    ],
    entry_points={
        'console_scripts': [
            'run-mc3-dashboard=mc3_dash.app:main',
        ],
    },
)