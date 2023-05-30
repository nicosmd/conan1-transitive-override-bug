# Introduction

This Repo demonstrates a bug found in conan1 version >=1.47 (tested with 1.47 and 1.60).
The bug is caused by diamond dependency variation, where the root downstream package
overrides an upstream dependency, which is requried transitive by other packages as well but in a
lower version.

The follwing diagram illustrates the dependency graph:

![image](http://www.plantuml.com/plantuml/png/SoWkIImgAStDuOhEoKnAYLNGrRLJ036JOnMi50pq3D754q7YXde62XhvPQb5HPafgROXHQMfcbmGJGXrKFteuad8uabOr3kavgK0tGC0)

# Reproduction

In order to reproduce the bug, you need to run the `build.sh` script in the root of this repository.

In the end you should recieve the following error message:

```
WARN: libc/0.1: requirement liba/0.1 overridden by libd/0.1 to liba/1.0
ERROR: libb/0.1: requirement liba/0.1 overridden by libc/0.1 to liba/1.0
```
# Remarks

The error does not occure, when liba is not set explicitley as an requirement of libc but
retrieved implicit through libb. It also does not occure when `override=True` is added
to the requires statement of liba in libc. This bug seems to be no solved in conan2.
