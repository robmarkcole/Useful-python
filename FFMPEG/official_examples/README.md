* Examples -> https://github.com/kkroening/ffmpeg-python/tree/master/examples
* `facetime.py` -> captures video from mac webcam and records to .mp4 file

## tensorflow_stream.py
* https://github.com/kkroening/ffmpeg-python/blob/master/examples/README.md#tensorflow-streaming
* `python3 tensorflow_stream.py in_robin.mp4 out.mp4 --dream` -> takes some time to run..!

Demonstrates using ffmpeg to decode video input, process the frames in
python, and then encode video output using ffmpeg.

This example uses two ffmpeg processes - one to decode the input video
and one to encode an output video - while the raw frame processing is
done in python with numpy.

At a high level, the signal graph looks like this:

  (input video) -> [ffmpeg process 1] -> [python] -> [ffmpeg process 2] -> (output video)

This example reads/writes video files on the local filesystem, but the
same pattern can be used for other kinds of input/output (e.g. webcam,
rtmp, etc.).

The simplest processing example simply darkens each frame by
multiplying the frame's numpy array by a constant value; see
``process_frame_simple``.

A more sophisticated example processes each frame with tensorflow using
the "deep dream" tensorflow tutorial; activate this mode by calling
the script with the optional `--dream` argument.  (Make sure tensorflow
is installed before running)