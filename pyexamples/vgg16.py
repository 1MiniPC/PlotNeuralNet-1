import sys
sys.path.append('../')
from pycore.tikzeng import *
print(to_cor())
# Definición de la arquitectura VGG16
arch = [
    to_head( '..' ),
    to_cor(),
    to_begin(),
    to_input('fish.png',to='(-4.2,0,0)', width=10, height=10, name="input"),  # Reemplazar con la ruta de tu imagen
    to_ConvConvRelu(name="conv1_1", s_filer=256, n_filer=(64,64), offset="(0,0,0)", to="(0,0,0)", width=(2,2), height=40, depth=40, caption="Conv 1"),
    to_Pool(name="pool1", offset="(0,0,0)", to="(conv1_1-east)", width=1, height=20, depth=20, opacity=0.5),

    to_ConvConvRelu(name='conv2_1', s_filer=128, n_filer=(128,128), offset="(2,0,0)", to="(pool1-east)", width=(3,3), height=30, depth=30, caption="Conv 2"),
    to_Pool(name="pool2", offset="(0,0,0)", to="(conv2_1-east)", width=1, height=16, depth=16, opacity=0.5),

    to_connection( "pool1", "conv2_1"),

    to_ConvConvConvRelu(name='conv3_1', s_filer=64, n_filer=(256,256,256), offset="(2,0,0)", to="(pool2-east)", width=(4,4,4), height=25, depth=25, caption="Conv 3"),
    to_Pool(name="pool3", offset="(0,0,0)", to="(conv3_1-east)", width=1, height=12, depth=12, opacity=0.5),

    to_connection( "pool2", "conv3_1"),

    to_ConvConvConvRelu(name='conv4_1', s_filer=32, n_filer=(512,512,512), offset="(2,0,0)", to="(pool3-east)", width=(6,6,6), height=20, depth=20, caption="Conv 4"),
    to_Pool(name="pool4", offset="(0,0,0)", to="(conv4_1-east)", width=1, height=8, depth=8, opacity=0.5),

    to_connection( "pool3", "conv4_1"),

    to_ConvConvConvRelu(name='conv5_1', s_filer=16, n_filer=(512,512,512), offset="(2,0,0)", to="(pool4-east)", width=(5,5,5), height=15, depth=15, caption="Conv 5"),
    to_Pool(name="pool5", offset="(0,0,0)", to="(conv5_1-east)", width=1, height=6, depth=6, opacity=0.5),

    to_connection( "pool4", "conv5_1"),

    to_FullyConnected(name='fc6', s_filer=512, n_filer=1, offset="(2,0,0)", to="(pool5-east)", width=2, height=2, depth=40, caption="FC 1"),
    to_connection( "pool5", "fc6"),
    to_SoftMax(name='soft1', s_filer=4, offset="(2,0,0)", to="(fc6-east)", width=2, height=2, depth=10, caption="SoftMax"),
    to_connection( "fc6", "soft1"),

    to_end()
]

def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex' )

if __name__ == '__main__':
    main()
