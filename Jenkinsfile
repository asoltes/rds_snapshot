pipeline {
  agent any
  parameters {
    select(
      name: 'REGION',
      choices: ['us-east-1', 'us-east-2', 'ap-southeast-1', 'ap-southeast-2'],
      description: 'Select the Region of RDS.'
    )

    extendedChoice(
      name: 'RDS_INSTANCE',
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
        sh "pip install boto3"
        sh "python3 rds_snap.py --db_instances $RDS_INSTANCE --region $REGION"
      }
    }

    // Add more stages as needed
  }
}
