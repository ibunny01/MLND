import gzip

with gzip.open('MNIST_data/train-images-idx3-ubyte.gz') as f:
    file_content = f.read()
    print file_content
