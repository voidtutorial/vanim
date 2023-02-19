inotifywait -e close_write -m . |
while read -r directory events filename; do
  if [ "$filename" = "main.py" ]; then
        manim -ql main.py
	vlc --play-and-exit $(pwd)/media/videos/main/480p15/BufferOverflow.mp4
  fi
done
