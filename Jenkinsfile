pipeline {
  agent any
  
  parameters {
    extendedChoice(name: 'RDS_INSTANCE', 
                    description: 'Check the Instance you need to snapshot',
                    type: 'PT_CHECKBOX',
                    value: '',
                    multiSelectDelimiter: ',',
                    groovyScript: """
                      return ['database-1', 'database-2', 'database-3', 'database-4']
                    """
    )
  }

  stages {
    stage('Snapshot') {
      steps {
        withCredentials([awsAccessKeyId(credentialsId: 'aws-credentials', variable: 'AWS_ACCESS_KEY_ID'),
                          awsSecretKey(credentialsId: 'aws-credentials', variable: 'AWS_SECRET_ACCESS_KEY')]) {
          sh "pip install boto3"
          sh "python3 rds_snap.py -db $RDS_INSTANCE"
        }
      }
    }
    
    // Add more stages as needed
  }
}
