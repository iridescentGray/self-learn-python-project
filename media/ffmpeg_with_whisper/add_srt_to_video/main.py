from datetime import timedelta
import os
import whisperx
import subprocess


def transcribe_video(input_video):
    batch_size = 32
    compute_type = "float32"
    device = "cpu"

    model = whisperx.load_model("large-v2", device=device, compute_type=compute_type)

    audio = whisperx.load_audio(input_video)
    result = model.transcribe(audio, batch_size=batch_size, language="en")

    model_a, metadata = whisperx.load_align_model(
        language_code=result["language"], device=device
    )
    result = whisperx.align(
        result["segments"],
        model_a,
        metadata,
        audio,
        device,
        return_char_alignments=False,
    )

    segments = result["segments"]

    # if srt file exists, delete it
    if os.path.exists("subtitles.srt"):
        os.remove("subtitles.srt")
    for index, segment in enumerate(segments):
        startTime = str(0) + str(timedelta(seconds=int(segment["start"]))) + ",000"
        endTime = str(0) + str(timedelta(seconds=int(segment["end"]))) + ",000"
        text = segment["text"]
        print(text)
        segment = f"{index + 1}\n{startTime} --> {endTime}\n{text[1:] if text[0] == ' ' else text}\n\n"

        srtFilename = os.path.join(f"subtitles.srt")
        with open(srtFilename, "a", encoding="utf-8") as srtFile:
            srtFile.write(segment)

    return srtFilename


def add_srt_to_video(input_video, output_file):

    # FFmpeg command
    subtitles_file = "subtitles.srt"

    # FFmpeg command
    ffmpeg_command = f"""ffmpeg -i {input_video} -vf "subtitles={subtitles_file}:force_style='FontName=Arial,FontSize=10,PrimaryColour=&HFFFFFF,OutlineColour=&H000000,BorderStyle=3,Outline=1,Shadow=1,Alignment=2,MarginV=10'" -c:a copy {output_file} -y """

    # Run the FFmpeg command
    subprocess.run(ffmpeg_command, shell=True)


def main():
    input_video_path = "input.mp4"
    output_file = "output.mp4"
    transcribe_video(input_video_path)
    add_srt_to_video(input_video_path, output_file)


main()
