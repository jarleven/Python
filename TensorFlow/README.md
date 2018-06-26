run -it -p 8888:8888 tensorflow/tensorflow


Inspiration from here : https://www.youtube.com/watch?v=QfNvhPx5Px8


https://www.reddit.com/r/MachineLearning/comments/4f1gjk/how_do_i_run_the_tensorflow_docker_image_without/
How do I run the tensorflow docker image without jupyter notebook?!?!
If you want, for example, to run a bash shell just put /bin/bash at the end of your docker run command, e.g.:

docker run -it gcr.io/tensorflow/tensorflow /bin/bash
