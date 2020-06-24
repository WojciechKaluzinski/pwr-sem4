import settings
import zlib


def count_crc(series):  # funkcja, która oblicza crc za pomocą biblioteki zlib
    my_crc = "{0:b}".format(zlib.crc32(series.encode()))
    shortage = settings.CRC - len(my_crc)
    return '0' * shortage + my_crc


def stuffing(series):  # funkcja, która przygotowuje format wiadomości do wysłania
    result = ""
    count = 0  # licznik jedynek
    for x in series:
        if x == '1':
            count += 1
            result += x
            if count == settings.TRESHOLD:  # uzupełnianie 0 co pięć jedynek
                result += '0'
                count = 0
        else:
            count = 0
            result += x
    return result


def de_stuffing(series):  # funkcja, która przygotowuje format wiadomości do zdekodowania
    result = ""
    counter = 0
    for x in series:
        if x == '1':
            counter += 1
            result += x
        else:
            if counter < settings.TRESHOLD:
                result += x
            counter = 0
    return result


def set_markers(series):  # funkcja, która dodaje znaczniki początku i końca wiadomości
    return settings.START_MARKER + series + settings.END_MARKER


def remove_markers(series):  # funkcja, która usuwa znaczniki początku i końca wiadomości
    return series[len(settings.START_MARKER):(len(series) - len(settings.END_MARKER))]


def enc_frame(series):  # funkcja kodująca ramke
    return set_markers(stuffing(series + count_crc(series)))


def dec_frame(series):  # funkcja dekodująca ramkę
    dec_data = de_stuffing(remove_markers(series))
    info = dec_data[:len(dec_data) - settings.CRC]
    crc = dec_data[len(dec_data) - settings.CRC:]

    if count_crc(info) == crc:
        return info
    else:
        print("coś poszło nie tak")
        return ""
