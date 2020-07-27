# Filename Shortener
This Python script shortens file names in a given directory.

## Usage
```
python filename-shortener.py <directory>
```

## What is does
It expects the following files to be shortened;
```
Foo_Bar.Baz_10.09.19868475.pdf
```

It will
1. keep the prefix chunk to the first low dash (`Foo`)
2. sha1-hash everything ahead to the extension (`Bar.Baz_10.09.19868475`)
3. shorten the hash to the first 8 characters
4. process a `dd.MM.yyyy` date to `yyMMdd` and put that to the front
5. keep the extension

Result:
```
860910-Foo_73ad33ff.pdf
```

