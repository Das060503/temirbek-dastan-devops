pipeline {
    agent any

    environment {
        STUDENT_NAME = 'Dastan'
        STUDENT_SURNAME = 'Temirbek'
        STUDENT_GROUP = 'IT2-2308'
        STUDENT_ID = '37621'
        IMAGE_NAME = 'temirbek-dastan-devops'
        CONTAINER_NAME = 'temirbek-dastan-container'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'python3 -m py_compile app/app.py'
                echo 'Build check completed successfully'
            }
        }

        stage('Test') {
            steps {
                sh '''
                    test -f Dockerfile
                    test -f app/app.py
                    grep -q "STUDENT_NAME" app/app.py
                '''
                echo "Student: ${STUDENT_NAME} ${STUDENT_SURNAME}"
                echo "Group: ${STUDENT_GROUP}"
                echo "Student ID: ${STUDENT_ID}"
            }
        }

        stage('Docker Build') {
            steps {
                sh 'docker build -t ${IMAGE_NAME} .'
            }
        }

        stage('Docker Run') {
            steps {
                sh '''
                    docker rm -f ${CONTAINER_NAME} 2>/dev/null || true

                    docker run -d \
                      --name ${CONTAINER_NAME} \
                      -p 8080:8080 \
                      -e STUDENT_NAME=${STUDENT_NAME} \
                      -e STUDENT_SURNAME=${STUDENT_SURNAME} \
                      -e STUDENT_GROUP=${STUDENT_GROUP} \
                      -e STUDENT_ID=${STUDENT_ID} \
                      ${IMAGE_NAME}

                    sleep 3
                    curl --fail http://localhost:8080
                    docker ps
                '''
            }
        }
    }
}
