# -*- coding: utf-8 -*-
import logging
log = logging.getLogger(__name__)

                
def model_repr(object, attrs=[], separator=u', '):
    base = u'%s: ' % object.__class__.__name__
    str_attrs = []
    for attr in attrs:
        if hasattr(object, attr):
            str_attrs.append(u'%s: %s' % (attr, getattr(object, attr)))
    return base + separator.join(str_attrs)


