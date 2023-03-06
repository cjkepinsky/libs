from setuptools import setup

setup(
    name='dslibs',
    version='0.0.6',
    description='data science related tools & helpers',
    url='https://github.com/cjkepinsky/libs',
    author='Chris J. Kepinsky',
    author_email='chris.kepinski@gmail.com',
    license='MIT',
    packages=['dslibs'],
    install_requires=[
        'babyplots',
        'matplotlib',
        'numpy',
        'pandas',
        'scipy',
        'seaborn',
        'sklearn',
        'statistics',
        'umap',
        'xgboost',
    ],
    zip_safe=False
)
