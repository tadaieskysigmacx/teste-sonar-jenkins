# teste-sonar-jenkins

Aplicacao Python minima usada para validar a integracao **GitHub Actions + SonarQube Community** (com o plugin de branches/PR). O nome do repositorio e historico; o Jenkins nao e mais usado.

- `main`: codigo limpo, com testes -> Quality Gate **passa**.
- `feature/frete`: funcionalidade nova com testes -> **passa**.
- `feature/relatorio-inseguro`: vulnerabilidade, bug e sem testes -> **barra** (check `sonar` falha).

Workflow: `.github/workflows/sonar.yml`. Configuracao do Sonar: `sonar-project.properties`.
