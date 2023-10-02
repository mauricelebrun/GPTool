import mido
from mido import MidiFile, MidiTrack, Message


def send_midi():# Set the Pure Data MIDI input port name (change this to your PD port name)
    pd_port_name = "IAC Driver puredata"

    output_port = mido.open_output(pd_port_name)
    note_number = 60  # MIDI note number for middle C
    velocity = 64  # Velocity (0-127)
    channel = 1  # MIDI channel number (must match the 'notein' object in PD)
    note_on = Message('note_on', note=note_number, velocity=velocity, channel=channel)
    output_port.send(note_on)
    output_port.close()
