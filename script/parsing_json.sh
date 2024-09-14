#!/bin/bash
# author: dr. dennis wylie

grep -P "\}\s*$" "$1" | jq -c -r '[.created_at, .user.id_str, .id_str, .retweet_count, .favorite_count, .retweeted_status.user.id_str, .retweeted_status.id_str, .retweeted_status.retweet_count, .retweeted_status.favorite_count, .user.screen_name, .retweeted_status.user.screen_name]' | perl -pe 's/^\[|\]$//g'
