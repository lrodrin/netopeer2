"""
This module implements the measurement of the OSNR and BER for slice 1

Copyright (c) 2017-2018 Laura Rodriguez Navas <laura.rodriguez.navas@cttc.cat>
"""

import data as d


def get_ber_and_osnr_parameters(host, port, login, password):
    connection = d.connect(host, port, login, password)

    try:
        # config = connection.get(
        #     filter='<nc:filter type="xpath" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" '
        #            'xmlns:sliceable-transceiver-sdm="urn:sliceable-transceiver-sdm" '
        #            'select="/sliceable-transceiver-sdm:transceiver-state"/>')

        # config = connection.get(
        #     filter='<nc:filter type="xpath" xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" '
        #            'xmlns:ietf-interfaces="urn:ietf:params:xml:ns:yang:ietf-interfaces" '
        #            'select="/ietf-interfaces:interfaces-state"/interface>')

        template = """<transceiver xmlns="urn:sliceable-transceiver-sdm">
                <slice>
                <optical-signal><opticalchannelid>1</opticalchannelid><monitor><osnr></osnr></monitor></optical-signal>
                <optical-signal><opticalchannelid>2</opticalchannelid><monitor><osnr></osnr></monitor></optical-signal>
                <optical-signal><opticalchannelid>3</opticalchannelid><monitor><osnr></osnr></monitor></optical-signal>
                <optical-signal><opticalchannelid>4</opticalchannelid><monitor><osnr></osnr></monitor></optical-signal>
                <optical-signal><opticalchannelid>5</opticalchannelid><monitor><osnr></osnr></monitor></optical-signal>
                <optical-signal><opticalchannelid>6</opticalchannelid><monitor><osnr></osnr></monitor></optical-signal>
                <optical-signal><opticalchannelid>7</opticalchannelid><monitor><osnr></osnr></monitor></optical-signal>
                <optical-signal><opticalchannelid>8</opticalchannelid><monitor><osnr></osnr></monitor></optical-signal>
                <optical-signal><opticalchannelid>9</opticalchannelid><monitor><osnr></osnr></monitor></optical-signal>
                <optical-signal><opticalchannelid>10</opticalchannelid><monitor><osnr></osnr></monitor></optical-signal>
                <optical-signal><opticalchannelid>11</opticalchannelid><monitor><osnr></osnr></monitor></optical-signal>
                <optical-signal><opticalchannelid>12</opticalchannelid><monitor><osnr></osnr></monitor></optical-signal>
                <optical-signal><opticalchannelid>13</opticalchannelid><monitor><osnr></osnr></monitor></optical-signal>
                <optical-signal><opticalchannelid>14</opticalchannelid><monitor><osnr></osnr></monitor></optical-signal>
                <optical-signal><opticalchannelid>15</opticalchannelid><monitor><osnr></osnr></monitor></optical-signal>
                <optical-signal><opticalchannelid>16</opticalchannelid><monitor><osnr></osnr></monitor></optical-signal>
                
                <optical-signal><opticalchannelid>9</opticalchannelid><monitor><ber></ber></monitor></optical-signal>
                <optical-signal><opticalchannelid>25</opticalchannelid><monitor><ber></ber></monitor></optical-signal>
                <optical-signal><opticalchannelid>41</opticalchannelid><monitor><ber></ber></monitor></optical-signal>
                <optical-signal><opticalchannelid>57</opticalchannelid><monitor><ber></ber></monitor></optical-signal>
                <optical-signal><opticalchannelid>73</opticalchannelid><monitor><ber></ber></monitor></optical-signal>
                <optical-signal><opticalchannelid>89</opticalchannelid><monitor><ber></ber></monitor></optical-signal>
                
                </slice>
                </transceiver>"""

        config = connection.get_config(source='running', filter=('subtree', template))
        print(config)


    except Exception as e:
        print(e)

    finally:
        connection.close_session()


if __name__ == '__main__':
    host = '10.1.7.83'
    port = 830
    login = 'root'
    password = 'netlabN.'

    get_ber_and_osnr_parameters(host, port, login, password)
