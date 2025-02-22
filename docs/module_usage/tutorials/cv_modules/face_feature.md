---
comments: true
---

# 人脸特征模块使用教程

## 一、概述
人脸特征模块通常以经过检测提取和关键点矫正处理的标准化人脸图像作为输入，从这些图像中提取具有高度辨识性的人脸特征，以便供后续模块使用，如人脸匹配和验证等任务。

## 二、支持模型列表

<details><summary> 👉模型列表详情</summary>

<table>
<thead>
<tr>
<th>模型</th><th>模型下载链接</th>
<th>输出特征维度</th>
<th>AP (%)<br/>AgeDB-30/CFP-FP/LFW</th>
<th>GPU推理耗时 (ms)</th>
<th>CPU推理耗时</th>
<th>模型存储大小 (M)</th>
<th>介绍</th>
</tr>
</thead>
<tbody>
<tr>
<td>MobileFaceNet</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0b2/MobileFaceNet_infer.tar">推理模型</a>/<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/MobileFaceNet_pretrained.pdparams">训练模型</a></td>
<td>128</td>
<td>96.28/96.71/99.58</td>
<td></td>
<td></td>
<td>4.1</td>
<td>基于MobileFaceNet在MS1Mv3数据集上训练的人脸特征提取模型</td>
</tr>
<tr>
<td>ResNet50_face</td><td><a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_inference_model/paddle3.0b2/ResNet50_face_infer.tar">推理模型</a>/<a href="https://paddle-model-ecology.bj.bcebos.com/paddlex/official_pretrained_model/ResNet50_face_pretrained.pdparams">训练模型</a></td>
<td>512</td>
<td>98.12/98.56/99.77</td>
<td></td>
<td></td>
<td>87.2</td>
<td>基于ResNet50在MS1Mv3数据集上训练的人脸特征提取模型</td>
</tr>
</tbody>
</table>
<p>注：以上精度指标是分别在AgeDB-30、CFP-FP和LFW数据集上测得的Accuracy。所有模型 GPU 推理耗时基于 NVIDIA Tesla T4 机器，精度类型为 FP32， CPU 推理速度基于 Intel(R) Xeon(R) Gold 5117 CPU @ 2.00GHz，线程数为8，精度类型为 FP32。</p></details>

## 三、快速集成
> ❗ 在快速集成前，请先安装 PaddleX 的 wheel 包，详细请参考 [PaddleX本地安装教程](../../../installation/installation.md)

完成whl包的安装后，几行代码即可完成人脸特征模块的推理，可以任意切换该模块下的模型，您也可以将人脸特征模块中的模型推理集成到您的项目中。运行以下代码前，请您下载[示例图片](https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/face_recognition_001.jpg)到本地。

```python
from paddlex import create_model

model_name = "MobileFaceNet"

model = create_model(model_name)
output = model.predict("face_recognition_001.jpg", batch_size=1)

for res in output:
    res.print(json_format=False)
    res.save_to_json("./output/res.json")
```

关于更多 PaddleX 的单模型推理的 API 的使用方法，可以参考[PaddleX单模型Python脚本使用说明](../../instructions/model_python_API.md)。
## 四、二次开发
如果你追求更高精度的现有模型，可以使用PaddleX的二次开发能力，开发更好的人脸特征模型。在使用PaddleX开发人脸特征模型之前，请务必安装PaddleX的PaddleClas插件，安装过程可以参考 [PaddleX本地安装教程](../../../installation/installation.md)

