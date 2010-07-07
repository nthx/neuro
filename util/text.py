# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)

                
def model_repr(object, attrs=[], separator=u', '):
    base = u'%s: ' % object.__class__.__name__
    str_attrs = []
    for attr in attrs:
        method = False
        if '()' in attr:
            attr = attr.replace('()', '')
            method = True
        if hasattr(object, attr):
            value = method and getattr(object, attr)() or getattr(object, attr)
            str_attrs.append(u'%s: %s' % (attr, value))
    return base + separator.join(str_attrs)


