// Pipeline do repositorio: testa com cobertura e envia a analise ao SonarQube.
// Requer a Shared Library "ci-lib" (ver relatorio de implantacao).
@Library('ci-lib') _

pipeline {
  agent any

  options {
    timeout(time: 30, unit: 'MINUTES')
    disableConcurrentBuilds()
    // Analise por branch/PR precisa do historico git completo (blame, "new code")
    skipDefaultCheckout(true)
  }

  stages {
    stage('Checkout') {
      steps {
        checkout([
          $class: 'GitSCM',
          branches: scm.branches,
          userRemoteConfigs: scm.userRemoteConfigs,
          extensions: scm.extensions + [[$class: 'CloneOption', shallow: false, noTags: false, timeout: 20]]
        ])
      }
    }

    stage('Testes') {
      steps {
        sh '''
          python3 -m venv .venv
          .venv/bin/pip install -q -r requirements-dev.txt
          .venv/bin/pytest --cov=app --cov-report=xml:coverage.xml --junitxml=test-results.xml
        '''
      }
      post { always { junit allowEmptyResults: true, testResults: 'test-results.xml' } }
    }

    stage('SonarQube') {
      steps {
        sonarScan(
          projectKey: 'tadaieskysigmacx_teste-sonar-jenkins',
          projectName: 'teste-sonar-jenkins',
          scmProvider: 'github',
          sources: 'app',
          extraArgs: '-Dsonar.tests=tests -Dsonar.python.coverage.reportPaths=coverage.xml'
        )
      }
    }
  }
}
