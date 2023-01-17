# A repo for predicting country flags

## Data Availability

If you just want to launch the application, no additional data is needed, you can skip to point Running an app.
You can generate data by running python files listed below. You can also download zip file from:
https://drive.google.com/file/d/1TCYs8i38u4kbz8IYy0FsI5h6HCefW-9o/view?usp=sharing
and unzip it in base directory of this project.

## Web scraping initial flag dataset

To perform web scraping run file download_flags.py

```
python download_flags.py
```

## Data Augmentation

To perform data augmentation run file augm_dataset.py (This make take a while)

```
python augm_dataset.py
```

## CNN development

CNN model was developed in jupyter notebook (CNN.ipynb) using tensorflow and saved to file my_h5_model_8_5.h5 (in app dir)

## Running an app

### Using docker image

1. Go to directory with Dockerfile (app)
2. Build docker image with:

```
docker build -t streamlit .
```

3. Run created coker image with:

```
docker run -p 8501:8501 streamlit
```

4.  To view the app, go to http://0.0.0.0:8501 or http://localhost:8501

### Using streamlit directly

1. Go to directory with stream_app.py (app)
2. Install requirements from file:

```
pip install -r requirements.txt
```

3. Run streamlit application with:

```
streamlit run stream_app.py
```

4. To view the app, go to http://0.0.0.0:8501 or http://localhost:8501
