#!/bin/bash
echo "start dist"
rm ./dist/*
python setup.py clean --all
python setup.py sdist build
#python setup.py bdist_wheel --universal
echo "start upload"
#python setup.py sdist upload
#python setup.py bdist_wheel upload
twine upload dist/*