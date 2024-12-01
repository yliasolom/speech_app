import os
import argparse
import whisper
import warnings
from functions.modify_audio import modify_audio
from functions.transcribe_audio import transcribe_audio, save_to_json

warnings.filterwarnings("ignore", category=FutureWarning)


def main():
    parser = argparse.ArgumentParser(description="Модифицировать аудио и перевести в текст.")

    parser.add_argument("--input_audio", type=str, help="Путь к аудиофайлу.")
    parser.add_argument(
        "--output_audio", type=str, default=os.path.join('results', "modified_audio.wav"),
        help="Путь для сохранения измененного аудиофайла."
    )
    parser.add_argument(
        "--speed", type=float, default=1.1, help="Коэффициент скорости воспроизведения (default 1.1)."
    )
    parser.add_argument(
        "--volume", type=int, default=2, help="Изменение громкости в децибелах (default 2)."
    )
    parser.add_argument(
        "--output_transcription", type=str, default=os.path.join('results', "transcription.json"),
        help="Путь для сохранения результата транскрипции."
    )
    parser.add_argument(
        "--modify", action="store_true", help="Включить модификацию аудиофайла."
    )
    parser.add_argument(
        "--transcribe", action="store_true", help="Включить транскрипцию аудиофайла."
    )

    args = parser.parse_args()

    if args.modify:
        print("Изменение аудиофайла:")
        modify_audio(args.input_audio, args.output_audio, speed=args.speed, volume=args.volume)

    if args.transcribe:
        model_path = os.path.join(os.getcwd(), 'models', 'tiny.pt')
        if os.path.exists(model_path):
            model = whisper.load_model(model_path)
        else:
            model = whisper.load_model('tiny')

        print("Транскрибация аудиофайла:")
        result = transcribe_audio(args.input_audio, model)
        save_to_json(result, args.output_transcription)


if __name__ == "__main__":
    main()
