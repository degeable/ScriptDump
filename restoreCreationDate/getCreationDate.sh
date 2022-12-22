
echo $(date -j -f "%Y%m%d%H%M" -v-6H $(mdls "$1" | grep kMDItemContentCreationDate | head -n1 | awk '{gsub("[^[:digit:]]+"," ");print $1$2$3$4$5}') +%Y%m%d%H%M)
