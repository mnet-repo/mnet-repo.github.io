#!/bin/sh

echo 'Content-Type: application/octet-stream'
echo 'Content-Transfer-Encoding: binary'
echo 'Content-Disposition: attachment; filename="env.tgz"'
echo ''

tar czf - -C "$ENV_DIR" .
