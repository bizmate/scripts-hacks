#!/bin/bash
#
#   Requires a number of env variables to be setup
#   This version relies on some manual hacks, ideally all this should be in capistrano or puppet
#   The remote deployment script is located at : /$SERVER_USER/jenkins_deploy.sh
#   Make sure you set CLOUD_PATH, CLOUD_USER, CLOUD_HOST, CLOUD_PUBKEY, APP_BRANCH


CSDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
SERVERDIR="$CLOUD_PATH"
FWSLASH=/
SERVER_USER="$CLOUD_USER"
SERVER_HOST="$CLOUD_HOST"
SSH_KEY_PATH="$CLOUD_PUBKEY"

echo "Current script dir: $CSDIR"

date_time=$(date +%Y%m%d_%H%M)
echo "Current script date: $date_time"
archive=App_$date_time
archive_name=$archive.zip
echo "Run git archive: $archive_name"
git archive --format zip --output ./$archive_name "$APP_BRANCH"
echo "SCP archive $archive_name to server"
scp -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i "$SSH_KEY_PATH" "$archive_name" "$SERVER_USER"@"$SERVER_HOST":$SERVERDIR
#echo "Delete $archive_name "
rm $archive_name

echo "Running remote setup "
ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i "$SSH_KEY_PATH" "$SERVER_USER"@"$SERVER_HOST" "unzip \"$SERVERDIR$archive_name\" -d \"$SERVERDIR$archive\" > /dev/null;/$SERVER_USER/jenkins_deploy.sh $archive"