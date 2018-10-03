# -*- coding: utf-8 -*-
from collections import OrderedDict

import six
from pyangbind.lib.base import PybindBase
from pyangbind.lib.yangtypes import RestrictedClassType
from pyangbind.lib.yangtypes import YANGDynClass
from pyangbind.lib.yangtypes import YANGListType

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
    import builtins as __builtin__

    long = int
elif six.PY2:
    import __builtin__

from . import elements


class output(PybindBase):
    """
    This class was auto-generated by the PythonClass plugin for PYANG
    from YANG module node-topology - based on the path /node_topology_rpc/test/output. Each member element of
    the container is represented as a class variable - with a specific
    YANG type.
    """
    __slots__ = ('_path_helper', '_extmethods', '__response_id', '__elements',)

    _yang_name = 'output'

    _pybind_generated_by = 'container'

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__elements = YANGDynClass(
            base=YANGListType(False, elements.elements, yang_name="elements", parent=self, is_container='list',
                              user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None),
            is_container='list', yang_name="elements", parent=self, path_helper=self._path_helper,
            extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:node-topology',
            defining_module='node-topology', yang_type='list', is_config=True)
        self.__response_id = YANGDynClass(
            base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32),
            is_leaf=True, yang_name="response-id", parent=self, path_helper=self._path_helper,
            extmethods=self._extmethods, register_paths=False, namespace='urn:node-topology',
            defining_module='node-topology', yang_type='uint32', is_config=True)

        load = kwargs.pop("load", None)
        if args:
            if len(args) > 1:
                raise TypeError("cannot create a YANG container with >1 argument")
            all_attr = True
            for e in self._pyangbind_elements:
                if not hasattr(args[0], e):
                    all_attr = False
                    break
            if not all_attr:
                raise ValueError("Supplied object did not have the correct attributes")
            for e in self._pyangbind_elements:
                nobj = getattr(args[0], e)
                if nobj._changed() is False:
                    continue
                setmethod = getattr(self, "_set_%s" % e)
                if load is None:
                    setmethod(getattr(args[0], e))
                else:
                    setmethod(getattr(args[0], e), load=load)

    def _path(self):
        if hasattr(self, "_parent"):
            return self._parent._path() + [self._yang_name]
        else:
            return [u'node_topology_rpc', u'test', u'output']

    def _get_response_id(self):
        """
        Getter method for response_id, mapped from YANG variable /node_topology_rpc/test/output/response_id (uint32)
        """
        return self.__response_id

    def _set_response_id(self, v, load=False):
        """
        Setter method for response_id, mapped from YANG variable /node_topology_rpc/test/output/response_id (uint32)
        If this variable is read-only (config: false) in the
        source YANG file, then _set_response_id is considered as a private
        method. Backends looking to populate this variable should
        do so via calling thisObj._set_response_id() directly.
        """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(v, base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']},
                                                         int_size=32), is_leaf=True, yang_name="response-id",
                             parent=self, path_helper=self._path_helper, extmethods=self._extmethods,
                             register_paths=False, namespace='urn:node-topology', defining_module='node-topology',
                             yang_type='uint32', is_config=True)
        except (TypeError, ValueError):
            raise ValueError({
                'error-string': """response_id must be of a type compatible with uint32""",
                'defined-type': "uint32",
                'generated-type': """YANGDynClass(base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32), is_leaf=True, yang_name="response-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, namespace='urn:node-topology', defining_module='node-topology', yang_type='uint32', is_config=True)""",
            })

        self.__response_id = t
        if hasattr(self, '_set'):
            self._set()

    def _unset_response_id(self):
        self.__response_id = YANGDynClass(
            base=RestrictedClassType(base_type=long, restriction_dict={'range': ['0..4294967295']}, int_size=32),
            is_leaf=True, yang_name="response-id", parent=self, path_helper=self._path_helper,
            extmethods=self._extmethods, register_paths=False, namespace='urn:node-topology',
            defining_module='node-topology', yang_type='uint32', is_config=True)

    def _get_elements(self):
        """
        Getter method for elements, mapped from YANG variable /node_topology_rpc/test/output/elements (list)
        """
        return self.__elements

    def _set_elements(self, v, load=False):
        """
        Setter method for elements, mapped from YANG variable /node_topology_rpc/test/output/elements (list)
        If this variable is read-only (config: false) in the
        source YANG file, then _set_elements is considered as a private
        method. Backends looking to populate this variable should
        do so via calling thisObj._set_elements() directly.
        """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(v, base=YANGListType(False, elements.elements, yang_name="elements", parent=self,
                                                  is_container='list', user_ordered=False,
                                                  path_helper=self._path_helper, yang_keys='False', extensions=None),
                             is_container='list', yang_name="elements", parent=self, path_helper=self._path_helper,
                             extmethods=self._extmethods, register_paths=False, extensions=None,
                             namespace='urn:node-topology', defining_module='node-topology', yang_type='list',
                             is_config=True)
        except (TypeError, ValueError):
            raise ValueError({
                'error-string': """elements must be of a type compatible with list""",
                'defined-type': "list",
                'generated-type': """YANGDynClass(base=YANGListType(False,elements.elements, yang_name="elements", parent=self, is_container='list', user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None), is_container='list', yang_name="elements", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:node-topology', defining_module='node-topology', yang_type='list', is_config=True)""",
            })

        self.__elements = t
        if hasattr(self, '_set'):
            self._set()

    def _unset_elements(self):
        self.__elements = YANGDynClass(
            base=YANGListType(False, elements.elements, yang_name="elements", parent=self, is_container='list',
                              user_ordered=False, path_helper=self._path_helper, yang_keys='False', extensions=None),
            is_container='list', yang_name="elements", parent=self, path_helper=self._path_helper,
            extmethods=self._extmethods, register_paths=False, extensions=None, namespace='urn:node-topology',
            defining_module='node-topology', yang_type='list', is_config=True)

    response_id = __builtin__.property(_get_response_id, _set_response_id)
    elements = __builtin__.property(_get_elements, _set_elements)

    _pyangbind_elements = OrderedDict([('response_id', response_id), ('elements', elements), ])