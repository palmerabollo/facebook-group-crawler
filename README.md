Facebook Crawler
==

Simple crawler to get information from Facebook Groups using Facebook Graph API and analyze it.

Crawler
--

You need a Facebook token. You can get a temporal one using the [Graph API Explorer](https://developers.facebook.com/tools/explorer/).

```shell
export FB_ACCESS_TOKEN=<your facebook access token>
export OUTPUT_FOLDER=<your output directory>
./run.sh
```

An alternative to preprocess the generated files:

```shell
cd $OUTPUT_FOLDER
ls | grep "post_right_" | grep "_comment_" | xargs -n 512 cat | jq '.created_time + " " + (.like_count|tostring) + " " + .from.id + " " + .message' >> right_comments.txt
ls | grep "post_left_" | grep "_comment_" | xargs -n 512 cat | jq '.created_time + " " + (.like_count|tostring) + " " + .from.id + " " + .message' >> left_comments.txt
```

Analysis
--

Prerequisites: python, jupyter

```shell
cd analysis
jupyter notebook
```

LICENSE
--

Copyright 2016 Guido García
Fair License - https://opensource.org/licenses/Fair