simpatico
=========

A C source code style checker..

## What is it?

This style marker should enforce the rules outlayed in
the 'csse2310-style-guide.pdf' which was created for the computer
science course 'CSSE2310' at the University of Queensland.

## Motivation

If/when this project becomes more reliable than the previous
implementations of the automarker then the tutors of this 
course will swap over to using 'simpatico' for their marking.

Also, many hours of marking time is quite expensive for such
a menial task, and this project could save money as well 
as time and effort.

## Current method

Currently a C++ program called 'vera++' tokenises the C
source code input and feeds it to a very large tcl script
which generates the errors. 

This script has many issues and is terribly hard to modify.
One of the major problems with the current script is that
it generates a large number of style errors for validly 
styled C code.

After the automarker is complete the course tutors must go
through the generated errors extremely carefully to validate
the process. Very frequently the tutors make mistakes.

## Error Format

Each style error must be declared in the format:
    filename:lineNumber: [CATEGORY] Description

The categories and potential error messages are listed below. More details are given in
`rules.md` and in `csse2310-style-guide.pdf`.

### NAMING

Potential error messages:
- File naming error: _filename_
- Variable naming error: _name_
- #define naming error: _name_
- Function naming error: _name_
- Type naming error: _name_

### BRACES

Potential error messages:
- (TODO)

Categories:
- space before brace
- correct placement
- correct alignment

### INDENTATION

Potential error messages:
- (TODO)

Categories:
- multiples of four spaces
- nesting correctly indented
- line continuation

### WHITESPACE

Potential error messages:
- No space around _operator_
- No space after ,
- No space after ;
- No vertical space between functions

(_operator_ will be one of `=`, `+=`, `&=`, etc.)

Further categories:
- Appropriate vertical whitespace

### COMMENTS

Potential error messages:
(none automatically generated)

Categories:
- globals
- functions (parameters esp.)
- lengthy or tricky code

### OVERALL

Potential error messages:
- Function _name_ is _n_ lines
- Use of goto

Further categories:
- modularity / no excessive duplication of code

### LINE-LENGTH

Potential error messages:
- Line is _n_ characters

## Usage

* Shell:

```bash
$ ./simpatico.py file1.c [file2.c ...]
```

* API:

```python
import simpatico
errors = simpatico.check('program.c')   # a list of violations
e = errors[0]
print e.format()
print [e.filename, e.line, e.category, e.description]
```

```
program.c:1: [OVERALL] goto
['program.c', 1, 'OVERALL', 'goto']
```

* Testing:

```bash
$ python tests
```
