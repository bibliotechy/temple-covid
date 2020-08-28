git pull origin master
docker-compose build
docker-compose run extractor
git add json
git commit -m "`date`"
git push origin master
