from pydub import AudioSegment


def modify_audio(file_path, output_file, speed=1, volume=1):
    """
    Модифицирует аудиофайл, изменяя скорость и громкость.

    :param speed: Коэффициент скорости (по умолчанию 1.0 - без изменений).
    :param volume: Уровень громкости (в децибелах, по умолчанию 0).
    :return: cохраняет измененный аудиофайл.
    """
    audio = AudioSegment.from_wav(file_path)

    # изменение скорости
    print(f"Исходная длительность: {audio.duration_seconds:.2f} секунд")
    modified_audio = audio._spawn(audio.raw_data, overrides={"frame_rate": int(audio.frame_rate * speed)})
    print(f"Измененная длительность: {modified_audio.duration_seconds:.2f} секунд")

    # изменение громкости
    print(f"Исходная громкость (dBFS): {audio.dBFS}")
    modified_volume = modified_audio + volume
    print(f"Измененная громкость (dBFS): {modified_volume.dBFS}")

    modified_volume.export(output_file, format="wav")
    print(f"Измененный аудиофайл сохранен в {output_file}")
