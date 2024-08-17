#!/usr/bin/env python

"""Tests for `brixy` package."""

from brixy import log_step

@log_step()
def step2():
    return 1+3

@log_step()
def step3():
    raise ValueError('This is not right')

def test_logstep():

    @log_step()
    def step1():
        return 1+1

    
    result = step1()
    assert result == 2
    result = step2()
    assert result == 4

    try:
        step3()
        assert False, "Exception not thrown"
    except ValueError:
        assert True

def test_logstep_indenting():
    @log_step()
    def step1():
        return step2()+step2()
    
    result = step1()

    assert result == 8

    @log_step()
    def step_a():
        return step1()+step1()

    result_2 = step_a()
    assert result_2 == 16