from setuptools import setup
try:
    import multiprocessing
except ImportError:
    pass


setup(
    name='httpie-apikeyquery',
    description='ApiKeyQuery plugin for HTTPie.',
    python_requires=">=2.7.10",
    long_description=open('README.rst').read().strip(),
    version='1.0.2',
    author='Dj Walker-Morgan',
    author_email='codepope@gmail.com',
    license='BSD',
    url='https://github.com/codepope/httpie-apikeyquery',
    download_url='https://github.com/codepope/httpie-apikeyquery',
    py_modules=['httpie_apikeyquery'],
    zip_safe=False,
    entry_points={
        'httpie.plugins.auth.v1': [
            'httpie_oauth1 = httpie_apikeyquery:ApiKeyQueryAuthPlugin'
        ]
    },
    install_requires=[
        'httpie >= 0.9.2',
    ],
)