### 4.1 数据准备
在进行模型训练前，需要准备相应任务模块的数据集。PaddleX 针对每一个模块提供了数据校验功能，<b>只有通过数据校验的数据才可以进行模型训练</b>。此外，PaddleX为每一个模块都提供了demo数据集，您可以基于官方提供的 Demo 数据完成后续的开发。若您希望用私有数据集进行后续的模型训练，人脸特征模块的训练数据集采取通用图像分类数据集格式组织，可以参考[PaddleX图像分类任务模块数据标注教程](../../../data_annotations/cv_modules/image_classification.md)。若您希望用私有数据集进行后续的模型评估，请注意人脸特征模块的验证数据集格式与训练数据集的方式有所不同，请参考[4.1.4节 人脸特征模块数据集组织方式](#414-人脸特征模块数据集组织方式)

#### 4.1.1 Demo 数据下载
您可以参考下面的命令将 Demo 数据集下载到指定文件夹：

```bash
cd /path/to/paddlex
wget https://paddle-model-ecology.bj.bcebos.com/paddlex/data/face_rec_examples.tar -P ./dataset
tar -xf ./dataset/face_rec_examples.tar -C ./dataset/
```
#### 4.1.2 数据校验
一行命令即可完成数据校验：

```bash
python main.py -c paddlex/configs/face_recognition/MobileFaceNet.yaml \
    -o Global.mode=check_dataset \
    -o Global.dataset_dir=./dataset/face_rec_examples
```
执行上述命令后，PaddleX 会对数据集进行校验，并统计数据集的基本信息，命令运行成功后会在log中打印出`Check dataset passed !`信息。校验结果文件保存在`./output/check_dataset_result.json`，同时相关产出会保存在当前目录的`./output/check_dataset`目录下，产出目录中包括可视化的示例样本图片。

<details><summary>👉 <b>校验结果详情（点击展开）</b></summary>

<p>校验结果文件具体内容为：</p>
<pre><code class="language-bash">{
  &quot;done_flag&quot;: true,
  &quot;check_pass&quot;: true,
  &quot;attributes&quot;: {
    &quot;train_label_file&quot;: &quot;../../dataset/face_rec_examples/train/label.txt&quot;,
    &quot;train_num_classes&quot;: 995,
    &quot;train_samples&quot;: 1000,
    &quot;train_sample_paths&quot;: [
      &quot;check_dataset/demo_img/01378592.jpg&quot;,
      &quot;check_dataset/demo_img/04331410.jpg&quot;,
      &quot;check_dataset/demo_img/03485713.jpg&quot;,
      &quot;check_dataset/demo_img/02382123.jpg&quot;,
      &quot;check_dataset/demo_img/01722397.jpg&quot;,
      &quot;check_dataset/demo_img/02682349.jpg&quot;,
      &quot;check_dataset/demo_img/00272794.jpg&quot;,
      &quot;check_dataset/demo_img/03151987.jpg&quot;,
      &quot;check_dataset/demo_img/01725764.jpg&quot;,
      &quot;check_dataset/demo_img/02580369.jpg&quot;
    ],
    &quot;val_label_file&quot;: &quot;../../dataset/face_rec_examples/val/pair_label.txt&quot;,
    &quot;val_num_classes&quot;: 2,
    &quot;val_samples&quot;: 500,
    &quot;val_sample_paths&quot;: [
      &quot;check_dataset/demo_img/Don_Carcieri_0001.jpg&quot;,
      &quot;check_dataset/demo_img/Eric_Fehr_0001.jpg&quot;,
      &quot;check_dataset/demo_img/Harry_Kalas_0001.jpg&quot;,
      &quot;check_dataset/demo_img/Francis_Ford_Coppola_0001.jpg&quot;,
      &quot;check_dataset/demo_img/Amer_al-Saadi_0001.jpg&quot;,
      &quot;check_dataset/demo_img/Sergei_Ivanov_0001.jpg&quot;,
      &quot;check_dataset/demo_img/Erin_Runnion_0003.jpg&quot;,
      &quot;check_dataset/demo_img/Bill_Stapleton_0001.jpg&quot;,
      &quot;check_dataset/demo_img/Daniel_Bruehl_0001.jpg&quot;,
      &quot;check_dataset/demo_img/Clare_Short_0004.jpg&quot;
    ]
  },
  &quot;analysis&quot;: {},
  &quot;dataset_path&quot;: &quot;./dataset/face_rec_examples&quot;,
  &quot;show_type&quot;: &quot;image&quot;,
  &quot;dataset_type&quot;: &quot;ClsDataset&quot;
}
</code></pre>
<p>上述校验结果中，<code>check_pass</code> 为 <code>True</code> 表示数据集格式符合要求，其他部分指标的说明如下：</p>
<ul>
<li><code>attributes.train_num_classes</code>：该数据集训练类别数为 995；</li>
<li><code>attributes.val_num_classes</code>：该数据集验证类别数为 2；</li>
<li><code>attributes.train_samples</code>：该数据集训练集样本数量为 1000；</li>
<li><code>attributes.val_samples</code>：该数据集验证集样本数量为 500；</li>
<li><code>attributes.train_sample_paths</code>：该数据集训练集样本可视化图片相对路径列表；</li>
</ul></details>

#### 4.1.3 数据集格式转换/数据集划分（可选）
在您完成数据校验之后，可以通过<b>修改配置文件</b>或是<b>追加超参数</b>的方式对数据集的格式进行转换，也可以对数据集的训练/验证比例进行重新划分。

<details><summary>👉 <b>格式转换/数据集划分详情（点击展开）</b></summary>

<p>人脸特征模块不支持数据格式转换与数据集划分。</p></details>

#### 4.1.4 人脸特征模块数据集组织方式

人脸特征模块验证数据集与训练数据集格式不同，若需要在私有数据上训练模型和评估模型精度，请按照如下方式组织自己的数据集：

```bash
face_rec_dataroot      # 数据集根目录，目录名称可以改变
├── train              # 训练数据集的保存目录，目录名称不可以改变
   ├── images          # 图像的保存目录，目录名称可以改变，但要注意与label.txt中的内容对应
      ├── xxx.jpg      # 人脸图像文件
      ├── xxx.jpg      # 人脸图像文件
      ...
   └── label.txt       # 训练集标注文件，文件名称不可改变。每行给出图像相对`train`的路径和人脸图像类别（人脸身份）id，使用空格分隔，内容举例：images/image_06765.jpg 0
├── val                # 验证数据集的保存目录，目录名称不可以改变
   ├── images          # 图像的保存目录，目录名称可以改变，但要注意与pari_label.txt中的内容对应
      ├── xxx.jpg      # 人脸图像文件
      ├── xxx.jpg      # 人脸图像文件
      ...
   └── pair_label.txt  # 验证数据集标注文件，文件名称不可改变。每行给出两个要比对的人脸图像路径和一个表示该对图像是否属于同一个人的0、1标签，使用空格分隔。
```

验证集标注文件`pair_label.txt`的内容示例:

```bash
# 人脸图像1.jpg 人脸图像2.jpg 标签(0表示该行的两个人脸图像文件不属于同一个人，1表示属于同一个人)
images/Angela_Merkel_0001.jpg images/Angela_Merkel_0002.jpg 1
images/Bruce_Gebhardt_0001.jpg images/Masao_Azuma_0001.jpg 0
images/Francis_Ford_Coppola_0001.jpg images/Francis_Ford_Coppola_0002.jpg 1
images/Jason_Kidd_0006.jpg images/Jason_Kidd_0008.jpg 1
images/Miyako_Miyazaki_0002.jpg images/Munir_Akram_0002.jpg 0
```

### 4.2 模型训练
一条命令即可完成模型的训练，以此处MobileFaceNet的训练为例：

```bash
python main.py -c paddlex/configs/face_recognition/MobileFaceNet.yaml \
    -o Global.mode=train \
    -o Global.dataset_dir=./dataset/face_rec_examples
```
需要如下几步：

* 指定模型的`.yaml` 配置文件路径（此处为`MobileFaceNet.yaml`）
* 指定模式为模型训练：`-o Global.mode=train`
* 指定训练数据集路径：`-o Global.dataset_dir`
其他相关参数均可通过修改`.yaml`配置文件中的`Global`和`Train`下的字段来进行设置，也可以通过在命令行中追加参数来进行调整。如指定前 2 卡 gpu 训练：`-o Global.device=gpu:0,1`；设置训练轮次数为 10：`-o Train.epochs_iters=10`。更多可修改的参数及其详细解释，可以查阅模型对应任务模块的配置文件说明[PaddleX通用模型配置文件参数说明](../../instructions/config_parameters_common.md)。

<details><summary>👉 <b>更多说明（点击展开）</b></summary>

<ul>
<li>模型训练过程中，PaddleX 会自动保存模型权重文件，默认为<code>output</code>，如需指定保存路径，可通过配置文件中 <code>-o Global.output</code> 字段进行设置。</li>
<li>PaddleX 对您屏蔽了动态图权重和静态图权重的概念。在模型训练的过程中，会同时产出动态图和静态图的权重，在模型推理时，默认选择静态图权重推理。</li>
<li>
<p>训练其他模型时，需要的指定相应的配置文件，模型和配置的文件的对应关系，可以查阅<a href="../../../support_list/models_list.md">PaddleX模型列表（CPU/GPU）</a>。
在完成模型训练后，所有产出保存在指定的输出目录（默认为<code>./output/</code>）下，通常有以下产出：</p>
</li>
<li>
<p><code>train_result.json</code>：训练结果记录文件，记录了训练任务是否正常完成，以及产出的权重指标、相关文件路径等；</p>
</li>
<li><code>train.log</code>：训练日志文件，记录了训练过程中的模型指标变化、loss 变化等；</li>
<li><code>config.yaml</code>：训练配置文件，记录了本次训练的超参数的配置；</li>
<li><code>.pdparams</code>、<code>.pdema</code>、<code>.pdopt.pdstate</code>、<code>.pdiparams</code>、<code>.pdmodel</code>：模型权重相关文件，包括网络参数、优化器、EMA、静态图网络参数、静态图网络结构等；</li>
</ul></details>

## <b>4.3 模型评估</b>
在完成模型训练后，可以对指定的模型权重文件在验证集上进行评估，验证模型精度。使用 PaddleX 进行模型评估，一条命令即可完成模型的评估：

```bash
python main.py -c paddlex/configs/face_recognition/MobileFaceNet.yaml \
    -o Global.mode=evaluate \
    -o Global.dataset_dir=./dataset/face_rec_examples
```
与模型训练类似，需要如下几步：

* 指定模型的`.yaml` 配置文件路径（此处为`MobileFaceNet.yaml`）
* 指定模式为模型评估：`-o Global.mode=evaluate`
* 指定验证数据集路径：`-o Global.dataset_dir`
其他相关参数均可通过修改`.yaml`配置文件中的`Global`和`Evaluate`下的字段来进行设置，详细请参考[PaddleX通用模型配置文件参数说明](../../instructions/config_parameters_common.md)。

<details><summary>👉 <b>更多说明（点击展开）</b></summary>

<p>在模型评估时，需要指定模型权重文件路径，每个配置文件中都内置了默认的权重保存路径，如需要改变，只需要通过追加命令行参数的形式进行设置即可，如<code>-o Evaluate.weight_path=./output/best_model/best_model/model.pdparams</code>。</p>
<p>在完成模型评估后，会产出<code>evaluate_result.json</code>，其记录了评估的结果，具体来说，记录了评估任务是否正常完成，以及模型的评估指标，包含 Accuracy；</p></details>

### <b>4.4 模型推理</b>
在完成模型的训练和评估后，即可使用训练好的模型权重进行推理预测。在PaddleX中实现模型推理预测可以通过两种方式：命令行和wheel 包。

#### 4.4.1 模型推理
* 通过命令行的方式进行推理预测，只需如下一条命令，运行以下代码前，请您下载[示例图片](https://paddle-model-ecology.bj.bcebos.com/paddlex/imgs/demo_image/face_recognition_001.jpg)到本地。
```bash
python main.py -c paddlex/configs/face_recognition/MobileFaceNet.yaml \
    -o Global.mode=predict \
    -o Predict.model_dir="./output/best_model/inference" \
    -o Predict.input="face_recognition_001.jpg"
```
与模型训练和评估类似，需要如下几步：

* 指定模型的`.yaml` 配置文件路径（此处为`MobileFaceNet.yaml`）
* 指定模式为模型推理预测：`-o Global.mode=predict`
* 指定模型权重路径：`-o Predict.model_dir="./output/best_model/inference"`
* 指定输入数据路径：`-o Predict.input="..."`
其他相关参数均可通过修改`.yaml`配置文件中的`Global`和`Predict`下的字段来进行设置，详细请参考[PaddleX通用模型配置文件参数说明](../../instructions/config_parameters_common.md)。

#### 4.4.2 模型集成
模型可以直接集成到 PaddleX 产线中，也可以直接集成到您自己的项目中。

1.<b>产线集成</b>

人脸特征模块可以集成的PaddleX产线有[<b>人脸识别</b>](../../../pipeline_usage/tutorials/cv_pipelines/face_recognition.md)，只需要替换模型路径即可完成相关产线的人脸特征模块的模型更新。在产线集成中，你可以使用高性能部署和服务化部署来部署你得到的模型。

2.<b>模块集成</b>

您产出的权重可以直接集成到人脸特征模块中，可以参考[快速集成](#三快速集成)的 Python 示例代码，只需要将模型替换为你训练的到的模型路径即可。
