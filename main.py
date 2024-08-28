import threading

import librosa
import sounddevice as sd
from PyQt5 import QtWidgets
from threading import Thread
from scipy import signal
import sys

import bih_coefs
import design
import kih_coefs
import numpy

isPlaying = False
wavPath = ''
dbGainValues = [0, 0, 0, 0, 0, 0]
isKih = True


def playAudio():
    global isPlaying, wavPath

    if not isPlaying:
        isPlaying = True
        audioData, sampleRate = librosa.load(wavPath)

        audioThread = Thread(target=playChunks, args=(audioData,))
        audioThread.start()
    else:
        sd.stop()
        isPlaying = False


def playChunks(audioData):
    global isPlaying

    CHUNK_SIZE = 45000

    outputStream = sd.OutputStream(samplerate=22050, channels=1)
    outputStream.start()

    while True:
        for i in range(0, len(audioData), CHUNK_SIZE):
            if not isPlaying:
                outputStream.stop()
                outputStream.close()
                return

            chunk = audioData[i:i + CHUNK_SIZE]
            if isKih:
                filtered_chunk = kih_filter(chunk)
            else:
                filtered_chunk = bih_filter(chunk)
            outputStream.write(numpy.reshape(filtered_chunk, -1).astype(numpy.float32))


def kih_filter(bufferChunk):
    threads = []
    results = []

    filter_coefs = [kih_coefs.kih_0_100, kih_coefs.kih_101_722, kih_coefs.kih_723_1966, kih_coefs.kih_1967_4453,
                    kih_coefs.kih_4454_9428, kih_coefs.kih_9429_20000]

    for i in range(0, len(filter_coefs)):
        svertka = Thread(target=results.append,
                         args=(convolve(bufferChunk, filter_coefs[i], dbGainValues[i]),))  # кортеж
        threads.append(svertka)
        svertka.start()

    for thread in threads:
        thread.join()

    result_convolve = results[0]
    for i in range(1, len(results)):
        result_convolve += results[i]

    return result_convolve


def bih_filter(bufferChunk):
    # return bufferChunk
    sections = len(bih_coefs.NUM_0_100) // 2

    den = bih_coefs.DEN_0_100[1::2]
    num = numpy.delete(
        numpy.multiply(numpy.array(list(bih_coefs.NUM_0_100[1]) * (sections + 1)).reshape(sections + 1, 3),
                       bih_coefs.NUM_0_100[::2][:, 0].reshape(sections + 1, 1)), sections, 0)
    coff = numpy.concatenate((num, den), axis=1)

    filtered_data = signal.sosfilt(coff, bufferChunk)

    return filtered_data


def convolve(chunk, koef, dbGain):
    gain = 10 ** (dbGain / 20)
    return numpy.convolve(chunk, koef) * gain


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = design.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
