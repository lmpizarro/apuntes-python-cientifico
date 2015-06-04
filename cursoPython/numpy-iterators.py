{
 "metadata": {
  "name": "",
  "signature": "sha256:22f4585d210d9e05b173a8ed7296aaa9127c15702e655b8664511fc7d8d9c972"
 },
 "nbformat": 3,
 "nbformat_minor": 0,
 "worksheets": [
  {
   "cells": [
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "# Introducci\u00f3n a numpy [link](http://www.python-course.eu/numpy.php)\n",
      "\n",
      "### Comparaci\u00f3n de tiempos entre python standard y python numpy\n",
      "\n"
     ]
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "import numpy\n",
      "import time\n",
      "\n",
      "def trad_version():\n",
      "    t1 = time.time()\n",
      "    X = range(10000000)\n",
      "    Y = range(10000000)\n",
      "    Z = []\n",
      "    for i in range(len(X)):\n",
      "        Z.append(X[i] + Y[i])\n",
      "    return time.time() - t1\n",
      "\n",
      "def numpy_version():\n",
      "    t1 = time.time()\n",
      "    X = numpy.arange(10000000)\n",
      "    Y = numpy.arange(10000000)\n",
      "    Z = X + Y\n",
      "    return time.time() - t1"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [],
     "prompt_number": 3
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "trad_version()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 4,
       "text": [
        "19.6796452999115"
       ]
      }
     ],
     "prompt_number": 4
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "numpy_version()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 5,
       "text": [
        "0.3110647201538086"
       ]
      }
     ],
     "prompt_number": 5
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "19.679/0.311"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "metadata": {},
       "output_type": "pyout",
       "prompt_number": 7,
       "text": [
        "63.276527331189705"
       ]
      }
     ],
     "prompt_number": 7
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "# Creaci\u00f3n de arrays en Numpy\n",
      "\n",
      "Si hacemos una busqueda con \"python numpy\" como par\u00e1metro, el resultado muestra que la creaci\u00f3n de array est\u00e1 dentro de los primeros resultados."
     ]
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a = [2,3,1,0]\n",
      "print (a)\n",
      "x = numpy.array([2,3,1,0])\n",
      "print (x)  # notar la diferencia en la salida del print\n",
      "x = numpy.array([[1,2.0],[0,0],(1+1j,3.)]) # notar el mix de tuplas, listas y tipos\n",
      "print(\"%s %d %s\"%(x, x.ndim, x.shape))  # ndim: dimensi\u00f3n del array, shape: col x filas\n",
      "\n",
      "# creada con enteros\n",
      "x = numpy.array([42,47,11], int)\n",
      "print (\"int \", x)\n",
      "\n",
      "# creada con enteros\n",
      "x = numpy.array([42,47,11], float)\n",
      "print (\"float \", x)\n",
      "\n",
      "# Una matriz llena con ceros\n",
      "x = numpy.zeros((2, 3)) \n",
      "print(x)\n",
      "# 6 valores equiespaciados entre 1 y 4: linspace\n",
      "x = numpy.linspace(1., 4., 6)\n",
      "print(x)\n",
      "\n",
      "#  3 D\n",
      "x=numpy.empty((2,3,5))\n",
      "x=numpy.arange(30).reshape(2,3,5)\n",
      "x = numpy.array([[[ 0,  1,  2],\n",
      "        [ 3,  4,  5],\n",
      "        [ 6,  7,  8]],\n",
      "       [[ 9, 10, 11],\n",
      "        [12, 13, 14],\n",
      "        [15, 16, 17]]])\n",
      "\n",
      "print (x)\n",
      "print ()\n",
      "print ()\n",
      "\n",
      "# vamos a ver que de esta manera \n",
      "# no es la mejor forma de iterar\n",
      "# el array\n",
      "for e in x:\n",
      "    print (\"n1\")\n",
      "    print (e)\n",
      "    for e2 in e:\n",
      "        print (\"n2\")\n",
      "        print (e2)\n",
      "        for e3 in e2:\n",
      "            print(\"n3\")\n",
      "            print (e3)\n",
      "# sumar una constante a todos los elementos del array\n",
      "y = x + 2\n",
      "print (y)\n",
      "\n",
      "# lo mismo con la multiplicaci\u00f3n por una constante\n",
      "y = y * 2\n",
      "\n",
      "#\n",
      "# No hay que iterar sobre todos los elementos\n",
      "#"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "[2, 3, 1, 0]\n",
        "[2 3 1 0]\n",
        "[[ 1.+0.j  2.+0.j]\n",
        " [ 0.+0.j  0.+0.j]\n",
        " [ 1.+1.j  3.+0.j]] 2 (3, 2)\n",
        "int  [42 47 11]\n",
        "float  [ 42.  47.  11.]\n",
        "[[ 0.  0.  0.]\n",
        " [ 0.  0.  0.]]\n",
        "[ 1.   1.6  2.2  2.8  3.4  4. ]\n",
        "[[[ 0  1  2]\n",
        "  [ 3  4  5]\n",
        "  [ 6  7  8]]\n",
        "\n",
        " [[ 9 10 11]\n",
        "  [12 13 14]\n",
        "  [15 16 17]]]\n",
        "\n",
        "\n",
        "n1\n",
        "[[0 1 2]\n",
        " [3 4 5]\n",
        " [6 7 8]]\n",
        "n2\n",
        "[0 1 2]\n",
        "n3\n",
        "0\n",
        "n3\n",
        "1\n",
        "n3\n",
        "2\n",
        "n2\n",
        "[3 4 5]\n",
        "n3\n",
        "3\n",
        "n3\n",
        "4\n",
        "n3\n",
        "5\n",
        "n2\n",
        "[6 7 8]\n",
        "n3\n",
        "6\n",
        "n3\n",
        "7\n",
        "n3\n",
        "8\n",
        "n1\n",
        "[[ 9 10 11]\n",
        " [12 13 14]\n",
        " [15 16 17]]\n",
        "n2\n",
        "[ 9 10 11]\n",
        "n3\n",
        "9\n",
        "n3\n",
        "10\n",
        "n3\n",
        "11\n",
        "n2\n",
        "[12 13 14]\n",
        "n3\n",
        "12\n",
        "n3\n",
        "13\n",
        "n3\n",
        "14\n",
        "n2\n",
        "[15 16 17]\n",
        "n3\n",
        "15\n",
        "n3\n",
        "16\n",
        "n3\n",
        "17\n",
        "[[[ 2  3  4]\n",
        "  [ 5  6  7]\n",
        "  [ 8  9 10]]\n",
        "\n",
        " [[11 12 13]\n",
        "  [14 15 16]\n",
        "  [17 18 19]]]"
       ]
      },
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "\n"
       ]
      }
     ],
     "prompt_number": 44
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "# Rutinas de creaci\u00f3n de arrays [link](http://docs.scipy.org/doc/numpy/reference/routines.array-creation.html#routines-array-creation)\n",
      "\n",
      "## Unos y ceros\n",
      "\n",
      "## Desde datos existentes\n",
      "\n",
      "## Rangos num\u00e9ricos\n",
      "\n",
      "## Construcci\u00f3n de matr\u00edces\n",
      "\n",
      "## La clase matrix\n",
      "\n",
      "## Otras\n",
      "\n",
      "### Son raras"
     ]
    },
    {
     "cell_type": "markdown",
     "metadata": {},
     "source": [
      "## nditer \n",
      "\n",
      "Efficient multi-dimensional iterator object to iterate over arrays"
     ]
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a = numpy.arange(6).reshape(2,3)\n",
      "print (a)\n",
      "for x in numpy.nditer(a.copy(order='F')):\n",
      "    print(x)\n",
      "    \n",
      "print (\"------------------\")\n",
      "for x in numpy.nditer(a):\n",
      "    print(x)\n",
      " \n",
      "# una manera de acceder a cada uno de los elementos\n",
      "# del array\n",
      "for x in numpy.nditer(a, op_flags=['readwrite']):\n",
      "   x[...] = 2 * x\n",
      "\n",
      "print (a)\n",
      "\n",
      "it = numpy.nditer(a, flags=['f_index'])\n",
      "\n",
      "while not it.finished:\n",
      "    print (\"%d <%d>\" % (it[0], it.index))\n",
      "    it.iternext()"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "[[0 1 2]\n",
        " [3 4 5]]\n",
        "0\n",
        "3\n",
        "1\n",
        "4\n",
        "2\n",
        "5\n",
        "------------------\n",
        "0\n",
        "1\n",
        "2\n",
        "3\n",
        "4\n",
        "5\n",
        "[[ 0  2  4]\n",
        " [ 6  8 10]]\n",
        "0 <0>\n",
        "2 <2>\n",
        "4 <4>\n",
        "6 <1>\n",
        "8 <3>\n",
        "10 <5>\n"
       ]
      }
     ],
     "prompt_number": 65
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [],
     "language": "python",
     "metadata": {},
     "outputs": []
    }
   ],
   "metadata": {}
  }
 ]
}
