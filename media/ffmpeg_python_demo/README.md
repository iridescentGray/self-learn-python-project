# ffmpeg-python

Python bindings for FFmpeg - with complex filtering support

## Related documents

    github: https://github.com/kkroening/ffmpeg-python

## tips

### speed

    想要加速,试试ffmpeg 不重编码直接复制流。不过因为 I/P/B 帧类型的问题，不重编码切的时间点没那么精确。
    ffmpeg -i input.mp4 -ss 00:01:30 -to 00:21:40 -c copy output.mp4
