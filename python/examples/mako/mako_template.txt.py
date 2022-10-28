# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1666981179.8300376
_enable_loop = True
_template_filename = 'mako_template.txt'
_template_uri = 'mako_template.txt'
_source_encoding = 'utf-8'
_exports = ['hello']


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def hello():
            return render_hello(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('This is a template.\r\nMore stuff at https://www.makotemplates.org/\r\n\r\nDocs at https://docs.makotemplates.org/en/latest/\r\n\r\n')
        __M_writer('\r\nCall a func: ')
        __M_writer(str(hello()))
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_hello(context):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        __M_writer('\r\n    hello world\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "mako_template.txt", "uri": "mako_template.txt", "source_encoding": "utf-8", "line_map": {"16": 0, "23": 1, "24": 8, "25": 9, "31": 6, "35": 6, "41": 35}}
__M_END_METADATA
"""
