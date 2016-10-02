#!/usr/bin/env bash
pdftotext "$1" - | tr ' ' '\n' | sed 's/[^[:alpha:].]//g' |sed 's/^\.*$//g'|sed 's/\.$//g' | grep -v "^\s*$" | sort -f| uniq -ic | sort -bnr

