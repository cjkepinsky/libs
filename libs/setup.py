from setuptools import setup

setup(
    name='libs',
    version='0.1',
    description='data science related tools & helpers',
    url='https://github.com/cjkepinsky/libs',
    author='Chris J. Kepinsky',
    author_email='chris.kepinski@gmail.com',
    license='MIT',
    packages=['libs'],
    install_requires=[
        'babyplots',
        'matplotlib',
        'numpy',
        'pandas',
        're',
        'scipy',
        'seaborn',
        'sklearn',
        'statistics',
        'sys',
        'umap',
        'xgboost',
    ],
    zip_safe=False
)
