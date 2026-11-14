pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Freeze dependencies') {
            steps {
                bat 'cd employee-api && uv pip freeze > requirements.txt'
            }
        }

        stage('Build versioned package') {
            steps {
                bat 'powershell.exe -Command "Compress-Archive -Path employee-api\\main.py, employee-api\\requirements.txt -DestinationPath employee-api-build-%BUILD_NUMBER%-%GIT_COMMIT:~0,7%.zip -Force"'
            }
        }

        stage('Archive') {
            steps {
                archiveArtifacts artifacts: 'employee-api-build-*.zip', fingerprint: true
            }
        }
    }
}