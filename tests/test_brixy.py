#!/usr/bin/env python

"""Tests for `brixy` package."""

from brixy import brixy

@brixy.log_step
def step2():
    return 1+3

@brixy.log_step
def step3():
    raise ValueError('This is not right')

def test_logstep():

    @brixy.log_step
    def step1():
        return 1+1

    
    result = step1()
    assert result == 2
    result = step2()
    assert result == 4

    try:
        step3()
        assert False, "Exception not thrown"
    except ValueError as e:
        assert True