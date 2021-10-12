# accident_detection
## Steps for reproduction:
You need a separate images folder with images with respective train and test splits in the root directory. Thus, the directory would look like
root/  
└─ images/  
&nbsp;&nbsp;&nbsp;├─ train/  
&nbsp;&nbsp;&nbsp;├─ test/
     
## TFRecords generation
You would need to install few dependencies on your machine for the generate_tfrecords.py to work. 
### Setup steps:

> First, we will clone tensorflow model garden repository  

<b>Step1.</b> Create a Tensorflow folder / directory in your root directory.  
<b>Step2.</b> Open a terminal in this directory and run the following command-  
git clone https://github.com/tensorflow/models  
  
The directory should look like -   
root/  
└─ images/  
&nbsp;&nbsp;&nbsp;&nbsp;├─ train/  
&nbsp;&nbsp;&nbsp;&nbsp;├─ test/  
&nbsp;&nbsp;&nbsp;&nbsp;├─ Img1.jpg<br/>
&nbsp;&nbsp;&nbsp;&nbsp;├─ Img1.xml<br/>
&nbsp;&nbsp;&nbsp;&nbsp;├─ Img2.jpg<br/>
&nbsp;&nbsp;&nbsp;&nbsp;├─ Img2.xml<br/>
&nbsp;&nbsp;&nbsp;&nbsp;├─ ...<br/>
└─ Tensorflow/<br/>
&nbsp;&nbsp;&nbsp;&nbsp;├─ models/<br/><br/>

> Next, we will install Google protocol buffers  

<b>Step3.</b>Visit https://github.com/protocolbuffers/protobuf/releases and choose the latest zip file based on your machine's configurations from <b>Assets</b>.<br/>
<b>Step4.</b>Extract the zip in your Tensorflow directory. I have renamed the directory as protoc.<br/>
The directory should look like - <br/>
root/<br/>
└─ images/<br/>
&nbsp;&nbsp;&nbsp;&nbsp;├─ train/<br/>
&nbsp;&nbsp;&nbsp;&nbsp;├─ test/<br/>
&nbsp;&nbsp;&nbsp;&nbsp;├─ Img1.jpg<br/>
&nbsp;&nbsp;&nbsp;&nbsp;├─ Img1.xml<br/>
&nbsp;&nbsp;&nbsp;&nbsp;├─ Img2.jpg<br/>
&nbsp;&nbsp;&nbsp;&nbsp;├─ Img2.xml<br/>
&nbsp;&nbsp;&nbsp;&nbsp;├─ ...<br/>
└─ Tensorflow/<br/>
&nbsp;&nbsp;&nbsp;&nbsp;├─ models/<br/>
&nbsp;&nbsp;&nbsp;&nbsp;├─ protoc/<br/><br/>
<b>Step5.</b>
<b>On Windows,</b><br/>
<b>S5.1</b> Click on This PC(My Computer) > (Right click) Local Disk C > Properties. > Advanced System settings > Environment Variables > select Path > Edit...<br/>
<b>S5.2</b> Copy the path of the bin folder under in the protoc directory and add it to the paths. 
<br/>It would look like D: \<your_root_folder_path>\Tensorflow\protoc\bin<br/>
<b>S5.3</b> OK<br/><br/>
<b>On Mac and Linux,</b><br/>
<b>S5.1</b> Copy protoc executable under bin<br/>
<b>S5.2</b> Paste it in /usr/local/bin/<br/><br/>

> Open Terminal in Tensorflow directory, aexecute the following commands<br/>
~~~
 cd models
 protoc object_detection/protos/*.proto --python_out=.
 export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
 cp object_detection/packages/tf2/setup.py .
 python -m pip install .
~~~

> Now, we are set to run generate_tfrecords.py  

### File configuration and execution
Open generate_tfrecords.py<br/>
Under class_text_to_int function add all your datasets classes with return values as the label mappings. Refer to the comments in the file.<br/><br/>

> Now, open terminal in the directory containing generate_tfrecords.py and enter the following command  
~~~
python generate_tfrecord.py --csv_input=dat/train_labels.csv  --output_path=dat/train.record --image_dir=images/ 
python generate_tfrecord.py --csv_input=dat/test_labels.csv  --output_path=dat/test.record --image_dir=images/ 
~~~
Successful run of the file would result in the exit message - Successfully created the TFRecords: <path>
