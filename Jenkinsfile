pipeline {
  agent any
  parameters {
    choice(
      name: 'REGION',
      choices: ['us-east-1', 'us-east-2', 'ap-southeast-1', 'ap-southeast-2'],
      description: 'Select the Region of RDS.'
    )
  }

  stages {
    stage('Prompt User') {
      steps {
        script {
          def userInput = input(
            id: 'userInput',
            message: 'Select the databases to snapshot:',
            parameters: [
              [$class: 'MultiSelectionParameterDefinition', 
               name: 'DB_INSTANCES',
               choices: ['database-1', 'database-2', 'database-3'],
               description: 'Select one or more databases to snapshot.']
            ]
          )

          withAWS(roleAccount:"${AWS_ACCOUNT_NUMBER}", role:"${ASSUME_IAM_ROLE_NAME}", region:"${params.REGION}") {
            // Get AWS Account Number substring of last 4 characters
            def awsAccountNumberShortened = sh (
              script: "aws sts get-caller-identity --query 'Account'",
              returnStdout: true
            ).trim().substring(0,4)
          }

          sh "pip install boto3"
          sh "python3 rds_snap.py --db_instances ${userInput.DB_INSTANCES.join(',')} --region ${params.REGION}"
        }
      }
    }

    // Add more stages as needed
  }
}
