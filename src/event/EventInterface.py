#######################################################
# 
# EventInterface.py
# Python implementation of the Interface EventInterface
# Generated by Enterprise Architect
# Created on:      06-Mar-2022 12:13:39
# Original author: janbi
# 
#######################################################
from srcv import ParticipantInterface
from srcv import ResultInterface

class EventInterface:
    m_ParticipantInterface= ParticipantInterface()

    m_ResultInterface= ResultInterface()

    def create(start_time, name):
        pass