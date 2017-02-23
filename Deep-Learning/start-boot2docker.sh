#!/usr/bin/env bash

function install_tensorflow()
{
    # install Docker for Mac
    brew cask install docker

    docker run --name tensorflow-udacity -it -p 8888:8888 gcr.io/tensorflow/tensorflow
    # nvidia-docker run -it -p 8888:8888 gcr.io/tensorflow/tensorflow:latest-gpu
}

function startup_noMNIST()
{
    docker run -p 8888:8888 -it --memory=8g --rm b.gcr.io/tensorflow-udacity/assignments:0.3.0
}
