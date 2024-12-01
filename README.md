# Audio Modification and Transcription Tool

Инструмент позволяет модифицировать аудиофайлы (скорости и громкости) и транскрибировать их в текст с помощью модели Whisper от OpenAI.

## Установка:

1. Клонировать репозиторий:

    ```bash
    git clone https://your-repository-url.git](https://github.com/yliasolom/speech_app.git
    cd speech_app
    ```

2. Установить проект с `setup.py`:

    ```bash
    pip install .
    ```

    Это установит все зависимости, указанные в `setup.py`.

## Аргументы:

### `--modify`
Флаг для включения модификации аудиофайла (изменение скорости и громкости).

### `--transcribe`
Флаг для выполнения транскрипции аудиофайла в текст.

Если оба флага не указаны, программа не выполнит никаких операций.

### `--input_audio`
Путь к входному аудиофайлу `.wav`. Этот аргумент обязателен для обоих режимов (модификация и транскрипция).

### `--output_audio`
Путь для сохранения измененного аудиофайла. По умолчанию сохраняется в директории `results` с именем `modified_audio.wav`.

### `--speed`
Коэффициент скорости воспроизведения. По умолчанию равен `1.1`. Если значение меньше 1, файл будет воспроизводиться медленнее, если больше — быстрее.

### `--volume`
Уровень изменения громкости в децибелах. По умолчанию равен `2`.

### `--output_transcription`
Путь для сохранения результата транскрипции. По умолчанию сохраняется в директории `results` с именем `transcription.json`.

## Пример использования:

1. **Модификация аудиофайла** (изменение скорости и громкости):

    ```bash
    python main.py --modify --input_audio examples/test_ru.wav --speed 2 --volume 2
    ```
   
   Это выполнит изменение аудиофайла и сохранит результат в файл `results/modified_audio.wav`.


2. **Транскрипция аудиофайла в текст**:

    ```bash
    python main.py --transcribe --input_audio  examples/test_ru.wav 
    ```

    Это выполнит транскрипцию аудиофайла и сохранит результат в файл `results/transcription.json`.

3. **Одновременная модификация и транскрипция**:

    ```bash
    python main.py --modify --transcribe --input_audio examples/test_ru.wav --speed 1.2 --volume 3 
    ```

    Это выполнит как модификацию аудиофайла (с изменением скорости и громкости), так и транскрипцию аудиофайла в текст.
