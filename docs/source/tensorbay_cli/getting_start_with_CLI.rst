########################
 Getting Start with CLI
########################

The TensorBay Command Line Interface is a tool to operate on your datasets.
It supports Windows, Linux, and Mac platforms.

You can use TensorBay CLI to:
 - Create and delete dataset.
 - List data on TensorBay.
 - Upload data to TensorBay.

**************
 Installation
**************

To use TensorBay CLI, please install TensorBaySDK first. See :ref:`quick_start:Installation`
for more details.

******
 TBRN
******

TensorBay Resource Name(TBRN) uniquely defines the data stored in TensorBay.
TBRN begins with ``tb:``. Default segment can be defined as ``""`` (empty string).
The following is the general format for TBRN:

.. code::

    tb:[dataset_name]:[segment_name]://[remote_path]

**************
 Sub-Commands
**************

============ =========================================
Sub-Commands Description
============ =========================================
config       Configure the accessKey and URL(optional)
create       Create a dataset
delete       Delete a dataset
ls           List data under the path
cp           Upload data
============ =========================================

**config**

.. code:: console

    gas config [accessKey] [url]

Configure the accessKey and URL(optional). AccessKey_ is used for identification when using TensorBay to operate on your dataset.
The default url is "https://gas.graviti.cn/".

.. _accesskey: https://gas.graviti.cn/access-key

You can set the accessKey and URL into configuration:

.. code:: console

    gas config Accesskey-***** https://gas.graviti.cn/

To show configuration information:

.. code:: console

    gas config

You can also log in with specified accessKey and URL to interact with TensorBay.

.. code:: console

    gas -u [url] -k [accessKey] [command] [args]

For example, to list all dataset with accessKey and URL:

.. code:: console

    gas -u https://gas.uat.graviti.cn/ -k Accesskey-***** ls

**create**

.. code:: console

    gas create [tbrn]

    tbrn:
      tb:[dataset_name]

Create a dataset with given name. Take `BSTLD`_ for example:

.. _BSTLD: https://www.graviti.cn/open-datasets/BSTLD

.. code:: console

    gas create tb:BSTLD

**delete**

.. code:: console

    gas delete [tbrn]


    tbrn:
      tb:[dataset_name]

Delete the dataset with given name. Take `BSTLD`_ for example:

.. code:: console

    gas delete tb:BSTLD

**ls**

.. code:: console

    gas ls [Options] [tbrn]

    Options:
      -a, --all     List all files under all segments.
                    Only works when [tbrn] is tb:[dataset_name].

    tbrn:
      None
      tb:[dataset_name]
      tb:[dataset_name]:[segment_name]
      tb:[dataset_name]:[segment_name]://[remote_path]

List data under the path. If the path is empty, list the names of all datasets.
You can list data in the following ways:

| 1. List the names of all datasets.

.. code:: console

    gas ls

| 2. List the names of all segments of `BSTLD`_.

.. code:: console

    gas ls tb:BSTLD

| 3. List all the files in all the segments of `BSTLD`_.

.. code:: console

    gas ls -a tb:BSTLD

| 4. List all the files in the ``train`` segment of `BSTLD`_.

.. code:: console

    gas ls tb:BSTLD:train

| 5. List all the files inside ``chimpanzee`` directory in the ``""`` (empty string) segment of `7 Categories AnimalPose`_.

.. _7 Categories AnimalPose: https://www.graviti.cn/open-datasets/AnimalPose7

.. code:: console

    gas ls tb:7\ Categories\ AnimalPose:://chimpanzee

**cp**

.. code:: console

    gas cp [Options] [local_path1] [local_path2]... [tbrn]

    Options:
      -r, --recursive     Copy directories recursively.
      -j, --jobs INTEGER  The number of threads.

    tbrn:
      tb:[dataset_name]:[segment_name]
      tb:[dataset_name]:[segment_name]://[remote_path]

Upload data to TensorBay. ``[segment_name]`` is required. If only upload one file and
``[remote_path]`` doesn't end with ``"/"``, then the file will be uploaded and renamed as
``[remote_path]``.

You can upload your data in the following ways:

| 1. Upload a single file.

.. code:: console

    gas cp image1.jpg tb:dataset:seg://object/


The file will be saved as:

.. code:: console

    tb:dataset:seg://object/image1.jpg


| 2. Upload multiple files.

.. code:: console

    gas cp image1.jpg image2.jpg tb:dataset:seg://object/


The files will be saved as:

.. code:: console

    tb:dataset:seg://object/image1.jpg
    tb:dataset:seg://object/image2.jpg
    tb:dataset:seg://object/image3.jpg

| 3. Upload files in folders.

.. code:: console

    gas cp -r image.jpg folder1/ tb:dataset:seg://object

If the structure of the folder is like:

.. code:: console
   :name: folder-structure

    folder1
    ├── sub1
    │   └── image1.jpg
    └── image2.jpg

The files will be saved as:

.. code:: console

    tb:dataset:seg://object/image.jpg
    tb:dataset:seg://object/folder1/image2.jpg
    tb:dataset:seg://object/folder1/sub1/image1.jpg

| 4. Multi-thread upload.

Upload a folder with 8 threads:

.. code:: console

    gas cp -r -j 8 folder/ tb:dataset:seg://object
