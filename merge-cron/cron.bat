cd repo/main
git pull
cd ../staging-data
git pull
git merge main --strategy-option theirs
git push --set-upstream origin staging-data
cd ../..
