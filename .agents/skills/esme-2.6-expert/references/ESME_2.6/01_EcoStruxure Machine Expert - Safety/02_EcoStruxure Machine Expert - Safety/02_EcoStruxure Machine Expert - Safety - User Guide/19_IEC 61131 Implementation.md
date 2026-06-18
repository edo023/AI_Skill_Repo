# IEC 61131 Implementation

The standard IEC 61131 has been established to standardize the multiple languages, sets of instructions, interfaces between controller and programming system, and different concepts existing in the field of automation systems. The great variety of controller concepts has led to an incompatibility between the different hardware platforms and manufacturers. The result was a great effort to be made for training, hard- and software investments.

The advantage of using IEC 61131 conform controllers and programming systems is a portability of all platforms and the use of same concepts reducing costs for automation systems.

## IEC 61131 features implemented in Machine Expert – Safety

Due to specific safety requirements, only a subset of features defined by the IEC 61131-3 standard is implemented in Machine Expert – Safety.

The following list details the available IEC features:

* Programming means symbolic programming.
* Variables have to be declared (similar to the variable declaration in higher programming languages).
* [Global and local](VariablesinSafeFox.html#VariablesinSafeFox) data are differentiated.
* [I/O variables](VariablesinSafeFox.html#VariablesinSafeFox) can be defined (always as global variables).
* The source code of a Safety Logic Controller program is structured using [Program Organization Units (POUs)](pousinSafeFOX.html#pousinSafeFOX). User defined function blocks can be created and [instantiated](instantiation.html#instantiation).
* The programming languages [Function Block Diagram (FBD) and Ladder Diagram (LD)](programminglanguagesiniec61131_3.html#programminglanguagesiniec61131_3) are available for developing graphical code.
* The programming language [Structured Text (ST)](programminglanguagesiniec61131_3.html#programminglanguagesiniec61131_3) is available for developing ST code.
* Usage of [Safety Logic Controller-specific firmware libraries](librariesinSafeFOX.html#librariesinSafeFOX).

EIO0000002147.09