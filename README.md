# cse185-demo-project (mypileup)

This is a demonstration project for CSE185. It implements the "pileup" method available through samtools.

# Install instructions

Installation requires the `pyfaidx` and `pysam` libraries to be installed. You can install these with `pip`:

```
pip install pyfaidx pysam
```

Once required libraries are installed, you can install `mypileup` with the following command:

```
python setup.py install
```

Note: if you do not have root access, you can run the commands above with additional options to install locally:
```
pip install --user pyfaidx pysam
python setup.py install --user
```

If the install was successful, typing `mypileup --help` should show a useful message.