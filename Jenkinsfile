#!groovy

node {
    // It's often recommended to run a django project from a virtual environment.
    // This way you can manage all of your depedencies without affecting the rest of your system.
    def installed = fileExists 'bin/activate'

    if (!installed) {
        stage("Install Python Virtual Enviroment") {
            sh 'virtualenv env'
        }
    }

    // The stage below is attempting to get the latest version of our application code.
    // Since this is a multi-branch project the 'checkout scm' command is used. If you're working with a standard
    // pipeline project then you can replace this with the regular 'git url:' pipeline command.
    // The 'checkout scm' command will automatically pull down the code from the appropriate branch that triggered this build.
    stage ("Get Latest Code") {
        checkout scm
    }

    // If you're using pip for your dependency management, you should create a requirements file to store a list of all depedencies.
    // In this stage, you should first activate the virtual environment and then run through a pip install of the requirements file.
    stage ("Install Application Dependencies") {

        sh '''
            . env/bin/activate
            env/bin/pip install -r chinook/requirments.txt
            a=$(ps ax | grep 8000 | grep python | awk '{print $1}')
            kill -9 $a
            nohup env/bin/python chinook/manage.py runserver 0.0.0.0:8000 &
           '''
    }

    // Typically, django recommends that all the static assets such as images and css are to be collected to a single folder and
    // served separately outside the django application via apache or a CDN. This command will gather up all the static assets and
    // ready them for deployment.


    // After all of the dependencies are installed, you can start to run your tests.
    // The code below assumes that you're using the django-jenkins python libary to run the test but you can
    // also use the built in django test runner, nose or tox

}
