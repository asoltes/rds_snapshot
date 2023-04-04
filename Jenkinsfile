pipeline {
  agent any
  parameters {
    choice(
      name: 'REGION',
      choices: ['us-east-1', 'us-east-2', 'ap-southeast-1', 'ap-southeast-2'],
      description: 'Select the Region of RDS.'
    )

    extendedChoice(
      name: 'RDS_INSTANCE',
      description: 'Check the Instance you need to snapshot',
      multiSelectDelimiter: ',',
      type: 'PT_CHECKBOX',
      groovyScript: """
        return ['database-1', 'database-2']
      """
    )
  }

  stages {
    stage('RDS Snapshot') {
      steps {
        script {
          withAWS(roleAccount:"${AWS_ACCOUNT_NUMBER}", role:"${ASSUME_IAM_ROLE_NAME}", region:"${REGION}") {
            // Get AWS Account Number substring of last 4 characters
            def awsAccountNumberShortened = sh (
              script: "aws sts get-caller-identity --query 'Account'",
              returnStdout: true
            ).trim().substring(0,4)
          }

          sh "pip install boto3"
          sh "python3 rds_snap.py --db_instances $RDS_INSTANCE --region $REGION"
        }
      }
    }

    // Add more stages as needed
  }
}
