import os
import whisper
import json

import warnings
warnings.filterwarnings("ignore", category=FutureWarning)


def transcribe_audio(file_path, model):
    """
    Транскрибиоует аудиофайл с помощью модели Whisper.

    https://github.com/openai/whisper

    :param file_path: Путь к входному аудиофайлу для расшифровки.
    :param model: Загруженная модель Whisper для распознавания речи.
    :return: Словарь с транкрибированным текстом.
    """
    audio = whisper.load_audio(file_path)
    audio = whisper.pad_or_trim(audio)

    # log-Mel spectrogram
    mel = whisper.log_mel_spectrogram(audio, n_mels=model.dims.n_mels).to(model.device)

    _, probs = model.detect_language(mel)
    print(f"Детектированный язык: {max(probs, key=probs.get)}")

    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)
    print(f"Результат расшифровки: {result.text}")

    return {"text": result.text}


def save_to_json(result, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
        print('Результат транскрипции сохранен в {}'.format(output_file))
