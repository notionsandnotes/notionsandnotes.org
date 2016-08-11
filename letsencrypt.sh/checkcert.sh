#!/bin/sh

cd "$(dirname "$0")"

checks=$(find certs -name cert.pem -type l -exec openssl x509 -checkend 2592000 -in {} \;)
expires="Certificate will not expire"
echo "$checks"

case "$checks" in
*$expires*)  exit 0 ;;
*)
    validtill=$(find certs -name cert.pem -type l -exec openssl x509 -enddate -noout -in {} \; | cut -d= -f2- )
    daysleft=$(( ( $(date -d "$validtill"  +'%s') - $(date +'%s')) /(60*60*24) ))
    notify-send -i appointment-soon "SSL Certificate about to expire" "Site www.notionsandnotes.org \nValid till $validtill \n$daysleft days till expiry"
    ;;
esac

random=`bash -c 'echo $RANDOM'`
rmin=$(( $random % 30 ))
rmin=$(( $rmin + 10))
tasknr=$(at -f "0" now+${rmin}min 2>&1 | tail -n 1 | cut -d ' ' -f2)

if ping -q -c 1 -W 1 8.8.8.8 >/dev/null; then
  ./letsencrypt.sh --cron
  atrm $tasknr
fi
