#!groovy
node {

    try {
        stage 'Checkout'
            checkout scm

            sh 'git log HEAD^..HEAD --pretty="%h %an - %s" > GIT_CHANGES'
            def lastChanges = readFile('GIT_CHANGES')

        stage 'Test'
            sh 'virtualenv env -p python3.6'
            sh '. env/bin/activate'
            sh 'env/bin/pip install -r chinook/requirements.txt'
            sh 'pkill -9 python'
            sh 'nohup env/bin/python3.6 chinook/manage.py runserver &'


        stage 'Publish results'
            slackSend color: "good", message: "Build successful: `${env.JOB_NAME}#${env.BUILD_NUMBER}` <${env.BUILD_URL}|Open in Jenkins>"
    }

    catch (err) {
        slackSend color: "danger", message: "Build failed :face_with_head_bandage: \n`${env.JOB_NAME}#${env.BUILD_NUMBER}` <${env.BUILD_URL}|Open in Jenkins>"

        throw err
    }

}