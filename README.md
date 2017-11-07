# Ultimecia - A video art playground

In this repo I will push some of the outcomes of me playing around with video. The target won't be so much video compressing itself, as trying to get a better understanding of how image is expressed in computer science, and how we as humans can win a new artistic perspective on video through CS.

For manipulating video we will primarily use scikit-video and ffmpeg.

## How to cut a video

When experimenting with different techniques and parameters, it's a good idea to get a small sample of a larger video. If you are interested in a particular part of a video, you can cut it using ffmpeg. For example:

```
ffmpeg -i "foo.mkv" -codec copy -ss 0:15:00 -t 0:03:00 out.mkv
```

The previous command would get 3 minutes of the video "foo.mkv", starting from 0:15:00 (therefore, from 0:15:00 to 0:18:00) and will save the output at out.mkv
