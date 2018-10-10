#!/bin/bash

asciidoctor -a stylesheet=index.css -a theme=flask 01_eda.adoc
asciidoctor -a stylesheet=index.css -a theme=flask 02_recommendations.adoc
