"""
This module implements the measurement of the OSNR and BER for slice 1

Copyright (c) 2017-2018 Laura Rodriguez Navas <laura.rodriguez.navas@cttc.cat>
"""

import kddi.data as d


def get_ber_and_osnr_parameters(connection):
    try:
        config = connection.get(
            filter='<nc:filter type="xpath" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" '
                   'xmlns:sliceable-transceiver-sdm="urn:sliceable-transceiver-sdm" '
                   'select="/sliceable-transceiver-sdm:transceiver-state"/>')

        print(d.pretty_print(config.xml))

    except Exception as e:
        print(e)


if __name__ == '__main__':
    host = '10.1.7.66'
    port = 830
    login = 'root'
    password = 'netlabN.'

    connection = d.connect(host, port, login, password)
    get_ber_and_osnr_parameters(connection)
    connection.close_session()
