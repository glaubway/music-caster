import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
import io
from PIL import Image


def get_audio_wave(file):
    data, samplerate = sf.read(file)
    n = len(data)
    time_axis = np.linspace(0, n / samplerate, n, endpoint=False)

    ch1, ch2 = data.transpose()

    sound_axis = ch1 + ch2
    accent_color = '#00bfff'
    bg = '#121212'
    buf = io.BytesIO()
    fig = plt.figure(figsize=(4.5 * 60, .75 * 60), dpi=5)
    plt.plot(time_axis, sound_axis, color=accent_color)
    plt.axis('off')
    plt.margins(x=0)
    fig.patch.set_facecolor(bg)
    plt.savefig(buf, format='png', bbox_inches='tight', transparent=True)
    im = Image.open(buf)
    # return im.resize((int(im.size[0] / 3), int(im.size[1] / 3)))


test_file = 'C:/Users/maste/MEGA/Music/No Mana - Memories of Nothing.flac'

get_audio_wave(test_file)
