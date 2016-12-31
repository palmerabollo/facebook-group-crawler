#
# Simple Facebook crawler.
# It gets information from Facebook Groups using Facebook Graph API and saves it to files.
#

from __future__ import print_function

import time, os, sys, datetime
import requests
import json
import facebook

if len(sys.argv) != 3:
    print('Usage: crawler <group_id> <tag>')
    sys.exit(1)

group_id = sys.argv[1]
tag = sys.argv[2]

# You can get a temporary access token here: https://developers.facebook.com/tools/explorer/
access_token = os.environ['FB_ACCESS_TOKEN']
if not access_token:
    print('No FB_ACCESS_TOKEN env var found')
    sys.exit(1)

output_folder = os.environ['OUTPUT_FOLDER']
if not access_token:
    print('No OUTPUT_FOLDER env var found')
    sys.exit(1)

print('Processing group ' + group_id + ' with tag ' + tag)

def dump_post(post):
    """
    Write every post to a file and paginate/dump its comments.
    It uses a .metadata file to track posts and avoid processing the same post twice
    """

    filename = '/' + output_folder + '/' + 'post_' + tag + '_' + post['id']

    if os.path.isfile(filename + '.metadata'):
        print('Skip post ' + post['id'] + ' already crawled')
        return

    print('Dump post ' + post['id'])
    comments = post.pop('comments', None) # we want to process comments separately

    with open(filename + '.json', mode='w') as outfile:
        json.dump(post, outfile, indent=4)

    if comments:
        print('Dump comments', end='')
        while True: # paginate comments
            try:
                [dump_comment(post=post, comment=comment) for comment in comments['data']]
                comments = requests.get(comments['paging']['next']).json()
                time.sleep(1) # be polite, we don't want FB to ban us
                print('.', end='')
            except KeyError, TypeError:
                # Break when there are no more pages (['paging']['next']) and exit
                print('')
                break

    with open(filename + '.metadata', mode='w') as outfile:
        json.dump({'timestamp': str(datetime.datetime.now())}, outfile)

def dump_comment(post, comment):
    """
    Write every comment to a file
    """

    filename = '/' + output_folder + '/' + 'post_' + tag + '_' + post['id'] + '_comment_' + comment['id']
    with open(filename + '.json', mode='w') as outfile:
        json.dump(comment, outfile, indent=4)

try:
    # Version 2.3 still allows access to the feed of a private group.
    # The token needs user_groups & user_managed_groups permissions
    graph = facebook.GraphAPI(access_token, version='2.3')
    posts = graph.get_connections(group_id, 'feed?limit=100&fields=id,from,story,link,source,name,description,type,created_time,updated_time,comments{created_time,from,message,like_count,id}')
except facebook.GraphAPIError:
    print('Invalid or expired token. Get a new one.')
    sys.exit(1)

MAX_PAGES = 50
current_page = 0
while current_page < MAX_PAGES:
    try:
        print('Page ' + str(current_page))
        [dump_post(post=post) for post in posts['data']]
        posts = requests.get(posts['paging']['next']).json()
        current_page += 1
        time.sleep(0.2) # be polite, we don't want FB to ban us
    except KeyError:
        # Break when there are no more pages (['paging']['next']) and exit
        break
    except KeyboardInterrupt:
        print('User cancelled.')
        break
    except facebook.GraphAPIError:
        print('Invalid or expired token. Get a new one.')
        break
