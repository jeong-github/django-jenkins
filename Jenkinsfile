pipeline {
    agent any

    environment {
        // Docker Hub ID와 레포지토리 이름 (예: jeonghyuck/jenkins-test)
        REPOSITORY = "jeonghyuck/chan-django"

        // Jenkins에 미리 등록한 Docker Hub 자격 증명 ID
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-jenkins')

        // 초기 이미지 태그 (빌드 번호 사용)
        IMAGE_TAG = "${env.BUILD_NUMBER}"
    }

    stages {


        stage('Build Docker Image') {
            steps {
                script {
                    // Dockerfile이 현재 디렉토리에 존재해야 함
                    sh 'docker build -t $REPOSITORY:$BUILD_NUMBER .'
                }
            }
        }

        stage('Docker Hub 로그인') {
            steps {
                script {
                    // Jenkins Credentials Plugin 사용
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                }
            }
        }

        stage('Docker 이미지 푸시') {
            steps {
                script {
                    sh 'docker push $REPOSITORY:$BUILD_NUMBER'
                }
            }
        }






    }
}
