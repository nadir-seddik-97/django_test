from setuptools import setup, find_packages

setup(
    name='receipt',
    version='1.0',
    python_requires='>=3.7',
    include_package_data=True,
    install_requires=[
        'Django',
        'django-crispy-forms',
        'mysqlclient',
        'crispy-bootstrap5',
        'psycopg2-binary',
    ],

    packages=find_packages(),
)
