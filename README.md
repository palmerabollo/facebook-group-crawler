Facebook Crawler
==

Hacky crawler to get and analyze information from Facebook Groups using Facebook Graph API.

**Note: This module no longer works since Facebook Graph API no longer provides access to private groups**

Crawler
--

You need a Facebook token. You can get a temporal one using the [Graph API Explorer](https://developers.facebook.com/tools/explorer/).

```shell
export FB_ACCESS_TOKEN=<your facebook access token>
export OUTPUT_FOLDER=<your output directory>
./run.sh
```

Analysis
--

Prerequisites: python2 (download messages), python3 + jupyter (analyis)

```shell
cd analysis
jupyter notebook
```

LICENSE
--

Copyright 2016 Guido García
Fair License - https://opensource.org/licenses/Fair
