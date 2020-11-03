cmd /c docker-compose down
rmdir /s /q db
cmd /c docker rmi backend
cmd /c docker-compose up -d