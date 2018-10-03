# -*- coding: utf-8 -*-
from collections import OrderedDict

import six
from pyangbind.lib.base import PybindBase
from pyangbind.lib.yangtypes import YANGDynClass

# PY3 support of some PY2 keywords (needs improved)
if six.PY3:
    import builtins as __builtin__

    long = int
elif six.PY2:
    import __builtin__

from . import supported_modulation_format
from . import supported_center_frequency_range
from . import supported_bandwidth


class available_transceiver(PybindBase):
    """
    This class was auto-generated by the PythonClass plugin for PYANG
    from YANG module node-topology - based on the path /node/port/available-transceiver. Each member element of
    the container is represented as a class variable - with a specific
    YANG type.
    """
    __slots__ = (
    '_path_helper', '_extmethods', '__transceiver_id', '__transceiver_type', '__supported_modulation_format',
    '__supported_center_frequency_range', '__supported_bandwidth', '__supported_FEC', '__supported_equalization',
    '__supported_monitoring',)

    _yang_name = 'available-transceiver'

    _pybind_generated_by = 'container'

    def __init__(self, *args, **kwargs):

        self._path_helper = False

        self._extmethods = False
        self.__supported_bandwidth = YANGDynClass(base=supported_bandwidth.supported_bandwidth,
                                                  is_container='container', yang_name="supported-bandwidth",
                                                  parent=self, path_helper=self._path_helper,
                                                  extmethods=self._extmethods, register_paths=True, extensions=None,
                                                  namespace='urn:node-topology', defining_module='node-topology',
                                                  yang_type='container', is_config=True)
        self.__transceiver_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="transceiver-id", parent=self,
                                             path_helper=self._path_helper, extmethods=self._extmethods,
                                             register_paths=True, namespace='urn:node-topology',
                                             defining_module='node-topology', yang_type='string', is_config=True)
        self.__supported_FEC = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="supported-FEC", parent=self,
                                            path_helper=self._path_helper, extmethods=self._extmethods,
                                            register_paths=True, namespace='urn:node-topology',
                                            defining_module='node-topology', yang_type='string', is_config=True)
        self.__transceiver_type = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="transceiver-type",
                                               parent=self, path_helper=self._path_helper, extmethods=self._extmethods,
                                               register_paths=True, namespace='urn:node-topology',
                                               defining_module='node-topology', yang_type='string', is_config=True)
        self.__supported_center_frequency_range = YANGDynClass(
            base=supported_center_frequency_range.supported_center_frequency_range, is_container='container',
            yang_name="supported-center-frequency-range", parent=self, path_helper=self._path_helper,
            extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:node-topology',
            defining_module='node-topology', yang_type='container', is_config=True)
        self.__supported_equalization = YANGDynClass(base=six.text_type, is_leaf=True,
                                                     yang_name="supported-equalization", parent=self,
                                                     path_helper=self._path_helper, extmethods=self._extmethods,
                                                     register_paths=True, namespace='urn:node-topology',
                                                     defining_module='node-topology', yang_type='string',
                                                     is_config=True)
        self.__supported_monitoring = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="supported-monitoring",
                                                   parent=self, path_helper=self._path_helper,
                                                   extmethods=self._extmethods, register_paths=True,
                                                   namespace='urn:node-topology', defining_module='node-topology',
                                                   yang_type='string', is_config=True)
        self.__supported_modulation_format = YANGDynClass(base=supported_modulation_format.supported_modulation_format,
                                                          is_container='container',
                                                          yang_name="supported-modulation-format", parent=self,
                                                          path_helper=self._path_helper, extmethods=self._extmethods,
                                                          register_paths=True, extensions=None,
                                                          namespace='urn:node-topology',
                                                          defining_module='node-topology', yang_type='container',
                                                          is_config=True)

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
            return [u'node', u'port', u'available-transceiver']

    def _get_transceiver_id(self):
        """
        Getter method for transceiver_id, mapped from YANG variable /node/port/available_transceiver/transceiver_id (string)
        """
        return self.__transceiver_id

    def _set_transceiver_id(self, v, load=False):
        """
        Setter method for transceiver_id, mapped from YANG variable /node/port/available_transceiver/transceiver_id (string)
        If this variable is read-only (config: false) in the
        source YANG file, then _set_transceiver_id is considered as a private
        method. Backends looking to populate this variable should
        do so via calling thisObj._set_transceiver_id() directly.
        """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(v, base=six.text_type, is_leaf=True, yang_name="transceiver-id", parent=self,
                             path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True,
                             namespace='urn:node-topology', defining_module='node-topology', yang_type='string',
                             is_config=True)
        except (TypeError, ValueError):
            raise ValueError({
                'error-string': """transceiver_id must be of a type compatible with string""",
                'defined-type': "string",
                'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="transceiver-id", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:node-topology', defining_module='node-topology', yang_type='string', is_config=True)""",
            })

        self.__transceiver_id = t
        if hasattr(self, '_set'):
            self._set()

    def _unset_transceiver_id(self):
        self.__transceiver_id = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="transceiver-id", parent=self,
                                             path_helper=self._path_helper, extmethods=self._extmethods,
                                             register_paths=True, namespace='urn:node-topology',
                                             defining_module='node-topology', yang_type='string', is_config=True)

    def _get_transceiver_type(self):
        """
        Getter method for transceiver_type, mapped from YANG variable /node/port/available_transceiver/transceiver_type (string)
        """
        return self.__transceiver_type

    def _set_transceiver_type(self, v, load=False):
        """
        Setter method for transceiver_type, mapped from YANG variable /node/port/available_transceiver/transceiver_type (string)
        If this variable is read-only (config: false) in the
        source YANG file, then _set_transceiver_type is considered as a private
        method. Backends looking to populate this variable should
        do so via calling thisObj._set_transceiver_type() directly.
        """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(v, base=six.text_type, is_leaf=True, yang_name="transceiver-type", parent=self,
                             path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True,
                             namespace='urn:node-topology', defining_module='node-topology', yang_type='string',
                             is_config=True)
        except (TypeError, ValueError):
            raise ValueError({
                'error-string': """transceiver_type must be of a type compatible with string""",
                'defined-type': "string",
                'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="transceiver-type", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:node-topology', defining_module='node-topology', yang_type='string', is_config=True)""",
            })

        self.__transceiver_type = t
        if hasattr(self, '_set'):
            self._set()

    def _unset_transceiver_type(self):
        self.__transceiver_type = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="transceiver-type",
                                               parent=self, path_helper=self._path_helper, extmethods=self._extmethods,
                                               register_paths=True, namespace='urn:node-topology',
                                               defining_module='node-topology', yang_type='string', is_config=True)

    def _get_supported_modulation_format(self):
        """
        Getter method for supported_modulation_format, mapped from YANG variable /node/port/available_transceiver/supported_modulation_format (container)
        """
        return self.__supported_modulation_format

    def _set_supported_modulation_format(self, v, load=False):
        """
        Setter method for supported_modulation_format, mapped from YANG variable /node/port/available_transceiver/supported_modulation_format (container)
        If this variable is read-only (config: false) in the
        source YANG file, then _set_supported_modulation_format is considered as a private
        method. Backends looking to populate this variable should
        do so via calling thisObj._set_supported_modulation_format() directly.
        """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(v, base=supported_modulation_format.supported_modulation_format, is_container='container',
                             yang_name="supported-modulation-format", parent=self, path_helper=self._path_helper,
                             extmethods=self._extmethods, register_paths=True, extensions=None,
                             namespace='urn:node-topology', defining_module='node-topology', yang_type='container',
                             is_config=True)
        except (TypeError, ValueError):
            raise ValueError({
                'error-string': """supported_modulation_format must be of a type compatible with container""",
                'defined-type': "container",
                'generated-type': """YANGDynClass(base=supported_modulation_format.supported_modulation_format, is_container='container', yang_name="supported-modulation-format", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:node-topology', defining_module='node-topology', yang_type='container', is_config=True)""",
            })

        self.__supported_modulation_format = t
        if hasattr(self, '_set'):
            self._set()

    def _unset_supported_modulation_format(self):
        self.__supported_modulation_format = YANGDynClass(base=supported_modulation_format.supported_modulation_format,
                                                          is_container='container',
                                                          yang_name="supported-modulation-format", parent=self,
                                                          path_helper=self._path_helper, extmethods=self._extmethods,
                                                          register_paths=True, extensions=None,
                                                          namespace='urn:node-topology',
                                                          defining_module='node-topology', yang_type='container',
                                                          is_config=True)

    def _get_supported_center_frequency_range(self):
        """
        Getter method for supported_center_frequency_range, mapped from YANG variable /node/port/available_transceiver/supported_center_frequency_range (container)
        """
        return self.__supported_center_frequency_range

    def _set_supported_center_frequency_range(self, v, load=False):
        """
        Setter method for supported_center_frequency_range, mapped from YANG variable /node/port/available_transceiver/supported_center_frequency_range (container)
        If this variable is read-only (config: false) in the
        source YANG file, then _set_supported_center_frequency_range is considered as a private
        method. Backends looking to populate this variable should
        do so via calling thisObj._set_supported_center_frequency_range() directly.
        """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(v, base=supported_center_frequency_range.supported_center_frequency_range,
                             is_container='container', yang_name="supported-center-frequency-range", parent=self,
                             path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True,
                             extensions=None, namespace='urn:node-topology', defining_module='node-topology',
                             yang_type='container', is_config=True)
        except (TypeError, ValueError):
            raise ValueError({
                'error-string': """supported_center_frequency_range must be of a type compatible with container""",
                'defined-type': "container",
                'generated-type': """YANGDynClass(base=supported_center_frequency_range.supported_center_frequency_range, is_container='container', yang_name="supported-center-frequency-range", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:node-topology', defining_module='node-topology', yang_type='container', is_config=True)""",
            })

        self.__supported_center_frequency_range = t
        if hasattr(self, '_set'):
            self._set()

    def _unset_supported_center_frequency_range(self):
        self.__supported_center_frequency_range = YANGDynClass(
            base=supported_center_frequency_range.supported_center_frequency_range, is_container='container',
            yang_name="supported-center-frequency-range", parent=self, path_helper=self._path_helper,
            extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:node-topology',
            defining_module='node-topology', yang_type='container', is_config=True)

    def _get_supported_bandwidth(self):
        """
        Getter method for supported_bandwidth, mapped from YANG variable /node/port/available_transceiver/supported_bandwidth (container)
        """
        return self.__supported_bandwidth

    def _set_supported_bandwidth(self, v, load=False):
        """
        Setter method for supported_bandwidth, mapped from YANG variable /node/port/available_transceiver/supported_bandwidth (container)
        If this variable is read-only (config: false) in the
        source YANG file, then _set_supported_bandwidth is considered as a private
        method. Backends looking to populate this variable should
        do so via calling thisObj._set_supported_bandwidth() directly.
        """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(v, base=supported_bandwidth.supported_bandwidth, is_container='container',
                             yang_name="supported-bandwidth", parent=self, path_helper=self._path_helper,
                             extmethods=self._extmethods, register_paths=True, extensions=None,
                             namespace='urn:node-topology', defining_module='node-topology', yang_type='container',
                             is_config=True)
        except (TypeError, ValueError):
            raise ValueError({
                'error-string': """supported_bandwidth must be of a type compatible with container""",
                'defined-type': "container",
                'generated-type': """YANGDynClass(base=supported_bandwidth.supported_bandwidth, is_container='container', yang_name="supported-bandwidth", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, extensions=None, namespace='urn:node-topology', defining_module='node-topology', yang_type='container', is_config=True)""",
            })

        self.__supported_bandwidth = t
        if hasattr(self, '_set'):
            self._set()

    def _unset_supported_bandwidth(self):
        self.__supported_bandwidth = YANGDynClass(base=supported_bandwidth.supported_bandwidth,
                                                  is_container='container', yang_name="supported-bandwidth",
                                                  parent=self, path_helper=self._path_helper,
                                                  extmethods=self._extmethods, register_paths=True, extensions=None,
                                                  namespace='urn:node-topology', defining_module='node-topology',
                                                  yang_type='container', is_config=True)

    def _get_supported_FEC(self):
        """
        Getter method for supported_FEC, mapped from YANG variable /node/port/available_transceiver/supported_FEC (string)
        """
        return self.__supported_FEC

    def _set_supported_FEC(self, v, load=False):
        """
        Setter method for supported_FEC, mapped from YANG variable /node/port/available_transceiver/supported_FEC (string)
        If this variable is read-only (config: false) in the
        source YANG file, then _set_supported_FEC is considered as a private
        method. Backends looking to populate this variable should
        do so via calling thisObj._set_supported_FEC() directly.
        """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(v, base=six.text_type, is_leaf=True, yang_name="supported-FEC", parent=self,
                             path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True,
                             namespace='urn:node-topology', defining_module='node-topology', yang_type='string',
                             is_config=True)
        except (TypeError, ValueError):
            raise ValueError({
                'error-string': """supported_FEC must be of a type compatible with string""",
                'defined-type': "string",
                'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="supported-FEC", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:node-topology', defining_module='node-topology', yang_type='string', is_config=True)""",
            })

        self.__supported_FEC = t
        if hasattr(self, '_set'):
            self._set()

    def _unset_supported_FEC(self):
        self.__supported_FEC = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="supported-FEC", parent=self,
                                            path_helper=self._path_helper, extmethods=self._extmethods,
                                            register_paths=True, namespace='urn:node-topology',
                                            defining_module='node-topology', yang_type='string', is_config=True)

    def _get_supported_equalization(self):
        """
        Getter method for supported_equalization, mapped from YANG variable /node/port/available_transceiver/supported_equalization (string)
        """
        return self.__supported_equalization

    def _set_supported_equalization(self, v, load=False):
        """
        Setter method for supported_equalization, mapped from YANG variable /node/port/available_transceiver/supported_equalization (string)
        If this variable is read-only (config: false) in the
        source YANG file, then _set_supported_equalization is considered as a private
        method. Backends looking to populate this variable should
        do so via calling thisObj._set_supported_equalization() directly.
        """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(v, base=six.text_type, is_leaf=True, yang_name="supported-equalization", parent=self,
                             path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True,
                             namespace='urn:node-topology', defining_module='node-topology', yang_type='string',
                             is_config=True)
        except (TypeError, ValueError):
            raise ValueError({
                'error-string': """supported_equalization must be of a type compatible with string""",
                'defined-type': "string",
                'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="supported-equalization", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:node-topology', defining_module='node-topology', yang_type='string', is_config=True)""",
            })

        self.__supported_equalization = t
        if hasattr(self, '_set'):
            self._set()

    def _unset_supported_equalization(self):
        self.__supported_equalization = YANGDynClass(base=six.text_type, is_leaf=True,
                                                     yang_name="supported-equalization", parent=self,
                                                     path_helper=self._path_helper, extmethods=self._extmethods,
                                                     register_paths=True, namespace='urn:node-topology',
                                                     defining_module='node-topology', yang_type='string',
                                                     is_config=True)

    def _get_supported_monitoring(self):
        """
        Getter method for supported_monitoring, mapped from YANG variable /node/port/available_transceiver/supported_monitoring (string)
        """
        return self.__supported_monitoring

    def _set_supported_monitoring(self, v, load=False):
        """
        Setter method for supported_monitoring, mapped from YANG variable /node/port/available_transceiver/supported_monitoring (string)
        If this variable is read-only (config: false) in the
        source YANG file, then _set_supported_monitoring is considered as a private
        method. Backends looking to populate this variable should
        do so via calling thisObj._set_supported_monitoring() directly.
        """
        if hasattr(v, "_utype"):
            v = v._utype(v)
        try:
            t = YANGDynClass(v, base=six.text_type, is_leaf=True, yang_name="supported-monitoring", parent=self,
                             path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True,
                             namespace='urn:node-topology', defining_module='node-topology', yang_type='string',
                             is_config=True)
        except (TypeError, ValueError):
            raise ValueError({
                'error-string': """supported_monitoring must be of a type compatible with string""",
                'defined-type': "string",
                'generated-type': """YANGDynClass(base=six.text_type, is_leaf=True, yang_name="supported-monitoring", parent=self, path_helper=self._path_helper, extmethods=self._extmethods, register_paths=True, namespace='urn:node-topology', defining_module='node-topology', yang_type='string', is_config=True)""",
            })

        self.__supported_monitoring = t
        if hasattr(self, '_set'):
            self._set()

    def _unset_supported_monitoring(self):
        self.__supported_monitoring = YANGDynClass(base=six.text_type, is_leaf=True, yang_name="supported-monitoring",
                                                   parent=self, path_helper=self._path_helper,
                                                   extmethods=self._extmethods, register_paths=True,
                                                   namespace='urn:node-topology', defining_module='node-topology',
                                                   yang_type='string', is_config=True)

    transceiver_id = __builtin__.property(_get_transceiver_id, _set_transceiver_id)
    transceiver_type = __builtin__.property(_get_transceiver_type, _set_transceiver_type)
    supported_modulation_format = __builtin__.property(_get_supported_modulation_format,
                                                       _set_supported_modulation_format)
    supported_center_frequency_range = __builtin__.property(_get_supported_center_frequency_range,
                                                            _set_supported_center_frequency_range)
    supported_bandwidth = __builtin__.property(_get_supported_bandwidth, _set_supported_bandwidth)
    supported_FEC = __builtin__.property(_get_supported_FEC, _set_supported_FEC)
    supported_equalization = __builtin__.property(_get_supported_equalization, _set_supported_equalization)
    supported_monitoring = __builtin__.property(_get_supported_monitoring, _set_supported_monitoring)

    _pyangbind_elements = OrderedDict([('transceiver_id', transceiver_id), ('transceiver_type', transceiver_type),
                                       ('supported_modulation_format', supported_modulation_format),
                                       ('supported_center_frequency_range', supported_center_frequency_range),
                                       ('supported_bandwidth', supported_bandwidth), ('supported_FEC', supported_FEC),
                                       ('supported_equalization', supported_equalization),
                                       ('supported_monitoring', supported_monitoring), ])