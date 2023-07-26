#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Hd Tx Hackrf Wxkj
# GNU Radio version: 3.10.1.1

from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
from gnuradio import fft
from gnuradio.fft import window
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import network
import math
import nrsc5
import osmosdr
import time




class hd_tx_hackrf_wxkj(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Hd Tx Hackrf Wxkj", catch_exceptions=True)

        ##################################################
        # Variables
        ##################################################
        self.usrp_interp = usrp_interp = 500
        self.quad_rate = quad_rate = 75e3
        self.max_dev = max_dev = 192e3
        self.dac_rate = dac_rate = 128e6
        self.usrp_rate = usrp_rate = int(dac_rate/usrp_interp)
        self.sps = sps = 2*math.pi*max_dev/quad_rate
        self.samp_rate = samp_rate = 2000000
        self.quad_rate_0 = quad_rate_0 = 75e3
        self.outbuffer = outbuffer = 1000
        self.input_gain = input_gain = 0.425
        self.freq = freq = 103.7e6
        self.fm_max_dev = fm_max_dev = 80e3
        self.audio_rate = audio_rate = 44100

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_2 = filter.rational_resampler_ccc(
                interpolation=256,
                decimation=243,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_1_1_1 = filter.rational_resampler_ccf(
                interpolation=2000,
                decimation=384,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_1_1_0 = filter.rational_resampler_ccc(
                interpolation=1000000,
                decimation=500000,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_1 = filter.rational_resampler_ccc(
                interpolation=125,
                decimation=49,
                taps=[],
                fractional_bw=0)
        self.osmosdr_sink_0 = osmosdr.sink(
            args="numchan=" + str(1) + " " + ""
        )
        self.osmosdr_sink_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.osmosdr_sink_0.set_sample_rate(samp_rate)
        self.osmosdr_sink_0.set_center_freq(freq, 0)
        self.osmosdr_sink_0.set_freq_corr(0, 0)
        self.osmosdr_sink_0.set_gain(0, 0)
        self.osmosdr_sink_0.set_if_gain(99999, 0)
        self.osmosdr_sink_0.set_bb_gain(0, 0)
        self.osmosdr_sink_0.set_antenna('', 0)
        self.osmosdr_sink_0.set_bandwidth(0, 0)
        self.nrsc5_sis_encoder_0 = nrsc5.sis_encoder(mode=nrsc5.pids_mode.FM, short_name='1037 KISS -FM', slogan='Hampton Roads #1 Hit Music Station', message='Check us out online at kissfmva.com', program_types=[nrsc5.program_type.TOP_40, nrsc5.program_type.ROCK, nrsc5.program_type.COUNTRY, nrsc5.program_type.NOSTALGIA, nrsc5.program_type.TALK], latitude=36.9165, longitude=-76.2146, altitude=17.0, country_code='US', fcc_facility_id=0)
        self.nrsc5_psd_encoder_0_1_0_0 = nrsc5.psd_encoder(4, 'Hampton Roads Trusted News Leader', 'News Radio 93.9 FM / 750 AM WPSZ', 128)
        self.nrsc5_psd_encoder_0_1 = nrsc5.psd_encoder(3, "The Best 80's Hits, Halloween Music and Christmas Music!", 'SmartFM', 128)
        self.nrsc5_psd_encoder_0_0_0 = nrsc5.psd_encoder(2, 'Newport News #1 For New Country', 'US99', 128)
        self.nrsc5_psd_encoder_0_0 = nrsc5.psd_encoder(0, 'Hampton Roads #1 Hit Music Station', '103.7 KISS FM', 128)
        self.nrsc5_psd_encoder_0 = nrsc5.psd_encoder(1, 'Hampton Roads Best Rock & Variety', '106 WDNR', 128)
        self.nrsc5_lot_encoder_0_1_0_0_0_0 = nrsc5.lot_encoder('WPSZHDLogo.png', 44, 0x1009)
        self.nrsc5_lot_encoder_0_1_0_0 = nrsc5.lot_encoder('SmartFMHDLogo.png', 44, 0x1007)
        self.nrsc5_lot_encoder_0_1_0 = nrsc5.lot_encoder('WDUSHDLogo.png', 43, 0x1005)
        self.nrsc5_lot_encoder_0_1 = nrsc5.lot_encoder('WXKJHDLogo.png', 43, 0x1001)
        self.nrsc5_lot_encoder_0_0_0_0_0_0_0 = nrsc5.lot_encoder('album_art.jpg', 1339, 0x1008)
        self.nrsc5_lot_encoder_0_0_0_0_0 = nrsc5.lot_encoder('album_art.jpg', 1339, 0x1006)
        self.nrsc5_lot_encoder_0_0_0_0 = nrsc5.lot_encoder('album_art.jpg', 1339, 0x1004)
        self.nrsc5_lot_encoder_0_0_0 = nrsc5.lot_encoder('album_art.jpg', 1338, 0x1002)
        self.nrsc5_lot_encoder_0_0 = nrsc5.lot_encoder('album_art.jpg', 1337, 0x1000)
        self.nrsc5_lot_encoder_0 = nrsc5.lot_encoder('WDNRHDLogo.png', 42, 0x1003)
        self.nrsc5_l2_encoder_0 = nrsc5.l2_encoder(5, 0, 146176, 2000)
        self.nrsc5_l1_fm_encoder_mp3_0 = nrsc5.l1_fm_encoder(3)
        self.nrsc5_hdc_encoder_0_0_0_0_0_0 = nrsc5.hdc_encoder(2, 4000)
        self.nrsc5_hdc_encoder_0_0_0_0 = nrsc5.hdc_encoder(2, 4000)
        self.nrsc5_hdc_encoder_0_0_0 = nrsc5.hdc_encoder(2, 8000)
        self.nrsc5_hdc_encoder_0_0 = nrsc5.hdc_encoder(2, 8000)
        self.nrsc5_hdc_encoder_0 = nrsc5.hdc_encoder(2, 16000)
        self.network_socket_pdu_1_1_0_0 = network.socket_pdu('TCP_SERVER', '', '9391', 10000, False)
        self.network_socket_pdu_1_1 = network.socket_pdu('TCP_SERVER', '', '6943', 10000, False)
        self.network_socket_pdu_1_0_0 = network.socket_pdu('TCP_SERVER', '', '9950', 10000, False)
        self.network_socket_pdu_1_0 = network.socket_pdu('TCP_SERVER', '', '10370', 10000, False)
        self.network_socket_pdu_1 = network.socket_pdu('TCP_SERVER', '', '52002', 10000, False)
        self.network_socket_pdu_0_0_0_0_0_0 = network.socket_pdu('TCP_SERVER', '', '9392', 10000, False)
        self.network_socket_pdu_0_0_0_0 = network.socket_pdu('TCP_SERVER', '', '6942', 10000, False)
        self.network_socket_pdu_0_0_0 = network.socket_pdu('TCP_SERVER', '', '9952', 10000, False)
        self.network_socket_pdu_0_0 = network.socket_pdu('TCP_SERVER', '', '10372', 10000, False)
        self.network_socket_pdu_0 = network.socket_pdu('TCP_SERVER', '', '52004', 10000, False)
        self.mmse_resampler_xx_0_1_1 = filter.mmse_resampler_ff(0, 192000/44100)
        self.mmse_resampler_xx_0_1_0_0 = filter.mmse_resampler_ff(0, 192000/44100)
        self.mmse_resampler_xx_0_1_0 = filter.mmse_resampler_ff(0, 192000/44100)
        self.mmse_resampler_xx_0_1 = filter.mmse_resampler_ff(0, 192000/44100)
        self.mmse_resampler_xx_0_0_0_1 = filter.mmse_resampler_ff(0, 192000/44100)
        self.mmse_resampler_xx_0_0_0_0_0 = filter.mmse_resampler_ff(0, 192000/44100)
        self.mmse_resampler_xx_0_0_0_0 = filter.mmse_resampler_ff(0, 192000/44100)
        self.mmse_resampler_xx_0_0_0 = filter.mmse_resampler_ff(0, 192000/44100)
        self.mmse_resampler_xx_0_0 = filter.mmse_resampler_ff(0, 192000/44100)
        self.mmse_resampler_xx_0 = filter.mmse_resampler_ff(0, 192000/44100)
        self.gr_frequency_modulator_fc_0_0 = analog.frequency_modulator_fc(2*math.pi*fm_max_dev/usrp_rate)
        self.gr_frequency_modulator_fc_0_0.set_max_output_buffer(1000)
        self.fft_vxx_0 = fft.fft_vcc(2048, False, window.rectangular(2048), True, 1)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, 2048)
        self.blocks_vector_source_x_0 = blocks.vector_source_c([math.sin(math.pi / 2 * i / 112) for i in range(112)] + [1] * (2048-112) + [math.cos(math.pi / 2 * i / 112) for i in range(112)], True, 1, [])
        self.blocks_repeat_0 = blocks.repeat(gr.sizeof_gr_complex*2048, 2)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_char*4608)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_1_0 = blocks.multiply_const_cc(0.750)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_cc(0.00750)
        self.blocks_keep_m_in_n_0 = blocks.keep_m_in_n(gr.sizeof_gr_complex, 2160, 4096, 0)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_float*1, int(audio_rate * 4.458))
        self.blocks_conjugate_cc_0 = blocks.conjugate_cc()
        self.blocks_add_xx_1 = blocks.add_vff(1)
        self.blocks_add_xx_0 = blocks.add_vcc(1)
        self.audio_source_1_0 = audio.source(192000, 'RDS_Injection', True)
        self.audio_source_1 = audio.source(192000, 'MPX', True)
        self.audio_source_0_0_1 = audio.source(192000, 'WXKJ', False)
        self.audio_source_0_0_0_0_0_0 = audio.source(192000, 'WPSZ', False)
        self.audio_source_0_0_0_0 = audio.source(192000, 'SmartFM', False)
        self.audio_source_0_0_0 = audio.source(192000, 'WDNR', True)
        self.audio_source_0_0 = audio.source(192000, 'WDUS', False)


        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.network_socket_pdu_0, 'pdus'), (self.nrsc5_lot_encoder_0_0, 'file'))
        self.msg_connect((self.network_socket_pdu_0_0, 'pdus'), (self.nrsc5_lot_encoder_0_0_0, 'file'))
        self.msg_connect((self.network_socket_pdu_0_0_0, 'pdus'), (self.nrsc5_lot_encoder_0_0_0_0, 'file'))
        self.msg_connect((self.network_socket_pdu_0_0_0_0, 'pdus'), (self.nrsc5_lot_encoder_0_0_0_0_0, 'file'))
        self.msg_connect((self.network_socket_pdu_0_0_0_0_0_0, 'pdus'), (self.nrsc5_lot_encoder_0_0_0_0_0_0_0, 'file'))
        self.msg_connect((self.network_socket_pdu_1, 'pdus'), (self.nrsc5_psd_encoder_0, 'set_meta'))
        self.msg_connect((self.network_socket_pdu_1_0, 'pdus'), (self.nrsc5_psd_encoder_0_0, 'set_meta'))
        self.msg_connect((self.network_socket_pdu_1_0_0, 'pdus'), (self.nrsc5_psd_encoder_0_0_0, 'set_meta'))
        self.msg_connect((self.network_socket_pdu_1_1, 'pdus'), (self.nrsc5_psd_encoder_0_1, 'set_meta'))
        self.msg_connect((self.network_socket_pdu_1_1_0_0, 'pdus'), (self.nrsc5_psd_encoder_0_1_0_0, 'set_meta'))
        self.msg_connect((self.nrsc5_l1_fm_encoder_mp3_0, 'clock'), (self.nrsc5_psd_encoder_0, 'clock'))
        self.msg_connect((self.nrsc5_l1_fm_encoder_mp3_0, 'clock'), (self.nrsc5_psd_encoder_0_0, 'clock'))
        self.msg_connect((self.nrsc5_l1_fm_encoder_mp3_0, 'clock'), (self.nrsc5_psd_encoder_0_0_0, 'clock'))
        self.msg_connect((self.nrsc5_l1_fm_encoder_mp3_0, 'clock'), (self.nrsc5_psd_encoder_0_1, 'clock'))
        self.msg_connect((self.nrsc5_l1_fm_encoder_mp3_0, 'clock'), (self.nrsc5_psd_encoder_0_1_0_0, 'clock'))
        self.msg_connect((self.nrsc5_l2_encoder_0, 'ready'), (self.nrsc5_lot_encoder_0, 'ready'))
        self.msg_connect((self.nrsc5_l2_encoder_0, 'ready'), (self.nrsc5_lot_encoder_0_0, 'ready'))
        self.msg_connect((self.nrsc5_l2_encoder_0, 'ready'), (self.nrsc5_lot_encoder_0_0_0, 'ready'))
        self.msg_connect((self.nrsc5_l2_encoder_0, 'ready'), (self.nrsc5_lot_encoder_0_0_0_0, 'ready'))
        self.msg_connect((self.nrsc5_l2_encoder_0, 'ready'), (self.nrsc5_lot_encoder_0_0_0_0_0, 'ready'))
        self.msg_connect((self.nrsc5_l2_encoder_0, 'ready'), (self.nrsc5_lot_encoder_0_0_0_0_0_0_0, 'ready'))
        self.msg_connect((self.nrsc5_l2_encoder_0, 'ready'), (self.nrsc5_lot_encoder_0_1, 'ready'))
        self.msg_connect((self.nrsc5_l2_encoder_0, 'ready'), (self.nrsc5_lot_encoder_0_1_0, 'ready'))
        self.msg_connect((self.nrsc5_l2_encoder_0, 'ready'), (self.nrsc5_lot_encoder_0_1_0_0, 'ready'))
        self.msg_connect((self.nrsc5_l2_encoder_0, 'ready'), (self.nrsc5_lot_encoder_0_1_0_0_0_0, 'ready'))
        self.msg_connect((self.nrsc5_l2_encoder_0, 'ready'), (self.nrsc5_sis_encoder_0, 'ready'))
        self.msg_connect((self.nrsc5_lot_encoder_0, 'aas'), (self.nrsc5_l2_encoder_0, 'aas'))
        self.msg_connect((self.nrsc5_lot_encoder_0_0, 'aas'), (self.nrsc5_l2_encoder_0, 'aas'))
        self.msg_connect((self.nrsc5_lot_encoder_0_0_0, 'aas'), (self.nrsc5_l2_encoder_0, 'aas'))
        self.msg_connect((self.nrsc5_lot_encoder_0_0_0_0, 'aas'), (self.nrsc5_l2_encoder_0, 'aas'))
        self.msg_connect((self.nrsc5_lot_encoder_0_0_0_0_0, 'aas'), (self.nrsc5_l2_encoder_0, 'aas'))
        self.msg_connect((self.nrsc5_lot_encoder_0_0_0_0_0_0_0, 'aas'), (self.nrsc5_l2_encoder_0, 'aas'))
        self.msg_connect((self.nrsc5_lot_encoder_0_1, 'aas'), (self.nrsc5_l2_encoder_0, 'aas'))
        self.msg_connect((self.nrsc5_lot_encoder_0_1_0, 'aas'), (self.nrsc5_l2_encoder_0, 'aas'))
        self.msg_connect((self.nrsc5_lot_encoder_0_1_0_0, 'aas'), (self.nrsc5_l2_encoder_0, 'aas'))
        self.msg_connect((self.nrsc5_lot_encoder_0_1_0_0_0_0, 'aas'), (self.nrsc5_l2_encoder_0, 'aas'))
        self.msg_connect((self.nrsc5_sis_encoder_0, 'aas'), (self.nrsc5_l2_encoder_0, 'aas'))
        self.connect((self.audio_source_0_0, 1), (self.mmse_resampler_xx_0_0_0, 0))
        self.connect((self.audio_source_0_0, 0), (self.mmse_resampler_xx_0_1, 0))
        self.connect((self.audio_source_0_0_0, 1), (self.mmse_resampler_xx_0_0_0_1, 0))
        self.connect((self.audio_source_0_0_0, 0), (self.mmse_resampler_xx_0_1_1, 0))
        self.connect((self.audio_source_0_0_0_0, 1), (self.mmse_resampler_xx_0_0_0_0, 0))
        self.connect((self.audio_source_0_0_0_0, 0), (self.mmse_resampler_xx_0_1_0, 0))
        self.connect((self.audio_source_0_0_0_0_0_0, 1), (self.mmse_resampler_xx_0_0_0_0_0, 0))
        self.connect((self.audio_source_0_0_0_0_0_0, 0), (self.mmse_resampler_xx_0_1_0_0, 0))
        self.connect((self.audio_source_0_0_1, 0), (self.mmse_resampler_xx_0, 0))
        self.connect((self.audio_source_0_0_1, 1), (self.mmse_resampler_xx_0_0, 0))
        self.connect((self.audio_source_1, 0), (self.blocks_delay_0, 0))
        self.connect((self.audio_source_1_0, 0), (self.blocks_add_xx_1, 1))
        self.connect((self.blocks_add_xx_0, 0), (self.osmosdr_sink_0, 0))
        self.connect((self.blocks_add_xx_1, 0), (self.gr_frequency_modulator_fc_0_0, 0))
        self.connect((self.blocks_conjugate_cc_0, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_add_xx_1, 0))
        self.connect((self.blocks_keep_m_in_n_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.blocks_multiply_const_vxx_1_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_conjugate_cc_0, 0))
        self.connect((self.blocks_null_source_0, 0), (self.nrsc5_l1_fm_encoder_mp3_0, 1))
        self.connect((self.blocks_repeat_0, 0), (self.blocks_vector_to_stream_0, 0))
        self.connect((self.blocks_vector_source_x_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_keep_m_in_n_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.blocks_repeat_0, 0))
        self.connect((self.gr_frequency_modulator_fc_0_0, 0), (self.rational_resampler_xxx_1_1_1, 0))
        self.connect((self.mmse_resampler_xx_0, 0), (self.nrsc5_hdc_encoder_0, 0))
        self.connect((self.mmse_resampler_xx_0_0, 0), (self.nrsc5_hdc_encoder_0, 1))
        self.connect((self.mmse_resampler_xx_0_0_0, 0), (self.nrsc5_hdc_encoder_0_0, 1))
        self.connect((self.mmse_resampler_xx_0_0_0_0, 0), (self.nrsc5_hdc_encoder_0_0_0_0, 1))
        self.connect((self.mmse_resampler_xx_0_0_0_0_0, 0), (self.nrsc5_hdc_encoder_0_0_0_0_0_0, 1))
        self.connect((self.mmse_resampler_xx_0_0_0_1, 0), (self.nrsc5_hdc_encoder_0_0_0, 1))
        self.connect((self.mmse_resampler_xx_0_1, 0), (self.nrsc5_hdc_encoder_0_0, 0))
        self.connect((self.mmse_resampler_xx_0_1_0, 0), (self.nrsc5_hdc_encoder_0_0_0_0, 0))
        self.connect((self.mmse_resampler_xx_0_1_0_0, 0), (self.nrsc5_hdc_encoder_0_0_0_0_0_0, 0))
        self.connect((self.mmse_resampler_xx_0_1_1, 0), (self.nrsc5_hdc_encoder_0_0_0, 0))
        self.connect((self.nrsc5_hdc_encoder_0, 0), (self.nrsc5_l2_encoder_0, 0))
        self.connect((self.nrsc5_hdc_encoder_0_0, 0), (self.nrsc5_l2_encoder_0, 2))
        self.connect((self.nrsc5_hdc_encoder_0_0_0, 0), (self.nrsc5_l2_encoder_0, 1))
        self.connect((self.nrsc5_hdc_encoder_0_0_0_0, 0), (self.nrsc5_l2_encoder_0, 3))
        self.connect((self.nrsc5_hdc_encoder_0_0_0_0_0_0, 0), (self.nrsc5_l2_encoder_0, 4))
        self.connect((self.nrsc5_l1_fm_encoder_mp3_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.nrsc5_l2_encoder_0, 0), (self.nrsc5_l1_fm_encoder_mp3_0, 0))
        self.connect((self.nrsc5_psd_encoder_0, 0), (self.nrsc5_l2_encoder_0, 6))
        self.connect((self.nrsc5_psd_encoder_0_0, 0), (self.nrsc5_l2_encoder_0, 5))
        self.connect((self.nrsc5_psd_encoder_0_0_0, 0), (self.nrsc5_l2_encoder_0, 7))
        self.connect((self.nrsc5_psd_encoder_0_1, 0), (self.nrsc5_l2_encoder_0, 8))
        self.connect((self.nrsc5_psd_encoder_0_1_0_0, 0), (self.nrsc5_l2_encoder_0, 9))
        self.connect((self.nrsc5_sis_encoder_0, 0), (self.nrsc5_l1_fm_encoder_mp3_0, 2))
        self.connect((self.rational_resampler_xxx_1, 0), (self.rational_resampler_xxx_2, 0))
        self.connect((self.rational_resampler_xxx_1_1_0, 0), (self.blocks_multiply_const_vxx_1_0, 0))
        self.connect((self.rational_resampler_xxx_1_1_1, 0), (self.rational_resampler_xxx_1_1_0, 0))
        self.connect((self.rational_resampler_xxx_2, 0), (self.blocks_multiply_const_vxx_0, 0))


    def get_usrp_interp(self):
        return self.usrp_interp

    def set_usrp_interp(self, usrp_interp):
        self.usrp_interp = usrp_interp
        self.set_usrp_rate(int(self.dac_rate/self.usrp_interp))

    def get_quad_rate(self):
        return self.quad_rate

    def set_quad_rate(self, quad_rate):
        self.quad_rate = quad_rate
        self.set_sps(2*math.pi*self.max_dev/self.quad_rate)

    def get_max_dev(self):
        return self.max_dev

    def set_max_dev(self, max_dev):
        self.max_dev = max_dev
        self.set_sps(2*math.pi*self.max_dev/self.quad_rate)

    def get_dac_rate(self):
        return self.dac_rate

    def set_dac_rate(self, dac_rate):
        self.dac_rate = dac_rate
        self.set_usrp_rate(int(self.dac_rate/self.usrp_interp))

    def get_usrp_rate(self):
        return self.usrp_rate

    def set_usrp_rate(self, usrp_rate):
        self.usrp_rate = usrp_rate
        self.gr_frequency_modulator_fc_0_0.set_sensitivity(2*math.pi*self.fm_max_dev/self.usrp_rate)

    def get_sps(self):
        return self.sps

    def set_sps(self, sps):
        self.sps = sps

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.osmosdr_sink_0.set_sample_rate(self.samp_rate)

    def get_quad_rate_0(self):
        return self.quad_rate_0

    def set_quad_rate_0(self, quad_rate_0):
        self.quad_rate_0 = quad_rate_0

    def get_outbuffer(self):
        return self.outbuffer

    def set_outbuffer(self, outbuffer):
        self.outbuffer = outbuffer

    def get_input_gain(self):
        return self.input_gain

    def set_input_gain(self, input_gain):
        self.input_gain = input_gain

    def get_freq(self):
        return self.freq

    def set_freq(self, freq):
        self.freq = freq
        self.osmosdr_sink_0.set_center_freq(self.freq, 0)

    def get_fm_max_dev(self):
        return self.fm_max_dev

    def set_fm_max_dev(self, fm_max_dev):
        self.fm_max_dev = fm_max_dev
        self.gr_frequency_modulator_fc_0_0.set_sensitivity(2*math.pi*self.fm_max_dev/self.usrp_rate)

    def get_audio_rate(self):
        return self.audio_rate

    def set_audio_rate(self, audio_rate):
        self.audio_rate = audio_rate
        self.blocks_delay_0.set_dly(int(self.audio_rate * 4.458))




def main(top_block_cls=hd_tx_hackrf_wxkj, options=None):
    tb = top_block_cls()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    tb.start()

    try:
        input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
