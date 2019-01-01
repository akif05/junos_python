curl -u 'akif05' https://api.github.com/user/repos -d '{"name":"junos_python"}'
# echo "# junos_python" >> README.md
git init
git add -A
git commit -m "first commit"
git remote add origin https://github.com/akif05/junos_python.git
git push -u origin master

