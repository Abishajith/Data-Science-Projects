##Cost Prediction 

construction cost received from various source .It is analysed and combined each month to find the final cost 



### Step 1: Clone the repository
```bash
git clone https://github.com/sethusaim/Sensor-Fault-Detection.git

### Step 2- Create a conda environment after opening the repository

```bash
conda create -p venv python==3.8 -y

## activate the environment
```bash
conda activate venv/

### Step 3 - Install the requirements
```bash
pip install -r requirements.txt
```

### Step 4 - Install setup.py
```bash
python setup.py install
```


### Step 4 - setup folders
--> pipeline----------> training pipileine, prediction file
--> components
--> data_access ------> connect the file to data base and create csv file
--> cloud storage ----> regarding S3 bucket, upload, download
--> configuration-----> connection related config, s3 bucket, mongo db, kafka etc
--> constant----------> to maintain folders names
--> entity -----------> to define the i/p and o/p of every component
                 -----> artifact_entity.py-->describes the output of each stage in training data
                 -----> config_entity.py-->i/p to the every stage 
--> ml----------------> feature eng, custom model, custom graph

exception.py ---------> error related 
logger.py-------------> audit your code
