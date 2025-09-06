pipeline {
    agent any
    
    environment {
        DOCKER_IMAGE = 'lasanthi821/gscomp334'
        DOCKER_REGISTRY = 'docker.io'
    }
    
    stages {
        // Stage 1: Pull Git Repository
        stage('Pull Git Repository') {
            steps {
                echo 'Stage 1: Pulling Git repository...'
                git branch: 'main',
                url: 'https://github.com/Lasanthikalpani/NCC_2025.git'
                echo '✅ Repository cloned successfully'
            }
        }
        
        // Stage 2: Build Docker Image
        stage('Build Docker Image') {
            steps {
                echo 'Stage 2: Building Docker image...'
                script {
                    docker.build("${env.DOCKER_IMAGE}:latest")
                }
                echo '✅ Docker image built successfully'
            }
        }
        
        // Stage 3: Push to Docker Hub
        stage('Push to Docker Hub') {
            steps {
                echo 'Stage 3: Pushing Docker image to Docker Hub...'
                script {
                    withCredentials([usernamePassword(
                        credentialsId: 'gscomp334-dockerhub-token',
                        usernameVariable: 'DOCKER_USERNAME',
                        passwordVariable: 'DOCKER_TOKEN'
                    )]) {
                        // Use bat for Windows instead of sh
                        bat """
                            echo %DOCKER_TOKEN% | docker login -u %DOCKER_USERNAME% --password-stdin
                            docker push ${env.DOCKER_IMAGE}:latest
                            docker logout ${env.DOCKER_REGISTRY}
                        """
                    }
                }
                echo '✅ Docker image pushed to Docker Hub successfully'
            }
        }
    }
    
    post {
        always {
            echo 'Pipeline execution completed'
            cleanWs()
        }
        success {
            echo '🎉 Pipeline executed successfully!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
    }
}