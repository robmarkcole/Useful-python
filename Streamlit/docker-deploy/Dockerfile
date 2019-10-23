FROM continuumio/miniconda3:latest

MAINTAINER Anshul Jindal "anshul.jindal@tum.de"

RUN mkdir -p /home/streamlit
WORKDIR /home/streamlit

RUN conda install --yes \
    numpy==1.16.3 \
    pandas==0.24.2 \
    && conda clean -afy

RUN pip install streamlit 
RUN pip install xlrd 

COPY . /home/streamlit 

EXPOSE 8501

CMD [ "streamlit", "run", "web.py" ]
