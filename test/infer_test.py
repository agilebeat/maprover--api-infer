try:
  import unzip_requirements
except ImportError:
  pass


import json
import boto3 


import tensorflow as tf
from tensorflow.python.platform import gfile
#from tensorflow.python.keras.preprocessing import image
from PIL import Image

import numpy as np
import base64
import io

atile_b64 = "iVBORw0KGgoAAAANSUhEUgAAAQAAAAEACAMAAABrrFhUAAAAz1BMVEVWVlZlZWVpaWl2dnZ5eXl-fn6AgICTk5OkpKTDtqq4uLjGua7Iuq_JvbPNwrjQvbzGxsbRxr3Ix8bJyMfJycnUxMPTycDMy8nUysLOzcrWzMPXyMbWzcXXycjOzs7YzMfQz83azMrZ0MnS0tLU09DW1dLV1dXd0tHY19PZ19Tf1NLf1dXZ2dnc2tbh1tXi29Xh2dnf3dnk29jg3tre3t7j3Nzl3drl3t3l4dzi4uLp497n4uLn5eDm5ubq5uPu6uTu7u7y7-ny8vL29vb___8VavDyAAAPPUlEQVR4nOVda2ObxhLdNL2tkzS9qh5RXce6UmXLSSM78SOxFRsBlv7_b7qgBwww-2AYGNTMF9uSQpijPcvOOcOiQmq8f_XH3_-CUGQAwuXb395Ln371qABAGH5-9bv0-VeOSgDEPHgnnUHFqAjA4fOgKgAHz4PqAIThX4fMAw4AIh68PVgesABwyDxgAiD0_zxQHnABEIZPh8kDPgAOlAecAIT-u1d_SidUNlgBCMPvb9_-TzqlcsEMQBj-c2A8YAfg0HjAD0DEg98OiAd1ABDz4GDEknoACP0_DoUHNQGw4cFBrItqA-BQeFAjABEP3rSfB3UCEPHgzVvpBG1RLwBheNF2HtQNQMyDv6STNEXtAIThw5s2r4saAKDdPGgEgND_vbU8aAaADQ-kU8WjKQDC8O928qA5AFrKgwYBCMNvb9onljQKQBt50DAAMQ_aVSQ2DUDEg3aJhs0D0DIeSAAQ8aA9TQUiALSJB-pKBoHWNJmpr4OlDALLdvBABcHkRAaBdpipEQCBN_iBeRADEARfxHgg3mS2BSAITk9lEBDnwR6AiAefhSCQbTJLAAiCq4Evg4BokxkAIOLBRAYBSR5kAAgeB99kEJBrMssCEASffjQe5AEIgpOJDAJCPCgC8IPxAAEgCC6keCDQZIYCEPHgQgaB5nmgASDiwb0MAv67ZnmgA0CSB402mekBCIKBFA-abK4xARDcDx5kEGiw2dIIQMwDGQSa44EFgMAf_CMEQUM8sAEQ8-C7DALNNJnZARAUDZtotnQBQFA0rL-5xgmAIBATz2vngSMAEQ-kRMOam8ycARDkQa1mqjsAguJ5nc2WZQAQFM_razIrB0CwHNwIQVAXD0oCICga1tRkVhoAQdHwWx08IAAgJxrWwQN1R0BAlAfMi2M1G3oUCAR5wCsaqnXQm1EQ-LfwQK3X67sOiQdioiFrk1kMwHo1PSbxQEw0ZGwy2wCwXgddIg-ExHM-HuwAiHmwoEBw8DxIAFivRiMKAnI8uGHhQQpAxIPOnIKAmGjIspMZBGC9nndJPJhIiecMTWZZANar4ykFATnxvLKZmgNgvfZoi4J7KbGkKg-Ul0dgPe-RFgVi4nk1Hqjp8SqPwHOfxAM50bAKD1Sw6M4Lg2BB44GYaFih2VJF5z3vFHiwmvVpPJgIIUBuMlOb8x6NEB6QFsfLQ-PBFoAgGvMHzwNak5nan_esGxR4QCwSxcRzyo5-CQCBdzwt8IAolsiJ5-V5oMB53yE8IBaJcqJh2SYzlTnvWa_Ig_HosETDks01WQACbzgr8oBWJD6K8aDUjn4qf97RmC_ygFYkSvLAuamgAEDEg_5zgQejMQWBQ-ABAkDg9WeFQeBReSDUaejMAwyAmAdsRaKcaOjWXIMDEATTYYEHz0NSkSgnGjo1mekACDykSCSKJZI8sIrnWgDQInFNLBIvTlrLAwMAQTBmKxIFeWBpKjACwFkkyonn5mZLMwAxD4qLY6KjLiYaGpvMbAAE3mjMVSTKieeGJjMrADgPiIvj-8GTEARaM9UBAI1YQisS5XigaTJzAgAXS7qkxbGcaIjzwA0ATZFIE0vkxHOMB64AaIpEmqMuJp4jPHAHIC4SCzwgFolyPCg0mZUAAOfBvEfkgdDiOM-DUgCgRSLRURflwXsyAIHXYysSPTHREDaZlQUALxKJYomYaAh4UB6AiAdsjrrcti1JkxkFAE5HXU483zWZkQDQFIk0sUSOB5udzIgAcDrqcuJ53FxDBoBTLJHrPP_8ig5AxAO-IlFMPA-rAKBx1EmLYzHRsBIArI66kHheEQCdo046lIh4XhkAtEgkOuoSPKgOAKuj3rx4zgEAq6PetGjIAwCno96weM4EAKuj3igP2ACIxZLi4pjoqDe4XQUjAJyOenOiIScAWbFktRsPxCKxKfGcFwBYJPZfdHY8IBaJzfBA8eYPi8T5y18W24FALBIbuQNDMecfwCLx9Yuj1dFRTIcpzVFvQDxXzNnHkTrqwa8_KbVZJhId9fpFQ8Wb-y5SHrxU6j-7xTGtSKxbPFfMqe9j56h3VRSvd5cFolhSr2iomBNPYi-WPC9m0_2Vkeio18oDxZs2DMYisUbRUDFnnQlGR702HijelHPBWCTWJZ4r3owLgRWJxD1L6uGBYk64GIijvp4ekw5Vh3iueLPFgtFRr0E0VLzJ4oG2XdPEkkdusUQx56oJtO2aJpYwi-eKN1FtMDrqvDxQvHkagtFR5xQNFXOahlgMC2NgHVDFEjbxXPEmaYpe8XJI54HHJZ4r5iz1cVdcFG55QLxH_SsPDxRzmvro4Pmv6Y46Cw8Ub5b6mBVLwzSIYgmHeK6Y89SF14ffePF6QCwSq4vnijdPbQxBzr0Fo6NeteNW8eapi7tpmupipmm7poklFcVzxZypJjrpN77qbF6Z8jnqlcRzxZekIeagk2i2u-57PT6xpIJoqPiy1IfXTXN87icvMzrqdPFccSVpihGYATMWEaOjThUNFUuG5liMwCDPpscpltB4oBgStEUXfM2d_JuM96iTRENVOT1rzMGXPEcmOca2awIPVLXkXAIUAasu9oFFl63turx4rqqk5hRTMMRHmqXOHFkcEx31sjxQFVJzCg_IIIF2we-NsHtzaTwoJ54ramKuARd8XcN3it6jTisSgzJiiaKl5RxQBrkzL_MYNzIrIRoqyvFLRLEI0Ic3ZLtH3V08V6TDg_iv8SuCMsjUPq8zOuq-o3iuKAcHMfBPJvp3vR74Lp38QEZH3U00VKRjJ3EfwbwcfNG9DYsAx9Udp6PuIhoq0pGT2O6qfjXAk1vkZBC3QItE0wVEHw7iuaIcN4mL_W0-OA86piLAENg96sQi0fqgREU67D7SbfUxHmAyiFtwFomWjltFOuguMkuuq8Ey9zYoAp57JQ_NWCSaxXNFOeQu7nMXmkmWByOQAsH8YXTUTeK5oi21NlF4rkSGBwYZxC04HXX9Xs-KWnKAGRDngVEGcQtGR10rnityyeHjDxbZ8-DOIoO4BSKWUB31K7xIjB-xQVtq6YrOHQ-gDEIcAHEw3qOOi4bbZ4wQfKn8DJjjgYsM4haoWEJz1LHtKvYPWSntSxmfrDM5hV4obSmfBCqWEB31omiYPGWmpC81MRcaXbCUo1kdMBg3MiuIhuAxO2VKDs0MuI9bKINQrzIwGIvEnGiYec6Quy9lebRUGRnELTjvUc_wIPugpWfHbbHuzUXWB3IRYAhGRx3yIP-kKbeSwzwAfNwLrRyMjnr6oMTCo7ZcmngtM-Ax7AY5IZ0gHpyO-l48V4SSwzMLLQ_j9FiLc4NeRAhGR33XcasISy3LDJgpAny9XkQLRkd9I54rfDsgU8lhmQEvAaDz681Lp6fEbLFYMIolFycbPQDbO9ngz1pmQFgE9HYv8vKAUSzxB2rzswwPJua9kcdQBkk_-pmVB4yOutr9xHwp1J-1zIBPwAv1xvAdXh6wOepq_4vrg6YsMyBsCe9kCw9mHjAViSr9FS85cqh-NXclXsMi4DL_Luv1gMlRV_CPWd-Kqq0IAP-yg7zPywMOR11l_kJLDujPTsw2wzn0QtG90XxWHjA46ir3t7n0XppnwCWUQY41H7ph5UFlR10VXjGV3hYCwJbwrt6fn3DyoKqjroovYf7stvT-Yp4BH6AX-sHwQX9wxQZAVbFEYS-idzxHqJaRQcwfvSn4aBWikqOOAoD7s6OOuQr-CGWQWzMA7DwgO-oaADT-bOHKDiIjgwxt-XPzgOyo6wDQ7CHe1RcCY9gN4nQnDy8PiEWiHgB0D_HV8Ewzuz9BL_TMJf-QmQe0ItEEgKb0vkZzycsgbuEPPvEhQHLUjQDo9tJHBvgl9EJxiPBgXRcRHHULAHjpXeRBRgbplsg_ZOdBSUfdCgBacnid3GXuDHqhZZ8mxcuDko66HQAU1fVsCHmwhC3hY22m2uDlQSmZ1wUAjWh4niYAZRBDEWCICad_UEYscQIgOL1FUd0XvLdGGcQtWHlQwlF3AsA7jRa6CKp7HpQoAgxxM3jkg8DZUXcCYFME-ahoGBd9dhnEMVh54FgkugDwZddY8oDzYJlpCa-QPzcPnBx1FwDSKvgDNrt0ShcBhqidB3lH3QGAUzCtL-HT6aezRTzKwEhbnOtTcw1WHtgddTsAy0nm_G5TVF_H-2X24bHpMyAIXh7YHHU7AAUZ6DxB9WelfoZHtssgbsHMA6OjbgXgU7G1LuHBnVI__ZqOsec-T_4hc31gdNStAKA64J4HR0eroxev90cdMu4GzsoDk6NuA-AUX9j6ZxsebPbN_uXl7vCjMec-b6w80IslFgAeJ7rzW6aodl7096gS18F4sPIAFIn7fe83jroFAJMQfp2gukqOPe9xPlmZlwfJMi7Z9z4uEs0AIDMgPL-z4v5wq2OdaEgKXh7se4HSfe9XUzMAFifkAdsfTScaEoOTB2mRmOx7vzYCoJkBk-gWLi87HnA-HKIeHiT73psA0M-A27gtXlx2s4tWPCfFN04eJI76y-0qzgSAhQBQBjgkHmwd9f2-9wYAPln2ooANgYho2F4e7IrE7b73BgCsAwB-4ZglwVAapsF6PQBiiR4A2w4EH0Ct3fUf0L41puJoG5x1cuqoawGwzYDQCtl0Q3zEOm6HnJMhMw88MwA2ApyDxfVWBkBFw76pU6R0sPJg66jrALDNgD4QAhMlXCMackLAyoO4nNEBYBsAoBsA6kCoaHjcWh5ERaIGANsMCL2wjBm8xPrWeh8ZEeBdF41xAGwzILwrJi8E3qKWRGt5gANgIwBsB5kVcjtHpNhxW3mAAnBh24-sD7ywXvHtjHi-50GXVSxh4wEKgG0AwDIY7wZAeWDosCIEEw8wAKy7UIEqSOuFYTzgFQ15eIAAYJ0Br0EZrFeCl6gl0ToeIADYCJAZAKZ2kOuSnYaEqM6DIgDWGRCWwT3jmPbPjos8OG4XD4oA2AcAGNK2ivcJfRAtq1hSkQcFAKz7UX4E87tDR-Qlas21hwd5AB5tu_DBnmjjTQHJP8D6N3lFwyo8yANgJcBZoQy2Rgt5cHVyjwNwcW_5n3zQD-DeEHaJdRqyioYleOCdnJw-hBcDHwPAOgA0ZbAtUB70XZvK3f6LwYUbAPsct1sAZgGwrgEzZXApxe8JFUtYRUM3HqSX-e_xLXwZAAybI-0CXNfL9kSHl6ho2DQPMvc-Xw28_wOdOCXrBLEiywAAAABJRU5ErkJggg=="
    
