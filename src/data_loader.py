#!pip install roboflow

from roboflow import Roboflow
rf = Roboflow(api_key="DsOms9paR2rcumZ9jh3E")
project = rf.workspace("robotdog-5oy4l").project("my-first-project-vluen")
version = project.version(4)
dataset = version.download("yolov8")
                