#!/usr/bin/env python

from __future__ import print_function

import os
import sys
import glob

import yaml

from jinja2 import Environment, FileSystemLoader
try:
    from ansible.utils.module_docs import get_docstring
except Exception:
    from ansible.utils.plugin_docs import get_docstring


def main():
    path = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else path

    if os.path.isdir(path):
        modules = glob.glob(os.path.join(path, '*.py'))
        dests = map(lambda x: os.path.join(out, x.split(os.path.sep)[-1].replace('.py', '.md')), modules)
    elif not os.path.exists(path):
        raise Exception('{} not found. You must specify the path to a module'.format(path))
    else:
        modules = [path]
        dests = [out]
    processed = list(map(process_doc, modules))
    map(lambda x: template_module(*x), zip(processed, dests))


def process_doc(module):
    doc, examples, returndocs, metadata = get_docstring(module)
    if not doc:
        print("No docstring retrieved for {}".format(module), file=sys.stderr)
        return
    if examples and filter(lambda x: x, examples):
        examples = filter(lambda x: x, examples)
        examples_list = examples.split('\n')
        doc['examples'] = examples_list
    if returndocs:
        doc['returndocs'] = returndocs
    print('Retrieved docstring for {}'.format(doc['module']))
    return doc


def template_module(module, dest):
    if module is None:
        print("No docstring retrieved for {}".format(module), file=sys.stderr)
        print("Docs for {} could not be generated".format(module), file=sys.stderr)
        return
    env = Environment(
        loader=FileSystemLoader('templates')
    )

    template = env.get_template('module_template.md.j2')
    with open(dest, 'w') as f:
        f.write(template.render(**module))
    print('Generated docs for {}'.format(module['module']))


if __name__ == '__main__':
    main()
