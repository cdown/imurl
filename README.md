imurl is a tool to download all of the images in an [imgur][] album into the
current directory.

```
$ ls
$ imurl http://imgur.com/a/Rbab9
$ ls -1
0-sqyIOdW.jpg
1-mszJPA4.jpg
2-KKMieoH.jpg
3-1Lf7PFN.jpg
4-5f4BTkl.jpg
5-oiqRUVm.jpg
```

[imgur]: https://imgur.com

## Installing dependencies

    $ pip install -r requirements.txt

[pip]: https://pypi.python.org/pypi/pip

## Testing

[![Build status][travis-image]][travis-builds]

    $ pip install -r tests/requirements.txt
    $ nosetests

[travis-builds]: https://travis-ci.org/cdown/imurl
[travis-image]: https://travis-ci.org/cdown/imurl.png?branch=master

## License

imurl is [ISC licensed][isc]. See the LICENSE file for full details.

[isc]: http://en.wikipedia.org/wiki/ISC_license
