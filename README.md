# jaxtyping-export-repro

Reproduction of issue described in https://github.com/google/jaxtyping/pull/49

Instructions:
```
cd package
pip install -e .
cd ../
pyright try_import.py
```

Error:
```
npx: installed 1 in 3.41s
No configuration file found.
No pyproject.toml file found.
stubPath /home/brent/exporttest/typings is not a valid directory.
Assuming Python platform Linux
Searching for source files
Found 1 source file
pyright 1.1.282
/home/brent/exporttest/try_import.py
  /home/brent/exporttest/try_import.py:2:24 - error: "Imported" is not exported from module "exporttest.src"
    Import from "typing_extensions" instead (reportPrivateImportUsage)
1 error, 0 warnings, 0 informations 
```
