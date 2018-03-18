#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `holdmykeys` package."""

import pytest

# from holdmykeys import holdmykeys
# from holdmykeys import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_truth(response):
    assert 1 + 1 == 2
