# teste-sonar-jenkins

Aplicacao Python minima usada para validar a integracao GitHub + Jenkins + SonarQube (Community + plugin de branches/PR).

- `main`: codigo limpo, com testes (cobertura alta) -> Quality Gate **passa**.
- `feature/frete`: nova funcionalidade com testes -> Quality Gate **passa**.
- `feature/relatorio-inseguro`: codigo com vulnerabilidade, bug e sem testes -> Quality Gate **barra**.
