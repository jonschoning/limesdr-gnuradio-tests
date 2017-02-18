#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: Nullsource To Osmocom Sink
# Generated: Fri Feb 17 23:25:25 2017
##################################################

from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import osmosdr
import time


class nullsource_to_osmocom_sink(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Nullsource To Osmocom Sink")

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 10e6
        self.center_freq = center_freq = 910e6

        ##################################################
        # Blocks
        ##################################################
        self.osmosdr_sink_0 = osmosdr.sink( args="numchan=" + str(1) + " " + 'driver=lime' )
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(center_freq, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(35, 0)
        self.osmosdr_sink_0.set_if_gain(0, 0)
        self.osmosdr_sink_0.set_bb_gain(0, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
          
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_gr_complex*1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_null_source_0, 0), (self.osmosdr_sink_0, 0))    

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)

    def get_center_freq(self):
        return self.center_freq

    def set_center_freq(self, center_freq):
        self.center_freq = center_freq
        self.osmosdr_sink_0.set_center_freq(self.center_freq, 0)


def main(top_block_cls=nullsource_to_osmocom_sink, options=None):

    tb = top_block_cls()
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