def run_classify_image(img):
    
    f = gfile.FastGFile("../tf-models/tf_model.pb", 'rb')
    graph_def = tf.GraphDef()
   # Parses a serialized binary message into the current message.
    graph_def.ParseFromString(f.read())
    f.close()

    sess = tf.Graph()
    with sess.as_default() as graph:
        tf.import_graph_def(graph_def)
        softmax_tensor = sess.get_tensor_by_name('import/activation_8_1/Softmax:0')

    with tf.Session(graph=graph) as sess:
        predictions = sess.run(softmax_tensor, {'import/conv2d_1_input_1:0': img})
         
    return predictions    
        

def printTensors():

    # read pb into graph_def
    with tf.gfile.GFile("../tf-models/tf_model.pb", "rb") as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())

    # import graph_def
    with tf.Graph().as_default() as graph:
        tf.import_graph_def(graph_def)

    # print operations
    for op in graph.get_operations():
        print(op.name)


def infer():
    tile_base64 = atile_b64 
    

    img = base64.urlsafe_b64decode(tile_base64)
    img = io.BytesIO(img)
    img = Image.open(img)

    rgb_im = img.convert('RGB')
    img = np.asarray(rgb_im)/255.
    img = np.expand_dims(img, axis=0)

    predictions = run_classify_image(img)


    if predictions[0][0] > predictions[0][1]:
        dic = False
    else:
        dic = True

    response = {
        "statusCode": 200,
        "headers": {'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*'},
        "body": json.dumps({'RailClass': dic})
    }
    
    return response


if __name__== "__main__":
    infer()
    #printTensors()









