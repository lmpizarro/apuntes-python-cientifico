{
 "metadata": {
  "name": "",
  "signature": "sha256:a3225b475d61e1ac1ef012485442bcecc2539165dda55847a8c95c4a6ddf076b"
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
     "prompt_number": 1
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "time_trad = trad_version()\n",
      "print(time_trad)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "21.37397336959839\n"
       ]
      }
     ],
     "prompt_number": 5
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "time_np = numpy_version()\n",
      "print(time_np)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "0.32607078552246094\n"
       ]
      }
     ],
     "prompt_number": 6
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "print(time_trad/time_np)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "65.55010236611975\n"
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
      "# Broadcasting\n",
      "\n",
      "### Las reglas del broadcasting \n",
      "* Array Broadcasting in numpy [link](http://wiki.scipy.org/EricsBroadcastingDoc)\n",
      "* Broadcasting [link](http://docs.scipy.org/doc/numpy/user/basics.broadcasting.html)\n",
      "\n",
      "En una operaci\u00f3n entre 2 arreglos, Numpy intenta que el arreglo de menor dimensi\u00f3n adquiera las dimensiones del mayor y realizar la operaci\u00f3n."
     ]
    },
    {
     "cell_type": "code",
     "collapsed": false,
     "input": [
      "a = numpy.array([1.0, 2.0, 3.0])\n",
      "b = numpy.array([2.0, 2.0, 2.0])\n",
      "print(a*b)\n",
      "b = 2.0\n",
      "print(a*b, b)\n",
      "\n",
      "b = numpy.array([2])\n",
      "print(a*b, b)\n",
      "\n",
      "#  3 D\n",
      "x=numpy.empty((2,3,5))\n",
      "x=numpy.arange(30).reshape(2,3,5)\n",
      "print(x)\n",
      "\n",
      "print()\n",
      "y = numpy.array([2,1,3,1,2])\n",
      "print (\"y*x broadcasted\")\n",
      "print()\n",
      "print (y*x)\n",
      "\n",
      "# repeat\n",
      "print(\"repeat --->\")\n",
      "print(y.repeat(2))\n",
      "z= numpy.tile(y,(3, 1))\n",
      "print(\"tile .....\", z.shape, x.shape)\n",
      "print(z*x)\n",
      "\n",
      "\n",
      "\n",
      "# genera error\n",
      "z= numpy.tile(y,(2, 1))\n",
      "print(z*x)\n",
      "\n",
      "# tambi\u00e9n genera error\n",
      "w = numpy.array([2,1])\n",
      "v = numpy.tile(w,(3,1))\n",
      "print (v*x)"
     ],
     "language": "python",
     "metadata": {},
     "outputs": [
      {
       "output_type": "stream",
       "stream": "stdout",
       "text": [
        "[ 2.  4.  6.]\n",
        "[ 2.  4.  6.] 2.0\n",
        "[ 2.  4.  6.] [2]\n",
        "[[[ 0  1  2  3  4]\n",
        "  [ 5  6  7  8  9]\n",
        "  [10 11 12 13 14]]\n",
        "\n",
        " [[15 16 17 18 19]\n",
        "  [20 21 22 23 24]\n",
        "  [25 26 27 28 29]]]\n",
        "\n",
        "y*x broadcasted\n",
        "\n",
        "[[[ 0  1  6  3  8]\n",
        "  [10  6 21  8 18]\n",
        "  [20 11 36 13 28]]\n",
        "\n",
        " [[30 16 51 18 38]\n",
        "  [40 21 66 23 48]\n",
        "  [50 26 81 28 58]]]\n",
        "repeat --->\n",
        "[2 2 1 1 3 3 1 1 2 2]\n",
        "tile ..... (3, 5) (2, 3, 5)\n",
        "[[[ 0  1  6  3  8]\n",
        "  [10  6 21  8 18]\n",
        "  [20 11 36 13 28]]\n",
        "\n",
        " [[30 16 51 18 38]\n",
        "  [40 21 66 23 48]\n",
        "  [50 26 81 28 58]]]\n"
       ]
      },
      {
       "ename": "ValueError",
       "evalue": "operands could not be broadcast together with shapes (3,2) (2,3,5) ",
       "output_type": "pyerr",
       "traceback": [
        "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m\n\u001b[1;31mValueError\u001b[0m                                Traceback (most recent call last)",
        "\u001b[1;32m<ipython-input-49-0fd205e73d97>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m()\u001b[0m\n\u001b[0;32m     30\u001b[0m \u001b[0mv\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mnumpy\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtile\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mw\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m3\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;36m1\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     31\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 32\u001b[1;33m \u001b[0mprint\u001b[0m \u001b[1;33m(\u001b[0m\u001b[0mv\u001b[0m\u001b[1;33m*\u001b[0m\u001b[0mx\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     33\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     34\u001b[0m \u001b[1;31m# genera error\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
        "\u001b[1;31mValueError\u001b[0m: operands could not be broadcast together with shapes (3,2) (2,3,5) "
       ]
      }
     ],
     "prompt_number": 49
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
