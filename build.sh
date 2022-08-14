# py_exclude='*.pyc *.ipynb \*__pycache__\* *ipynb_checkpoints* *.git* *cache/* */testing/* Pipfile Pipfile.lock build.zip'

# cd .. && (cd selenium_linux && zip -r ../build.zip . -x -x $py_exclude)  && mv build.zip selenium_linux/build.zip


pip3 uninstall my-main-package && (cd main-package && python3 setup.py install) && (cp -r myenv/lib/python3.8/site-packages/. lambda_functions/packages/python)