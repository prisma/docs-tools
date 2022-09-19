cd repo/main
git pull
cd ../staging
git pull
git merge main
git push --set-upstream origin staging
cd ../..
