#include <iostream>

int main(int argc, char *argv[])
{
    // this is convolution vector : Gaussian Blur
    // url: https://en.wikipedia.org/wiki/Kernel_(image_processing)
    float conv_mat[3][3] = {
        { 1, 2, 1 },
        { 2, 4, 2 },
        {1, 2, 1} };

    // implementation 1
    for (int sub_j = 0; sub_j < 3; sub_j++)
        for (int sub_i = 0; sub_i < 3; sub_i++)
        {
            conv_mat[sub_i][sub_j] /= 16.0f;
        }

    // implementation 2
    for (int sub = 0; sub < 9; sub++)
        (&conv_mat[0][0])[sub] = 16.0f;


    return 0;
}
