#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# created_on: 2020-01-03 17:26

"""Renderer."""

from jinja2 import Template


__author__ = 'Toran Sahu <toran.sahu@yahoo.com>'
__license__ = 'Distributed under terms of the MIT license'


def do():
    template = None
    with open('index.html', 'r') as fd:
        template = Template(fd.read())
    
    context_vars = {"name": "Nidhi", "items": ["apple", "orange", "kiwi"]}
    print(template.render(context_vars))


if __name__ == "__main__":
    do()
