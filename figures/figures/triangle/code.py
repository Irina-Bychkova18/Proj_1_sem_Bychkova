from math import sqrt
__all__ = ['triangle_perimeter', 'triangle_area']


def triangle_perimeter(a=7, b=2, c=8):
    d = a + b + c
    print(d)


def triangle_area(a=7, b=2, c=8):
    k = sqrt((a+b+c)/2*(((a+b+c)/2-a)*((a+b+c)/2-b)*((a+b+c)/2-c)))
    print(k)