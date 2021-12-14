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

<b>Step1- </b> Create a Tensorflow folder / directory in your root directory.  
<b>Step2- </b> Open a terminal in this directory and run the following command- 
~~~
git clone https://github.com/tensorflow/models  
~~~ 
 
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
  
<b>On Windows,</b><br/>
<b>Step3.1- </b>Visit https://github.com/protocolbuffers/protobuf/releases and choose the latest zip file from <b>Assets</b> based on your machine's configurations.  
<b>Step3.2- </b>Download and extract. Rename the extract folder to protoc.  
<b>Step3.3- </b> Click on This PC(My Computer) > (Right click) Local Disk C > Properties. > Advanced System settings > Environment Variables > select Path > Edit...<br/>
<b>Step3.4- </b> Copy the path of the bin folder under in the protoc directory and add it to the paths. 
<br/>It would look like D: \<your_root_folder_path>\Tensorflow\protoc\bin<br/>
<b>Step3.5- </b> OK<br/><br/>
<b>On Mac,</b><br/>
Open terminal and simply install protobuf using homebrew.  
~~~
brew install protobuf
~~~
*If you don't have homebrew installed on your machine. Execute the following command on a new terminal and then run the above command.*
~~~
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
~~~  
  
<b>On Linux,</b>  
Execute the following command on a new terminal
~~~
apt-get install protobuf-compiler
~~~
> Next, we will compile the .proto files that will be used for the generation of the tfrecord files.
   
Open Terminal in Tensorflow directory and execute the following commands<br/>
~~~
 cd models/research
 protoc object_detection/protos/*.proto --python_out=.
 export PYTHONPATH=$PYTHONPATH:`pwd`:`pwd`/slim
 cp object_detection/packages/tf2/setup.py .
 python -m pip install .
~~~

> Now, we will create the labels.csv files

### Labels csv generation
<b>Note:</b> Make sure that you have split your xml files between your train and test folders in the images directory and created a dat directory in your model_trainig directory.

Open a new terminal
~~~
cd model_training
~~~

Now execute <b>annotations.py</b>

After a successful run of the file, you should see 2 success messages:  
~~~
Succesfully converted xml to csv  
Successfully created label maps  
~~~
and 3 new files viz.  
* label_map.pbtxt  
* test_labels.csv  
* train_labels.csv 
 
created in your dat directory.

> Now, we are set to run generate_tfrecords.py  

### File configuration and execution
Open <b>generate_tfrecords.py</b><br/>
Under <b>class_text_to_int</b> function add all your datasets classes with return values as the label mappings. Refer to the comments in the file.<br/><br/>

> Now, open terminal in the directory containing generate_tfrecords.py and enter the following command  
~~~
python generate_tfrecord.py --csv_input=dat/train_labels.csv  --output_path=dat/train.record --image_dir=images/ 
python generate_tfrecord.py --csv_input=dat/test_labels.csv  --output_path=dat/test.record --image_dir=images/ 
~~~
Successful run of the file would result in the exit message - Successfully created the TFRecords: \<path\>
