from setuptools import setup, find_packages
setup(
    name='rigeocoder',
    version='0.9',
    license="BSD",
    py_modules = ['rigeocoder'],
    
    install_requires = ["geopy>=0.94.2"],

    description = 'Rhode Island Geocoding with URI + google fallback',

    author='Provplan',
    author_email='amedrano@provplan.org',
    url='https://github.com/ProvidencePlan/rigeocoder',
    download_url='https://github.com/ProvidencePlan/rigeocoder.git',
    include_package_data = True,

    zip_safe=False,
    classifiers=[
	    'Development Status::4- Beta',
	    'Environment :: Web Environment',
	    'Intended Audience :: ',
	    'License :: BSD License',
	    'Operating System :: OS independent',
	    'Programming Language :: Python',
    ]
)
