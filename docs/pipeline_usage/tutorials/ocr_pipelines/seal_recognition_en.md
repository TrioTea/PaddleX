[简体中文](seal_recognition.md) | English
  
# Tutorial for Using Seal Text Recognition Pipeline  
  
## 1. Introduction to the Seal Text Recognition Pipeline  
Seal text recognition is a technology that automatically extracts and recognizes seal content from documents or images. The recognition of seal text is part of document processing and has various applications in many scenarios, such as contract comparison, inventory access approval, and invoice reimbursement approval.  
  
![](https://paddle-model-ecology.bj.bcebos.com/paddlex/PaddleX3.0/doc_images/practical_tutorial/PP-ChatOCRv3_doc_seal/01.png)  
  
The **Seal Text Recognition** pipeline includes a layout area analysis module, a seal text detection module, and a text recognition module.  
  
**If you prioritize model accuracy, please choose a model with higher accuracy. If you prioritize inference speed, please choose a model with faster inference. If you prioritize model storage size, please choose a model with a smaller storage footprint.**  
  
<details>  
   <summary> 👉 Detailed Model List </summary>  
  

**Layout Analysis Module Models:**
  
|Model Name|mAP (%)|GPU Inference Time (ms)|CPU Inference Time|Model Size (M)|
|-|-|-|-|-|
|PicoDet-L_layout_3cls|89.3|15.7425|159.771|22.6 M|
|RT-DETR-H_layout_3cls|95.9|114.644|3832.62|470.1M|
|RT-DETR-H_layout_17cls|92.6|115.126|3827.25|470.2M|

**Note: The evaluation set for the above accuracy indicators is a self-built layout area analysis dataset from PaddleX, containing 10,000 images. The GPU inference time for all models above is based on an NVIDIA Tesla T4 machine with a precision type of FP32. The CPU inference speed is based on an Intel(R) Xeon(R) Gold 5117 CPU @ 2.00GHz with 8 threads, and the precision type is also FP32.**


**Seal Text Detection Module Models**:

| Model | Detection Hmean (%) | GPU Inference Time (ms) | CPU Inference Time (ms) | Model Size (M) | Description |
|-------|---------------------|-------------------------|-------------------------|--------------|-------------|
| PP-OCRv4_server_seal_det | 98.21 | 84.341 | 2425.06 | 109 | PP-OCRv4's server-side seal text detection model, featuring higher accuracy, suitable for deployment on better-equipped servers |
| PP-OCRv4_mobile_seal_det | 96.47 | 10.5878 | 131.813 | 4.6 | PP-OCRv4's mobile seal text detection model, offering higher efficiency, suitable for deployment on edge devices |

**Note: The above accuracy metrics are evaluated on a self-built dataset containing 500 circular seal images. GPU inference time is based on an NVIDIA Tesla T4 machine with FP32 precision. CPU inference speed is based on an Intel(R) Xeon(R) Gold 5117 CPU @ 2.00GHz with 8 threads and FP32 precision.**

**Text Recognition Module Models**:


| Model Name | Average Recognition Accuracy (%) | GPU Inference Time (ms) | CPU Inference Time | Model Size (M) |
|-|-|-|-|-|
|PP-OCRv4_mobile_rec |78.20|7.95018|46.7868|10.6 M|
|PP-OCRv4_server_rec |79.20|7.19439|140.179|71.2 M|

**Note: The evaluation set for the above accuracy indicators is a self-built Chinese dataset from PaddleOCR, covering various scenarios such as street scenes, web images, documents, and handwriting. The text recognition subset includes 11,000 images. The GPU inference time for all models above is based on an NVIDIA Tesla T4 machine with a precision type of FP32. The CPU inference speed is based on an Intel(R) Xeon(R) Gold 5117 CPU @ 2.00GHz with 8 threads, and the precision type is also FP32.**

</details>  

## 2.  Quick Start
The pre trained model production line provided by PaddleX can quickly experience the effect. You can experience the effect of the seal text recognition production line online, or use the command line or Python locally to experience the effect of the seal text recognition production line.

### 2.1 Online Experience
You can [experience online](https://aistudio.baidu.com/community/app/182491/webUI) the effect of seal text recognition in the v3 production line for extracting document scene information, using official demo images for recognition, for example:

! []( https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/pipelines/seal_recognition/02.png )

If you are satisfied with the performance of the production line, you can directly integrate and deploy the production line. If you are not satisfied, you can also use private data to fine tune the models in the production line online.

### 2.2 Local Experience
Before using the seal text recognition production line locally, please ensure that you have completed the wheel package installation of PaddleX according to the  [PaddleX Local Installation Guide](../../../installation/installation_en.md).

### 2.3 Command line experience
One command can quickly experience the effect of seal text recognition production line, use [test file](https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/seal_text_det.png), and replace ` --input ` with the local path for prediction

```
paddlex --pipeline seal_recognition --input seal_text_det.png --device gpu:0 --save_path output 
```

Parameter description:

```
--Pipeline: Production line name, here is the seal text recognition production line
--Input: The local path or URL of the input image to be processed
--The GPU serial number used by the device (e.g. GPU: 0 indicates the use of the 0th GPU, GPU: 1,2 indicates the use of the 1st and 2nd GPUs), or the CPU (-- device CPU) can be selected for use
```

When executing the above Python script, the default seal text recognition production line configuration file is loaded. If you need to customize the configuration file, you can execute the following command to obtain it:

<details>
<summary>  👉 Click to expand</summary>

```bash
paddlex --get_pipeline_config seal_recognition
```

After execution, the seal text recognition production line configuration file will be saved in the current path. If you want to customize the save location, you can execute the following command (assuming the custom save location is `./my_path `):

```bash
paddlex --get_pipeline_config seal_recognition --save_path ./my_path --save_path output 
```

After obtaining the production line configuration file, you can replace '-- pipeline' with the configuration file save path to make the configuration file effective. For example, if the configuration file save path is `/ seal_recognition.yaml`， Just need to execute:

```bash
paddlex --pipeline ./seal_recognition.yaml --input seal_text_det.png --save_path output 
```
Among them, parameters such as `--model` and `--device` do not need to be specified and will use the parameters in the configuration file. If the parameters are still specified, the specified parameters will prevail.

</details>

After running, the result obtained is:

<details>
<summary>  👉 Click to expand</summary>

```
{'input_path': 'seal_text_det.png', 'layout_result': {'input_path': 'seal_text_det.png', 'boxes': [{'cls_id': 2, 'label': 'seal', 'score': 0.9813116192817688, 'coordinate': [0, 5.2238655, 639.59766, 637.6985]}]}, 'ocr_result': [{'input_path': PosixPath('/root/.paddlex/temp/tmp19fn93y5.png'), 'dt_polys': [array([[468, 469],
       [472, 469],
       [477, 471],
       [507, 501],
       [509, 505],
       [509, 509],
       [508, 513],
       [506, 514],
       [456, 553],
       [454, 555],
       [391, 581],
       [388, 581],
       [309, 590],
       [306, 590],
       [234, 577],
       [232, 577],
       [172, 548],
       [170, 546],
       [121, 504],
       [118, 501],
       [118, 496],
       [119, 492],
       [121, 490],
       [152, 463],
       [156, 461],
       [160, 461],
       [164, 463],
       [202, 495],
       [252, 518],
       [311, 530],
       [371, 522],
       [425, 501],
       [464, 471]]), array([[442, 439],
       [445, 442],
       [447, 447],
       [449, 490],
       [448, 494],
       [446, 497],
       [440, 499],
       [197, 500],
       [193, 499],
       [190, 496],
       [188, 491],
       [188, 448],
       [189, 444],
       [192, 441],
       [197, 439],
       [438, 438]]), array([[465, 341],
       [470, 344],
       [472, 346],
       [476, 356],
       [476, 419],
       [475, 424],
       [472, 428],
       [467, 431],
       [462, 433],
       [175, 434],
       [170, 433],
       [166, 430],
       [163, 426],
       [161, 420],
       [161, 354],
       [162, 349],
       [165, 345],
       [170, 342],
       [175, 340],
       [460, 340]]), array([[326,  34],
       [481,  85],
       [485,  88],
       [488,  90],
       [584, 220],
       [586, 225],
       [587, 229],
       [589, 378],
       [588, 383],
       [585, 388],
       [581, 391],
       [576, 393],
       [570, 392],
       [507, 373],
       [502, 371],
       [498, 367],
       [496, 359],
       [494, 255],
       [423, 162],
       [322, 129],
       [246, 151],
       [205, 169],
       [144, 252],
       [139, 360],
       [137, 365],
       [134, 369],
       [128, 373],
       [ 66, 391],
       [ 61, 392],
       [ 56, 390],
       [ 51, 387],
       [ 48, 382],
       [ 47, 377],
       [ 49, 230],
       [ 50, 225],
       [ 52, 221],
       [149,  89],
       [153,  86],
       [157,  84],
       [318,  34],
       [322,  33]])], 'dt_scores': [0.9943362380813267, 0.9994290391836306, 0.9945320407374245, 0.9908104427126033], 'rec_text': ['5263647368706', '吗繁物', '发票专用章', '天津君和缘商贸有限公司'], 'rec_score': [0.9921098351478577, 0.997374951839447, 0.9999369382858276, 0.9901710152626038]}]}
```
</details>

![](https://raw.githubusercontent.com/cuicheng01/PaddleX_doc_images/main/images/pipelines/seal_recognition/03.png)

The visualized image not saved by default. You can customize the save path through `--save_path`, and then all results will be saved in the specified path. 


###  2.2 Python Script Integration
A few lines of code can complete the fast inference of the production line. Taking the seal text recognition production line as an example:

```python
from paddlex import create_pipeline

pipeline = create_pipeline(pipeline="seal_recognition")

output = pipeline.predict("seal_text_det.png")
for res in output:
    res.print() 
    res.save_to_img("./output/") # Save the results in img
```

The result obtained is the same as the command line method.

In the above Python script, the following steps were executed:

（1）Instantiate the  production line object using `create_pipeline`: Specific parameter descriptions are as follows:

| Parameter | Description | Type | Default |
|-|-|-|-|
|`pipeline`| The name of the production line or the path to the production line configuration file. If it is the name of the production line, it must be supported by PaddleX. |`str`|None|
|`device`| The device for production line model inference. Supports: "gpu", "cpu". |`str`|`gpu`|
|`use_hpip`| Whether to enable high-performance inference, only available if the production line supports it. |`bool`|`False`|

（2）Invoke the `predict` method of the  production line object for inference prediction: The `predict` method parameter is `x`, which is used to input data to be predicted, supporting multiple input methods, as shown in the following examples:

| Parameter Type | Parameter Description |
|---------------|-----------------------------------------------------------------------------------------------------------|
| Python Var    | Supports directly passing in Python variables, such as numpy.ndarray representing image data. |
| str         | Supports passing in the path of the file to be predicted, such as the local path of an image file: `/root/data/img.jpg`. |
| str           | Supports passing in the URL of the file to be predicted, such as the network URL of an image file: [Example](https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/seal_text_det.png). |
| str           | Supports passing in a local directory, which should contain files to be predicted, such as the local path: `/root/data/`. |
| dict          | Supports passing in a dictionary type, where the key needs to correspond to a specific task, such as "img" for image classification tasks. The value of the dictionary supports the above types of data, for example: `{"img": "/root/data1"}`. |
| list          | Supports passing in a list, where the list elements need to be of the above types of data, such as `[numpy.ndarray, numpy.ndarray], ["/root/data/img1.jpg", "/root/data/img2.jpg"], ["/root/data1", "/root/data2"], [{"img": "/root/data1"}, {"img": "/root/data2/img.jpg"}]`. |

（3）Obtain the prediction results by calling the `predict` method: The `predict` method is a `generator`, so prediction results need to be obtained through iteration. The `predict` method predicts data in batches, so the prediction results are in the form of a list.

（4）Process the prediction results: The prediction result for each sample is of `dict` type and supports printing or saving to files, with the supported file types depending on the specific pipeline. For example:

| Method | Description | Method Parameters |
|--------|-------------|-------------------|
| save_to_img | Save the results as an img format file | `- save_path`: str, the path to save the file. When it's a directory, the saved file name will be consistent with the input file type; |

Where `save_to_img` can save visualization results (including OCR result images, layout analysis result images).

If you have a configuration file, you can customize the configurations of the seal recognition  pipeline by simply modifying the `pipeline` parameter in the `create_pipeline` method to the path of the pipeline configuration file.

For example, if your configuration file is saved in `/ my_path/seal_recognition.yaml` ， Then only need to execute:


```python
from paddlex import create_pipeline
pipeline = create_pipeline(pipeline="./my_path/seal_recognition.yaml")
output = pipeline.predict("seal_text_det.png")
for res in output:
    res.print() ## 打印预测的结构化输出
    res.save_to_img("./output/") ## 保存可视化结果
```

## 3. Development integration/deployment
If the production line can meet your requirements for inference speed and accuracy, you can directly develop integration/deployment.

If you need to directly apply the production line to your Python project, you can refer to the example code in [2.2.2 Python scripting] (# 222 python scripting integration).

In addition, PaddleX also offers three other deployment methods, detailed as follows:

🚀 ** High performance deployment: In actual production environments, many applications have strict standards for the performance indicators of deployment strategies, especially response speed, to ensure efficient system operation and smooth user experience. To this end, PaddleX provides a high-performance inference plugin aimed at deep performance optimization of model inference and pre-processing, achieving significant acceleration of end-to-end processes. For a detailed high-performance deployment process, please refer to the [PaddleX High Performance Deployment Guide] (../../../pipelin_deploy/high_performance_deploy. md).

☁️ ** Service deployment * *: Service deployment is a common form of deployment in actual production environments. By encapsulating inference functions as services, clients can access these services through network requests to obtain inference results. PaddleX supports users to achieve service-oriented deployment of production lines at low cost. For detailed service-oriented deployment processes, please refer to the PaddleX Service Deployment Guide (../../../ipeline_deploy/service_deploy. md).

Here are API references and examples of calling multilingual services:



## 4.  Secondary development
If the default model weights provided by the seal text recognition production line are not satisfactory in terms of accuracy or speed in your scenario, you can try using your own specific domain or application scenario data to further fine tune the existing model to improve the recognition performance of the seal text recognition production line in your scenario.

### 4.1 Model fine-tuning
Due to the fact that the seal text recognition production line consists of three modules, the performance of the model production line may not be as expected due to any of these modules.

You can analyze images with poor recognition performance and refer to the following rules for analysis and model fine-tuning:

* If the seal area is incorrectly located within the overall layout, the layout detection module may be insufficient. You need to refer to the [Customization](../../../module_usage/tutorials/ocr_modules/layout_detection_en.md#customization) section in the [Layout Detection Module Development Tutorial](../../../module_usage/tutorials/ocr_modules/layout_detection_en.md) and use your private dataset to fine-tune the layout detection model.
* If there is a significant amount of text that has not been detected (i.e. text miss detection phenomenon), it may be due to the shortcomings of the text detection model. You need to refer to the [Secondary Development](../../../module_usage/tutorials/ocr_modules/seal_text_detection_en.md#customization) section in the [Seal Text Detection Module Development Tutorial](../../../module_usage/tutorials/ocr_modules/seal_text_detection_en.md) to fine tune the text detection model using your private dataset.
* If seal texts are undetected (i.e., text miss detection), the text detection model may be insufficient. You need to refer to the [Customization](../../../module_usage/tutorials/ocr_modules/text_recognition_en.md#customization) section in the [Text Detection Module Development Tutorial](../../../module_usage/tutorials/ocr_modules/text_recognition_en.md) and use your private dataset to fine-tune the text detection model.

* If many detected texts contain recognition errors (i.e., the recognized text content does not match the actual text content), the text recognition model requires further improvement. You need to refer to the [Customization](../../../module_usage/tutorials/ocr_modules/text_recognition_en.md#customization) section.

### 4.2 Model Application
After completing fine-tuning training using a private dataset, you can obtain a local model weight file.

If you need to use the fine tuned model weights, simply modify the production line configuration file and replace the local path of the fine tuned model weights with the corresponding position in the production line configuration file

```python
......
 Pipeline:
  layout_model: RT-DETR-H_layout_3cls #can be modified to the local path of the fine tuned model
  text_det_model: PP-OCRv4_server_seal_det  #can be modified to the local path of the fine tuned model
  text_rec_model: PP-OCRv4_server_rec #can be modified to the local path of the fine tuned model
  layout_batch_size: 1
  text_rec_batch_size: 1
  device: "gpu:0"
......
```
Subsequently, refer to the command line or Python script in the local experience to load the modified production line configuration file.

##  5.  Multiple hardware support
PaddleX supports various mainstream hardware devices such as Nvidia GPU, Kunlun Core XPU, Ascend NPU, and Cambrian MLU, and can seamlessly switch between different hardware devices by simply modifying the **`--device`** parameter.

For example, if you use Nvidia GPU for inference on a seal text recognition production line, the Python command you use is:

```
paddlex --pipeline seal_recognition --input seal_text_det.png --device gpu:0 --save_path output
```

At this point, if you want to switch the hardware to Ascend NPU, simply modify the ` --device ` in the Python command to NPU:

```
paddlex --pipeline seal_recognition --input seal_text_det.png --device npu:0 --save_path output
```

If you want to use the seal text recognition production line on a wider range of hardware, please refer to the [PaddleX Multi Hardware Usage Guide](../../../other_devices_support/installation_other_devices_en.md)。







