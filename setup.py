import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-licensing',
    version='0.2.4',
    packages=['licensing'],
    include_package_data=True,
    license='Public Domain',
    description='A Django model and data for adding licensing info to data.',
    long_description=README,
    url='http://github.com/editorsnotes/django-licensing',
    download_url='http://github.com/editorsnotes/django-licensing/tarball/0.2.4',
    author='Ryan Shaw',
    author_email='ryanshaw@unc.edu',
    keywords = ['django', 'licenses', 'licences'],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: Public Domain',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
