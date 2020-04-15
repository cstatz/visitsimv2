// Copyright (c) Lawrence Livermore National Security, LLC and other VisIt
// Project developers.  See the top-level LICENSE file for dates and other
// details.  No copyright assignment is required to contribute to VisIt.

#define SIMV2_USE_NUMPY
#if defined(SIMV2_USE_NUMPY)
# define NPY_NO_DEPRECATED_API NPY_1_7_API_VERSION
# define PY_ARRAY_UNIQUE_SYMBOL  PyArray_API_simV2
# include <numpy/arrayobject.h>
#endif
