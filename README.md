# intercom-articles-bulk-update

## Overview
The purpose of this project is to bulk update all Intercom articles by replacing text. My product is going through a name change, and we need to update references to the old name.

First, intercom_getArticles.py is used to generate a CSV file of all your Intercom Article IDs. Then, intercom_update.py references the CSV and loops through each article, updating the title, description, and body.

## Prerequisites
1. You'll need your Intercom auth token.

## Instructions:
1. Replace the token variable in intercom_getArticles.py with your auth token, or create a config.ini file and add.
2. Run the intercom_getArticles.py
3. Once you successfully run, you should have an "articles.csv" file in your dir.
4. Run intercom_update.py, which references the CSV and loops through each artcile ID, updating title, description, and body.

