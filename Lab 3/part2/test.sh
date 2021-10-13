numFiles=$(ls photos | wc -l)
echo $numFiles
touch photos/"photo$numFiles.jpg"
